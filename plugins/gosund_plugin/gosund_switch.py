from src.common.plugin_interfaces.switch_plugin_interface import SwitchPluginInterface
from src.common.property_management.property import Property


# TODO: Implement the class
class GosundSwitch(SwitchPluginInterface):
    def __init__(self):
        pass

    def _get_power_property(self) -> Property:
        return super()._get_power_property()

    def _get_on_value(self):
        return super()._get_on_value()

    def _get_off_value(self):
        return super()._get_off_value()

    def on(self):
        return super().on()

    def off(self):
        return super().off()
