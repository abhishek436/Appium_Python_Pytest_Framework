from Pages.BasePage import Basepage
from Pages.BioMetric_StatusCheck import Status_Check

class HomeScreen(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def goToAndroidBioMetric(self):
        self.click("bioMetric_btn_XPATH")
        return Status_Check(self.driver)