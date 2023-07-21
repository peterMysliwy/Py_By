
# EXTRA_IMPORTS #
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection
from testpluginplugin import TestPluginPlugin
from gpib_drop_downplugin import GPIB_drop_downPlugin

# Set PYSIDE_DESIGNER_PLUGINS to point to this directory and load the plug_in

if __name__ == '__main__':
    QPyDesignerCustomWidgetCollection.addCustomWidget(TestPluginPlugin())
    QPyDesignerCustomWidgetCollection.addCustomWidget(GPIB_drop_downPlugin())
