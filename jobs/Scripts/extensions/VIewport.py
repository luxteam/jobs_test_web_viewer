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


def test_003(args, case, driver, current_try, image_path):
    utils.load_scene("C:\\Users\\user\\Documents\\RSLambo\\RSLambo\\Sphere\\SphereRS.usda", 20, driver)
    utils.find_by_xpath("//./button/div[ text() = 'Scene Index' ]", driver).click()
    sleep(2)
    assert utils.find_by_xpath("//h3[ text() = 'Scene Index' ]", driver, True) != [], "Opened \"Scene index\" tab not found"
