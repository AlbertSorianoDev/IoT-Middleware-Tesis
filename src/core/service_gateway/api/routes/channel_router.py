from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from typing import List

from src.core.access_gateway import channel
from src.core.service_gateway.services.channel_service import ChannelService
from src.core.service_gateway.api.schemas.channel_schema import ChannelSchema
from src.core.service_gateway.api.schemas.channel_creating_schema import (
    ChannelCreatingSchema,
)


class ChannelRouter:
    channel_router = APIRouter(prefix="/channel", tags=["Channel"])

    @channel_router.get("/{channel_id}", response_model=ChannelSchema)
    async def get_channel_by_id(channel_id: UUID):
        service = ChannelService()
        channel_data = service.get_channel_by_id(channel_id)

        if channel_data:
            return JSONResponse(content=channel_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Equipment not found"}, status_code=404
            )

    @channel_router.get("s", response_model=List[ChannelSchema])
    async def get_channels():
        service = ChannelService()
        channels_data = service.get_channels()

        return JSONResponse(content=channels_data, status_code=200)

    @channel_router.post("", response_model=ChannelSchema)
    async def create_channel(channel_create: ChannelCreatingSchema):
        service = ChannelService()
        channel_data = service.create_channel(channel_create)

        if channel_data:
            return JSONResponse(content=channel_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating equipment"}, status_code=500
            )

    # TODO: Implement update_channel method
    @channel_router.put("/{channel_id}")
    async def update_channel(channel_id: UUID, channel_update: ChannelCreatingSchema):
        channel_data = {
            "id": channel_id,
            **channel_update.model_dump(),
        }

        if channel_data:
            return JSONResponse(content=channel_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error updating channel"}, status_code=500
            )

    # TODO: Implement delete_channel method
    @channel_router.delete("/{channel_id}")
    async def delete_channel(channel_id: UUID):
        if True:
            return JSONResponse(content={"message": "Channel Deleted"}, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error deleting channel"}, status_code=500
            )
