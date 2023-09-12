from appium_driver import appium_driver_fixture
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time


def test_app_functionality(appium_driver_fixture):
    driver = appium_driver_fixture

    time.sleep(2)
    # search for raptors
    el7 = driver.find_element(by=AppiumBy.ID, value="com.fivemobile.thescore:id/search_bar_text_view")
    el7.click()
    time.sleep(1)
    el8 = driver.find_element(by=AppiumBy.ID, value="com.fivemobile.thescore:id/search_src_text")
    el8.send_keys("raptors")
    time.sleep(1)
    # select raptors from results dropdown
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(229, 466)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    # capture screenshot of raptors page for verification
    time.sleep(1)
    screenshot_raptors = 'raptors.png'
    driver.get_screenshot_as_file(screenshot_raptors)
    # select schedule subtab
    time.sleep(1)
    el9 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.LinearLayout[@content-desc=\"Schedule\"]/android.widget.TextView")
    el9.click()
    # capture screenshot of raptors schedule sub-tab for verification
    time.sleep(1)
    screenshot_raptorsched = 'raptorsched.png'
    driver.get_screenshot_as_file(screenshot_raptorsched)
    # navigate back to previous page
    time.sleep(1)
    el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
    el10.click()

    # end of test script
