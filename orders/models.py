# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from viewflow.models import Process


class Order(models.Model):
    content = models.TextField()
    last_updated_on = models.DateTimeField(auto_now=True)

    waiter = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='waiters', null=True, blank=True)
    take_the_order_start = models.DateTimeField(null=True, blank=True)
    take_the_order_end = models.DateTimeField(null=True, blank=True)

    chef = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='chefs', null=True, blank=True)
    prepare_pizza_start = models.DateTimeField(null=True, blank=True)
    prepare_pizza_end = models.DateTimeField(null=True, blank=True)

    bring_pizza_start = models.DateTimeField(null=True, blank=True)
    bring_pizza_end = models.DateTimeField(null=True, blank=True)

    receive_pizza_start = models.DateTimeField(null=True, blank=True)
    receive_pizza_end = models.DateTimeField(null=True, blank=True)

    eat_pizza_start = models.DateTimeField(null=True, blank=True)
    eat_pizza_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        permissions = (
            ('can_take_the_order', 'Can "Take The Order"'),
        )


class MyPizzaProcess(Process):
    content = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=True, blank=True)
