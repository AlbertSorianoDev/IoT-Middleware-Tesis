from abc import ABC, abstractmethod

from src.common.plugin_interfaces.channel_plugin_interface import ChannelPluginInterface
from src.common.property_management.property import Property


class SensorPluginInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_sensor_property(self) -> Property:
        pass

    @abstractmethod
    def set_channel_plugin(self, channel: ChannelPluginInterface) -> None:
        pass

    @abstractmethod
    def on_delete(self) -> None:
        pass
