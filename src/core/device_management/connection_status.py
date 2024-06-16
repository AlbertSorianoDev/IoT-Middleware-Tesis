from enum import Enum


class ConnectionStatus(Enum):
    CONNECTED = 1
    DISCONNECTED = 2
    CONNECTING = 3
    DISCONNECTING = 4
    UNKNOWN = 5
    ERROR = 6
