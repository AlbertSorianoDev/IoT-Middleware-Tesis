from typing import Dict, List

from src.core.plugin_managment.plugin_controller import PluginController


class PluginService:
    def __init__(self):
        self.plugin_controller = PluginController()

    def get_plugin_names_by_actuator_type(self, actuator_type: str) -> List[str]:
        actuator_class = self.plugin_controller.actuator_factory.actuator_classes.get(
            actuator_type
        )

        if not actuator_class:
            return []

        interface = actuator_class.PLUGIN_INTERFACE

        plugins = self.plugin_controller.get_plugin_names_by_interface_name(
            interface.__name__
        )
        return plugins

    def get_plugin_configuration_params(self, plugin_name: str) -> Dict[str, str]:
        plugin = self.plugin_controller.get_plugin_by_class_name(plugin_name)
        return plugin.params
