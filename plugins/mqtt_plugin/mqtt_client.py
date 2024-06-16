import paho.mqtt.client as mqtt

from typing import Callable, Dict

from src.common.plugin_interfaces.channel_plugin_interface import ChannelPluginInterface


class MQTTClient(ChannelPluginInterface):
    subscribers_new_id = 1

    def __init__(
        self,
        *,
        client_id: str,
        host: str,
        port: int,
        username: str,
        password: str,
    ):
        self.client = mqtt.Client(client_id=client_id)
        self.client.username_pw_set(username, password)
        self.client.on_message = self.on_message
        self.client.reconnect_delay_set(min_delay=1, max_delay=120)

        self.broker_host = host
        self.broker_port = port
        self.keep_alive = 60

        self.subscribe_topics: Dict[str, Dict[int, Callable]] = {}

        self.client.connect(self.broker_host, self.broker_port, self.keep_alive)
        self.client.loop_start()

    def on_message(self, client, userdata, message):
        if message.topic in self.subscribe_topics:
            for function_callable in self.subscribe_topics[message.topic].values():
                function_callable(message.payload.decode("utf-8"))

    def subscribe(self, topic: str, qos: int, callable_function: Callable) -> int:
        self.subscribe_topics.get

        if self.subscribe_topics.get(topic) is None:
            self.subscribe_topics[topic] = {}

        self.subscribe_topics[topic][self.subscribers_new_id] = callable_function
        self.client.subscribe(topic, qos)

        subscriber_id = self.subscribers_new_id
        self.subscribers_new_id += 1

        return subscriber_id

    def unsubscribe(self, topic: str, subscriber_id: int):
        if self.subscribe_topics.get(topic):
            self.subscribe_topics[topic].pop(subscriber_id)

            if not self.subscribe_topics[topic]:
                self.client.unsubscribe(topic)

    def on_delete(self):
        self.client.loop_stop()
        self.client.disconnect()
