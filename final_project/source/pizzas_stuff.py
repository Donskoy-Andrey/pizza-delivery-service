"""Bakery stuff declaration"""

from typing import Literal
from dataclasses import dataclass
import numpy as np


class NoExistPizzaSizeError(KeyError):
    """Not found such pizza's size"""


class NoExistPizzaError(KeyError):
    """Not found pizza in menu"""


class Pizza:
    """Standard class for pizza"""

    def __init__(
        self, pizza_name: str, ingredients: list[str],
    ):
        self.pizza_name = pizza_name
        self.ingredients = ingredients

    def __eq__(self, other: 'Pizza'):
        if self.pizza_name == other.pizza_name:
            return True
        return False

    def __str__(self):
        ingredients_list = ', '.join(self.ingredients)
        return f'{self.pizza_name}: {ingredients_list}.'


class SpecificSizePizza(Pizza):
    """Class for different shapes of pizza"""

    def __init__(
        self, pizza_name: str, ingredients: list[str],
    ):
        super().__init__(pizza_name, ingredients)

        self._size = None
        self._ingredients_amount = None

    @property
    def size(self):
        """Get pizza's size"""
        return self._size

    @size.setter
    def size(self, size: Literal['L', 'XL']):
        """Set pizza's size"""

        if size not in ['L', 'XL', None]:
            print('Pizza`s size should be one of the [`L`, `XL`].')
            raise NoExistPizzaSizeError

        self._size = size
        if self._size == 'L':
            self.ingredients_amount = np.random.randint(
                1, 5, size=len(self.ingredients)
            )
        elif self._size == 'XL':
            self.ingredients_amount = np.random.randint(
                5, 10, size=len(self.ingredients)
            )

    @property
    def ingredients_amount(self):
        """Get pizza's ingredients amount"""
        return self._ingredients_amount

    @ingredients_amount.setter
    def ingredients_amount(self, amounts: list[int]):
        """Set pizza's ingredients amount"""
        self._ingredients_amount = amounts

    def __iter__(self):
        return iter(zip(self.ingredients, self.ingredients_amount))

    def get_receipt(self):
        """
        Print pizza's receipt. Template:
        `Receipt: {`ingredient1: amount1`, `ingredient2: amount2`, ...}`
        """
        print(f'Receipt: {dict(self)}')


@dataclass
class Menu:
    """Class for restaurant's Menu"""

    pizzas = [
        SpecificSizePizza(
            'Margherita',
            ['tomato sauce', 'mozzarella', 'tomatoes']
        ),
        SpecificSizePizza(
           'Pepperoni',
           ['tomato sauce', 'mozzarella', 'pepperoni']
        ),
        SpecificSizePizza(
            'Hawaiian',
            ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        )
    ]

    def __str__(self):
        header = "\n==================== MENU ====================\n"
        return header+'\n'.join([str(pizza) for pizza in self.pizzas])+header

    def __getitem__(self, item: str):
        current_pizza = None
        for pizza in self.pizzas:
            if pizza.pizza_name.lower() == item.lower():
                current_pizza = pizza

        if current_pizza is None:
            print(Menu())
            print(
                'No pizza like that. '
                'Choose something else from our menu above.'
            )
            raise NoExistPizzaError

        return current_pizza
