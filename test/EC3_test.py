import pymongo
import pytest


def calculate_difference_percentage(count1, count2):
    if count2 == 0:
        return float("inf")
    difference = abs(count1 - count2)
    return (difference / count2) * 100


def test_mongo_collections():
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client["IoTDB"]

    actuation_collection = db["actuation"]
    measurement_collection = db["measurement"]

    actuation_count = actuation_collection.count_documents({})
    measurement_count = measurement_collection.count_documents({})

    difference_percentage = calculate_difference_percentage(
        actuation_count, measurement_count
    )

    assert (
        difference_percentage <= 1
    ), f"Diferencia porcentual es {difference_percentage:.2f}%, lo cual es mayor al 1%"


if __name__ == "__main__":
    pytest.main()
