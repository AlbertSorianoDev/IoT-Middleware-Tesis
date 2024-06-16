from uuid import UUID
from typing import List, Dict, Any

from src.core.application_management.equipment_controller import EquipmentController
from src.core.service_gateway.api.schemas.device_schema import DeviceSchema
from src.core.service_gateway.api.schemas.actuator_creating_schema import (
    ActuatorCreatingSchema,
)
from src.core.service_gateway.api.schemas.operation_schema import OperationSchema
from src.core.service_gateway.api.schemas.sensor_creating_schema import (
    SensorCreatingSchema,
)
from src.core.service_gateway.api.schemas.sensor_states_schema import SensorStatesSchema


class DeviceService:
    def __init__(self) -> None:
        self.equipment_control = EquipmentController()

    def get_device_by_id(self, actuator_id: UUID) -> DeviceSchema | None:
        device = self.equipment_control.get_device_by_id(actuator_id)

        if device:
            return device.to_dict()

        return None

    def get_devices_by_equipment_id(self, equipment_id: UUID) -> List[DeviceSchema]:
        equipment = self.equipment_control.get_equipment_by_id(equipment_id)

        if not equipment:
            return []

        devices = equipment.devices

        return [device.to_dict() for device in devices]

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

    def create_sensor(self, sensor_create: SensorCreatingSchema) -> DeviceSchema | None:
        sensor = self.equipment_control.create_sensor(**sensor_create.model_dump())

        if sensor:
            return sensor.to_dict()

        return None

    def get_sensor_states(self, sensor_id: UUID) -> SensorStatesSchema | None:
        sensor = self.equipment_control.get_device_by_id(sensor_id)

        if sensor:
            return sensor.states

        return None
