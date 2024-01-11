test:
	poetry run pytest

menu:
	poetry run python final_project/source/cli.py menu

order:
	poetry run python final_project/source/cli.py order pepperoni L --delivery

order_no_delivery:
	poetry run python final_project/source/cli.py order pepperoni XL

order_no_size:
	poetry run python final_project/source/cli.py order pepperoni S

order_no_pizza:
	poetry run python final_project/source/cli.py order ThreeCheese L