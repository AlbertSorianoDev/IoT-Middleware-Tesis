from src.common.interfaces.switch_plugin_interface import SwitchPluginInterface


class MQTTSwitch(SwitchPluginInterface):
    def __init__(
        self,
        *,
        event_topic: str,
        command_topic: str,
        on_value: str,
        off_value: str,
    ) -> None:
        self.event_topic = event_topic
        self.command_topic = command_topic
        self.on_value = on_value
        self.off_value = off_value

    def on_operation(self):
        print("MQTT Switch on operation")

    def off_operation(self):
        print("MQTT Switch off operation")
