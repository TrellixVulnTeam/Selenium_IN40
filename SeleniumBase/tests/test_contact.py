from seleniumbase import BaseCase


# https://www.youtube.com/watch?v=D0-QGMacMxA&t=5338s

class ContactTest(BaseCase):
    def test_contact_page(self):
        self.open("https://practice.automationbro.com/contact/")

        self.send_keys("[class~='contact-name'] > input[class='input-text']", "Test")
        self.send_keys("[class~='contact-email'] > input[class='input-text']", "test@gmail.com")
        self.send_keys("[class~='contact-phone'] > input[class='input-text']", "1234567")
        self.send_keys("[class~='contact-message'] > textarea[class='input-text']", "Sample Message")

        self.click("button[class~='evf-submit']")

        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "[class~='everest-forms-notice']")
