import unittest
from unittest.mock import patch, call
from final_project.source.logger import log
from final_project.source.pizzas_stuff import SpecificSizePizza


class TestLog(unittest.TestCase):

    def setUp(self):
        self.pizza = SpecificSizePizza(
            'Pizza_name',
            ['ing1', 'ing2']
        )
        self.pizza.size = 'L'

    @patch('time.sleep')
    @patch('final_project.source.logger.print')
    def test_default_decorator_text(self, mock_print, mock_sleep):
        mock_sleep.return_value = None

        @log()
        def func(pizza):
            pass

        func(self.pizza)

        self.assertEqual(
            mock_print.call_args_list[0],
            call('func(Pizza_name(size=`L`)).')
        )

    @patch('time.sleep')
    @patch('final_project.source.logger.randint')
    @patch('final_project.source.logger.print')
    def test_default_decorator_text_none_text(
        self, mock_print, mock_randint, mock_sleep
    ):
        mock_sleep.return_value = None
        mock_randint.return_value = 0

        @log()
        def func(pizza):
            pass

        func(self.pizza)

        self.assertEqual(
            mock_print.call_args_list[1],
            call('func - 0 seconds!\n')
        )

    @patch('time.sleep')
    @patch('final_project.source.logger.randint')
    @patch('final_project.source.logger.print')
    def test_non_default_decorator_text(
        self, mock_print, mock_randint, mock_sleep
    ):
        mock_sleep.return_value = None
        mock_randint.return_value = 0

        @log('Some text template {}!')
        def func(pizza):
            pass

        func(self.pizza)

        self.assertEqual(
            mock_print.call_args_list[1],
            call('Some text template 0!\n')
        )
