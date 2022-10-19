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
from steps import FinalRenderSteps, ViewportSteps
from locators import PropertiesLocators, ViewportLocators, SceneIndexLocators

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    pass

def test_002(args, case, driver, current_try):
    pyautogui.moveTo(800, 750)
    sleep(1)
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.moveRel(-200, 100)
    sleep(1)
    pyautogui.mouseUp()
    sleep(8)

# default render is jpeg
def test_003(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)

def test_004(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.start_render(driver)

def test_005(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_006(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_007(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_008(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_009(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    FinalRenderSteps.start_render(driver)

def test_010(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")
    ViewportSteps.library_select_material(driver, 'Gold')
    sleep(8)


def test_011(args, case, driver, current_try):
    library = utils.find_by_xpath(ViewportLocators.LIBRARY, driver)
    library.click()
    sleep(1)
    # TODO: evaluate object coordinates
    material = utils.find_by_xpath("//div[ @class = 'click-area' ]//h2[ text() = 'Gold']", driver)
    source_coords = material.location
     
    sleep(1)
    #pyautogui.moveTo(source_coords.get('x') + 30, source_coords.get('y') + 30)
    # pyautogui.moveTo(800, 750)
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


def test_012(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")

    ViewportSteps.library_select_material(driver, "Gold")
    ViewportSteps.library_select_material(driver, "Aluminum")
    sleep(8)

def test_013(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")

    ViewportSteps.properties_set_move(driver, x=10)
    ViewportSteps.properties_set_rotate(driver, x=None, y=-10, z=None)
    ViewportSteps.properties_set_scale(driver, x=None, y=None, z=5)
    sleep(8)

def test_014(args, case, driver, current_try):
    pass

def test_015(args, case, driver, current_try):
    pyautogui.moveTo(800, 750)
    sleep(1)
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.moveRel(-200, 100)
    sleep(1)
    pyautogui.mouseUp()
    sleep(8)

def test_016(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)

def test_017(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.start_render(driver)

def test_018(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_019(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_020(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_021(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_022(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    FinalRenderSteps.start_render(driver)

def test_023(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")
    ViewportSteps.library_select_material(driver, 'Gold')
    sleep(8)


def test_024(args, case, driver, current_try):
    library = utils.find_by_xpath(ViewportLocators.LIBRARY, driver)
    library.click()
    sleep(1)
    # TODO: evaluate object coordinates
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
    sleep(8)


def test_025(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")
    ViewportSteps.library_select_material(driver, 'Gold')
    ViewportSteps.library_select_material(driver, 'Aluminum')
    sleep(8)

def test_026(args, case, driver, current_try):
    # TODO: set object name
    ViewportSteps.find_and_select_object_in_index(driver, "<Object name>")

    ViewportSteps.properties_set_move(driver, x=10)
    ViewportSteps.properties_set_rotate(driver, x=None, y=-10, z=None)
    ViewportSteps.properties_set_scale(driver, x=None, y=None, z=5)
    sleep(8)

def test_027(args, case, driver, current_try):
    pass

def test_028(args, case, driver, current_try):
    pyautogui.moveTo(800, 750)
    sleep(1)
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.moveRel(-200, 100)
    sleep(1)
    pyautogui.mouseUp()
    sleep(8)

def test_029(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)

def test_030(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.start_render(driver)

def test_031(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_032(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)

def test_033(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_034(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)

def test_035(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    FinalRenderSteps.start_render(driver)

def test_036(args, case, driver, current_try):
    ViewportSteps.find_and_select_object_in_index(driver, "Sphere_001")
    ViewportSteps.library_select_material(driver, 'Gold')
    sleep(8)


def test_037(args, case, driver, current_try):
    library = utils.find_by_xpath(ViewportLocators.LIBRARY, driver)
    library.click()
    sleep(1)
    # TODO: evaluate object coordinates
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
    sleep(8)


def test_038(args, case, driver, current_try):
    ViewportSteps.find_and_select_object_in_index(driver, "Sphere_001")
    ViewportSteps.library_select_material(driver, 'Gold')
    ViewportSteps.library_select_material(driver, 'Aluminum')

def test_039(args, case, driver, current_try):
    ViewportSteps.find_and_select_object_in_index(driver, "Sphere_001")
    ViewportSteps.properties_set_move(driver, x=10)
    ViewportSteps.properties_set_rotate(driver, x=None, y=-10, z=None)
    ViewportSteps.properties_set_scale(driver, x=None, y=None, z=5)
    sleep(8)