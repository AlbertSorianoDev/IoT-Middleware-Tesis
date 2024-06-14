from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pkgutil import walk_packages
from importlib import import_module

from src.core.service_gateway.v1.api_v1 import APIV1
from src.core.device_managment.equipment_controller import EquipmentController


class LifeCicle:

    tags_metadata = [
        {
            "name": "API v1 Documentation",
            "description": "API version 1. Check the docs at /api/v1/docs.",
        },
    ]

    app = FastAPI(openapi_tags=tags_metadata)

    def __init__(self):

        # Pre-import all modules to avoid import errors
        self.pre_import_modules("src")

        # Device Manager Initialization
        self.equipment_control = EquipmentController("./plugins")

        # FastAPI Configuration
        self.app.title = "IoT Middleware Suite Service"
        self.app.version = "1.0.0"

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # APIs Initialization
        api_v1 = APIV1().api_v1

        # Mount APIs
        self.app.mount("/api/v1", api_v1)

    def pre_import_modules(self, package_name):
        package = import_module(package_name)
        package_path = package.__path__
        for _, module_name, is_pkg in walk_packages(package_path):
            full_module_name = f"{package_name}.{module_name}"
            import_module(full_module_name)
            if is_pkg:
                self.pre_import_modules(full_module_name)

    @app.get("/", tags=["Index"], include_in_schema=False)
    async def index():
        return JSONResponse(
            content={"message": "Welcome to IoT Middleware Service"},
            status_code=200,
        )
