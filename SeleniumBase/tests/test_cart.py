from selenium.webdriver import Keys

from pageObjects.cart_page import CartPage


class CartTest(CartPage):

    def setUp(self, masterqa_mode=False):
        super(CartTest, self).setUp()
        self.open("https://practice.automationbro.com/shop")

    def test_add_to_cart(self):
        # aad item to the cart
        self.click(self.converse_add_to_cart_btn)

        # assert product is added to the cart
        self.assert_text("1", self.cart_count_text)

        # open cart page
        self.open_page()

        # get current subtotal
        text = self.get_text(self.subtotal_text)

        # change cart quantity
        self.set_value(self.product_quantity_input, "2")
        self.send_keys(self.product_quantity_input, Keys.ENTER)
        self.click(self.update_cart_btn)

        # wait for loading to be completed
        # self.wait_for_element_visible(self.loading_overlay)
        self.wait_for_element_not_visible(self.loading_overlay)

        # assert subtotal to be different from the original subtotal
        updated_text = self.get_text(self.subtotal_text)
        self.assertNotEqual(text, updated_text)
