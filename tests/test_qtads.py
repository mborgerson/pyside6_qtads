import sys
import unittest

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QStatusBar

import PySide6QtAds as QtAds


class SimpleWindow(QMainWindow):
    """
    Creates a main window with a dock manager.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(0, 0, 400, 21)

        self.menu_bar = QMenuBar(self)
        self.menu_view = QMenu(self.menu_bar)
        self.menu_view.setTitle("View")

        self.menu_bar.addAction(self.menu_view.menuAction())
        self.setMenuBar(self.menu_bar)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # Create the dock manager. Because the parent parameter is a QMainWindow
        # the dock manager registers itself as the central widget.
        self.dock_manager = QtAds.CDockManager(self)

        # Create example content label - this can be any application specific
        # widget
        dock_inner_widget = QLabel()
        dock_inner_widget.setWordWrap(True)
        dock_inner_widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        dock_inner_widget.setText("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. ")

        # Create a dock widget with the title Label 1 and set the created label
        # as the dock widget content
        dock_widget = QtAds.CDockWidget("Label 1")
        dock_widget.setWidget(dock_inner_widget)

        # Add the toggleViewAction of the dock widget to the menu to give
        # the user the possibility to show the dock widget if it has been closed
        self.menu_view.addAction(dock_widget.toggleViewAction())

        # Add the dock widget to the top dock widget area
        self.dock_manager.addDockWidget(QtAds.TopDockWidgetArea, dock_widget)


class TestSimpleWindow(unittest.TestCase):
    """
    Basic QtAds tests.
    """

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = SimpleWindow()
        self.window.show()

    def tearDown(self):
        self.window.close()

    def test_window_is_visible(self):
        assert self.window.isVisible()


if __name__ == '__main__':
    unittest.main()
