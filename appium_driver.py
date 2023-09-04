import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def appium_driver_fixture(request):
    desired_cap = {
        "platformName": "Android",
        "appium:platformVersion": "11",
        "appium:deviceName": "\"appium:platformVersion\": \"11\"",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/vabbiiibo.com/Downloads/com.fivemobile.thescore_23.9.0-23090_minAPI24(arm64-v8a,armeabi-v7a,"
                      "x86,x86_64)(nodpi)_apkmirror.com.apk",
        "noReset": True  # continue customer session to avoid unexpected pop-ups for permission and bet app download
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
