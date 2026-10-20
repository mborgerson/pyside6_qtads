import  unittest 
from base_qt_test import BaseQtTest
import PySide6QtAds as QtAds
from PySide6.QtWidgets import QWidget, QLabel
import shiboken6
import gc

from typing import List, Any


class TestDockWidget(QtAds.CDockWidget):
    pass

class TestDockWidgetTab(QtAds.CDockWidgetTab):
    pass

class TestDockAreaTitleBar(QtAds.CDockAreaTitleBar):
    pass

class TestAutoHideTab(QtAds.ads.CAutoHideTab):
    pass

class TestFactory(QtAds.CDockComponentsFactory):

    def createDockWidgetTab(self, DockWidget: QtAds.CDockWidget) -> QtAds.CDockWidgetTab:
        return TestDockWidgetTab(DockWidget, None)

    def createDockAreaTitleBar(self, DockArea: QtAds.CDockAreaWidget) -> QtAds.CDockAreaTitleBar:
        return TestDockAreaTitleBar(DockArea)

    def createDockWidgetSideTab(self, DockWidget: QtAds.CDockWidget) -> QtAds.ads.CAutoHideTab:
        return TestAutoHideTab(DockWidget)
    
class TestFactoryThatKeepsRef(QtAds.CDockComponentsFactory):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._storage: List[Any] = []

    def createDockWidgetTab(self, DockWidget: QtAds.CDockWidget) -> QtAds.CDockWidgetTab:
        tab = TestDockWidgetTab(DockWidget, None)
        self._storage.append(tab)
        return tab

    def createDockAreaTitleBar(self, DockArea: QtAds.CDockAreaWidget) -> QtAds.CDockAreaTitleBar:
        titlebar = TestDockAreaTitleBar(DockArea)
        self._storage.append(titlebar)
        return titlebar

    def createDockWidgetSideTab(self, DockWidget: QtAds.CDockWidget) -> QtAds.ads.CAutoHideTab:
        sidetab = TestAutoHideTab(DockWidget)
        self._storage.append(sidetab)
        return sidetab

class TestCDockComponentsFactory(BaseQtTest):

    def test_can_use_factory(self):
        QtAds.CDockManager.setAutoHideConfigFlags(QtAds.CDockManager.DefaultAutoHideConfig)
        container = QWidget()
        dock_manager = QtAds.CDockManager(container)
        factory = TestFactory()
        dock_manager.setComponentsFactory(factory)
        dw1 = QtAds.CDockWidget(dock_manager, "AutoHide")
        dw1.setWidget(QLabel("Hello"))
        dw2 = QtAds.CDockWidget(dock_manager, "Tab")
        dw2.setWidget(QLabel("Hello"))
        dock_manager.addAutoHideDockWidget(QtAds.SideBarLeft, dw1) 
        dock_manager.addDockWidgetTab(QtAds.TopDockWidgetArea, dw2)
        self.app.processEvents()
     
    def test_ownership_transferred(self):
        QtAds.CDockManager.setAutoHideConfigFlags(QtAds.CDockManager.DefaultAutoHideConfig)
        container = QWidget()
        dock_manager = QtAds.CDockManager(container)

        factory = TestFactoryThatKeepsRef()
        self.assertTrue(shiboken6.ownedByPython(factory))
        dock_manager.setComponentsFactory(factory)
        self.assertFalse(shiboken6.ownedByPython(factory))  # Given to QTAds

        dw1 = QtAds.CDockWidget(dock_manager, "AutoHide")
        dw1.setWidget(QLabel("Hello"))
        dw2 = QtAds.CDockWidget(dock_manager, "Tab")
        dw2.setWidget(QLabel("Hello"))

        dock_manager.addAutoHideDockWidget(QtAds.SideBarLeft, dw1) 
        dock_manager.addDockWidgetTab(QtAds.TopDockWidgetArea, dw2)
        for created_element in factory._storage:
            error_msg = f"Element of type  {created_element.__class__.__name__} still owned by python"
            self.assertFalse(shiboken6.ownedByPython(created_element), error_msg)

    def test_ads_bug_847_find_dock_widget(self):
        container = QWidget()
        dock_manager = QtAds.CDockManager(container)
        factory = TestFactory()
        dock_manager.setComponentsFactory(factory)  # Removes this and it's fine!
        dw1 = TestDockWidget(dock_manager, "dw1")
        dock_manager.addDockWidget(QtAds.TopDockWidgetArea, dw1)
        dw2 = dock_manager.findDockWidget("dw1")

        # https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/847
        self.assertIs(dw1, dw2, "Bad PySide6 binding, Check ADS Bug #847")  # Fails with 4.5.0.5 and PySide6.10+.  Should be the same.

    def test_ads_bug_847_slot_get_right_wrapper(self):
        dw_received = []

        def about_to_be_remove_slot(dw: TestDockWidget) -> None:
            dw_received.append(dw)

        container = QWidget()
        dock_manager = QtAds.CDockManager(container)
        factory = TestFactory()
        dock_manager.setComponentsFactory(factory)  # Removes this and it's fine!
        dock_manager.dockWidgetAboutToBeRemoved.connect(about_to_be_remove_slot)
        dw1 = TestDockWidget(dock_manager, "dw1")
        dock_manager.addDockWidget(QtAds.TopDockWidgetArea, dw1)
        dock_manager.removeDockWidget(dw1)

        self.app.processEvents()

        self.assertEqual(len(dw_received), 1)
        self.assertIsInstance(dw_received[0], TestDockWidget)
        self.assertIs(dw_received[0], dw1)          

if __name__ == '__main__':
     unittest.main()