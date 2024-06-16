from pydantic import BaseModel
from typing import Dict, Optional
from uuid import UUID


class SensorCreatingSchema(BaseModel):
    equipment_id: UUID
    label: str
    description: str
    plugin_class_name: str
    brand: Optional[str]
    model: Optional[str]
    config_params: Optional[Dict[str, str | int | float]]
