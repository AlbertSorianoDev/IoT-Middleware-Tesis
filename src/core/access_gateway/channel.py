from typing import Dict
from uuid import UUID, uuid4

from src.common.plugin_interfaces.channel_plugin_interface import ChannelPluginInterface


class Channel:
    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: ChannelPluginInterface,
        config_params: Dict[str, str]
    ):
        self.id = uuid4()
        self.label = label
        self.description = description
        self.plugin_class = plugin_class
        self.config_params = config_params

        self.plugin: ChannelPluginInterface | None = None

        self._instance_plugin()

    def _instance_plugin(self):
        self.plugin = self.plugin_class(**self.config_params)

    def on_delete(self):
        self.plugin.on_delete()
        self.plugin = None

    def to_dict(self):
        return {
            "id": str(self.id),
            "label": self.label,
            "description": self.description,
            "plugin_class_name": self.plugin_class.__name__,
            "config_params": self.config_params,
        }
