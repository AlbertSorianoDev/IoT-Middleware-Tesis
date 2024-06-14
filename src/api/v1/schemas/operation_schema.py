from uuid import UUID
from pydantic import BaseModel
from typing import Dict


class OperationSchema(BaseModel):
    device_id: UUID
    operation: str
    operation_params: Dict[str, str]
