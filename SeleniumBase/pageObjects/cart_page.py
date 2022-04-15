from seleniumbase import BaseCase


class CartPage(BaseCase):
    converse_add_to_cart_btn = "a[aria-label='Add “Converse” to your cart']"
    cart_count_text = "ul[id='primary-menu'] span[class='count']"
    subtotal_text = "tr[class='cart-subtotal']  [class~='woocommerce-Price-amount']"
    update_cart_btn = "button[name='update_cart']"
    product_quantity_input = "input[id^='quantity']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

    def open_page(self):
        self.open("https://practice.automationbro.com/cart")
