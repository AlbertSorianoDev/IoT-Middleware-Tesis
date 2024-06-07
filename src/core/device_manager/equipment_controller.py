from typing import Dict, Any
from uuid import UUID

from src.core.plugin_manager.plugin_loader import PluginLoader
from src.core.utils.singleton import SingletonMeta
from src.core.device_manager.equipment import Equipment, Device
from src.core.actuator_manager.actuator import Actuator
from src.core.actuator_manager.actuator_factory import ActuatorFactory

# al crear device se debe separar actuador de sensor
# Aplicar el diseño de fábrica para los actuadores específicos como switch, etc.
# Aplicar el diseño de builder para la clase actuador y sensor


class EquipmentController(metaclass=SingletonMeta):
    def __init__(self, plugin_path: str = ""):
        self.equipments_index: Dict[UUID, Equipment] = {}
        # self.sensors_index: Dict[UUID, Device] = {}
        self.devices_index: Dict[UUID, Device] = {}

        self.plugin_loader = PluginLoader(plugin_path)
        self.actuator_factory = ActuatorFactory()

    def create_equipment(self, label: str, description: str):
        new_equipement = Equipment(label=label, description=description)
        self.equipments_index[new_equipement.id] = new_equipement

        return new_equipement

    def create_actuator(
        self,
        *,
        equipment_id: UUID,
        label: str,
        description: str,
        actuator_type: str,
        plugin_class_name: str,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, Any] = None,
    ) -> Actuator:
        equipment = self.equipments_index.get(equipment_id)

        if not equipment:
            raise ValueError(f"Equipment {equipment_id} not found")

        plugin = self.plugin_loader.get_plugin_by_class_name(plugin_class_name)

        if not plugin:
            raise ValueError(f"Plugin {plugin_class_name} not found")

        new_actuator = self.actuator_factory.create_actuator(
            actuator_type=actuator_type,
            label=label,
            description=description,
            plugin_class=plugin.cls,
            brand=brand,
            model=model,
            config_params=config_params,
        )

        equipment.add_device(new_actuator)
        self.devices_index[new_actuator.id] = new_actuator

        return new_actuator

    def get_equipment_by_id(self, equipment_id: UUID):
        return self.equipments_index.get(equipment_id)

    def get_device_by_id(self, device_id: UUID):
        return self.devices_index.get(device_id)
