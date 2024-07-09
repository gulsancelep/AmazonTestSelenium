from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from amazon.page.cart_page import CartPage
from amazon.page.category_page import CategoryPage
from amazon.page.login_page import LoginPage
from amazon.page.main_page import MainPage
from amazon.page.product_page import ProductPage
import unittest


class AmazonBaseTest(unittest.TestCase):
    url = "https://www.amazon.com/"

    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    driver.get(url)
    driver.implicitly_wait(15)

    amazon_main = MainPage(driver)
    amazon_login = LoginPage(driver)
    amazon_category = CategoryPage(driver)
    amazon_product = ProductPage(driver)
    amazon_cart = CartPage(driver)

    def navigate_to_home_page(self):
        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
