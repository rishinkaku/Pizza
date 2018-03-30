# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from viewflow.flow.views import UpdateProcessView

from .models import Order


class TakeTheOrderView(UpdateProcessView):
    def activation_done(self, *args, **kwargs):
        super().activation_done(*args, **kwargs)
        order = Order.objects.get(pk=self.activation.process.order.id)
        order.take_the_order_end = datetime.datetime.now()
        order.save()
