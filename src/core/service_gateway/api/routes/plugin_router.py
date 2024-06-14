from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List, Dict

from src.core.service_gateway.services.plugin_service import PluginService


class PluginRouter:
    plugin_router = APIRouter(prefix="/plugin", tags=["Plugin"])

    @plugin_router.get("s/actuator", response_model=List[str])
    async def get_actuator_plugins_per_type(actuator_type: str):
        service = PluginService()
        plugins = service.get_plugin_names_by_actuator_type(actuator_type)

        return JSONResponse(content=plugins, status_code=200)

    @plugin_router.get("/config_params", response_model=Dict[str, str])
    async def get_plugin_configuration_params(plugin_name: str):
        service = PluginService()
        params = service.get_plugin_configuration_params(plugin_name)

        return JSONResponse(content=params, status_code=200)
