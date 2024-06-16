from typing import List
from uuid import UUID

from src.core.application_management.equipment_controller import EquipmentController
from src.core.service_gateway.api.schemas.channel_schema import ChannelSchema
from src.core.service_gateway.api.schemas.channel_creating_schema import (
    ChannelCreatingSchema,
)


class ChannelService:
    def __init__(self):
        self.equipment_controller = EquipmentController()

    def get_channel_by_id(self, channel_id: UUID) -> ChannelSchema | None:
        equipment = self.equipment_controller.channels_index.get(channel_id)

        if equipment:
            return equipment.to_dict()

        return None

    def get_channels(self) -> List[ChannelSchema]:
        return [
            channel.to_dict()
            for channel in self.equipment_controller.channels_index.values()
        ]

    def create_channel(self, channel_create: ChannelCreatingSchema):
        channel = self.equipment_controller.create_channel(
            **channel_create.model_dump()
        )

        if channel:
            return channel.to_dict()

        return None
