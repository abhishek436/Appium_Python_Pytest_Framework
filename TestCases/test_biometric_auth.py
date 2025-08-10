from TestCases.BaseTest import BaseTest
from Pages.HomeScreen import HomeScreen  # Add this import or adjust the path as needed
from Pages.BioMetric_StatusCheck import Status_Check
import pytest
class Test_Bio_Auth(BaseTest):

    @pytest.mark.smoke
    def test_auth_pass_biometric(self):
        home = HomeScreen(self.driver)
        home.goToAndroidBioMetric().clickOnPassCallBack()
        actualMessage = home.goToAndroidBioMetric().getStatusMessage()

        expectedMessage = 'SUCCEEDED'

        assert actualMessage == expectedMessage, f"Expected '{expectedMessage}', but got '{actualMessage}'"

    @pytest.mark.smoke
    def test_auth_fail_biometric(self):
        home = HomeScreen(self.driver)
        home.goToAndroidBioMetric().clickOnFailCallBack()
        actualMessage = home.goToAndroidBioMetric().getStatusMessage()

        expectedMessage = 'FAIL'

        assert actualMessage == expectedMessage, f"Expected '{expectedMessage}', but got '{actualMessage}'"



        
