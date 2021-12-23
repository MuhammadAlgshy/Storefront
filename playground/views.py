from django.shortcuts import render
from django.db.models import Value, F, ExpressionWrapper, DecimalField
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import *
from tags.models import TaggedItem


def index(request):
    return render(request, 'index.html')


def say_hello(request):

    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = -1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    return render(request, 'hello.html', {'name': 'Mohammad'})
