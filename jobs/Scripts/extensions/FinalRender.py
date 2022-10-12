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
from locators import *
from steps import FinalRenderSteps

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils

def test_001(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)

def test_002(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.start_render(driver)

def test_003(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "7680", "4320")
    FinalRenderSteps.start_render(driver)

def test_004(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "7680", "4320")
    FinalRenderSteps.start_render(driver)

def test_005(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.start_render(driver)

def test_006(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.start_render(driver)

def test_007(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "4096", "3072")
    FinalRenderSteps.start_render(driver)

def test_008(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "4096", "3072")
    FinalRenderSteps.start_render(driver)

def test_009(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_010(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "7680", "4320")
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
