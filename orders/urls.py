from django.urls import path
from orders.views import order, answer

orders_urlpatterns = [
    path('order/', order),
    path('answer/', answer)
]