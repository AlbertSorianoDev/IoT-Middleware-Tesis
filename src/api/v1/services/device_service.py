from uuid import UUID
from typing import List

from src.core.device_manager.equipment_controller import EquipmentController
from src.api.v1.schemas.device_schema import DeviceSchema
from src.api.v1.schemas.actuator_creating_schema import ActuatorCreatingSchema


class DeviceService:
    def __init__(self) -> None:
        self.equipment_control = EquipmentController()

    def get_device_by_id(self, actuator_id: UUID) -> DeviceSchema | None:
        actuator = self.equipment_control.get_device_by_id(actuator_id)

        if actuator:
            return actuator.to_dict()

        return None

    def get_devices_by_equipment_id(self, equipment_id: UUID) -> List[DeviceSchema]:
        equipment = self.equipment_control.get_equipment_by_id(equipment_id)
        # TODO: Add validation for equipment not found

        actuators = equipment.devices

        return [actuator.to_dict() for actuator in actuators]

    def create_actuator(
        self,
        actuator_create: ActuatorCreatingSchema,
    ) -> DeviceSchema | None:
        actuator = self.equipment_control.create_actuator(
            **actuator_create.model_dump()
        )

        if actuator:
            return actuator.to_dict()

        return None
