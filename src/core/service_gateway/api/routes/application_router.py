from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID, uuid4

from src.core.service_gateway.api.schemas.application_creating_schema import (
    ApplicationCreatingSchema,
)
from src.core.service_gateway.api.schemas.application_schema import ApplicationSchema
from src.core.service_gateway.api.schemas.credentials_schema import CredentialsSchema


class ApplicationRouter:
    application_router = APIRouter(prefix="/application", tags=["Application"])

    @application_router.post("", response_model=ApplicationSchema)
    async def create_application(application_create: ApplicationCreatingSchema):
        application_data = {
            "id": uuid4(),
            **application_create.model_dump(),
            "created_at": datetime.now(),
            "last_keys_at": datetime.now(),
        }

        if application_data:
            return JSONResponse(content=application_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating application"}, status_code=500
            )

    @application_router.get(
        "/application_id/credentials", response_model=CredentialsSchema
    )
    async def get_application_credentials(application_id: UUID):
        application_data = {
            "api_key": "api_key",
            "api_secret": "api_secret",
        }

        if application_data:
            return JSONResponse(content=application_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error getting application"}, status_code=500
            )

    @application_router.delete("")
    async def delete_application(application_id: UUID):

        if True:
            return JSONResponse(
                content={"message": "Application deleted"}, status_code=200
            )
        else:
            return JSONResponse(
                content={"message": "Error deleting application"}, status_code=500
            )
