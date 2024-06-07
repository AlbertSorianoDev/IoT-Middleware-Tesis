from src.core.device_manager.equipment_controller import EquipmentController


class PluginService:
    def __init__(self):
        self.equipment_control = EquipmentController()

    def get_plugin_names_by_actuator_type(self, actuator_type: str):
        actuator_class = self.equipment_control.actuator_factory.actuator_classes.get(
            actuator_type
        )

        if not actuator_class:
            return []

        interface = actuator_class.plugin_interface

        plugins = (
            self.equipment_control.plugin_loader.get_plugin_names_by_interface_name(
                interface.__name__
            )
        )
        return plugins

    def get_plugin_configuration_params(self, plugin_name: str):
        plugin = self.equipment_control.plugin_loader.get_plugin_by_class_name(
            plugin_name
        )
        return plugin.params
