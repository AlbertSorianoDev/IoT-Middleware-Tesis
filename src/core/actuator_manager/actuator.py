from typing import Any, Dict

from src.core.device_manager.device import Device
from src.common.interfaces.actuator_plugin_interface import ActuatorPluginInterface


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
        attributes: Dict[str, Any] = None,
    ):
        super().__init__(
            label=label,
            description=description,
            plugin_class=plugin_class,
            brand=brand,
            model=model,
            attributes=attributes,
        )
        self.instance_plugin()

    def instance_plugin(self):
        self.plugin: ActuatorPluginInterface = self.plugin_class(**self.attributes)

    def on(self):
        self.plugin.on_operation()

    def off(self):
        self.plugin.off_operation()
