"""Logger declaration"""

import time
from random import randint
from functools import wraps
from typing import Optional, Callable
from final_project.source.pizzas_stuff import Pizza


def log(text: Optional[str] = None):
    """
    Decorator with text param

    text: template to print
    """
    def inner_log(func: Callable):
        @wraps(func)
        def wrapper(pizza: Pizza):

            time_to_prepare = randint(1, 5)
            print(
                f'{func.__name__}({pizza.pizza_name}'
                f'(size=`{pizza.__dict__["_size"]}`)).'
            )
            time.sleep(time_to_prepare)

            if text is None:
                print(f'{func.__name__} - {time_to_prepare} seconds!\n')
            else:
                print(text.format(time_to_prepare)+"\n")

            return func(pizza)
        return wrapper
    return inner_log
