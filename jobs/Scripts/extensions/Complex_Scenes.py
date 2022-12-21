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
from jobs.Scripts.steps import LibrarySteps, PropertiesSteps
from steps import FinalRenderSteps, ViewportSteps
from locators import LibraryLocators, ViewportLocators

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    pass

def test_002(args, case, driver, current_try):
    rotate_scene(driver)

def test_003(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    return FinalRenderSteps.start_render(driver)

def test_004(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    return FinalRenderSteps.start_render(driver)

def test_005(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_006(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_007(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver, delay=30)
    return render_time

def test_008(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver, delay=30)
    return render_time

def test_009(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    return FinalRenderSteps.start_render(driver)

def test_010(args, case, driver, current_try):
    rotate_scene(driver)
    ViewportSteps.select_element(driver, "MESH_1390")

    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 30)

def test_011(args, case, driver, current_try):
    rotate_scene(driver)    
    # find material
    LibrarySteps.click_library_tab(driver, 2)
    search = utils.find_by_xpath(LibraryLocators.SEARCH_MATERIAL, driver)
    search.click()
    sleep(2)
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys("Gold")
    sleep(2)

    # apply material
    pyautogui.moveTo(820, 760) # Gold material coordinates (second in list)
    pyautogui.dragTo(810, 420, 2, button='left') # Object coordinates
    sleep(2)
    LibrarySteps.click_library_tab(driver, 30)

def test_012(args, case, driver, current_try):
    rotate_scene(driver)
    ViewportSteps.select_element(driver, "MESH_1390")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(30)

    utils.choose_material("Aluminum", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 30)

def test_013(args, case, driver, current_try):
    rotate_scene(driver)
    ViewportSteps.select_element(driver, "MESH_1390")

    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", "-1")
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    PropertiesSteps.set(driver, "scale", "Z", "0.5")
    sleep(30)


def rotate_scene(driver):
    pyautogui.moveTo(1000, 300)
    sleep(0.5)
    pyautogui.dragTo(500, 450, 1, button="left")
    sleep(0.5)

    for i in range(4):
        pyautogui.moveTo(200, 900)
        sleep(0.5)
        pyautogui.dragTo(875, 525, 1, button="right")
        sleep(0.5)

    # zoom scene
    for i in range(30):
        pyautogui.scroll(1000)

    sleep(30)
