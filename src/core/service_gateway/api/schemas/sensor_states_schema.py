from pydantic import BaseModel


class SensorStatesSchema(BaseModel):
    value: str | int | float
    unit: str
