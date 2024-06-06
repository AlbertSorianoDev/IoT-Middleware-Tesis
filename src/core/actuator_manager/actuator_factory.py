from typing import Dict, Any

from src.core.actuator_manager.actuator import Actuator
from src.common.interfaces.actuator_plugin_interface import ActuatorPluginInterface


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
        attributes: Dict[str, Any] = None,
    ):
        if actuator_type in self.actuator_classes:
            return self.actuator_classes[actuator_type](
                label=label,
                description=description,
                plugin_class=plugin_class,
                brand=brand,
                model=model,
                attributes=attributes,
            )
        else:
            raise ValueError(f"Actuator type '{actuator_type}' not recognized.")
