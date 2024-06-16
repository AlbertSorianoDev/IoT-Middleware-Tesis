from pydantic import BaseModel
from typing import Dict


class ConfigParamsSchema(BaseModel):
    config_params: Dict[str, str | int | float]
