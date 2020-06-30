# from configparser import ConfigParser
import time

import pytest

# config = ConfigParser()
# config.read('config.ini')
# username = config['DEFAULT']['username']
# password = config['DEFAULT']['password']
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.CommanFunction import CommanFunction


@pytest.mark.usefixtures("textfixture")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("getCredentials")
class Basepage:
    c1 = CommanFunction()

    def setText(self, *tup):
        locator = (tup[0][0], tup[0][1])
        self.driver.find_element(*locator).send_keys(tup[1])

    def clickElement(self, *tup):
        locator = (tup[0][0], tup[0][1])
        self.driver.find_element(*locator).click()

    def sendkeysExecuter(self, data, *tup):
        locator = (tup[0][0], tup[0][1])
        self.driver.find_element(*locator).send_keys(data)

    def ClickByJavaExecuter(self, *tup):
        locator = (tup[0][0], tup[0][1])
        elementclick = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", elementclick)

    def wait(self, seconds):
        time.sleep(seconds)

    def waitForElementToBeVisible(self, *tup):
        locator = (tup[0][0], tup[0][1])
        elementfind = self.driver.find_element(*locator)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of(elementfind))

    def getTextElement(self, *tup):
        locator = (tup[0][0], tup[0][1])
        elementtxt = self.driver.find_element(*locator)
        return elementtxt.text

    def enterDropdownValue_usingIndex(self, index, *tup):
        locator = (tup[0][0], tup[0][1])
        dropDownElement = self.driver.find_element(*locator)
        select = Select(dropDownElement)
        select.select_by_index(index)

    def enterDropdownValue_usingVisibleText(self, visibleText, *tup):
        locator = (tup[0][0], tup[0][1])
        dropDownElement = self.driver.find_element(*locator)
        select = Select(dropDownElement)
        select.select_by_visible_text(visibleText)

    def enterDropdownValue_usingValue(self, value, *tup):
        locator = (tup[0][0], tup[0][1])
        dropDownElement = self.driver.find_element(*locator)
        select = Select(dropDownElement)
        select.select_by_value(value)

    def getSelectedValueFormDropDown(self, *tup):
        locator = (tup[0][0], tup[0][1])
        dropDownElement = self.driver.find_element(*locator)
        select = Select(dropDownElement)
        return select.first_selected_option.text

    def check_elementisCheckBoxOrNot(self, *tup):
        locator = (tup[0][0], tup[0][1])
        checkelement = self.driver.find_element(*locator)
        return checkelement.get_attribute("checked")

    def check_whetherTheCheckboxElementSelectedOrNot(self, *tup):
        locator = (tup[0][0], tup[0][1])
        checkselectedelement = self.driver.find_element(*locator)
        isChecked = checkselectedelement.get_attribute("checked")
        if isChecked is not None:
            return True
        else:
            return False

    def select_CheckBoxOnlyWhenItsNotSelected(self, *tup):
        locator = (tup[0][0], tup[0][1])
        checknotselectedelement = self.driver.find_element(*locator)
        result = checknotselectedelement.is_selected()
        if result:
            print('Checkbox already selected')
        else:
            checknotselectedelement.click()

    def select_RadioButtonOnlyWhenItsNotSelected(self, *tup):
        locator = (tup[0][0], tup[0][1])
        radioelement = self.driver.find_element(*locator)
        result = radioelement.is_selected()
        if result:
            print('radio button already selected')
        else:
            radioelement.click()
            print('radio button selected')

    def takeScreenShot(self, driver):
        driver.save_screenshot("screenshot.png")

    def doubleClick(self, driver, *tup):
        locator = (tup[0][0], tup[0][1])
        dcelement = self.driver.find_element(*locator)
        actionChains = ActionChains(driver)
        actionChains.double_click(dcelement).perform()

    def rightClick(self, driver, *tup):
        locator = (tup[0][0], tup[0][1])
        rcelement = self.driver.find_element(*locator)
        ActionChains(driver).context_click(rcelement).perform()

    def dragAndDrop(self, driver, *tup):
        locator1 = (tup[0][0], tup[0][1])
        source_element = self.driver.find_element(*locator1)
        locator2 = (tup[0][0], tup[0][1])
        dest_element = self.driver.find_element(*locator2)
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

    def switchToWindow(self, index, driver):
        window_after = driver.window_handles[index]
        driver.switch_to_window(window_after)

    def switchToFrame(self, driver, *tup):
        locator = (tup[0][0], tup[0][1])
        swelement = self.driver.find_element(*locator)
        driver.switch_to.frame(swelement)

    def switchToFrameDefault(self, driver):
        driver.switch_to.default_content()

    def scrollDownWindow(self, height, driver):
        driver.execute_script("window.scrollTo(0, " + height + ")")

    def scrollDownPage(self, driver):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def scrolltillelement(self, driver, *tup):
        locator = (tup[0][0], tup[0][1])
        scrollelement = self.driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView();", scrollelement)

    def assertElements(self, data1, data2):
        assert data1 == data2

    def AssertElementContains(self, fullstring, substring):
        if substring in fullstring:
            assert True, "Assert contains with pass"
        else:
            assert False, "contains with assertion not working"

    def alert_accept(self, driver):
        driver.switch_to_alert().accept()

    def alert_dismiss(self, driver):
        driver.switch_to_alert().dismiss()

    def alert_sendkey(self, driver, data):
        driver.switch_to_alert().send_keys(data)
