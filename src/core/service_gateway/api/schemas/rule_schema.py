from uuid import UUID

from src.core.service_gateway.api.schemas.rule_creating_schema import RuleCreatingSchema


class RuleSchema(RuleCreatingSchema):
    id: UUID
