from selenium import webdriver
import time
from time import sleep
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pyautogui import typewrite, press
import pytest
import pyautogui
import inspect

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver).click()
    sleep(1)
    assert utils.find_by_xpath("//./button/span[ text() = 'Materials' ]", driver) != None, "Opened \"Library\" tab not found"


def test_002(args, case, driver, current_try):
    button = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    button.click()
    sleep(1)
    button.click()
    sleep(2)
    assert utils.find_by_xpath("//h3[ text() = 'Materials' ]", driver, 3) == None


def test_003(args, case, driver, current_try):
    scene_tab = utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver)
    scene_tab.click()
    sleep(2)
    search = utils.find_by_xpath("//input[ @placeholder='Search Scene' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("Refridgerator_1")
    sleep(1)
    utils.find_by_class("bg-yellow-700", driver, True)[0].click()
    sleep(1)
    scene_tab.click()
    sleep(1)
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    utils.find_by_xpath("//./div[ @class='click-area' ]//h2[ text()='Gold' ]", driver).click()
    sleep(3)
    library.click()
    sleep(8)


def test_004(args, case, driver, current_try):
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    #source_coords = utils.find_by_xpath("//div[ @class = 'click-area' ]//h2[ text() = 'Gold' ]", driver).location
    sleep(1)
    #pyautogui.moveTo(source_coords.get('x') + 30, source_coords.get('y') + 30)
    pyautogui.moveTo(800, 750)
    sleep(1)
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.moveTo(760, 480)
    #pyautogui.moveRel(395, -290)
    #pyautogui.moveRel(395, -445)
    sleep(1)
    pyautogui.mouseUp()
    sleep(2)
    library.click()
    sleep(1)
    name = inspect.stack()[0][3]
    utils.save_screen("{}.png".format(name), driver)
    sleep(3)


def test_005(args, case, driver, current_try):
    scene_tab = utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver)
    scene_tab.click()
    sleep(2)
    search = utils.find_by_xpath("//input[ @placeholder='Search Scene' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("Refridgerator_1")
    sleep(1)
    utils.find_by_class("bg-yellow-700", driver, True)[0].click()
    sleep(1)
    scene_tab.click()
    sleep(1)
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    utils.find_by_xpath("//./div[ @class='click-area' ]//h2[ text()='Gold' ]", driver).click()
    sleep(3)
    utils.find_by_xpath("//./div[ @class='click-area' ]//h2[ text()='Aluminum' ]", driver).click()
    sleep(3)
    library.click()
    sleep(8)


def test_006(args, case, driver, current_try):
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    search = utils.find_by_xpath("//input[ @placeholder='Search' ]", driver)
    search.click()
    sleep(2)
    search.send_keys("TH Green Metal Rust")
    sleep(4)
    materials = utils.find_by_xpath("//div[ @class='material-card' ]//h2", driver, True)
    sleep(2)
    assert len(materials) == 2 and materials[1].text == "TH Green Metal Rust", "Materials are displayed in the wrong order"


def test_007(args, case, driver, current_try):
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    utils.find_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/button", driver).click()
    sleep(1)
    utils.find_by_xpath("//*[ text()='Publish date' ]", driver).click()
    sleep(1)
    assert utils.find_by_xpath("//div[ @class='materials-table-content' ]//h2", driver, True)[0].text == 'Gold', "Materials are displayed in the wrong order"


def test_008(args, case, driver, current_try):
    utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver).click()
    sleep(2)
    utils.find_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/button", driver).click()
    sleep(1)
    utils.find_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]//div//*[ text()='Title' ]", driver).click()
    sleep(5)
    materials = utils.find_by_xpath("//div[ contains(@class, 'materials-table-content') ]//h2", driver, True)
    materials_text = []
    for material in materials:
        if material.text != None:
            materials_text.append(material.text)
    materials_sorted = materials_text.copy()
    materials_sorted.sort()
    assert materials_sorted[:9] == materials_text[:9], "Materials are displayed in the wrong order"


def test_009(args, case, driver, current_try):
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    utils.find_by_xpath("//input[ @placeholder='Author' ]", driver).click()
    sleep(1)
    utils.find_by_xpath("//*[ text()='AMD' ]", driver).click()
    sleep(1)
    assert utils.find_by_xpath("//div[ @class='materials-table-content' ]//h2", driver, True)[0].text == 'Brick Irregular', "Materials are displayed in the wrong order"


def test_010(args, case, driver, current_try):
    library = utils.find_by_xpath("//./button/div[ text() = 'Library' ]", driver)
    library.click()
    sleep(1)
    utils.find_by_xpath("//button[ contains(@class, 'w-8') ]", driver).click()
    sleep(1)
    assert utils.find_by_xpath("//div[ @class='materials-table-content' ]//h2", driver, True)[0].text == 'Picasso Black Marble', "Materials are displayed in the wrong order"