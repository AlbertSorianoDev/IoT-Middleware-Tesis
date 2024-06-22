from abc import abstractmethod

from src.common.plugin_interfaces.actuator_plugin_interface import (
    ActuatorPluginInterface,
)


class LedScreenPluginInterface(ActuatorPluginInterface):
    @abstractmethod
    def set_text(self, value: int):
        """
        Set the brightness of the dimmer.
        The Middleware will call the method with the value int between (0, 100) to set.
        """
        pass
