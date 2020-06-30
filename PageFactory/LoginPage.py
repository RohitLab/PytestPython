from selenium.webdriver.common.by import By

from PageFactory.HomePage import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    loginBtn = (By.XPATH, "//*[@id='btnLogin']"[0])

    def loginUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def loginPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginBtn(self):
        submit_button = self.driver.find_elements_by_id("btnLogin")[0]
        submit_button.click()
        return HomePage(self.driver)

        # return self.driver.find_element(*LoginPage.loginBtn)
