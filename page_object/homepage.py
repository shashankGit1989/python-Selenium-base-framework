from seleniumbase import BaseCase


class HomePage(BaseCase):
    logo_icon = ".custom-logo-link"
    get_started = "#get-started"
    footer_copyright_text = ".tg-site-footer-section-1"
    navbar_menu_items = "(//*[@id='primary-menu'])[1]//*[starts-with(@id,'menu-item')]"

    def open_home_page(self):
        self.open("https://practice.automationbro.com/")
