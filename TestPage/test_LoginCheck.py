import allure

from PageFactory.LoginPage import LoginPage
from Utilities.Basepage import Basepage


class LoginCheck(Basepage):
    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyLoginTest(self, getCredentials):
        loginpage = LoginPage(self.driver)
        loginpage.loginUsername().send_keys(getCredentials["username"])
        loginpage.loginPassword().send_keys(getCredentials["password"])
        homepage = loginpage.loginBtn()
        self.c1.assertElements("Welcome Admin", homepage.getHomePageTitel())
