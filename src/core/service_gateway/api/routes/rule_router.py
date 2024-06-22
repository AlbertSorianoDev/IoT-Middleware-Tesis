from datetime import datetime
from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID, uuid4

from src.core.service_gateway.api.schemas.rule_creating_schema import RuleCreatingSchema
from src.core.service_gateway.api.schemas.rule_schema import RuleSchema


class RuleRouter:
    rule_router = APIRouter(prefix="/rule", tags=["Rule"])

    @rule_router.get("/{rule_id}", response_model=RuleSchema)
    async def get_rule_by_id(rule_id: UUID):
        rule_data = {
            "id": rule_id,
            "name": "Rule Name",
            "description": "Rule Description",
            "created_at": datetime.now(),
        }

        if rule_data:
            return JSONResponse(content=rule_data, status_code=200)
        else:
            return JSONResponse(content={"message": "Rule not found"}, status_code=404)

    @rule_router.get("s", response_model=List[RuleSchema])
    async def get_rules():
        rule_data = [
            {
                "id": uuid4(),
                "name": "Rule Name",
                "description": "Rule Description",
                "created_at": datetime.now(),
            },
            {
                "id": uuid4(),
                "name": "Rule Name",
                "description": "Rule Description",
                "created_at": datetime.now(),
            },
        ]

        return JSONResponse(content=rule_data, status_code=200)

    @rule_router.post("", response_model=RuleSchema)
    async def create_rule(rule_create: RuleCreatingSchema):
        rule_data = {
            "id": str(uuid4()),
            **rule_create.model_dump(),
        }

        rule_data["trigger_device_id"] = rule_data["trigger_device_id"].__str__()
        rule_data["affected_device_id"] = rule_data["affected_device_id"].__str__()

        if rule_data:
            return JSONResponse(content=rule_data, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error creating Rule"}, status_code=500
            )

    @rule_router.delete("")
    async def delete_rule(rule_id: UUID):

        if True:
            return JSONResponse(content={"message": "Rule deleted"}, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Error deleting Rule"}, status_code=500
            )
