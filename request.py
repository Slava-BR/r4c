import requests


# в отчет
requests.post('http://127.0.0.1:8000/api/', data={"model": "BB", "version": "BB", "created": "2023-09-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B1", "version": "BB", "created": "2023-09-27 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B1", "version": "B2", "created": "2023-09-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B2", "version": "B3", "created": "2023-09-27 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B2", "version": "B3", "created": "2023-09-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2023-09-23 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2023-09-24 00:00:01"})
#  Не должно быть в отчете
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2021-09-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2022-09-24 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2020-09-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2019-09-24 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2023-08-28 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2023-08-24 00:00:01"})
requests.post('http://127.0.0.1:8000/api/', data={"model": "B4", "version": "B1", "created": "2021-08-28 00:00:01"})

"""
1. убрать другие запросы
2. ЗАКАЗАТЬ 2 РАЗА B1-B2 - первый заказ пройдет, другой уйдет в очередь
3. ПОсле заказ:
   requests.post('http://127.0.0.1:8000/api/', data={"model": "B1", "version": "B2", "created": "2023-09-28 1:00:01"})
Должно придти письмо на почту пользователя.
"""
