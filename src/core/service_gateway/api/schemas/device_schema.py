from pydantic import BaseModel
from typing import Dict, Optional, Any


class DeviceSchema(BaseModel):
    id: str
    label: str
    description: str
    brand: Optional[str]
    model: Optional[str]
    connection_status: str
    plugin_class_name: str
    config_params: Optional[Dict[str, str]]
