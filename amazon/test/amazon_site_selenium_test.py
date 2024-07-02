from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from amazon.page.cart_page import CartPage
from amazon.page.category_page import CategoryPage
from amazon.page.login_page import LoginPage
from amazon.page.main_page import MainPage
from amazon.page.product_page import ProductPage


class Setup():
    """The section where we make the settings and create the objects"""
    driver = webdriver.Chrome("C:/Users/testinium/Desktop/chromedriver.exe")
    url = "https://www.amazon.com/"
    amazon_main = MainPage(driver)
    amazon_login = LoginPage(driver)
    amazon_category = CategoryPage(driver)
    amazon_product = ProductPage(driver)
    amazon_cart = CartPage(driver)

    def navigate_to_home_page(self):
        """driver settings made and website published"""

        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)


if __name__ == '__main__':
    Setup()