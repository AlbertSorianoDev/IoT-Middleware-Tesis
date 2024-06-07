from pydantic import BaseModel
from typing import Dict, Optional, Any
from uuid import UUID


class ActuatorCreatingSchema(BaseModel):
    equipment_id: UUID
    label: str
    description: str
    actuator_type: str
    plugin_class_name: str
    brand: Optional[str]
    model: Optional[str]
    config_params: Optional[Dict[str, str]]
