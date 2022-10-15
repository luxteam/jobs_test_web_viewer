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
from steps import LibrarySteps
from locators import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver) != None, "Opened \"Library\" tab not found"


def test_002(args, case, driver, current_try):
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.click_library_tab(driver, 1)
    assert utils.find_by_xpath(LibraryLocators.MATERIALS_TEXT, driver, 3) == None, "Opened \"Library\" tab found"


def test_003(args, case, driver, current_try):
    LibrarySteps.select_refridgerator_element(driver)
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.select_material(driver, "gold")
    LibrarySteps.click_library_tab(driver, 8)


def test_004(args, case, driver, current_try):
    pass


def test_005(args, case, driver, current_try):
    LibrarySteps.select_refridgerator_element(driver)
    LibrarySteps.click_library_tab(driver, 1)
    LibrarySteps.select_material(driver, "gold")
    LibrarySteps.select_material(driver, "aluminum")
    LibrarySteps.click_library_tab(driver, 8)


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