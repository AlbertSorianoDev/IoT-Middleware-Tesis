from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.api.v1.routes.equipment_router import EquipmentRouter


class APIV1:
    api_v1 = FastAPI()

    def __init__(self):
        self.api_v1.title = "IoT Middleware Suite API v1"
        self.api_v1.version = "0.0.1"

        equipment_router = EquipmentRouter().equipment_router
        self.api_v1.include_router(equipment_router)

    @api_v1.get("/", tags=["Index"], include_in_schema=False)
    async def index():
        return JSONResponse(
            content={"message": "Welcome to IoT Middleware Suite API v1"},
            status_code=200,
        )
