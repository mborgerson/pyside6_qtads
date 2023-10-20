import platform

if platform.system() == 'Windows':
	import os, PySide6, shiboken6
	with os.add_dll_directory(os.path.dirname(PySide6.__file__)), \
	     os.add_dll_directory(os.path.dirname(shiboken6.__file__)):
		from .PySide6QtAds import ads as _ads
else:
	# Runtime library dependencies resolved via rpath
	from .PySide6QtAds import ads as _ads

ads = _ads  # make PySide6QtAds.ads available

# DockWidgetArea
DockWidgetArea = _ads.DockWidgetArea
NoDockWidgetArea = _ads.NoDockWidgetArea
LeftDockWidgetArea = _ads.LeftDockWidgetArea
RightDockWidgetArea = _ads.RightDockWidgetArea
TopDockWidgetArea = _ads.TopDockWidgetArea
BottomDockWidgetArea = _ads.BottomDockWidgetArea
CenterDockWidgetArea = _ads.CenterDockWidgetArea
InvalidDockWidgetArea = _ads.InvalidDockWidgetArea
OuterDockAreas = _ads.OuterDockAreas
AllDockAreas = _ads.AllDockAreas

# SideBarLocation
SideBarLocation = _ads.SideBarLocation

# eBitwiseOperator
BitwiseAnd = _ads.BitwiseAnd
BitwiseOr = _ads.BitwiseOr

# eDragState
DraggingInactive = _ads.DraggingInactive
DraggingMousePressed = _ads.DraggingMousePressed
DraggingTab = _ads.DraggingTab
DraggingFloatingWidget = _ads.DraggingFloatingWidget

# eIcon
TabCloseIcon = _ads.TabCloseIcon
DockAreaMenuIcon = _ads.DockAreaMenuIcon
DockAreaUndockIcon = _ads.DockAreaUndockIcon
DockAreaCloseIcon = _ads.DockAreaCloseIcon
IconCount = _ads.IconCount

# TitleBarButton
TitleBarButtonTabsMenu = _ads.TitleBarButtonTabsMenu
TitleBarButtonUndock = _ads.TitleBarButtonUndock
TitleBarButtonClose = _ads.TitleBarButtonClose

# Classes
CDockAreaTabBar = _ads.CDockAreaTabBar
CDockAreaTitleBar = _ads.CDockAreaTitleBar
CDockAreaWidget = _ads.CDockAreaWidget
CDockComponentsFactory = _ads.CDockComponentsFactory
CDockContainerWidget = _ads.CDockContainerWidget
CDockFocusController = _ads.CDockFocusController
CDockManager = _ads.CDockManager
CDockSplitter = _ads.CDockSplitter
CDockOverlay = _ads.CDockOverlay
CDockOverlayCross = _ads.CDockOverlayCross
CDockWidget = _ads.CDockWidget
CDockWidgetTab = _ads.CDockWidgetTab
CDockingStateReader = _ads.CDockingStateReader
CElidingLabel = _ads.CElidingLabel
CFloatingDockContainer = _ads.CFloatingDockContainer
CFloatingDragPreview = _ads.CFloatingDragPreview
IFloatingWidget = _ads.IFloatingWidget
CIconProvider = _ads.CIconProvider
CSpacerWidget = _ads.CSpacerWidget
CTitleBarButton = _ads.CTitleBarButton
