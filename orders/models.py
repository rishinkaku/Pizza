# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from viewflow.models import Process


class MyPizzaProcess(Process):
    content = models.TextField()


class Order(models.Model):
    content = models.TextField()
    last_updated_on = models.DateTimeField(auto_now=True)

    waiter = models.ForeignKey(User, related_name='waiters',
                               null=True, blank=True)
    take_the_order_start = models.DateTimeField(null=True, blank=True)
    take_the_order_end = models.DateTimeField(null=True, blank=True)

    chef = models.ForeignKey(User, related_name='chefs',
                             null=True, blank=True)
    prepare_pizza_start = models.DateTimeField(null=True, blank=True)
    prepare_pizza_end = models.DateTimeField(null=True, blank=True)

    bring_pizza_start = models.DateTimeField(null=True, blank=True)
    bring_pizza_end = models.DateTimeField(null=True, blank=True)

    receive_pizza_start = models.DateTimeField(null=True, blank=True)
    receive_pizza_end = models.DateTimeField(null=True, blank=True)

    eat_pizza_start = models.DateTimeField(null=True, blank=True)
    eat_pizza_end = models.DateTimeField(null=True, blank=True)
