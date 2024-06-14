from uuid import UUID

from src.core.service_gateway.v1.schemas.equipment_creating_schema import (
    EquipmentCreatingSchema,
)


class EquipmentSchema(EquipmentCreatingSchema):
    id: UUID
