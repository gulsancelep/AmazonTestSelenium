import unittest
from amazon.test.amazon_site_selenium_test import Setup


class AmazonSiteSeleniumTest(unittest.TestCase, Setup):
    """TEST CASE
        1.  http://www.amazon.com sitesine gidecek ve anasayfanın açıldığını assertion ile onaylayacak,
        2. Login ekranını açıp, bir kullanıcı ile login olunacak ( daha önce siteye üyeliği varsa o olabilir )
        3. Ekranin ustundeki Search alanına 'samsung' yazıp ara butonuna tıklanacak,
        4. Gelen sayfada samsung icin sonuc bulunduğunu onaylayacak,
        5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanin şu an gösterimde oldugunu onaylayacak,
        6. Üstten 3. urunun içindeki 'Add to List' butonuna tıklayacak,
        7. Ekranin en üstündeki 'List' linkine tiklayacak içerisinden Wish listi seçecek,
        8. Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak,
        9. Favorilere alinan bu urunun yanindaki 'Delete' butonuna basarak, favorilerimden cikaracak,
        10. Sayfada bu urunun artik favorilere alinmadigini onaylayacak.
    """

    def setup(self):
        Setup.__init__(self)

    def testAmazon(self):
        self.navigate_to_home_page()
        assert self.url == self.driver.current_url, "URL ERROR"
        self.amazon_main.click_login_page()
        self.amazon_login.login()
        self.amazon_main.navigate_to_search()
        search_text_control = self.amazon_category.get_text_samsung()
        assert "Samsung" in search_text_control, "MATCHING ERROR WITH SAMSUNG TEXT"
        self.amazon_category.navigate_to_next_page()
        page_number = self.amazon_category.get_page_number()
        assert page_number == "2", "PAGE NUMBER IS WRONG"
        self.amazon_category.click_product()
        product_name = self.amazon_product.get_product_name()
        self.amazon_product.add_to_list()
        self.amazon_product.click_wish_list()
        cart_product_name = self.amazon_cart.get_cart_product_name()
        assert product_name == cart_product_name, "SELECTED PRODUCT WAS ADDED INCORRECTLY"
        self.amazon_cart.delete_item_from_cart()
        delete_text = self.amazon_cart.get_delete_text()
        assert delete_text == "Undo", "PRODUCT DELETE IS INCORRECT"

    def tear_down(self):
        self.driver.quit()


if __name__ == '__main__':
    AmazonSiteSeleniumTest()