from seleniumbase import BaseCase


class Cart(BaseCase):
    total_cart_price = "//div[@class='cart_totals' or @class='cart_totals ']//tr[2]//bdi"
    checkout_button = "//*[@href='https://practice.automationbro.com/checkout/']"
    quantity_input = "input[id^='quantity']"
    update_cart_button = "button[name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

