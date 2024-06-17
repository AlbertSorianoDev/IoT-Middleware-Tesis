from pydantic import BaseModel
from uuid import UUID
from typing import Dict


class RuleCreatingSchema(BaseModel):
    label: str
    description: str
    trigger_device_id: UUID
    trigger_state: str
    condition: str
    value: str | int | float | bool
    affected_device_id: UUID
    affected_command: str
    command_params: Dict[str, str | int | float | bool]
