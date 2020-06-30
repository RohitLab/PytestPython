from PageFactory.LoginPageUpdate import LoginPageUpdate
from Utilities.Basepage import Basepage


class Tests_checkLogin_Tests(Basepage):

    # def test_checkLogin(self, getCredentials):
    #     username = getCredentials["username"]
    #     password = getCredentials["password"]
    #     lp = LoginPageUpdate(self.driver)
    #     lp.enterdata(username, password)

    def test_login(self):
        loginPageFactory = LoginPageUpdate(self.driver)
        loginPageFactory.enterUserName("dnyanesh.gawali-atwu@force.com.aressbusb")
        loginPageFactory.enterPassword("Aress123$")
        loginPageFactory.clickLoginbtn()


