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
