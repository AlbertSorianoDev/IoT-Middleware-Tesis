from typing import Any, Dict

from src.core.device_manager.device import Device
from src.common.interfaces.actuator_plugin_interface import ActuatorPluginInterface
from src.common.property_manager.property import Property


class Actuator(Device):
    plugin_interface = ActuatorPluginInterface

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
        return {"power_state": self._power_state()}

    def _instance_plugin(self):
        self.plugin: ActuatorPluginInterface = self.plugin_class(**self.config_params)
        self.on_value = self.plugin._get_on_value()
        self.off_value = self.plugin._get_off_value()
        self.power_property = self.plugin._get_power_property()

    def _power_state(self):
        if self.power_property is None:
            return "unknown"

        if self.on_value == self.power_property.get_value():
            return "on"

        if self.off_value == self.power_property.get_value():
            return "off"

        return "unknown"

    def on(self):
        self.plugin.on_operation()

    def off(self):
        self.plugin.off_operation()
