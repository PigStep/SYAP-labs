# Имеется текстовый файл prices.txt с информацией о заказе из
# интернет - магазина. Каждая строка содержит информацию: название,
# количество единиц, стоимость за ед. Определить общую стоимость заказа.
# Пример файла:
# Микроволновка 2 150
# Чайник 5 140– 3 балла

# путь prices.txt
PRICES_PATH = r"lab3/task2/prices.txt"


def _read_prices(prices_path):
    with open(prices_path, "r", encoding="utf-8") as file:
        prices = file.readlines()

    return prices


def _get_prices(prices):
    orders = []
    for position in prices:
        order = tuple(position.split())
        orders.append(order)

    return orders


def _get_orders(prices_path):
    order_lines = _read_prices(prices_path)
    order_prices = _get_prices(order_lines)

    return order_prices


def count_order_cost(prices_path):
    order = _get_orders(prices_path)
    total_cost = 0

    for name, count, price in order:
        print(f"{name} - {count} шт. - {price} руб. - {int(price) * int(count)} руб.")
        total_cost += int(price) * int(count)

    print(f"Общая стоимость заказа: {total_cost} руб.")


if __name__ == "__main__":
    count_order_cost(PRICES_PATH)
