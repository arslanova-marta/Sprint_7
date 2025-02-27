import requests
import allure
import pytest
import json
from data import OrderData
from urls import Urls


class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными параметрами цвета')
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey_1, OrderData.order_data_black_2,
        OrderData.order_data_two_colors_3, OrderData.order_data_no_colors_4
    ])
    def test_order_crete_color_parametrize_success(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.URL_orders_create, data=order_data, headers=headers, timeout=5)
        assert response.status_code == 201 and 'track' in response.text
