from pydantic import BaseModel
from uuid import UUID


class EquipmentCreatingSchema(BaseModel):
    label: str
    description: str
    channel_id: UUID
