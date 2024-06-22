import pytest
import httpx
import asyncio

BASE_URL = "http://192.168.3.11:8000/api/v1"


async def create_channel(client):
    response = await client.post(
        f"{BASE_URL}/channel",
        json={
            "label": "MQTTChannel",
            "description": "MQTTLocal",
            "plugin_class_name": "MQTTClient",
            "config_params": {
                "client_id": "str",
                "host": "192.168.3.100",
                "port": 1883,
                "username": "soriano",
                "password": "0000",
            },
        },
    )
    response.raise_for_status()
    return response.json()["id"]


async def create_equipment(client, channel_id):
    response = await client.post(
        f"{BASE_URL}/equipment",
        json={
            "label": "EquipoMQTT Temperatura",
            "description": "Sensores virtuales de temperatura",
            "channel_id": channel_id,
        },
    )
    response.raise_for_status()
    return response.json()["id"]


async def create_sensor(client, equipment_id, i):
    response = await client.post(
        f"{BASE_URL}/device/sensor",
        json={
            "equipment_id": equipment_id,
            "label": f"MQTTSensor Temperatura {i}",
            "description": "Sensor de Temperatura MQTT Test",
            "plugin_class_name": "MQTTNumericSensor",
            "brand": "GenericMQTT",
            "model": "ESP8266",
            "config_params": {"topic": f"temperature{i}", "qos": 0},
        },
    )
    response.raise_for_status()


async def create_sensors(client, equipment_id, start_index):
    tasks = [
        create_sensor(client, equipment_id, i)
        for i in range(start_index, start_index + 5)
    ]
    await asyncio.gather(*tasks)


@pytest.mark.asyncio
async def test_create_mqtt_setup():
    async with httpx.AsyncClient() as client:
        # Crear canal
        channel_id = await create_channel(client)

        # Crear equipo
        equipment_id = await create_equipment(client, channel_id)

        # Crear sensores en paralelo
        tasks = [create_sensors(client, equipment_id, i * 5) for i in range(100)]
        await asyncio.gather(*tasks)

        # Validar la cantidad de dispositivos creados
        response = await client.get(f"{BASE_URL}/devices/{equipment_id}")
        response.raise_for_status()
        devices = response.json()

        assert (
            len(devices) == 500
        ), f"Se esperaban 500 dispositivos, pero se encontraron {len(devices)}"


if __name__ == "__main__":
    pytest.main()
