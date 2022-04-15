from seleniumbase import BaseCase


class HomePage(BaseCase):
    logo_icon: str = ".custom-logo-link"
    get_started_btn: str = "#get-started"
    heading_text: str = "h1[class~='elementor-heading-title']"
    copyright_text: str = "[class='tg-site-footer-section-1']"
    menu_links: str = "ul[id='primary-menu'] > li[class~='menu-item-type-post_type']"

    def open_page(self):
        self.open("https://practice.automationbro.com/")

    def login(self):
        self.open("https://practice.automationbro.com/my-account")
        self.add_text("[id='username']", "user_test")
        self.add_text("[id='password']", "testuser##123")
        self.click("button[name='login']")
        self.assert_text("Logout", "[class~='woocommerce-MyAccount-navigation-link--customer-logout']")
