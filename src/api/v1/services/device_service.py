from uuid import UUID
from typing import List, Dict, Any

from src.core.device_managment.equipment_controller import EquipmentController
from src.api.v1.schemas.device_schema import DeviceSchema
from src.api.v1.schemas.actuator_creating_schema import ActuatorCreatingSchema
from src.api.v1.schemas.operation_schema import OperationSchema


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

    def get_actuator_types(self) -> List[str]:
        return list(self.equipment_control.actuator_factory.actuator_classes.keys())

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

    def get_operations_by_actuator_type(
        self, actuator_type: str
    ) -> Dict[str, Dict[str, str]] | None:
        return self.equipment_control.get_operations_by_actuator_type(actuator_type)

    def do_an_operation_by_actuator_id(self, operation_data: OperationSchema) -> bool:
        operation_result = self.equipment_control.do_an_operation_by_actuator_id(
            **operation_data.model_dump()
        )

        return operation_result
