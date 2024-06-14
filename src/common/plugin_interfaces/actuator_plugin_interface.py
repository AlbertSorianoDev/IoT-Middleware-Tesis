from abc import ABC, abstractmethod

from src.common.property_management.property import Property


class ActuatorPluginInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _get_power_property(self) -> Property:
        pass

    @abstractmethod
    def _get_on_value(self):
        pass

    @abstractmethod
    def _get_off_value(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass
