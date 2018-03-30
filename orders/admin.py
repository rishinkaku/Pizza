# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Order

admin.site.register(Order, admin.ModelAdmin)
