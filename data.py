class Data:
    valid_login = 'Max1994'
    valid_password = 'qwerty'
    valid_firstname = 'Max'
    valid_courier_data = {'login': 'Max1994', 'password': 'qwerty', 'firstName': 'Max'}
    courier_data_without_name = {'login': 'Max1994', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Max1994', 'password': '123456'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Геральт',
        'lastName': 'ИзРивии',
        'address': 'Новиградский проспект, 16',
        'metroStation': 8,
        'phone': '+78005553535',
        'rentTime': 3,
        'deliveryDate': '2024-06-26',
        'comment': 'Хм, распогодилось :)',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Йеннифэр',
        'lastName': 'изВенгерберга',
        'address': 'Туссент, улица Яблоневая',
        'metroStation': 10,
        'phone': '+78888888888',
        'rentTime': 7,
        'deliveryDate': '2024-06-28',
        'comment': '— Правда, — сказала пустельга, — это осколок льда.',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Цирилла Фиона',
        'lastName': 'Рианнон',
        'address': 'Шалфей и Розмарин',
        'metroStation': 15,
        'phone': '+70009991122',
        'rentTime': 1,
        'deliveryDate': '2024-06-30',
        'comment': 'Ужасненько хочется покататься!',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Калантэ',
        'lastName': 'ArdRhena',
        'address': 'Замок Цинтры',
        'metroStation': 20,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Сопротивляться судьбе может быть не менее рискованно, чем отдать себя в ее руки',
        'color': []
    }
