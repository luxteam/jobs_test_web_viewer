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
from steps import ViewportSteps
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
    ViewportSteps.search_scene(driver, "Refridgerator_1")
    assert utils.find_by_class("bg-yellow-700", driver) != None, "Object with corresponding name isn't highlighted in list"


def test_005(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'scene index')
    ViewportSteps.search_scene(driver, "abc")
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
    ViewportSteps.search_scene(driver, "Refridgerator_1")
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
