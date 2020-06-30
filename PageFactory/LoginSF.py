from selenium.webdriver.common.by import By

from PageFactory.HomePageSF import HomePageSF


class LoginSF:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//*[@id='username']")
    password = (By.XPATH, "//*[@id='password']")
    loginBtn = (By.XPATH, "//*[@id='Login']")

    def loginUsernameSF(self):
        return self.driver.find_element(*LoginSF.username)
        Basepage.setText(*LoginSF.username, "xyz")
        # return self.driver.find_element(By.XPATH, "//*[@id='username']")

    def loginPasswordSF(self):
        return self.driver.find_element(*LoginSF.password)

    def loginBtnSF(self):
        self.driver.find_element(*LoginSF.loginBtn).click()
        return HomePageSF(self.driver)

