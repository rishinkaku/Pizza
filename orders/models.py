# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    content = models.TextField()
    last_updated_on = models.DateTimeField(auto_now=True)

    waiter = models.ForeignKey(User, related_name='waiters')
    take_the_order_start = models.DateTimeField()
    take_the_order_end = models.DateTimeField()

    chef = models.ForeignKey(User, related_name='chefs')
    prepare_pizza_start = models.DateTimeField()
    prepare_pizza_end = models.DateTimeField()

    bring_pizza_start = models.DateTimeField()
    bring_pizza_end = models.DateTimeField()

    receive_pizza_start = models.DateTimeField()
    receive_pizza_end = models.DateTimeField()

    eat_pizza_start = models.DateTimeField()
    eat_pizza_end = models.DateTimeField()
