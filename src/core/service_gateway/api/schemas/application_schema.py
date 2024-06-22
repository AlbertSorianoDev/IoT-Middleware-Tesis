from datetime import datetime
from uuid import UUID

from src.core.service_gateway.api.schemas.application_creating_schema import (
    ApplicationCreatingSchema,
)


class ApplicationSchema(ApplicationCreatingSchema):
    id: UUID
    created_at: datetime
    last_keys_at: datetime
