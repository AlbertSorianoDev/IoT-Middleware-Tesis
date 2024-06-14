from abc import ABC, abstractmethod


class DataType(ABC):
    @abstractmethod
    def set_value(self, value):
        pass

    @abstractmethod
    def get_value(self):
        pass
