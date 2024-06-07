from src.common.property_manager.data_type import DataType


class NumericData(DataType):
    def __init__(self):
        self.value = None

    def set_value(self, value: int | float | None) -> None:
        if isinstance(value, (int, float, type(None))):
            self.value = value
        else:
            raise ValueError("Invalid value for NumericData")

    def get_value(self) -> int | float | None:
        return self.value
