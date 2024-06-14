from typing import Any, Dict

from src.core.device_management.device import Device
from src.common.plugin_interfaces.actuator_plugin_interface import (
    ActuatorPluginInterface,
)
from src.common.property_management.property import Property


class Actuator(Device):
    PLUGIN_INTERFACE = ActuatorPluginInterface

    # States definition
    POWER_STATE = "power_state"

    # Unknown general state
    UNKNOWN = "UNKNOWN"

    # Power state values
    POWER_STATE_ON = "ON"
    POWER_STATE_OFF = "OFF"

    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: ActuatorPluginInterface,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, Any] = None,
    ):
        super().__init__(
            label=label,
            description=description,
            plugin_class=plugin_class,
            brand=brand,
            model=model,
            config_params=config_params,
        )

        self.on_value = None
        self.off_value = None
        self.power_property: Property | None = None

        self._instance_plugin()

    @property
    def states(self):
        return {self.POWER_STATE: self._power_state()}

    def _instance_plugin(self):
        self.plugin: ActuatorPluginInterface = self.plugin_class(**self.config_params)
        self.on_value = self.plugin._get_on_value()
        self.off_value = self.plugin._get_off_value()
        self.power_property = self.plugin._get_power_property()

    def _power_state(self):
        if self.power_property is None:
            return self.UNKNOWN

        if self.on_value == self.power_property.get_value():
            return self.POWER_STATE_ON

        if self.off_value == self.power_property.get_value():
            return self.POWER_STATE_OFF

        return self.UNKNOWN

    @classmethod
    def states_info(cls):
        return {
            cls.POWER_STATE: {
                "description": "The power state of the actuator, discrete value.",
                "values": f"{[cls.POWER_STATE_ON, cls.POWER_STATE_OFF, cls.UNKNOWN]}",
            }
        }

    def on(self):
        self.plugin.on()

    def off(self):
        self.plugin.off()
