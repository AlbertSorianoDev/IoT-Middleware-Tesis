from uuid import UUID, uuid4
from typing import Dict

from src.core.device_managment.connection_status import ConnectionStatus
from src.common.plugin_interfaces.actuator_plugin_interface import (
    ActuatorPluginInterface,
)


class Device:
    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: ActuatorPluginInterface,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, str] = None,
    ):
        self.id: UUID = uuid4()
        self.label: str = label
        self.description: str = description
        self.brand: str = brand
        self.model: str = model
        self.connection_status: ConnectionStatus = ConnectionStatus.UNKNOWN
        self.plugin_class = plugin_class
        self.config_params: Dict[str, str] = config_params

    def to_dict(self):
        return {
            "id": str(self.id),
            "label": self.label,
            "description": self.description,
            "brand": self.brand,
            "model": self.model,
            "connection_status": self.connection_status.name,
            "plugin_class_name": self.plugin_class.__name__,
            "config_params": self.config_params,
        }
