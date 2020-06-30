import os
import time

from CommanFunction import CommanFunction
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class orangeHRM:
    c1 = CommanFunction()
    driver = webdriver.Chrome(executable_path="D:/pythonWorkspace/PythonSelFramework/drivers/chrome/chromedriver.exe")
    # options = Options()
    # options.set_preference('dom.webnotifications.enabled', False)
    # print(os.getcwd())
    # os.chdir('../')
    # data = os.getcwd() + "\Drivers\geckodriver.exe"
    #
    # driver = webdriver.Firefox(executable_path=data, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    username = driver.find_element_by_id('txtUsername')
    password = driver.find_element_by_id('txtPassword')
    loginBtn = driver.find_element_by_xpath("//*[@id='btnLogin']")
    c1.enterTextElement(username, "Admin")
    c1.enterTextElement(password, "admin123")
    c1.clickElement(loginBtn)

    titleElement = driver.find_element_by_xpath("//*[@id='welcome']")
    c1.assertElements("Welcome Admin", c1.getTextElement(titleElement))

    time.sleep(5)
    AdminLink = driver.find_element_by_id("menu_admin_viewAdminModule")
    c1.ClickByJavaExecuter(AdminLink, driver)

    UserNameText = driver.find_element_by_xpath("//input[@id = 'searchSystemUser_userName']")
    c1.enterTextElement(UserNameText, "Melenium@500")
    UserRoleDDL = driver.find_element_by_xpath("//select[@id = 'searchSystemUser_userType']")
    c1.enterDropdownValue_usingVisibleText(UserRoleDDL, "ESS")
    EmployeeNameText = driver.find_element_by_xpath("//input[@id = 'searchSystemUser_employeeName_empName']")
    c1.enterTextElement(EmployeeNameText, "Fiona Grace")
    StatusDDL = driver.find_element_by_xpath("//select[@id = 'searchSystemUser_status']")
    c1.enterDropdownValue_usingVisibleText(StatusDDL, "Enabled")

