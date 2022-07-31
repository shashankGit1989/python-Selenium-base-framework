from seleniumbase import BaseCase
from page_object.homepage import HomePage
from page_object.myaccountt import MyAccount


class HomeTest(HomePage):
    def setUp(self, masterqa_mode=False):
        super().setUp();
        print("Setup - Running setup method")
        # open homepage
        HomePage.open_home_page(self)
        # Login
        MyAccount.login(self)

    def tearDown(self):
        print("TearDown - Running After each method ")
        super().tearDown()

    def test_home_page(self):
        self.assert_title("Practice E-Commerce Site – Automation Br")
        self.assert_element(HomePage.logo_icon)
        self.click(HomePage.get_started)
        navigatedUrl = self.get_current_url()
        # self.assert_equal(navigatedUrl, "https://practice.automationbro.com/#get-started",
        #                   "Navigation failed check the url")
        self.assert_true(HomePage.get_started in navigatedUrl)
        # scroll to bottom and verify copyright tests
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 ", HomePage.footer_copyright_text)

    def test_menu_links(self):
        # find menu elements
        expectedlinks = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']
        menuListElements = self.find_elements(HomePage.navbar_menu_items)
        for index, ele in enumerate(menuListElements):
            print(f"{index}  {ele.text}")
            self.assert_equal(expectedlinks[index], ele.text)
