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

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    pass


def test_002(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//h3[ text() = 'Scene Index' ]", driver, True) != [], "Opened \"Scene index\" tab not found"


def test_003(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//h3[ text() = 'Scene Index' ]", driver, True, 2) == [], "Opened \"Scene index\" tab found"


def test_004(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    search = utils.find_by_xpath("//input[ @placeholder='Search Scene' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("Kitchen_set")
    sleep(2)
    assert utils.find_by_class("bg-yellow-700", driver, True) != [], "Object with corresponding name isn't highlighted in list"


def test_005(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    search = utils.find_by_xpath("//input[ @placeholder='Search Scene' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("abc")
    sleep(2)
    utils.find_by_xpath("//div[ contains(@class, 'pl-2') ]//button", driver).click()
    sleep(2)
    assert search.get_attribute('value') == "", "Search bar input isn't cleared"


def test_006(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    utils.find_by_class("scene-index-prim-button-expand", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//div[ @id='scene-index-prim-0' ]//div[ @class='py-1' ]", driver).is_displayed() == True, "Parent tree is closed"


def test_007(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    utils.find_by_class("scene-index-prim-button-expand", driver).click()
    sleep(2)
    utils.find_by_class("scene-index-prim-button-expand", driver, True)[0].click()
    sleep(2)
    assert utils.find_by_xpath("//div[ @id='scene-index-prim-0' ]//div[ @class='py-1' ]", driver).is_displayed() == False, "Parent tree is opened"


def test_008(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    search = utils.find_by_xpath("//input[ @placeholder='Search Scene' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("Refridgerator_1")
    sleep(1)
    utils.find_by_class("bg-yellow-700", driver, True)[0].click()
    sleep(8)


def test_009(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    utils.find_by_xpath("//div[ contains(@class, 'scene-index-prim-append') ]//button[2]", driver).click()
    sleep(8)


def test_010(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    button = utils.find_by_xpath("//div[ contains(@class, 'scene-index-prim-append') ]//button[2]", driver)
    sleep(1)
    button.click()
    sleep(1)
    button.click()
    sleep(8)


def test_014(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Timeline' ]", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//div[ text() = ' Timeline view ' ]", driver, True) != [], "Timeline bar is hidden"


def test_015(args, case, driver, current_try):
    button = utils.find_by_xpath("//./button/div[ text() = 'Timeline' ]", driver)
    sleep(1)
    button.click()
    sleep(2)
    button.click()
    sleep(2)
    assert utils.find_by_xpath("//div[ text() = ' Timeline view ' ]", driver, True, 2) == [], "Timeline bar is opened"


def test_016(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Comments' ]", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//div[ text() = ' Comment 1' ]", driver, True) != [], "Comments bar is hidden"


def test_017(args, case, driver, current_try):
    button = utils.find_by_xpath("//./button/div[ text() = 'Comments' ]", driver)
    sleep(1)
    button.click()
    sleep(2)
    button.click()
    sleep(2)
    assert utils.find_by_xpath("//div[ text() = ' Comment 1' ]", driver, True) == [], "Comments bar is opened"


def test_018(args, case, driver, current_try):
    utils.find_by_xpath("//div[ contains(@class, 'app-header-center') ]//div[ contains(@class, 'menu-left') ]//button", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//h3[ text() = 'Selection viewport' ]", driver, True) != [], "Settings window is hidden"


def test_019(args, case, driver, current_try):
    utils.find_by_xpath("//button[ @class = 'button-iconed' ]", driver, True)[0].click()
    sleep(2)
    assert utils.find_by_xpath("//button[ @class = 'menu-item' ]", driver, True) != [], "Scene menu is closed"


def test_020(args, case, driver, current_try):
    button = utils.find_by_xpath("//button[ @class = 'button-iconed' ]", driver, True)[0]
    sleep(2)
    button.click()
    sleep(2)
    button.click()
    sleep(2)
    assert utils.find_by_xpath("//button[ @class = 'menu-item' ]", driver).is_displayed() == False, "Scene menu is opened"
