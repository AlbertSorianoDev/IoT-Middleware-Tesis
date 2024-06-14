from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.core.service_gateway.v1.routes.equipment_router import EquipmentRouter
from src.core.service_gateway.v1.routes.device_router import DeviceRouter
from src.core.service_gateway.v1.routes.plugin_router import PluginRouter


class APIV1:
    api_v1 = FastAPI()

    def __init__(self):
        self.api_v1.title = "IoT Middleware Suite API v1"
        self.api_v1.version = "0.0.1"

        equipment_router = EquipmentRouter().equipment_router
        device_router = DeviceRouter().device_router
        plugin_router = PluginRouter().plugin_router

        self.api_v1.include_router(equipment_router)
        self.api_v1.include_router(device_router)
        self.api_v1.include_router(plugin_router)

    @api_v1.get("/", tags=["Index"], include_in_schema=False)
    async def index():
        return JSONResponse(
            content={"message": "Welcome to IoT Middleware Suite API v1"},
            status_code=200,
        )
