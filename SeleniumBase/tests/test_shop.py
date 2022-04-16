from selenium.common.exceptions import NoSuchElementException

from pageObjects.shop_page import ShopPage


class ShopTest(ShopPage):
    def test_search_products(self):
        # open page
        self.open_page()

        # search for product
        self.send_keys(self.search_input, "Sunglasses")
        self.click(self.search_button)

        # assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException as ex:
            self.assert_text("No products were found matching your selection.", self.no_products_txt)

