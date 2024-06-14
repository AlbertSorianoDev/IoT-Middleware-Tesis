from uuid import UUID

from src.core.device_management.device import Device


class Sensor(Device):
    def __init__(
        self, *, label: str, description: str, brand: str = None, model: str = None
    ):
        super().__init__(label=label, description=description, brand=brand, model=model)
        self.unit = None
        self.value = None

    def to_dict(self):
        return {
            **super().to_dict(),
            "unit": self.unit,
            "value": self.value,
        }

    def __str__(self):
        return str(self.to_dict())

    def read(self):
        pass
