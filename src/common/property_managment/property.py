from typing import List

from src.common.property_managment.data_type import DataType


class Property:
    def __init__(self, data_type: DataType):
        self._subcribers: List[function] = []

        self.data_type: DataType = data_type

    def _publish(self) -> None:
        for observer in self._subcribers:
            observer(self.data_type.get_value())

    def subcribe(self, subscribe_function) -> None:
        self._subcribers.append(subscribe_function)

    def set_value(self, value):
        self.data_type.set_value(value)

    def get_value(self):
        return self.data_type.get_value()
