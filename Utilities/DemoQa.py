from selenium import webdriver

from CommanFunction import CommanFunction


class DemoQA:
    c1 = CommanFunction()
    driver = webdriver.Chrome(executable_path="D:/pythonWorkspace/PythonSelFramework/drivers/chrome/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://demoqa.com/")

    elementOption = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5')
    c1.clickElement(elementOption)

    # check box
    # elementCheckBox = driver.find_element_by_xpath('(//*[@id="item-1"])[1]')
    # c1.clickElement(elementCheckBox)
    # homecheckBox = driver.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/label/span[1]')
    # print(c1.check_elementisCheckBoxOrNot(homecheckBox))
    # c1.select_CheckBoxOnlyWhenItsNotSelected(homecheckBox)

    # radio button
    elementRadioButton = driver.find_element_by_xpath('(//*[@id="item-2"])[1]')
    c1.clickElement(elementRadioButton)
    checkBox = driver.find_element_by_xpath('//*[@id="impressiveRadio"]')
    # c1.select_RadioButtonOnlyWhenItsNotSelected(checkBox)
    c1.ClickByJavaExecuter(checkBox, driver)
    # checkBox2 = driver.find_element_by_xpath('//*[@id="yesRadio"]')
    # c1.select_RadioButtonOnlyWhenItsNotSelected(checkBox2)

    # # double click
    # elementbtn = driver.find_element_by_xpath('(//*[@id="item-4"])[1]')
    # c1.clickElement(elementbtn)
    # elementDoubleClick = driver.find_element_by_xpath('//*[@id="doubleClickBtn"]')
    # c1.rightClick(elementDoubleClick, driver)
    #
    # # Right click
    # elementbtn = driver.find_element_by_xpath('(//*[@id="item-4"])[1]')
    # c1.clickElement(elementbtn)
    # elementDoubleClick = driver.find_element_by_xpath('//*[@id="rightClickBtn"]')
    # c1.rightClick(elementDoubleClick, driver)
    #
    # # switch window
    # elementWindowsAndFrame = driver.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div')
    # c1.ClickByJavaExecuter(elementWindowsAndFrame, driver)
    #
    # elementbrowser = driver.find_element_by_xpath('(//*[@id="item-0"]/span)[3]')
    # c1.clickElement(elementbrowser)
    #
    # newTab = driver.find_element_by_xpath('//*[@id="tabButton"]')
    # c1.clickElement(newTab)
    # c1.switchToWindow(1, driver)
    # newBrowserElement = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(newBrowserElement.text, "This is a sample page")
    # c1.switchToWindow(0, driver)
    #
    # newWindow = driver.find_element_by_xpath('//*[@id="windowButton"]')
    # c1.clickElement(newWindow)
    # c1.switchToWindow(1, driver)
    # newBrowserElement = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(newBrowserElement.text, "This is a sample page")
    # c1.switchToWindow(0, driver)


    # iframe
    # elementWindowsAndFrame = driver.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div')
    # c1.ClickByJavaExecuter(elementWindowsAndFrame, driver)
    # elementIFrame = driver.find_element_by_xpath('(//*[@id="item-2"]/span)[2]')
    # c1.clickElement(elementIFrame)
    # frame = driver.find_element_by_xpath('//*[@id="frame1"]')
    # c1.switchToFrame(frame, driver)
    # textName = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(textName.text, "This is a sample page")

    # drag drop
    elementInteraction = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]/span/div')
    c1.ClickByJavaExecuter(elementInteraction, driver)
    elementDragDrop = driver.find_element_by_xpath('(//*[@id="item-3"])[4]')
    c1.ClickByJavaExecuter(elementDragDrop, driver)
    elementsource = driver.find_element_by_xpath('//*[@id="draggable"]')
    elementdestination = driver.find_element_by_xpath('//*[@id="droppable"]')
    c1.select_dragDrop(elementsource, elementdestination, driver)

