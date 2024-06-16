from pydantic import BaseModel
from typing import Dict


class ChannelCreatingSchema(BaseModel):
    label: str
    description: str
    plugin_class_name: str
    config_params: Dict[str, str | int | float]
