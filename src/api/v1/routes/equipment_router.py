from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.api.v1.services.equipment_service import EquipmentService


class EquipmentRouter:
    equipment_router = APIRouter(prefix="/equipment", tags=["Equipment"])

    @equipment_router.get("/{equipment_id}")
    async def get_equipment_by_id(equipment_id: int):
        service = EquipmentService()
        equipment = service.get_equipment_by_id(equipment_id)

        if equipment:
            return JSONResponse(content=equipment, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Equipment not found"}, status_code=404
            )

    @equipment_router.get("s")
    async def get_equipments():
        service = EquipmentService()
        equipments = service.get_equipments()

        return JSONResponse(content=equipments, status_code=200)

    @equipment_router.post("")
    async def create_equipment(label: str, description: str):
        service = EquipmentService()
        equipment = service.create_equipment(label, description)

        if equipment:
            return JSONResponse(content=equipment, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating equipment"}, status_code=500
            )
