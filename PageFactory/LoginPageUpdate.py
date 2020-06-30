import time

from selenium.webdriver.common.by import By

from Utilities.Basepage import Basepage


class LoginPageUpdate(Basepage):
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//*[@id='username']")
    password = (By.XPATH, "//*[@id='password']")
    loginBtn = (By.XPATH, "//*[@id='Login']")

    def enterUserName(self, username):
        Basepage.setText(self, self.username, username)

    def enterPassword(self, password):
        Basepage.setText(self, self.password, password)

    def clickLoginbtn(self):
        Basepage.clickElement(self, self.loginBtn)

# Basepage.setText(self, self.password, password)
