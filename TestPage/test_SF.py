import time

import allure
from _pytest import mark
from allure_commons._allure import step

from PageFactory.LoginSF import LoginSF
from Utilities.Basepage import Basepage


class Tests_TestSF_Tests(Basepage):

    # @mark.smoke
    @step("Do Login")
    @allure.severity(allure.severity_level.MINOR)
    def test_checkSalesForce(self, getCredentials):
        loginSF = LoginSF(self.driver)
        # loginSF.loginUsernameSF().send_keys(getCredentials["username"])
        # loginSF.loginPasswordSF().send_keys(getCredentials["password"])
        # homepageSF = loginSF.loginBtnSF()
        # time.sleep(30)
        # homepageSF.get_leads().click()
        # homepageSF.get_newLeads().click()
        # homepageSF.get_lastName().send_keys("robk")
        # homepageSF.get_companyName().send_keys("husane")
        # homepageSF.get_namesDDL().click()
        # homepageSF.get_nameDDLOption().click()
        # homepageSF.get_leadStatusDDL().click()
        # homepageSF.get_leadStatusDDLOption().click();
        # homepageSF.btn_btnSave().click()
        # time.sleep(5)
        # # ====self.c1.waitForElementToBeVisible(homepageSF.get_leads(), self.driver)
        # homepageSF.get_leads().click()
        # time.sleep(5)
        # homepageSF.get_leadsPageDDL().click()
        # self.c1.ClickByJavaExecuter(homepageSF.btn_optionDeleteDDL(), self.driver)
        # # =====self.c1.ScreenClick('submit.png')
        # homepageSF.btn_Delete().click()
        # =========================================================
        username = getCredentials["username"]
        password = getCredentials["password"]
        self.c1.waitForElementToBeVisible(loginSF.loginUsernameSF(), self.driver)
        self.c1.enterTextElement(loginSF.loginUsernameSF(), username)
        self.c1.enterTextElement(loginSF.loginPasswordSF(), password)
        homepageSF = loginSF.loginBtnSF()
        self.c1.waitForElementToBeVisible(homepageSF.get_leads(), self.driver)
        self.c1.clickElement(homepageSF.get_leads())
        self.c1.clickElement(homepageSF.get_newLeads())
        self.c1.enterTextElement(homepageSF.get_lastName(), "Ragnar")
        self.c1.enterTextElement(homepageSF.get_companyName(), "Lorthbrock")
        self.c1.clickElement(homepageSF.get_namesDDL())
        self.c1.clickElement(homepageSF.get_nameDDLOption())
        self.c1.clickElement(homepageSF.get_leadStatusDDL())
        self.c1.clickElement(homepageSF.get_leadStatusDDLOption())
        self.c1.clickElement(homepageSF.btn_btnSave())
        self.c1.AssertElementContains(homepageSF.get_txtCompanyNameOnHomepage().text, "Ragnar")
        self.c1.waitForElementToBeVisible(homepageSF.get_leads(), self.driver)
        self.c1.clickElement(homepageSF.get_leads())
        self.c1.waitForElementToBeVisible(homepageSF.get_leadsPageDDL(), self.driver)
        self.c1.clickElement(homepageSF.get_leadsPageDDL())
        self.c1.ClickByJavaExecuter(homepageSF.btn_optionDeleteDDL(), self.driver)
        self.c1.clickElement(homepageSF.btn_Delete())
