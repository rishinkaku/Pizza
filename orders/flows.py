from viewflow import flow, frontend
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import MyPizzaProcess, Order
from .views import TakeTheOrderView


def available_in_group(group_name):
    """Checks if user belongs to a certain group. Returns a function.
    """
    def _internal(user):
        return user.groups.filter(name=group_name).exists()
    return _internal


@flow.flow_func
def trigger_triggered(activation, *args, **kwargs):
    print("Calling trigger_triggered")
    activation.prepare()
    activation.done()


@frontend.register
class MyPizzaFlow(Flow):
    process_class = MyPizzaProcess

    start = (
        flow.Start(CreateProcessView, fields=['content'])
        .Available(available_in_group('customers'))
        .Next(this.order_pizza)
    )

    order_pizza = (
        flow.Handler(this.save_content_to_order)
        .Next(this.external_join)
    )

    # To run this, we need to know which task we are specifically referring to
    # This can be done by querying the database

    my_trigger = (
        flow.Function(trigger_triggered,
                      task_loader=lambda flow_task, task: task)
        .Next(this.external_join)
    )

    external_join = (
        flow.Join()
        .Next(this.take_the_order)
    )

    take_the_order = (
        flow.View(TakeTheOrderView, fields=['table_location'])
        .Permission('users.can_take_the_order')
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
