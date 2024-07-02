from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class LoginPage():
    """Performs the necessary operations to login to the page."""

    email = "burakkurt72@gmail.com"
    password = "*"
    EMAIL = (By.CSS_SELECTOR, "input[id='ap_email']")  # 0
    PASSWORD = (By.CSS_SELECTOR, "input[id='ap_password']")  # 0
    CONTINUE_BTN = (By.CSS_SELECTOR, ".a-button-input")  # 0
    SING_IN_BTN = (By.CSS_SELECTOR, ".a-button-input")  # 0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login(self):
        """Entering your login information"""

        self.methods.write_to_text(self.EMAIL, self.email, 0)
        self.methods.clicked(self.CONTINUE_BTN, 0)
        self.methods.write_to_text(self.PASSWORD, self.password, 0)
        self.methods.clicked(self.SING_IN_BTN, 0)