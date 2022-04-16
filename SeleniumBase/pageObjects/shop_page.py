from seleniumbase import BaseCase


class ShopPage(BaseCase):
    search_input = "input[id='woocommerce-product-search-field-0']"
    search_button = "button[type='submit'][value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_products_txt = ".woocommerce-info"

    def open_page(self):
        self.open("https://practice.automationbro.com/shop/")
