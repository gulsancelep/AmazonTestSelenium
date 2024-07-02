from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class CategoryPage():
    """Performs transactions on the Category Page"""

    NEXT_PAGE_BTN = (By.CSS_SELECTOR, ".s-pagination-separator")  # 0
    PRODUCT_CART = (By.CSS_SELECTOR, ".s-link-style.a-text-normal")  # 4
    SAMSUNG_TEXT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")  # 0
    PAGE_NUMBER = (By.CSS_SELECTOR, ".s-pagination-item.s-pagination-selected")  # 0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_next_page(self):
        """Performs the Next Page action"""

        self.methods.window_scroll_page(2000)
        self.methods.clicked(self.NEXT_PAGE_BTN, 0)

    def click_product(self):
        """Makes product selection"""

        self.methods.clicked(self.PRODUCT_CART, 4)

    def get_text_samsung(self):
        """Used to GET requested texts"""

        return self.methods.get_text(self.SAMSUNG_TEXT, 0)

    def get_page_number(self):
        """Used to GET requested texts"""

        return self.methods.get_text(self.PAGE_NUMBER, 0)