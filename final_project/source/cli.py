"""Bakery running module"""

from typing import Literal, Optional
import click
from final_project.source.logger import log
from final_project.source.pizzas_stuff import (
    NoExistPizzaError, NoExistPizzaSizeError,
    Pizza, Menu,
)


@click.group()
def cli():
    """Entry point for commands"""


@log()
def bake(pizza: Pizza):
    """Bake pizza"""


@log('Delivered for {} seconds!')
def deliver(pizza: Pizza):
    """Deliver pizza"""


@log('Picked up for {} seconds!')
def pickup(pizza: Pizza):
    """Pizza to go"""


@cli.command('menu')
def menu():
    """Show menu"""
    print(Menu())


@cli.command('order')
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
@click.option(
    '--delivery', is_flag=True, default=False,
    help='is necessary delivery or not'
)
def order(
    pizza: str, delivery: bool,
    size: Optional[Literal['L', 'XL']] = 'L1'
):
    """Entry point to order pizza"""

    print('Hello! Welcome to Avito Bakery!')

    # Choosing pizza as order
    try:
        pizza = Menu()[pizza]
    except NoExistPizzaError:
        return

    # Change size if necessary
    try:
        pizza.size = size
    except NoExistPizzaSizeError:
        return

    # Baking pizza
    bake(pizza)

    # Get pizza away
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)

    print('Thank you for your order! See you later!')


if __name__ == '__main__':
    cli()
