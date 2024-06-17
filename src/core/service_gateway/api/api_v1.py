from email.mime import application
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.core.service_gateway.api.routes import rule_router
from src.core.service_gateway.api.routes.application_router import ApplicationRouter
from src.core.service_gateway.api.routes.channel_router import ChannelRouter
from src.core.service_gateway.api.routes.equipment_router import EquipmentRouter
from src.core.service_gateway.api.routes.device_router import DeviceRouter
from src.core.service_gateway.api.routes.plugin_router import PluginRouter
from src.core.service_gateway.api.routes.rule_router import RuleRouter


class APIV1:
    api_v1 = FastAPI()

    def __init__(self):
        self.api_v1.title = "IoT Middleware Suite API v1"
        self.api_v1.version = "0.0.1"

        application_router = ApplicationRouter().application_router
        channel_router = ChannelRouter().channel_router
        equipment_router = EquipmentRouter().equipment_router
        device_router = DeviceRouter().device_router
        plugin_router = PluginRouter().plugin_router
        rule_router = RuleRouter().rule_router

        self.api_v1.include_router(application_router)
        self.api_v1.include_router(channel_router)
        self.api_v1.include_router(equipment_router)
        self.api_v1.include_router(device_router)
        self.api_v1.include_router(plugin_router)
        self.api_v1.include_router(rule_router)

    @api_v1.get("/", tags=["Index"], include_in_schema=False)
    async def index():
        return JSONResponse(
            content={"message": "Welcome to IoT Middleware Suite API v1"},
            status_code=200,
        )
