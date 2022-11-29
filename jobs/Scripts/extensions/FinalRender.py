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
    return FinalRenderSteps.start_render(driver)

def test_002(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    return FinalRenderSteps.start_render(driver)

def test_003(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_004(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_005(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    return FinalRenderSteps.start_render(driver)

def test_006(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    return FinalRenderSteps.start_render(driver)

def test_007(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_008(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "1080")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_009(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "1280", "720")
    return FinalRenderSteps.start_render(driver)

def test_010(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "1280", "720")
    return FinalRenderSteps.start_render(driver)

def test_011(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "1135", "625")
    return FinalRenderSteps.start_render(driver)

def test_012(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "1135", "625")
    return FinalRenderSteps.start_render(driver)

def test_013(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "9999")
    return FinalRenderSteps.start_render(driver)

def test_014(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_samples(driver, "9999")
    return FinalRenderSteps.start_render(driver)

def test_015(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "1")
    return FinalRenderSteps.start_render(driver)

def test_016(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_samples(driver, "1")
    return FinalRenderSteps.start_render(driver)

def test_017(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "1024")
    return FinalRenderSteps.start_render(driver)

def test_018(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_samples(driver, "1024")
    return FinalRenderSteps.start_render(driver)

def test_019(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "9999")
    return FinalRenderSteps.start_render(driver)

def test_020(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "9999")
    return FinalRenderSteps.start_render(driver)

def test_021(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "1")
    return FinalRenderSteps.start_render(driver)

def test_022(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "1")
    return FinalRenderSteps.start_render(driver)

def test_023(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "1024")
    return FinalRenderSteps.start_render(driver)

def test_024(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.set_samples(driver, "1024")
    FinalRenderSteps.start_render(driver)

def test_025(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.check_progress_bar(driver)

def test_026(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.stop_before_end(driver)

def test_027(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "2048", "1080")
    FinalRenderSteps.stop_before_end(driver, True)

def test_028(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.save_before_end(driver, args, case)