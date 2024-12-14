import time

from pages.homepage import HomePage
from pages.loginpage import LoginPage


class Test_Handle_Dropdown:


    def test_sort_product_by_z_a(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        home_page = HomePage(self.driver)
        time.sleep(3)
        home_page.handle_sort_dowpdown_by_visibletext("Name (Z to A)")
        time.sleep(3)
        home_page.click_on_menu_button()
        home_page.click_on_logout_link()
        time.sleep(3)