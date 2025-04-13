"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as exception:
            product.buy(1001)
        assert "Товара недостаточно" in str(exception.value)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    # Тест на добавление одного товара
    def test_add_product_in_cart(self, product, cart):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    # Тест на добавление трех товаров
    def test_add_free_product_in_cart(self, product, cart):
        cart.add_product(product, 2)
        cart.add_product(product, 8)
        cart.add_product(product, 8)
        assert cart.products[product] == 18

    # Тест на добавление товаров больше чем имеется
    def test_add_more_products_in_cart(self, product, cart):
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)

    # Тест на удаление товаров (всех)
    def test_remove_all_product_cart(self, product, cart):
        cart.add_product(product, 100)
        cart.remove_product(product)
        assert cart.products == {}

    # Тест на удаление одного товара
    def test_one_product_remove_cart(self, product, cart):
        cart.add_product(product, 10)
        cart.add_product(product, 7)
        cart.remove_product(product, 10)
        assert cart.products[product] == 7

    # Тест на очистку корзины
    def test_clear_cart(self, product, cart):
        cart.add_product(product, 25)
        cart.clear()
        assert not cart.products

    # Тест на вычисление итоговой суммы
    def test_get_summ_product_in_cart(self, product, cart):
        cart.add_product(product, 2)
        cart.add_product(product, 3)
        summ = cart.get_total_price()
        assert summ == 500

    # Тест на покупку продукта
    def test_buy_product(self, product, cart):
        cart.add_product(product, 4)
        cart.add_product(product, 3)
        cart.buy()
        assert product.quantity == 993
