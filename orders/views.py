import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from orders.forms import OrderForm
from orders.models import Order
from robots.models import Robot
from customers.models import Customer


# Create your views here.
@require_http_methods(["GET", "POST"])
def order(request):
    """
    Если форма заполнена, то проверяем: есть ли не проданный робот, если есть то, помечаем его проданным.
    Создаем заказ.
    :param request:
    :return:
    """
    form = OrderForm()
    if request.method == 'GET':
        return render(request, 'order/order.html', {'form': form})

    if request.method == 'POST':
        successful = True
        if robot := Robot.objects.filter(Q(serial=request.POST.get('model')) & Q(was_sold=False)):
            successful = False
            robot[0].was_sold = True
            robot[0].save()
        Order.objects.create(customer=Customer.objects.filter(email=request.POST.get('user_email'))[0],
                             robot_serial=request.POST.get('model'),
                             created=datetime.datetime.now(),
                             in_queue=successful
                             )
        return redirect(f'/answer?successful={successful}')


def answer(request):
    answer = 'Успешно' if request.GET.get('successful') == 'False' else 'Ващ заказ добавлен в очередь'
    return render(request, 'order/answer.html', {'answer': answer})
