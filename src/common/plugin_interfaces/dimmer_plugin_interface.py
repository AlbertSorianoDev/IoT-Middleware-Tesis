from abc import abstractmethod

from src.common.plugin_interfaces.actuator_plugin_interface import (
    ActuatorPluginInterface,
)


class DimmerPluginInterface(ActuatorPluginInterface):
    @abstractmethod
    def _get_brightness_property(self):
        pass

    @abstractmethod
    def set_brightness(self, value: int):
        """
        Set the brightness of the dimmer.
        The Middleware will call the method with the value int betwen (0, 100) to set.
        """
        pass
