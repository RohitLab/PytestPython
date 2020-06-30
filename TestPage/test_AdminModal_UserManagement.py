import allure
from allure_commons._allure import step
from pytest import mark
from selenium.webdriver.support.select import Select

from PageFactory.LoginPage import LoginPage
from Utilities.Basepage import Basepage


class Tests_AdminModalUserManagement_Tests(Basepage):

    # @mark.smoke
    @step("Do Login")
    @allure.severity(allure.severity_level.MINOR)
    def test_verifyLoginTest(self, getCredentials):
        loginpage = LoginPage(self.driver)
        loginpage.loginUsername().send_keys(getCredentials["username"])
        loginpage.loginPassword().send_keys(getCredentials["password"])
        homepage = loginpage.loginBtn()

    @step("Do Login 2")
    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyLoginTest2(self, getCredentials):
        loginpage = LoginPage(self.driver)
        loginpage.loginUsername().send_keys(getCredentials["username"])
        loginpage.loginPassword().send_keys(getCredentials["password"])
        homepage = loginpage.loginBtn()

    @step("Do Login and add data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_userManagement(self, getCredentials):
        loginpage = LoginPage(self.driver)
        loginpage.loginUsername().send_keys(getCredentials["username"])
        loginpage.loginPassword().send_keys(getCredentials["password"])
        homepage = loginpage.loginBtn()
        self.c1.assertElements("Welcome Admin", homepage.getHomePageTitel())
        homepage.getHomePageAdminLink()
        homepage.getUserNameText().send_keys("Melenium@500")
        select = Select(homepage.getUserRoleDDL())
        select.select_by_visible_text("ESS")
        homepage.getEmployeeNameText().send_keys("Fiona Grace")
        select = Select(homepage.getStatusDDL())
        select.select_by_visible_text("Enabled")
        homepage.getSubmitBtn().click()
        self.c1.assertElements("Melenium@500", homepage.getuserNameTableResult().text)


