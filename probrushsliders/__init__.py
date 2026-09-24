from .probrushsliders import *
from krita import *
from PyQt5 import *

# Fire up the toolbar object once the main window components wake up
# instance = Krita.instance()
# extension = instance.extensions()["ProBrushSliders"]
# instance.notifier().windowCreated.connect(extension.create_sliders_toolbar)

# Register
DOCKER_ID = "ProBrushSliders"
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(
    DOCKER_ID,
    DockWidgetFactoryBase.DockLeft,
    ProSlidersDocker
)
instance.addDockWidgetFactory(dock_widget_factory)