from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    title = (By.XPATH, "//*[@id='welcome']")

    AdminLink = (By.ID, "menu_admin_viewAdminModule")
    UserNameText = (By.XPATH, "//input[@id = 'searchSystemUser_userName']")
    UserRoleDDL = (By.XPATH, "//select[@id = 'searchSystemUser_userType']")
    EmployeeNameText = (By.XPATH, "//input[@id = 'searchSystemUser_employeeName_empName']")
    StatusDDL = (By.XPATH, "//select[@id = 'searchSystemUser_status']")
    userNameTableResult = (By.XPATH, "//tbody/tr[1]/td[2]/a")

    SubmitBtn = (By.XPATH, "//input[@id = 'searchBtn']")

    def getHomePageTitel(self):
        return self.driver.find_element(*HomePage.title).text

    def getHomePageAdminLink(self):
        # return self.driver.find_element(*HomePage.AdminLink)
        submit_button = self.driver.find_elements_by_id("menu_admin_viewAdminModule")[0]
        submit_button.click()

    def getUserNameText(self):
        return self.driver.find_element(*HomePage.UserNameText)

    def getUserRoleDDL(self):
        return self.driver.find_element(*HomePage.UserRoleDDL)

    def getEmployeeNameText(self):
        return self.driver.find_element(*HomePage.EmployeeNameText)

    def getStatusDDL(self):
        return self.driver.find_element(*HomePage.StatusDDL)

    def getuserNameTableResult(self):
        return self.driver.find_element(*HomePage.userNameTableResult)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.SubmitBtn)
