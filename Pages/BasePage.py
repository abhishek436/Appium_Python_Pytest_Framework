import logging
from Utilities.LogUtils import Logger
from Utilities import configReader
from appium.webdriver.common.appiumby import AppiumBy

log = Logger(__name__, logging.INFO)

class Basepage:
    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        if str(locator).endswith('_XPATH'):
            self.driver.find_element(by=AppiumBy.XPATH,value= configReader.readConfig("locators",locator)).click()

        log.logger.info(f"Clicking on an Element: {locator}")

    def getText(self,locator):
        if str(locator).endswith('_XPATH'):
            status = self.driver.find_element(by=AppiumBy.XPATH,value= configReader.readConfig("locators",locator)).text

        log.logger.info(f"Text Received from element: {status}")
        log.logger.info(f"Getting Text from element: {locator}")

        return status