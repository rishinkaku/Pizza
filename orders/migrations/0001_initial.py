# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('take_the_order_start', models.DateTimeField()),
                ('take_the_order_end', models.DateTimeField()),
                ('prepare_pizza_start', models.DateTimeField()),
                ('prepare_pizza_end', models.DateTimeField()),
                ('bring_pizza_start', models.DateTimeField()),
                ('bring_pizza_end', models.DateTimeField()),
                ('receive_pizza_start', models.DateTimeField()),
                ('receive_pizza_end', models.DateTimeField()),
                ('eat_pizza_start', models.DateTimeField()),
                ('eat_pizza_end', models.DateTimeField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chefs', to=settings.AUTH_USER_MODEL)),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
