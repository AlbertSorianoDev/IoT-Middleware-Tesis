from src.common.plugin_interfaces.channel_plugin_interface import ChannelPluginInterface
from src.common.plugin_interfaces.sensor_plugin_interface import SensorPluginInterface
from src.common.property_management.property import Property
from src.common.property_management.numeric_data import NumericData
from plugins.mqtt_plugin.mqtt_event_receiver import MQTTEventReceiver
from plugins.mqtt_plugin.mqtt_client import MQTTClient


class MQTTNumericSensor(SensorPluginInterface):
    def __init__(self, topic: str, qos: int):
        self.topic = topic
        self.qos = qos
        self.sensor_property = Property(NumericData())

        self.channel: MQTTClient
        self.mqtt_event_receiver: MQTTEventReceiver

    def set_channel_plugin(self, channel: ChannelPluginInterface) -> None:
        self.channel = channel

        self.mqtt_event_receiver = MQTTEventReceiver(
            client_class=self.channel,
            property=self.sensor_property,
            topic=self.topic,
            qos=self.qos,
        )

        self.mqtt_event_receiver.set_event()

    def get_sensor_property(self) -> Property:
        return self.sensor_property

    def on_delete(self):
        self.mqtt_event_receiver.delete_event()
