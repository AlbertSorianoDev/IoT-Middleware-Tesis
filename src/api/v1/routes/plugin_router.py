from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List

from src.api.v1.services.plugin_service import PluginService


class PluginRouter:
    plugin_router = APIRouter(prefix="/plugin", tags=["Plugin"])

    @plugin_router.get("s/actuator", response_model=List[str])
    async def get_actuator_plugins_per_type(actuator_type: str):
        service = PluginService()
        plugins = service.get_plugin_names_by_actuator_type(actuator_type)

        return JSONResponse(content=plugins, status_code=200)
