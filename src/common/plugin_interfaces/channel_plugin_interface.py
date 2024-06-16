from abc import ABC, abstractmethod


class ChannelPluginInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def on_delete(self):
        pass
