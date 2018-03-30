# Generated by Django 2.0.3 on 2018-03-30 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewflow', '0006_i18n'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPizzaProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('take_the_order_start', models.DateTimeField(blank=True, null=True)),
                ('take_the_order_end', models.DateTimeField(blank=True, null=True)),
                ('prepare_pizza_start', models.DateTimeField(blank=True, null=True)),
                ('prepare_pizza_end', models.DateTimeField(blank=True, null=True)),
                ('bring_pizza_start', models.DateTimeField(blank=True, null=True)),
                ('bring_pizza_end', models.DateTimeField(blank=True, null=True)),
                ('receive_pizza_start', models.DateTimeField(blank=True, null=True)),
                ('receive_pizza_end', models.DateTimeField(blank=True, null=True)),
                ('eat_pizza_start', models.DateTimeField(blank=True, null=True)),
                ('eat_pizza_end', models.DateTimeField(blank=True, null=True)),
                ('chef', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chefs', to=settings.AUTH_USER_MODEL)),
                ('waiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waiters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mypizzaprocess',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
