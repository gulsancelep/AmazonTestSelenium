from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class ProductPage:
    """Performs the necessary operations on the product page"""

    ADD_TO_LIST_BTN = (By.CSS_SELECTOR, ".a-button-input.a-declarative")
    WISH_LIST = (By.ID, "huc-view-your-list-button")
    TEXT = (By.CSS_SELECTOR, ".a-size-large.product-title-word-break")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def add_to_list(self):
        """adds to the list"""

        self.methods.clicked(self.ADD_TO_LIST_BTN, 0)

    def click_wish_list(self):
        """Wish List Selected"""

        self.methods.clicked(self.WISH_LIST, 0)

    def get_product_name(self):
        """Used to GET requested textsR"""

        return self.methods.get_text(self.TEXT, 0)

    def is_selected_product(self, product_name, cart_product_name):
        """Assert selected product"""

        assert product_name == cart_product_name, "SELECTED PRODUCT WAS ADDED INCORRECTLY"

    def is_deleted_product(self, delete_text):
        """Assert deleted product"""

        assert delete_text == "Undo", "PRODUCT DELETE IS INCORRECT"
