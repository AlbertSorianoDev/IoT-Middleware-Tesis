from typing import Any, Dict

from src.core.actuator_management.actuator import Actuator
from src.common.plugin_interfaces.switch_plugin_interface import SwitchPluginInterface
from src.core.access_gateway.channel import Channel


class Switch(Actuator):
    PLUGIN_INTERFACE = SwitchPluginInterface

    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: SwitchPluginInterface,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, Any] = None,
        channel: Channel = None,
    ):
        super().__init__(
            label=label,
            description=description,
            plugin_class=plugin_class,
            brand=brand,
            model=model,
            config_params=config_params,
            channel=channel,
        )
