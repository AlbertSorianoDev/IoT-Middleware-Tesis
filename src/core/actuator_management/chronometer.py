from typing import Any, Dict

from src.core.actuator_management.actuator import Actuator
from src.common.plugin_interfaces.dimmer_plugin_interface import DimmerPluginInterface
from src.common.property_management.property import Property


# TODO: Implement the class correctly (actual dimmer copy)
class Chronometer(Actuator):
    PLUGIN_INTERFACE = DimmerPluginInterface

    # States definition
    DIMMER_STATE = "dimmer_state"

    # Dimmer state values
    BRIGHTNESS_STATE = (0, 100)

    def __init__(
        self,
        *,
        label: str,
        description: str,
        plugin_class: DimmerPluginInterface,
        brand: str = None,
        model: str = None,
        config_params: Dict[str, Any] = None,
    ):
        super().__init__(
            label=label,
            description=description,
            plugin_class=plugin_class,
            brand=brand,
            model=model,
            config_params=config_params,
        )

        self.dimmer_property: Property | None = None

    @property
    def states(self):
        return {
            **super().states,
            self.DIMMER_STATE: self._brightness_state(),
        }

    def _instance_plugin(self):
        super()._instance_plugin()
        self.dimmer_property = self.plugin._get_dimmer_property()

    def _brightness_state(self):
        if self.dimmer_property is None:
            return self.UNKNOWN

        property_value = self.dimmer_property.get_value()

        if property_value in range(*self.BRIGHTNESS_STATE):
            return property_value

        return self.UNKNOWN

    @classmethod
    def states_info(cls):
        states = super().states_info()
        return states.update(
            {
                cls.DIMMER_STATE: {
                    "description": "The dimmer state, discrete value.",
                    "values": f"dimmer between {cls.BRIGHTNESS_STATE} or {cls.UNKNOWN}",
                }
            }
        )

    def set_brigthness(self, value: int):
        self.plugin.set_brigthness(value)
