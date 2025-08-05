from TestCases.BaseTest import BaseTest
from Pages.HomeScreen import HomeScreen  # Add this import or adjust the path as needed
from Pages.BioMetric_StatusCheck import Status_Check

class Test_Bio_Auth(BaseTest):

    def test_auth_biometric(self):
        home = HomeScreen(self.driver)
        home.goToAndroidBioMetric().clickOnPassCallBack()
        home.goToAndroidBioMetric().getStatusMessage()
        # statusCheck = Status_Check(self.driver)
        # statusCheck.clickOnPassCallBack()
        # statusCheck.getStatusMessage()
