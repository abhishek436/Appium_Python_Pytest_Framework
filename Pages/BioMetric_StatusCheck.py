from Pages.BasePage import Basepage

class Status_Check(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnPassCallBack(self):
        self.click("ForcePass_CallBack_XPATH")

    def getStatusMessage(self):
        self.getText("Authentication_Status_XPATH")
        print(self.getText("Authentication_Status_XPATH"))