from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class CartPage:
    """Performs transactions on the Card Page"""

    DELETE_BTN = (By.CSS_SELECTOR, 'span[data-action="reg-item-delete"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".a-row.a-size-small")
    DELETE_TEXT = (By.CSS_SELECTOR, "span[data-action='reg-item-delete-undo']")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def delete_item_from_cart(self):
        """The selected product is deleted"""

        self.methods.window_scroll_page(100)
        self.methods.clicked(self.DELETE_BTN, 0)

    def get_cart_product_name(self):
        """Used to GET requested texts"""

        return self.methods.get_text(self.PRODUCT_NAME, 0)

    def get_delete_text(self):
        """Used to GET requested texts"""

        return self.methods.get_text(self.DELETE_TEXT, 0)
