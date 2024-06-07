from pydantic import BaseModel


class EquipmentCreatingSchema(BaseModel):
    label: str
    description: str
