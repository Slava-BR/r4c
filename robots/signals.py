from django.core.mail import send_mail
from django.db.models import Min, Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from R4C.settings import EMAIL_HOST_USER
from orders.models import Order
from robots.models import Robot

TEXT_MESSAGE = ("Добрый день! \nНедавно вы интересовались нашим роботом модели {}, версии {}."
                " \nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами")


@receiver(post_save, sender=Robot)
def send_email(sender, instance, created, **kwargs):
    """
    Находит первого пользователя в очереди.
    Устанавливаем у robot флаг was_sold = True и у order - in_queue = False

    :param sender:Модельный класс.
    :param instance: значения объекта
    :param created: boolean, создан - True, обновлен - False
    :param kwargs:
    :return:
    """
    orders = Order.objects.filter(Q(in_queue=True) & Q(robot_serial=instance.serial))
    if orders and created:
        instance.was_sold = True
        instance.save()
        first_order = orders.get(created=orders.aggregate(min=Min('created'))['min'])
        send_mail(
            'Робот готов!)',
            TEXT_MESSAGE.format(instance.model, instance.version),
            EMAIL_HOST_USER,
            [first_order.customer.email],
            fail_silently=False, )
