# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from viewflow.flow.views import UpdateProcessView

from .models import Order


class TakeTheOrderView(UpdateProcessView):

    def form_valid(self, form):
        order = Order.objects.get(pk=self.activation.process.order.id)
        order.take_the_order_end = datetime.datetime.now()
        order.waiter = self.request.user
        order.save()
        return super().form_valid(form)
