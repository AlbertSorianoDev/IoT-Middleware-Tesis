from typing import Dict, Any

from src.core.actuator_management.actuator import Actuator
from src.core.access_gateway.channel import Channel
from src.common.plugin_interfaces.actuator_plugin_interface import (
    ActuatorPluginInterface,
)


class ActuatorFactory:
    def __init__(self):
        self.actuator_classes = {cls.__name__: cls for cls in Actuator.__subclasses__()}

    def create_actuator(
        self,
        *,
        actuator_type: str,
        label: str,
        description: str,
        plugin_class: ActuatorPluginInterface,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, Any] = None,
        channel: Channel = None,
    ):
        if actuator_type in self.actuator_classes:
            return self.actuator_classes[actuator_type](
                label=label,
                description=description,
                plugin_class=plugin_class,
                brand=brand,
                model=model,
                config_params=config_params,
                channel=channel,
            )
        else:
            raise ValueError(f"Actuator type '{actuator_type}' not recognized.")
