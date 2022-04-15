from typing import List

from seleniumbase import BaseCase


# https://www.youtube.com/watch?v=D0-QGMacMxA&t=5338s

class HomeTest(BaseCase):

    def setUp(self, masterqa_mode=False):
        super(HomeTest, self).setUp()

        # LOGIN
        self.open("https://practice.automationbro.com/my-account")
        self.add_text("[id='username']", "user_test")
        self.add_text("[id='password']", "testuser##123")
        self.click("button[name='login']")
        self.assert_text("Logout", "[class~='woocommerce-MyAccount-navigation-link--customer-logout']")

        self.open("https://practice.automationbro.com/")

    def tearDown(self):
        print("Running after each test")
        self.open("https://practice.automationbro.com/my-account/")
        self.click("[class~='woocommerce-MyAccount-navigation-link--customer-logout'] a")
        self.assert_element_visible("button[name='login']")
        super().tearDown()

    def test_home_page(self):
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

    def test_menu_links(self):
        # self.open("https://practice.automationbro.com/")

        expected_links: List = ["Home", "About", "Shop", "Blog", "Contact", "My account"]

        # find menu links elements
        menu_links: List = self.find_elements("ul[id='primary-menu'] > li[class~='menu-item-type-post_type']")

        # pytest -k "test_menu_links" --- run only this test
        # pytest -k "test_menu_links" -s --- to print out the results to console

        for index, link in enumerate(menu_links):
            # print(index, link.text)
            self.assert_equal(expected_links[index], link.text)
