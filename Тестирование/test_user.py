import pytest
import requests

@pytest.fixture
def api_url():
    return "https://petstore.swagger.io/v2"  # Замените на URL вашего API

# Теста для создания пользователей из массива
def test_create_users_with_array(api_url):
    # Подготовка данных для создания пользователей
    user_data = [
        {"id": 1, "username": "user1"},
        {"id": 2, "username": "user2"}
    ]

    # Отправка запроса POST для создания пользователей
    response = requests.post(f"{api_url}/user/createWithArray", json=user_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

# Теста для создания пользователей из списка
def test_create_users_with_list(api_url):
    # Подготовка данных для создания пользователей
    user_data = [
        {"id": 1, "username": "user1"},
        {"id": 2, "username": "user2"}
    ]

    # Отправка запроса POST для создания пользователей
    response = requests.post(f"{api_url}/user/createWithList", json=user_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

# Теста для поиска пользовтеля по имени
def test_get_user_by_username(api_url):
    # Имя пользователя для поиска
    username = "user1"

    # Отправка запроса GET для получения пользователя по имени пользователя
    response = requests.get(f"{api_url}/user/{username}")

    # Проверка статус-кода ответа
    assert response.status_code == 200

    # Проверка содержимого ответа
    user_data = response.json()
    assert user_data["username"] == username

# Теста для проверки обновления пользователя
def test_update_user(api_url):
    # Имя пользователя для обновления
    username = "user1"

    # Новые данные пользователя
    new_user_data = {"id": 1, "username": "updated_user1"}

    # Отправка запроса PUT для обновления пользователя
    response = requests.put(f"{api_url}/user/{username}", json=new_user_data)

    # Проверка статус-кода ответа
    assert response.status_code == 200

# Тест для проверки удаления пользоватлея
def test_delete_user(api_url):
    # Имя пользователя для удаления
    username = "user2"

    # Отправка запроса DELETE для удаления пользователя
    response = requests.delete(f"{api_url}/user/{username}")

    # Проверка статус-кода ответа
    assert response.status_code == 200
