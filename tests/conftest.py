import pytest
from selenium import webdriver

from utiliteis import ReadConfiguration


@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    global driver
    browser= ReadConfiguration.read_configuration("basic_info","browser")
    if browser == "chrome":
         driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    url = ReadConfiguration.read_configuration("basic_info", "url")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
