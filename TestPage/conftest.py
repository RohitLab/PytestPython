import os
import time

import pytest
from selenium import webdriver

# @pytest.fixture(scope="class")
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup(request):
    # driver = webdriver.Chrome(executable_path="D:/Softwares/chromedriver.exe")
    # driver = webdriver.Chrome(executable_path="D:/pythonWorkspace/PythonSelFramework/drivers/chrome/chromedriver.exe")
    # driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    # driver.maximize_window()

    options = Options()
    options.set_preference('dom.webnotifications.enabled', False)
    print(os.getcwd())
    os.chdir('../')
    data = os.getcwd() + "\Drivers\geckodriver.exe"

    driver = webdriver.Firefox(executable_path=data, options=options)
    # driver = webdriver.Firefox(executable_path=os.chdir('../') + "\\Driver\\geckodriver.exe", options=options)
    driver.implicitly_wait(10)
    driver.get("https://aressbusiness--aressbusb.my.salesforce.com/")
    # driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.maximize_window()

    request.cls.driver = driver
    yield

    # with pytest.raises(Exception) as excinfo:
    #     print("=========================Catch in baby", excinfo)
    # driver.close()

    # try:
    #     driver.close()
    # except:
    #     print("An exception occurred")
    # driver.close()


# @pytest.fixture(params=[{"username": "Admin", "password": "admin123"}])
# def getCredentials(request):
#     return request.param

@pytest.fixture(params=[{"username": "dnyanesh.gawali-atwu@force.com.aressbusb", "password": "Aress123$"}])
def getCredentials(request):
    return request.param


@pytest.fixture()
def textfixture():
    assert False
    print("hi")
