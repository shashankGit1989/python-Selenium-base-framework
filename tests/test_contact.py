from seleniumbase import BaseCase


class Contacts(BaseCase):
    def test_fill_contact_details(self):
        # go to contacts page
        self.open("https://practice.automationbro.com/contact/")
        # fill the details
        self.send_keys('.contact-name input', 'Test User')
        self.send_keys('.contact-email input', 'testemail@gmail.com')
        self.send_keys('.contact-phone input', '8965896589')
        self.send_keys('.contact-message textarea', 'This is text area test message')
        # submit
        self.click("//*[starts-with(@id,'evf-submit')]")
        # check message displayed
        self.assert_text("Thanks for  us! We will be in touch with you shortly", '//div[@role="alert"]')
