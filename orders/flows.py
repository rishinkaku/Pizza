from viewflow import flow, frontend
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import MyPizzaProcess


@frontend.register
class MyPizzaFlow(Flow):
    process_class = MyPizzaProcess

    # Start will be order_pizza
    start = (
        flow.Start(
            CreateProcessView,
            fields=['content']
        ).Next(this.split_after_order)
    )

    split_after_order = (
        flow.Split()
        .Next(this.wait_15_minutes)
        .Next(this.take_the_order)
    )

    wait_15_minutes = flow.End()    # TODO

    take_the_order = (
        flow.View(
            UpdateProcessView
        ).Next(this.prepare_pizza)
    )

    prepare_pizza = (
        flow.View(
            UpdateProcessView
        ).Next(this.bring_pizza)
    )

    bring_pizza = (
        flow.End()          # TODO continue
    )
