import pytest
import requests

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2"

# Тест создания заказа
def test_place_order(api_url):
    # Подготовка данных для заказа
    order_data = {
        "id": 1,  # Уникальный идентификатор заказа
        "petId": 1,  # Уникальный идентификатор питомца
        "quantity": 1,
        "shipDate": "2024-02-05T12:00:00Z",
        "status": "placed",
        "complete": True
    }

    # Отправка запроса POST для размещения заказа
    response = requests.post(f"{api_url}/store/order", json=order_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка данных о размещенном заказе
    added_order_data = response.json()
    assert added_order_data["id"] == order_data["id"]

# Тест поиска заказа
def test_find_order_by_id(api_url):
    # Уникальный идентификатор заказа, добавленного в предыдущем тесте
    order_id = 1

    # Отправка запроса GET для поиска заказа по его идентификатору
    response = requests.get(f"{api_url}/store/order/{order_id}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка данных о найденном заказе
    found_order_data = response.json()
    assert found_order_data["id"] == order_id



# Тест проверки несуществующего заказа
def test__no_find_order_by_id(api_url):
    # Уникальный заказа, которого нет
    order_id = 9989888989

    # Отправка запроса GET для поиска заказа по его идентификатору
    response = requests.get(f"{api_url}/store/order/{order_id}")

    # Проверка статус-кода ответа
    assert response.status_code == 404

# Тест удаления заказа
def test_delete_order(api_url):
    # Уникальный идентификатор заказа, добавленного в предыдущем тесте
    order_id = 1

    # Отправка запроса DELETE для удаления заказа
    response = requests.delete(f"{api_url}/store/order/{order_id}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка успешного удаления заказа
    response = requests.get(f"{api_url}/store/order/{order_id}")
    assert response.status_code == 404  # Заказ должен быть удален и не найден

# Тест получения inventory
def test_get_inventory(api_url):
    # Отправка запроса GET для получения инвентаря питомцев по статусу
    response = requests.get(f"{api_url}/store/inventory")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка содержимого ответа
    inventory_data = response.json()
    assert isinstance(inventory_data, dict)
    assert len(inventory_data) > 0
