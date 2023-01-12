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
    LibrarySteps.click_library_tab(driver)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver) != None, "Opened \"Library\" tab not found"


def test_002(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    LibrarySteps.click_library_tab(driver)
    sleep(1)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver, wait=1) == None, "Opened \"Library\" tab found"


def test_003(args, case, driver, current_try):
    LibrarySteps.test_material(driver, "Gold", element="fridge")


def test_004(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    utils.choose_material("Gold", driver, click=False, exact_title_match=True)
    drag_and_drop_kitchen()
    LibrarySteps.click_library_tab(driver)
    sleep(3)


def drag_and_drop_kitchen():
    pyautogui.moveTo(575, 750)
    sleep(0.5)
    pyautogui.mouseDown(button='left')
    sleep(0.5)
    pyautogui.moveTo(980, 410, 3)
    sleep(0.5)
    pyautogui.mouseUp(button='left')


def test_005(args, case, driver, current_try):
    LibrarySteps.test_material(driver, "Gold", element="fridge", exact_title_match=True)
    LibrarySteps.test_material(driver, "Aluminum", element="fridge")


def test_006(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    materials = LibrarySteps.search_material(driver, "TH Green Metal Rust")
    assert len(materials) == 2 and materials[1].text == "TH Green Metal Rust", "Materials are displayed in the wrong order"


def test_007(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    pass


def test_008(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    LibrarySteps.set_sorting(driver, 'title')
    LibrarySteps.sorting_by_title(driver)


def test_009(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    pass


def test_010(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver)
    pass