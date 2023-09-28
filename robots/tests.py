from django.test import TestCase
from robots.validator import data_is_valid


class ValidTestClass(TestCase):
    # Данные введены правильные
    def test_correct_data1(self):
        self.assertEqual(data_is_valid(model="R2", version="D2", created="2022-12-31 23:59:59"), True)

    def test_correct_data2(self):
        self.assertEqual(data_is_valid(model="13", version="XS", created="2023-01-01 00:00:00"), True)

    def test_correct_data3(self):
        self.assertEqual(data_is_valid(model="X5", version="LT", created="2023-01-01 00:00:01"), True)

    # неправильные значения.
    def test_incorrect_length_value_3(self):
        self.assertEqual(data_is_valid(model="X55", version="LT", created="2023-01-01 00:00:01"), False)

    def test_incorrect_length_value_0(self):
        self.assertEqual(data_is_valid(model="", version="LT", created="2023-01-01 00:00:01"), False)

    def test_invalid_symbol(self):
        self.assertEqual(data_is_valid(model="!5", version="LT", created="2023-01-01 00:00:01"), False)

