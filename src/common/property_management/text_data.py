from src.common.property_management.data_type import DataType


class TextData(DataType):
    def __init__(self):
        self.value = None

    def set_value(self, value: str | None) -> None:
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Invalid value for TextData")

    def get_value(self) -> str | None:
        return self.value
