from abc import abstractmethod

from src.common.property_management.receiver import Receiver


class EventReceiver(Receiver):
    @abstractmethod
    def set_event(self) -> None:
        pass
