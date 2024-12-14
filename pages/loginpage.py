
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_textfield_by_id = (By.ID, "user-name")
        self.password_textfield_by_id = (By.ID, "password")
        self.login_button_by_id = (By.ID, "login-button")

    def login(self, username, password):
        self.send_keys(self.username_textfield_by_id, username)
        self.send_keys(self.password_textfield_by_id, password)
        self.click(self.login_button_by_id)
