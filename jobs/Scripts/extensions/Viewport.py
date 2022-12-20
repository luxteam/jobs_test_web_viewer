from selenium import webdriver
import time
from time import sleep
import sys
import os
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautogui import typewrite, press
import pyautogui
import re
from steps import *
from locators import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    pass


def test_002(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    assert utils.find_by_xpath(ViewportLocators.SCENE_INDEX_TEXT, driver, True) != [], "Opened \"Scene index\" tab not found"


def test_003(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.click_tab(driver, 2, 'scene index')
    assert utils.find_by_xpath(ViewportLocators.SCENE_INDEX_TEXT, driver, True, 2) == [], "Opened \"Scene index\" tab found"


def test_004(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.search_scene_element(driver, "Refridgerator_1")
    assert utils.find_by_class("bg-yellow-700", driver, True) != [], "Object with corresponding name isn't highlighted in list"


def test_005(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.search_scene_element(driver, "abc")
    ViewportSteps.clear_field(driver)
    assert utils.find_by_xpath(ViewportLocators.SCENE_SEARCH, driver).get_attribute('value') == "", "Search bar input isn't cleared"


def test_006(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.click_parent_tree(driver)
    assert utils.find_by_xpath(ViewportLocators.PARENT_TREE, driver).is_displayed() == True, "Parent tree is closed"


def test_007(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.click_parent_tree(driver)
    ViewportSteps.click_parent_tree(driver)
    assert utils.find_by_xpath(ViewportLocators.PARENT_TREE, driver).is_displayed() == False, "Parent tree is opened"


def test_008(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.search_scene_element(driver, "Refridgerator_1")
    ViewportSteps.click_scene(driver)
    sleep(8)


def test_009(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    utils.find_by_xpath("//div[ contains(@class, 'scene-index-prim-append') ]//button[2]", driver).click()
    sleep(8)


def test_010(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    button = utils.find_by_xpath("//div[ contains(@class, 'scene-index-prim-append') ]//button[2]", driver)
    sleep(1)
    button.click()
    sleep(1)
    button.click()
    sleep(8)


def test_014(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    assert utils.find_by_xpath(ViewportLocators.TIMELINE_VIEW, driver, True) != [], "Timeline bar is hidden"


def test_015(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    ViewportSteps.click_tab(driver, 2, 'timeline')
    assert utils.find_by_xpath(ViewportLocators.TIMELINE_VIEW, driver, True, 2) == [], "Timeline bar is opened"


def test_016(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'comments')
    assert utils.find_by_xpath(ViewportLocators.COMMENT, driver, True) != [], "Comments bar is hidden"


def test_017(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'comments')
    ViewportSteps.click_tab(driver, 2, 'comments')
    assert utils.find_by_xpath(ViewportLocators.COMMENT, driver, True) == [], "Comments bar is opened"


def test_018(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'settings')
    assert utils.find_by_xpath(ViewportLocators.SETTINGS_TEXT, driver, True) != [], "Settings window is hidden"


def test_019(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'menu')
    assert utils.find_by_xpath(ViewportLocators.MENU_ITEM, driver, True) != [], "Scene menu is closed"


def test_020(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'menu')
    ViewportSteps.click_tab(driver, 2, 'menu')
    assert utils.find_by_xpath(ViewportLocators.MENU_ITEM, driver).is_displayed() == False, "Scene menu is opened"


def test_027(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'menu')
    utils.find_by_xpath(ViewportLocators.VERSIONS_MENU, driver).click()
    versions_window = utils.find_by_xpath(ViewportLocators.VERSIONS_WINDOW, driver)

    if args.mode == "desktop":
        expected_service_names = ["AMD RenderStudio", "Frontend", "Streamer"]
    else:
        expected_service_names = ["AMD RenderStudio", "Frontend", "Streamer", "Live", "Router", "Storage"]

    sleep(1)

    actual_service_names = versions_window.find_elements(By.XPATH, ViewportLocators.VERSION_SERVICE_NAMES)
    actual_service_rows = versions_window.find_elements(By.XPATH, ViewportLocators.VERSION_ROWS)

    for a in actual_service_rows:
        utils.case_logger.info("\"" + a.text + "\"")

    for a in actual_service_names:
        utils.case_logger.info("\"" + a.text + "\"")

    for i in range(len(expected_service_names)):
        actual_service_name = actual_service_names[i].text
        actual_service_row = actual_service_rows[i].text
        expected_service_name = expected_service_names[i]

        assert actual_service_name == expected_service_name, f"Found row for service {actual_service_name} instead of {expected_service_name}"

        if expected_service_name == "AMD RenderStudio":
            # There are two possible formats
            # Example: Version: 0.1.12. Branch: develop. Build: #87. Hash: b996aaa
            # Example: Version: 0.1.12. PR: #100. Build: #87. Hash: b996aaa
            if len(re.findall(r"^Version: \d+\.\d+\.\d+\. Branch: .*\. Build: #\d+\. Hash: [a-z0-9]{7}$", actual_service_row)) == 0:
                assert len(re.findall(r"^Version: \d+\.\d+\.\d+\. PR: #.*\. Build: #\d+\. Hash: [a-z0-9]{7}$", actual_service_row)) == 1, f"Service {actual_service_row} has invalid version line"
        else:
            # Example: Version: 0.30.0. Hash: a10c8f9
            assert len(re.findall(r"^Version: \d+\.\d+\.\d+\. Hash: [a-z0-9]{7}$", actual_service_row)) == 1, f"Row with versions {actual_service_row} is invalid"


def test_028(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.search_scene_element(driver, "CupCRed_1")
    ViewportSteps.click_scene(driver)
    sleep(8)


def test_029(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'menu')
    CommonSteps.select_menu_item(driver, 'Home')
    ViewportSteps.project_view(driver)
    sleep(8)


def test_030(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'menu')
    CommonSteps.select_menu_item(driver, 'Home')
    ViewportSteps.project_view(driver)
    case["scene_path"] = "Sphere\\SphereRS.usda"
    utils.load_scene(args, case, driver)
    sleep(8)


def test_031(args, case, driver, current_try):
    ViewportSteps.test_share_button(driver)
    sleep(30)
    assert CommonSteps.element_exists(driver, ViewportLocators.QR_CODE)
