import shoping_cart


class TestShopingCart:
    def test_shoping_cart(self):
        cart = shoping_cart.ShoppingCart()
        cart.add_item("apple", 1.5, 2)
        cart.add_item("banana", 0.5, 3)
        assert cart.get_total() == 4.5

        cart.add_item("apple", 1.5, 1)
        assert cart.get_total() == 6.0

        cart.remove_item("banana")
        assert cart.get_total() == 4.5
