from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from typing import List, Dict

from src.core.service_gateway.services.device_service import DeviceService
from src.core.service_gateway.api.schemas.device_schema import DeviceSchema
from src.core.service_gateway.api.schemas.actuator_creating_schema import (
    ActuatorCreatingSchema,
)
from src.core.service_gateway.api.schemas.operation_schema import OperationSchema
from src.core.service_gateway.api.schemas.sensor_creating_schema import (
    SensorCreatingSchema,
)
from src.core.service_gateway.api.schemas.sensor_states_schema import SensorStatesSchema


class DeviceRouter:
    device_router = APIRouter(prefix="/device", tags=["Device"])

    @device_router.get("/{device_id}", response_model=DeviceSchema | None)
    async def get_device_by_id(device_id: UUID):
        service = DeviceService()
        device_data = service.get_device_by_id(device_id)

        if device_data:
            return JSONResponse(content=device_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Actuator not found"}, status_code=404
            )

    @device_router.get("s/{equipment_id}", response_model=List[DeviceSchema])
    async def get_devices_by_equipment_id(equipment_id: UUID):
        service = DeviceService()
        devices_data = service.get_devices_by_equipment_id(equipment_id)

        return JSONResponse(content=devices_data, status_code=200)

    @device_router.get("/actuator/types", response_model=List[str])
    async def get_actuator_types():
        service = DeviceService()
        actuator_types = service.get_actuator_types()

        return JSONResponse(content=actuator_types, status_code=200)

    @device_router.post("/actuator", response_model=DeviceSchema | None)
    async def create_actuator(
        actuator_create: ActuatorCreatingSchema,
    ):
        service = DeviceService()
        actuator_data = service.create_actuator(actuator_create)

        if actuator_data:
            return JSONResponse(content=actuator_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating actuator"}, status_code=500
            )

    @device_router.get(
        "/actuator/{actuator_type}/operations", response_model=Dict[str, Dict[str, str]]
    )
    async def get_operations_by_actuator_type(actuator_type: str):
        service = DeviceService()
        actuator_operations_data = service.get_operations_by_actuator_type(
            actuator_type
        )

        if actuator_operations_data:
            return JSONResponse(content=actuator_operations_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Actuator not found"}, status_code=404
            )

    @device_router.post(
        "/actuator/{actuator_id}/operate", response_model=Dict[str, str]
    )
    async def do_an_operation_by_actuator_id(operation_data: OperationSchema):
        service = DeviceService()
        operation_result = service.do_an_operation_by_actuator_id(operation_data)

        if operation_result:
            return JSONResponse(
                content={"operation_realize": operation_result}, status_code=200
            )
        else:
            return JSONResponse(
                content={"message": "Error doing operation"}, status_code=500
            )

    @device_router.post("/sensor", response_model=DeviceSchema)
    async def create_sensor(sensor_create: SensorCreatingSchema):
        service = DeviceService()
        sensor_data = service.create_sensor(sensor_create)

        if sensor_data:
            return JSONResponse(content=sensor_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating sensor"}, status_code=500
            )

    @device_router.get("/sensor/{sensor_id}/states", response_model=SensorStatesSchema)
    async def get_sensor_states(sensor_id: UUID):
        service = DeviceService()
        sensor_states_data = service.get_sensor_states(sensor_id)

        if sensor_states_data:
            return JSONResponse(content=sensor_states_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Sensor not found"}, status_code=404
            )
