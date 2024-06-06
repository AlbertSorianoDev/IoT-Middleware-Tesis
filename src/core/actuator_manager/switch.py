from typing import Any, Dict

from src.core.actuator_manager.actuator import Actuator
from src.common.interfaces.switch_plugin_interface import SwitchPluginInterface


class Switch(Actuator):
    plugin_interface = SwitchPluginInterface

    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: SwitchPluginInterface,
        brand: str = None,
        model: str = None,
        attributes: Dict[str, Any] = None,
    ):
        super().__init__(
            label=label,
            description=description,
            plugin_class=plugin_class,
            brand=brand,
            model=model,
            attributes=attributes,
        )
