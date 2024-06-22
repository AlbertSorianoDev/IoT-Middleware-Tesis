from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from typing import List

from src.core.service_gateway.services.equipment_service import EquipmentService
from src.core.service_gateway.api.schemas.equipment_schema import EquipmentSchema
from src.core.service_gateway.api.schemas.equipment_creating_schema import (
    EquipmentCreatingSchema,
)


class EquipmentRouter:
    equipment_router = APIRouter(prefix="/equipment", tags=["Equipment"])

    @equipment_router.get("/{equipment_id}", response_model=EquipmentSchema)
    async def get_equipment_by_id(equipment_id: UUID):
        service = EquipmentService()
        equipment = service.get_equipment_by_id(equipment_id)

        if equipment:
            return JSONResponse(content=equipment, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Equipment not found"}, status_code=404
            )

    @equipment_router.get("s", response_model=List[EquipmentSchema])
    async def get_equipments():
        service = EquipmentService()
        equipments = service.get_equipments()

        return JSONResponse(content=equipments, status_code=200)

    @equipment_router.post("")
    async def create_equipment(equipment_create: EquipmentCreatingSchema):
        service = EquipmentService()
        equipment = service.create_equipment(equipment_create)

        if equipment:
            return JSONResponse(content=equipment, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating equipment"}, status_code=500
            )

    # TODO: Implement update_equipment method
    @equipment_router.put("/{equipment_id}")
    async def update_equipment(
        equipment_id: UUID, equipment_update: EquipmentCreatingSchema
    ):
        equipment_data = {
            "id": equipment_id,
            **equipment_update.model_dump(),
        }

        if equipment_data:
            return JSONResponse(content=equipment_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error updating equipment"}, status_code=500
            )

    # TODO: Implement delete_equipment method
    @equipment_router.delete("/{equipment_id}")
    async def delete_equipment(equipment_id: UUID):
        if True:
            return JSONResponse(
                content={"message": "Equipment deleted"}, status_code=200
            )
        else:
            return JSONResponse(
                content={"message": "Error deleting equipment"}, status_code=500
            )
