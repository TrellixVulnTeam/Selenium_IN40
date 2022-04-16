from typing import List
from pageObjects.home_page import HomePage


# https://www.youtube.com/watch?v=D0-QGMacMxA&t=5338s


class HomeTest(HomePage):

    def setUp(self, masterqa_mode=False):
        super(HomeTest, self).setUp()

        # LOGIN
        self.login()

        # open home page
        self.open_page()

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



        for index, link in enumerate(menu_links):
            # print(index, link.text)
            self.assert_equal(expected_links[index], link.text)


