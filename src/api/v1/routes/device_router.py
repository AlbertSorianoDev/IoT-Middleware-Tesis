from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from typing import List

from src.api.v1.services.device_service import DeviceService
from src.api.v1.schemas.device_schema import DeviceSchema
from src.api.v1.schemas.actuator_creating_schema import ActuatorCreatingSchema


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
