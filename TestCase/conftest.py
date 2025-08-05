import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    cap:Dict[str,Any] = {
    'platformName' : 'Android',
    'automationName' : 'uiautomator2',
    'deviceName' : 'AEHAGUON9DOJQOI7',
    'app' : 'C:\\Users\\dell\\OneDrive\\Desktop\\BitBarSampleApp.instrumented.apk',
    'appPackage' : 'com.bitbarsampleapp',
    'appActivity' : 'com.bitbarsampleapp.MainActivity',
    'noReset': True,
    'autoLaunch': True
}
    url = 'http://localhost:4723/wd/hub'

    driver = webdriver.Remote(url, options= AppiumOptions().load_capabilities(cap))

    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)