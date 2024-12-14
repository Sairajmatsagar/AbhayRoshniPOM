import time

from pages.homepage import HomePage
from pages.loginpage import LoginPage


class Test_Logout:

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user","secret_sauce")
        home_page = HomePage(self.driver)
        time.sleep(3)
        home_page.click_on_menu_button()
        time.sleep(3)
        home_page.click_on_logout_link()
        self.driver.save_screenshot("C:\\Users\\HP\\OneDrive\\Desktop\\sunroof.png")
        time.sleep(3)