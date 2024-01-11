import pytest
import unittest
from typing import Callable
from unittest.mock import patch, call
import numpy as np
from final_project.source.pizzas_stuff import (
    Menu, Pizza, SpecificSizePizza, NoExistPizzaSizeError, NoExistPizzaError
)


class TestPizza(unittest.TestCase):

    def test_init(self):
        pizza = Pizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        self.assertEqual(pizza.pizza_name, 'Pepperoni')
        self.assertEqual(
            pizza.ingredients,
            ['pepperoni', 'cheese', 'tomato sauce']
        )

    def test_eq(self):
        pizza1 = Pizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        pizza2 = Pizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        self.assertTrue(pizza1 == pizza2)

    def test_str(self):
        pizza = Pizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        self.assertEqual(
            str(pizza),
            'Pepperoni: pepperoni, cheese, tomato sauce.'
        )


class TestSpecificSizePizza(unittest.TestCase):

    def test_init(self):
        pizza = SpecificSizePizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        self.assertEqual(pizza.pizza_name, 'Pepperoni')
        self.assertEqual(
            pizza.ingredients,
            ['pepperoni', 'cheese', 'tomato sauce']
        )

    def test_size_property(self):
        pizza = SpecificSizePizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        pizza.size = 'L'
        self.assertEqual(pizza.size, 'L')

    def test_size_not_exist_size(self):
        pizza = SpecificSizePizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        with pytest.raises(NoExistPizzaSizeError):
            pizza.size = 'NoSize'

    def test_ingredients_amount_property(self):
        pizza = SpecificSizePizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        pizza.size = 'XL'
        print(pizza.ingredients_amount)
        self.assertTrue(
            all(type(item) is np.int64 for item in pizza.ingredients_amount)
        )

    @patch('final_project.source.pizzas_stuff.np.random.randint')
    def test_iter(self, random: Callable):
        random.return_value = [10, 10, 10]
        pizza = SpecificSizePizza(
            'Pepperoni',
            ['pepperoni', 'cheese', 'tomato sauce']
        )
        pizza.size = 'XL'
        self.assertEqual(
            dict(pizza),
            {'pepperoni': 10, 'cheese': 10, 'tomato sauce': 10}
        )


class TestMenu(unittest.TestCase):
    def test_pizza_not_exist(self):
        with pytest.raises(NoExistPizzaError):
            _ = Menu()["NotExistedPizza"]

    @patch('final_project.source.pizzas_stuff.print')
    def test_pizza_not_exist_output(self, mock_print):
        try:
            _ = Menu()["NotExistedPizza"]
        except NoExistPizzaError:
            output = (
                'No pizza like that. '
                'Choose something else from our menu above.'
            )

            self.assertEqual(
                mock_print.call_args_list[1],
                call(output)
            )


if __name__ == '__main__':
    unittest.main()
