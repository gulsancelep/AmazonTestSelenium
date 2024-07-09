from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class LoginPage:
    """Performs the necessary operations to login to the page."""

    email = "gulsan.celep@useinsider.com"
    password = "wsxzaq1."
    EMAIL = (By.CSS_SELECTOR, "input[id='ap_email']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='ap_password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".a-button-input")
    SING_IN_BTN = (By.CSS_SELECTOR, ".a-button-input")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login(self):
        """Entering your login information"""

        self.methods.write_to_text(self.EMAIL, self.email, 0)
        self.methods.clicked(self.CONTINUE_BTN, 0)
        self.methods.write_to_text(self.PASSWORD, self.password, 0)
        self.methods.clicked(self.SING_IN_BTN, 0)
