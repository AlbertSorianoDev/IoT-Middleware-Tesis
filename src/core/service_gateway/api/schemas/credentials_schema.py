from pydantic import BaseModel


class CredentialsSchema(BaseModel):
    api_key: str
    api_secret: str
