import pytest
import paho.mqtt.client as mqtt
import paho.mqtt.enums as mqtt_enums
import pymongo
import asyncio

MQTT_HOST = "192.168.3.100"
MQTT_PORT = 1883
MONGO_URI = "mongodb://192.168.3.11:27017"
DATABASE_NAME = "IoTDB"
MEASUREMENT_COLLECTION = "measurement"
TOPIC_BASE = "temperature"

NUM_SENSORS = 500
MESSAGE = "22.6789"
INTERVAL = 1
DURATION = 10
EXPECTED_MESSAGES = NUM_SENSORS * DURATION


def get_collection_count(collection):
    return collection.count_documents({})


def calculate_difference_percentage(count1, count2):
    if count2 == 0:
        return float("inf")
    difference = abs(count1 - count2)
    return (difference / count2) * 100


async def publish_messages():
    client = mqtt.Client(mqtt_enums.CallbackAPIVersion.VERSION2)
    client.connect(MQTT_HOST, MQTT_PORT, 60)

    def publish():
        for i in range(NUM_SENSORS):
            topic = f"{TOPIC_BASE}{i}"
            client.publish(topic, MESSAGE)

    client.loop_start()
    for _ in range(DURATION):
        publish()
        await asyncio.sleep(INTERVAL)
    client.loop_stop()

    client.disconnect()


@pytest.mark.asyncio
async def test_mqtt_simulation():
    # Conectar a MongoDB
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    measurement_collection = db[MEASUREMENT_COLLECTION]

    # Limpia la colección measurement antes de la prueba
    measurement_collection.delete_many({})

    # Publicar mensajes MQTT
    await publish_messages()

    # Esperar unos segundos para asegurar que los datos se hayan almacenado
    await asyncio.sleep(5)

    # Obtener la cantidad de documentos en la colección measurement
    measurement_count = get_collection_count(measurement_collection)

    # Calcular la diferencia en porcentaje
    difference_percentage = calculate_difference_percentage(
        EXPECTED_MESSAGES, measurement_count
    )

    # Evaluar si la diferencia es menor o igual al 1%
    assert (
        difference_percentage <= 1
    ), f"Diferencia porcentual es {difference_percentage:.2f}%, lo cual es mayor al 1%"

    # Imprimir resultados
    print(f"Cantidad de datos esperados: {EXPECTED_MESSAGES}")
    print(f"Cantidad de datos recibidos: {measurement_count}")
    print(f"Diferencia porcentual: {difference_percentage:.2f}%")


if __name__ == "__main__":
    pytest.main()
