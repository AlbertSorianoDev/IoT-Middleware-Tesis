from pydantic import BaseModel


class ApplicationCreatingSchema(BaseModel):
    label: str
    admin: bool
