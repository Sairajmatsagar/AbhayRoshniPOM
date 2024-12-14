import time

import pytest

from pages.loginpage import LoginPage
from utiliteis.Excelutils import get_cell_data, get_data_from_excel, read_data_from_exel_file


class Test_Login:

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(get_cell_data("C:\\Users\\HP\\PycharmProjects\\AbhayRoshniPOM\\testdata\\testdata.xlsx.xlsx", "testdata", 2, 1), get_cell_data("C:\\Users\\HP\\PycharmProjects\\AbhayRoshniPOM\\testdata\\testdata.xlsx.xlsx","testdata",2,2))
        time.sleep(10)

    @pytest.mark.parametrize("username,password",read_data_from_exel_file("C:\\Users\\HP\\PycharmProjects\\AbhayRoshniPOM\\testdata\\testdata.xlsx.xlsx","parametriseddataset"))
    def test_login_with_valid_credentials(self,username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username,password)

        time.sleep(10)