from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.menu_button_by_xpath = (By.XPATH, "//button[text()='Open Menu']")
        self.logout_link_by_link_text = (By.LINK_TEXT, "Logout")
        self.sort_dropdown_by_class_name = (By.CLASS_NAME,"product_sort_container")



    def click_on_menu_button(self):
        self.click(self.menu_button_by_xpath)

    def click_on_logout_link(self):
        self.click(self.logout_link_by_link_text)

    def handle_sort_dowpdown_by_visibletext(self,visible_text):
        wait = WebDriverWait(self.driver, 10)
        sort_dropdown=wait.until(expected_conditions.presence_of_element_located(self.sort_dropdown_by_class_name))
        select= Select(sort_dropdown)
        select.select_by_visible_text(visible_text)