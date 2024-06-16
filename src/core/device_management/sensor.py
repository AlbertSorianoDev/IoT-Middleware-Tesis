from uuid import UUID
from typing import Dict

from src.core.device_management.device import Device
from src.core.access_gateway.channel import Channel
from src.common.plugin_interfaces.sensor_plugin_interface import SensorPluginInterface
from src.common.property_management.property import Property


class Sensor(Device):
    # Unknown general state
    UNKNOWN = "UNKNOWN"

    def __init__(
        self,
        *,
        label: str,
        description: str,
        brand: str = None,
        model: str = None,
        plugin_class: SensorPluginInterface,
        channel: Channel,
        config_params: Dict[str, str] = None,
    ):
        super().__init__(
            label=label,
            description=description,
            brand=brand,
            model=model,
            plugin_class=plugin_class,
            config_params=config_params,
            channel=channel,
        )

        self.sensor_property: Property | None = None

        self._instance_plugin()

    @property
    def states(self):
        return {
            "value": (
                self.sensor_property.get_value()
                if self.sensor_property
                else self.UNKNOWN
            ),
            "unit": "u",
        }

    def _instance_plugin(self):
        self.plugin: SensorPluginInterface = self.plugin_class(**self.config_params)
        self.plugin.set_channel_plugin(self.channel.plugin)
        self.sensor_property = self.plugin.get_sensor_property()
