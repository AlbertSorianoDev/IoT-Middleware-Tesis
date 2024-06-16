from uuid import UUID, uuid4
from typing import List

from src.core.device_management.device import Device
from src.core.access_gateway.channel import Channel


class Equipment:
    def __init__(self, *, label: str, description: str, channel: Channel):
        self.id: UUID = uuid4()
        self.label: str = label
        self.description: str = description
        self.channel: Channel = channel

        self.devices: List[Device] = []
        self.location = None

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return f"Equipment({self.label})"

    def to_dict(self):
        return {
            "id": str(self.id),
            "label": self.label,
            "description": self.description,
            "channel_id": str(self.channel.id),
        }

    def add_device(self, device: Device):
        self.devices.append(device)
