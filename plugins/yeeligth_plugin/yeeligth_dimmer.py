from src.common.plugin_interfaces.dimmer_plugin_interface import DimmerPluginInterface


class YeelightDimmer(DimmerPluginInterface):
    def __init__(
        self,
    ) -> None:
        self.power_property = None

    def _get_brightness_property(self):
        return self.power_property

    def set_brightness(self, value: int):
        print("Yeelight Dimmer set brightness operation to ", value)

    def on(self):
        print("Yeelight Dimmer on operation")

    def off(self):
        print("Yeelight Dimmer off operation")
