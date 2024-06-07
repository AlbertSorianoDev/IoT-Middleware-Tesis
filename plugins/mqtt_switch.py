from src.common.interfaces.switch_plugin_interface import SwitchPluginInterface
from src.common.property_manager.property import Property
from src.common.property_manager.text_data import TextData


class MQTTSwitch(SwitchPluginInterface):
    def __init__(
        self,
        *,
        command_topic: str,
        on_value: str,
        off_value: str,
    ) -> None:
        self.command_topic = command_topic
        self.on_value = on_value
        self.off_value = off_value
        self.power_property = Property(TextData())

    def _get_power_property(self):
        return self.power_property

    def _get_on_value(self):
        return self.on_value

    def _get_off_value(self):
        return self.off_value

    def on_operation(self):
        print("MQTT Switch on operation")

    def off_operation(self):
        print("MQTT Switch off operation")
