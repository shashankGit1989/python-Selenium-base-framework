from selenium.common import NoSuchElementException
from seleniumbase import BaseCase


class Product(BaseCase):
    add_camera_cart = "//a[@data-product_id='374']"
    camera_view_cart = "//a[@data-product_id='374']/following-sibling::a[@title='View cart']"
    camera_final_price = "//a[@href='https://practice.automationbro.com/product/canon-antique-camera/']//ins//span[" \
                         "@class='woocommerce-Price-currencySymbol'] "
    cart_count = "ul[id='primary-menu'] span[class='count']"
    productSearchInput = "[id='woocommerce-product-search-field-0']"
    searchButton = "//button[@value='Search' and @type='submit']"
    noProductFound = "//div[@id='primary']//*[@class='woocommerce-info']"
    toy_Image = "(//figure//img)[1]"

    def openProductPage(self):
        self.open("https://practice.automationbro.com/shop/")

    def addItemToCart(self):
        # click on add to cart for camera
        self.click(self.add_camera_cart)
        #         #check cart count
        self.assert_text('1', self.cart_count)
        # open cart
        self.click(self.camera_view_cart)

    def searchProduct(self):
        self.send_keys(self.productSearchInput, 'Test')
        self.click(self.searchButton)
        try:
            self.assert_element(self.toy_Image)
        except NoSuchElementException:
            self.save_screenshot("No Product found", "custom_screenShot")
            self.assert_text("No products were found matching your selection.", self.noProductFound)
