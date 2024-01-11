## Запуск скрипта

1. ```pip install poetry==1.7.0```
2. ```poetry shell```
3. ```poetry install```

### Основные команды:

```poetry run python source/cli.py menu```: показать меню

```poetry run python source/cli.py order [PIZZA_NAME] [SIZE] [--delivery]```: заказ пиццы

### Предопределенные команды:

```make test```: прогон тестов

```make menu```: показать меню

```make order```: сделать стандартный заказ (пепперони размера L доставкой)

```make order_no_delivery```: сделать стандартный заказ (пепперони размера XL с собой)

### Обработка ошибок:

```make order_no_size```: попытка заказать несуществующий размер пиццы

```make order_no_pizza```: попытка заказать несуществующий вид пиццы