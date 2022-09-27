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


def test_material(args, case, driver, current_try):
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
    utils.choose_material(case["material_name"], driver)
    sleep(3)
    library.click()
    sleep(8)