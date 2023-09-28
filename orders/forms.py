from django import forms
from django.forms import ChoiceField
from robots.models import Robot
from customers.models import Customer


class OrderForm(forms.Form):
    """
    Форма из двух полей с выбором из существующих записей
    - user_email
    - model
    """

    def __init__(self):
        super().__init__()
        self.fields["user_email"] = ChoiceField(choices=tuple([(c.email, c.email) for c in Customer.objects.all()]))
        self.fields["model"] = ChoiceField(choices=tuple([(r.serial, r.serial) for r in Robot.objects.all().distinct('serial')]))
