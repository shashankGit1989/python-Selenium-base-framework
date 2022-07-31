import time

from selenium.webdriver import Keys
from seleniumbase import BaseCase
from page_object.cart_page import Cart
from page_object.product import Product


class BuyProduct(Product, Cart):
    def test_buy_product(self):
        Product.openProductPage(self)
        Product.addItemToCart(self)
        # check cart quantity
        self.assert_text("1", Cart.quantity_input)
        # change quantity
        self.set_value(Cart.quantity_input, "2")
        self.send_keys(Cart.quantity_input, Keys.RETURN)
        self.click(Cart.update_cart_button)
        # wait for amount to update
        self.wait_for_element_visible(Cart.loading_overlay)
        self.wait_for_element_not_visible(Cart.loading_overlay)
        # assert updated subtotal
        # price = self.get_text(Cart.total_cart_price)
        self.assert_text('$000.00', Cart.total_cart_price)

    def test_Find_Product(self):
        Product.openProductPage(self)
        Product.searchProduct(self)

