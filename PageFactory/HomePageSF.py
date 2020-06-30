from selenium.webdriver.common.by import By


class HomePageSF:
    def __init__(self, driver):
        self.driver = driver

    leads = (By.XPATH, "//span[@class='slds-truncate'][contains(text(),'Leads')]")
    newLeads = (By.XPATH, "//div[contains(text(),'New')]")
    lastName = (By.XPATH, "//*[@class='lastName compoundBorderBottom form-element__row input']")
    companyName = (By.XPATH, "(//input[@class=' input'])[3]")
    leadStatusDDL = (By.XPATH, "(//a[@class='select'])[1]")
    leadStatusDDLOption = (By.XPATH, "/html/body/div[9]/div/ul/li[4]/a")
    namesDDL = (By.XPATH, "(//a[@class='select'])[2]")
    nameDDLOption = (By.XPATH, "/html/body/div[8]/div/ul/li[3]/a")
    btnSave = (By.XPATH, "(//span[contains(text(),'Save')])[3]")
    txt_CompanyNameOnHomepage = (By.XPATH, "//*[@id='brandBand_2']//lightning-formatted-name")
    leadsPageDDL = (By.XPATH, "//tbody//tr[1]/td[10]//a")
    optionDeleteDDL = (By.XPATH, "//div/ul/li[2]/a/div[@title= 'Delete']")
    btnDelete = (By.XPATH, "//span[@class = ' label bBody'][contains(text(),'Delete')]")

    def get_leads(self):
        return self.driver.find_element(*HomePageSF.leads)

    def get_newLeads(self):
        return self.driver.find_element(*HomePageSF.newLeads)

    def get_lastName(self):
        return self.driver.find_element(*HomePageSF.lastName)

    def get_companyName(self):
        return self.driver.find_element(*HomePageSF.companyName)

    def get_leadStatusDDL(self):
        return self.driver.find_element(*HomePageSF.leadStatusDDL)

    def get_leadStatusDDLOption(self):
        return self.driver.find_element(*HomePageSF.leadStatusDDLOption)

    def get_namesDDL(self):
        return self.driver.find_element(*HomePageSF.namesDDL)

    def get_nameDDLOption(self):
        return self.driver.find_element(*HomePageSF.nameDDLOption)

    def btn_btnSave(self):
        return self.driver.find_element(*HomePageSF.btnSave)

    def get_txtCompanyNameOnHomepage(self):
        return self.driver.find_element(*HomePageSF.txt_CompanyNameOnHomepage)

    def get_leadsPageDDL(self):
        return self.driver.find_element(*HomePageSF.leadsPageDDL)

    def btn_optionDeleteDDL(self):
        return self.driver.find_element(*HomePageSF.optionDeleteDDL)

    def btn_Delete(self):
        return self.driver.find_element(*HomePageSF.btnDelete)


