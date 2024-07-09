from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class MainPage:
    """Performs transactions on the Main Page"""

    SEARCH_TEXT = "samsung"
    SEARCH_BAR = (By.CSS_SELECTOR, "input[id='twotabsearchtextbox']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, ".nav-line-1-container")
    SEARCH_IN_BTN = (By.CSS_SELECTOR, ".nav-right")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def is_home_page(self, url):
        """assert home page"""

        assert url == self.driver.current_url, "URL ERROR"

    def is_search_text(self, search_text_control):
        """assert search text"""

        assert "Samsung" in search_text_control, "MATCHING ERROR WITH SAMSUNG TEXT"

    def navigate_to_search(self):
        """On the search page, search for text in the search field"""

        self.methods.write_to_text(self.SEARCH_BAR, self.SEARCH_TEXT, 0)
        self.methods.clicked(self.SEARCH_IN_BTN, 0)

    def click_login_page(self):
        """Click login page"""

        self.methods.clicked(self.SIGN_IN_BTN, 0)
