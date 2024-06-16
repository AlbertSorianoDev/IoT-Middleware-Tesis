from uuid import UUID

from src.core.service_gateway.api.schemas.channel_creating_schema import (
    ChannelCreatingSchema,
)


class ChannelSchema(ChannelCreatingSchema):
    id: UUID
