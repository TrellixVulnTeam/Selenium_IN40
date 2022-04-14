from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://practice.automationbro.com/")

        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(".custom-logo-link")

        self.click("#get-started")
        get_current_url: str = self.get_current_url()
        self.assert_equal(get_current_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_current_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", "h1[class~='elementor-heading-title']")

        # get the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", "[class='tg-site-footer-section-1']")
