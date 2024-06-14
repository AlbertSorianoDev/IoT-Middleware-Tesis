from typing import List

from src.common.property_management.data_type import DataType


class Property:
    def __init__(self, data_type: DataType):
        self._subscribers: List[function] = []

        self.data_type: DataType = data_type

    def _publish(self) -> None:
        for observer in self._subscribers:
            observer(self.data_type.get_value())

    def subscribe(self, subscribe_function) -> None:
        self._subscribers.append(subscribe_function)

    def set_value(self, value):
        self.data_type.set_value(value)

    def get_value(self):
        return self.data_type.get_value()
