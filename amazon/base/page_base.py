from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """We call the functions to be used in the base class"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 35)

    def wait_for_element(self, selector, index):
        """allows the page to load and find the element"""

        if index >= 0:
            return self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def clicked(self, selector, index):
        """performs the click function"""

        self.wait_for_element(selector, index).click()

    def write_to_text(self, selector, text, index):
        """write to text"""

        web_element = self.wait_for_element(selector, index)
        web_element.send_keys(text)

    def window_scroll_page(self, y_coordinate):
        """Performs page scrolling"""

        self.driver.execute_script("window.scrollTo(0, " + str(y_coordinate) + ")")

    def get_text(self, selector, index):
        """gets the requested text"""

        element = self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return element.text
