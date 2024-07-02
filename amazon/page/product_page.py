from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class ProductPage():
    """ürün sayfasıda gerekli işlemleri yerine getirir"""

    ADD_TO_LIST_BTN = (By.CSS_SELECTOR, ".a-button-input.a-declarative")  # 0
    WISH_LIST = (By.CSS_SELECTOR, ".w-button")  # 0
    TEXT = (By.CSS_SELECTOR, ".a-size-large.product-title-word-break")  # 0

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