from abc import abstractmethod

from src.common.property_management.receiver import Receiver


class RequestReceiver(Receiver):
    @abstractmethod
    def request(self) -> None:
        pass
