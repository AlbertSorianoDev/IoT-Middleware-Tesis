from plugins.mqtt_plugin.mqtt_client import MQTTClient
from src.common.property_management.event_receiver import EventReceiver
from src.common.property_management.property import Property


class MQTTEventReceiver(EventReceiver):
    def __init__(
        self, client_class: MQTTClient, property: Property, topic: str, qos: int
    ):
        self.client_class = client_class
        self.topic = topic
        self.qos = qos
        self.property = property
        self.subscriber_id = 0

    def set_event(self):
        self.subscriber_id = self.client_class.subscribe(
            self.topic, self.qos, self.property.set_value
        )

    def on_delete(self):
        self.client_class.unsubscribe(self.topic, self.subscriber_id)
