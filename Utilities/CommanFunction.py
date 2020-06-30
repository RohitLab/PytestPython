import selenium
import pyautogui as pyautogui
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver import support, ActionChains
# from selenium.webdriver.support import expected_conditions as cond
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CommanFunction:

    def assertElements(self, data1, data2):
        assert data1 == data2

    def AssertElementContains(self, fullstring, substring):
        if substring in fullstring:
            assert True, "Assert contains with pass"
        else:
            assert False, "contains with assertion not working"

    def ClickByJavaExecuter(self, element, driver):
        driver.execute_script("arguments[0].click();", element)

    def waitForElementToBeVisible(self, element, driver):
        wait = WebDriverWait(driver, 20)
        wait.until(ec.visibility_of(element))

    def ScreenClick(self, imageName):
        pyautogui.click(pyautogui.locateCenterOnScreen(imageName))

    def clickElement(self, element):
        element.click()

    def enterTextElement(self, webElement, fieldValue):
        webElement.send_keys(fieldValue)

    def getTextElement(self, element):
        return element.text

    def enterDropdownValue_usingIndex(self, dropDownElement, index):
        select = Select(dropDownElement)
        select.select_by_index(index)

    def enterDropdownValue_usingVisibleText(self, dropDownElement, visibleText):
        select = Select(dropDownElement)
        select.select_by_visible_text(visibleText)

    def enterDropdownValue_usingValue(self, dropDownElement, Value):
        select = Select(dropDownElement)
        select.select_by_value(Value)

    def getSelectedValueFormDropDown(self, dropDownElement):
        select = Select(dropDownElement)
        return select.first_selected_option.text

    def takeScreenShot(self, driver):
        driver.save_screenshot("screenshot.png")

    def doubleClick(self, element, driver):
        actionChains = ActionChains(driver)
        actionChains.double_click(element).perform()

    def rightClick(self, element, driver):
        ActionChains(driver).context_click(element).perform()

    def switchToWindow(self, index, driver):
        window_after = driver.window_handles[index]
        driver.switch_to_window(window_after)

    def switchToFrame(self, element, driver):
        driver.switch_to.frame(element)

    def switchToFrameDefault(self, driver):
        driver.switch_to.default_content()

    def scrollDownWindow(self, height, driver):
        driver.execute_script("window.scrollTo(0, "+height+")")

    def dragAndDrop(self, source_element, dest_element, driver):
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

    def check_elementisCheckBoxOrNot(self, element):
        return element.get_attribute("checked")

    def check_whetherTheCheckboxElementSelectedOrNot(self, element):
        isChecked = element.get_attribute("checked")
        if isChecked is not None:
            return True
        else:
            return False

    def select_CheckBoxOnlyWhenItsNotSelected(self, element):
        result = element.is_selected()
        if result:
            print('Checkbox already selected')
        else:
            element.click()

    def select_RadioButtonOnlyWhenItsNotSelected(self, element):
        result = element.is_selected()
        if result:
            print('radio button already selected')
        else:
            element.click()
            print('radio button selected')

    def select_dragDrop(self, source_element, dest_element, driver):
        ActionChains(driver).drag_and_drop(source_element, dest_element).perform()