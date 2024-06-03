import pytest
import requests

# URL для тестирования API
base_url = "https://petstore.swagger.io/v2"

# Тест для метода POST /pet
def test_add_new_pet():
    # Подготовка данных для нового питомца
    new_pet_data = {
        "id": 1,  # Уникальный идентификатор питомца
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Rex",
        "photoUrls": [
            "https://www.example.com/rex.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "available"
    }

    # Отправка запроса POST для добавления нового питомца
    response = requests.post(f"{base_url}/pet", json=new_pet_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # проверка данных о добавленном питомце
    added_pet_data = response.json()
    assert added_pet_data["id"] == new_pet_data["id"]
    assert added_pet_data["category"]["id"] == new_pet_data["category"]["id"]
    assert added_pet_data["name"] == new_pet_data["name"]
    assert added_pet_data["photoUrls"] == new_pet_data["photoUrls"]
    assert added_pet_data["tags"][0]["id"] == new_pet_data["tags"][0]["id"]
    assert added_pet_data["tags"][0]["name"] == new_pet_data["tags"][0]["name"]
    assert added_pet_data["status"] == new_pet_data["status"]


# Тест для поиска питомца по ID /pet/{petId}
def test_find_pet_by_id():
    # Уникальный идентификатор питомца, добавленного в предыдущем тесте
    pet_id = 1

    # Отправка запроса GET для получения данных о питомце по его идентификатору
    response = requests.get(f"{base_url}/pet/{pet_id}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка данных о найденном питомце
    found_pet_data = response.json()
    assert found_pet_data["id"] == pet_id

#Тест для проверки обновления информации о питомце
def test_upd_pet():
    upd_pet_data = {
        "id": 1,  # Уникальный идентификатор питомца
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Pex",
        "photoUrls": [
            "https://www.example.com/rex.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "waiting"
    }

    response = requests.put(f"{base_url}/pet", json=upd_pet_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # проверка данных о обновленном питомце
    added_pet_data = response.json()
    assert added_pet_data["id"] == upd_pet_data["id"]
    assert added_pet_data["category"]["id"] == upd_pet_data["category"]["id"]
    assert added_pet_data["name"] == upd_pet_data["name"]
    assert added_pet_data["photoUrls"] == upd_pet_data["photoUrls"]
    assert added_pet_data["tags"][0]["id"] == upd_pet_data["tags"][0]["id"]
    assert added_pet_data["tags"][0]["name"] == upd_pet_data["tags"][0]["name"]
    assert added_pet_data["status"] == upd_pet_data["status"]


# Тест для поиска питомца по статусу /pet/findPetsByStatus
def test_find_pet_by_status():
    # Уникальный идентификатор питомца, добавленного в предыдущем тесте
    pet_status = ["pending"]

    # Отправка запроса GET для получения данных о питомце по его идентификатору
    response = requests.get(f"{base_url}/pet/findByStatus?status={pet_status}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка данных о найденном питомце
    found_pet_status = response.json()
    for pets in found_pet_status:
        assert pets["status"] == pet_status



# Тест для метода DELETE /pet/{petId}
def test_delete_pet():
    # Уникальный идентификатор питомца, добавленного в предыдущем тесте
    pet_id = 1

    # Отправка запроса DELETE для удаления питомца
    response = requests.delete(f"{base_url}/pet/{pet_id}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка успешного удаления питомца
    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 404  # Питомец должен быть удален и не найден
