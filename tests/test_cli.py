import unittest
from unittest.mock import patch
from click.testing import CliRunner
from final_project.source.cli import cli


class TestCli(unittest.TestCase):

    def test_running_menu(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['menu'])

        self.assertEqual(result.exit_code, 0)

    @patch('time.sleep')
    def test_running_order(self, mock_sleep):
        mock_sleep.return_value = None
        runner = CliRunner()
        result = runner.invoke(
            cli, ['order', 'pepperoni', 'L']
        )

        self.assertEqual(result.exit_code, 0)

    def test_running_incorrect_order(self):
        runner = CliRunner()
        result = runner.invoke(
            cli, ['order', 'pepperoni', 'A']
        )
        self.assertEqual(result.exit_code, 0)

    def test_running_incorrect_order_exception(self):
        runner = CliRunner()
        result = runner.invoke(
            cli, ['order', 'pepperoni', 'A']
        )
        output = (
            'Hello! Welcome to Avito Bakery!\n'
            'Pizza`s size should be one of the [`L`, `XL`].\n'
        )

        self.assertEqual(result.output, output)

    def test_running_incorrect_pizza(self):
        runner = CliRunner()
        result = runner.invoke(
            cli, ['order', 'pepper', 'L']
        )

        self.assertEqual(result.exit_code, 0)

    def test_running_incorrect_pizza_exception(self):
        runner = CliRunner()
        result = runner.invoke(
            cli, ['order', 'pepper', 'L']
        )

        output = (
            'No pizza like that. '
            'Choose something else from our menu above.'
        )
        self.assertEqual(
            result.output.split('\n')[-2], output
        )
