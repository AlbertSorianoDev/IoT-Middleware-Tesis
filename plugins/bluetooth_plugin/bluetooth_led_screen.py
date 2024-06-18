from src.common.plugin_interfaces.led_screen_plugin_interface import (
    LedScreenPluginInterface,
)
from src.common.property_management.property import Property


class BluetoothLedScreen(LedScreenPluginInterface):
    def __init__(self, bt_address: str, bt_serial_port: str):
        pass

    def _get_power_property(self) -> Property:
        return super()._get_power_property()

    def set_text(self, value: int):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def on_delete(self):
        pass
