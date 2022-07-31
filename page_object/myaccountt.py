from seleniumbase import BaseCase


class MyAccount(BaseCase):
    username = "#username"
    password = "#password"
    button_login = "//button[@name='login']"
    logout_content = ".woocommerce-MyAccount-content"

    def login(self):
        # Login
        self.click_link("My account")
        self.send_keys(MyAccount.username, "shank1989")
        self.send_keys(MyAccount.password, "shank@1989")
        self.click(MyAccount.button_login)
        self.assert_text("Log out", MyAccount.logout_content)
        self.click_link("Home")
