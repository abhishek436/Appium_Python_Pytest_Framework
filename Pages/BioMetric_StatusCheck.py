from Pages.BasePage import Basepage
import logging
from Utilities.LogUtils import Logger

log = Logger(__name__, logging.INFO)

class Status_Check(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnPassCallBack(self):
        self.click("ForcePass_CallBack_XPATH")

    def clickOnFailCallBack(self):
        self.click("ForceFail_CallBack_XPATH")

    def getStatusMessage(self):
        statusMessage = self.getText("Authentication_Status_XPATH")
        return statusMessage
        