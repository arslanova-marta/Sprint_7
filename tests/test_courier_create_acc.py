import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:

    def setup_method(self):
        self.courier_id = None  # Переменная для хранения ID курьера

    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    @allure.description('Happy path. Проверяются код и тело ответа.')
    def test_create_courier_account_success(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, json=payload)  # Используем json вместо data
        assert response.status_code == 201 and response.json() == {'ok': True}

        # Сохраняем ID курьера для удаления после теста
        response_data = response.json()
        self.courier_id = response_data.get("id")

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, json=payload)  # Используем json
        assert response.status_code == 409 and response.json() == {'message': 'Этот логин уже используется'}

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, json=empty_credentials)  # Используем json
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для создания '
                                                                              'учетной записи'}

    @allure.title('Проверка успешного создания аккаунта курьера с дополнительным полем lastName')
    @allure.description('Проверяется создание курьера с дополнительным полем lastName.')
    def test_create_courier_account_with_additional_field(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname(),
            'lastName': "Testovich"  # Дополнительное поле lastName
        }
        response = requests.post(Urls.URL_courier_create, json=payload)  # Используем json
        assert response.status_code == 201 and response.json() == {'ok': True}

        # Сохраняем ID курьера для удаления после теста
        response_data = response.json()
        self.courier_id = response_data.get("id")

    def teardown_method(self):
        # Удаляем созданного курьера после теста, если он был создан
        if self.courier_id:
            response = requests.delete(f"{Urls.URL_courier_delete}/{self.courier_id}")
            assert response.status_code == 200  # Убедись, что курьер был удалён
