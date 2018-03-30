from viewflow import flow, frontend
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import MyPizzaProcess, Order
from .views import TakeTheOrderView


@frontend.register
class MyPizzaFlow(Flow):
    process_class = MyPizzaProcess

    start = (
        flow.Start(CreateProcessView, fields=['content'])
        .Next(this.order_pizza)
    )

    order_pizza = (
        flow.Handler(this.save_content_to_order)
        .Next(this.split_after_order)
    )

    split_after_order = (
        flow.Split()
        .Next(this.wait_15_minutes)
        .Next(this.take_the_order)
    )

    wait_15_minutes = flow.End()    # TODO

    take_the_order = (
        flow.View(TakeTheOrderView)
        .Next(this.prepare_pizza)
    )

    prepare_pizza = (
        flow.View(
            UpdateProcessView
        ).Next(this.bring_pizza)
    )

    bring_pizza = (
        flow.End()          # TODO continue
    )

    def save_content_to_order(self, activation):
        order = Order()
        order.content = activation.process.content
        order.save()
        activation.process.order = order
        activation.process.save()
