from selenium import webdriver
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
from steps import LibrarySteps, ViewportSteps
from locators import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    ViewportSteps.click_tab(driver, 2, 'menu')
    ViewportSteps.click_tab(driver, 2, 'menu')
    sleep(10)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver).is_displayed(), "Opened \"Library\" tab not found"


def test_002(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.click_library_tab(driver, 1)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver) == None, "Opened \"Library\" tab found"


def test_003(args, case, driver, current_try):
    LibrarySteps.test_material(driver, "Gold")


def test_004(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    utils.choose_material("Gold", driver, click=False)
    drag_and_drop_kitchen()
    sleep(3)
    LibrarySteps.click_library_tab(driver, 12)


def drag_and_drop_kitchen():
    pyautogui.moveTo(575, 750)
    sleep(0.5)
    pyautogui.mouseDown(button='left')
    sleep(0.5)
    pyautogui.moveTo(980, 410, 3)
    sleep(0.5)
    pyautogui.mouseUp(button='left')


def test_005(args, case, driver, current_try):
    LibrarySteps.test_material(driver, "Gold")
    LibrarySteps.test_material(driver, "Aluminum")


def test_006(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.search_material(driver, "TH Green Metal Rust")


def test_007(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    pass


def test_008(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.set_sorting(driver, 'title')
    LibrarySteps.sorting_by_title(driver)


def test_009(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    pass


def test_010(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    pass