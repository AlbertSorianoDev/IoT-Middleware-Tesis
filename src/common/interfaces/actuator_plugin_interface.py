from abc import ABC, abstractmethod


class ActuatorPluginInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def on_operation(self):
        pass

    @abstractmethod
    def off_operation(self):
        pass
