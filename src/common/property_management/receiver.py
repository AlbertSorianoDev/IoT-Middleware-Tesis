from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def on_delete(self):
        pass
