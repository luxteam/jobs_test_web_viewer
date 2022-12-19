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
    rotate_lambo_scene(driver)

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
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_008(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_009(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    return FinalRenderSteps.start_render(driver)

def test_010(args, case, driver, current_try):
    rotate_lambo_scene(driver)
    ViewportSteps.select_element(driver, "MESH_026")

    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_011(args, case, driver, current_try):
    rotate_lambo_scene(driver)    
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
    pyautogui.dragTo(805, 420, 2, button='left') # Object coordinates
    sleep(2)
    LibrarySteps.click_library_tab(driver, 8)

def test_012(args, case, driver, current_try):
    rotate_lambo_scene(driver)
    ViewportSteps.select_element(driver, "MESH_026")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(8)

    utils.choose_material("Aluminum", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_013(args, case, driver, current_try):
    rotate_lambo_scene(driver)
    ViewportSteps.select_element(driver, "MESH_026")

    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", "-3")
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    PropertiesSteps.set(driver, "scale", "Z", "5")
    sleep(8)

def test_014(args, case, driver, current_try):
    pass

def test_015(args, case, driver, current_try):
    rotate_sphere_scene(driver)

def test_016(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    return FinalRenderSteps.start_render(driver)

def test_017(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    return FinalRenderSteps.start_render(driver)

def test_018(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_019(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_020(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_021(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_022(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    return FinalRenderSteps.start_render(driver)

def test_023(args, case, driver, current_try):
    rotate_sphere_scene(driver)
    ViewportSteps.select_element(driver, "Sphere_001")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 6)

def test_024(args, case, driver, current_try):
    rotate_sphere_scene(driver)
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
    pyautogui.dragTo(805, 420, 2, button='left') # Object coordinates
    sleep(2)
    LibrarySteps.click_library_tab(driver, 6)

def test_025(args, case, driver, current_try):
    rotate_sphere_scene(driver)
    ViewportSteps.select_element(driver, "Sphere_001")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(6)

    utils.choose_material("Aluminum", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 6)

def test_026(args, case, driver, current_try):
    rotate_sphere_scene(driver)
    ViewportSteps.select_element(driver, "Sphere_001")

    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", "-1")
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    PropertiesSteps.set(driver, "scale", "Z", "3")
    sleep(6)

def test_027(args, case, driver, current_try):
    pass

def test_028(args, case, driver, current_try):
    ViewportSteps.rotate_scene(driver)

def test_029(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    return FinalRenderSteps.start_render(driver)

def test_030(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    return FinalRenderSteps.start_render(driver)

def test_031(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_032(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_033(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_034(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_035(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    return FinalRenderSteps.start_render(driver)

def test_036(args, case, driver, current_try):
    ViewportSteps.select_element(driver, "MESH_014")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_037(args, case, driver, current_try):
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
    pyautogui.dragTo(805, 420, 2, button='left') # Object coordinates
    sleep(2)
    LibrarySteps.click_library_tab(driver, 8)

def test_038(args, case, driver, current_try):
    ViewportSteps.select_element(driver, "MESH_014")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(8)

    utils.choose_material("Aluminum", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_039(args, case, driver, current_try):
    ViewportSteps.select_element(driver, "MESH_014")

    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", "10")
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    PropertiesSteps.set(driver, "scale", "Z", "5")
    sleep(8)

def test_040(args, case, driver, current_try):
    pass

def test_041(args, case, driver, current_try):
    rotate_simple_scene(driver)

def test_042(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    return FinalRenderSteps.start_render(driver)

def test_043(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    return FinalRenderSteps.start_render(driver)

def test_044(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_045(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_format_to_png(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    return FinalRenderSteps.start_render(driver)

def test_046(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_047(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_resolution(driver, "3840", "2160")
    render_time = FinalRenderSteps.start_render(driver)
    FinalRenderSteps.return_to_viewport(driver)
    return render_time

def test_048(args, case, driver, current_try):
    FinalRenderSteps.open_final_render(driver)
    FinalRenderSteps.set_samples(driver, "100")
    return FinalRenderSteps.start_render(driver)

def test_049(args, case, driver, current_try):
    rotate_simple_scene(driver)
    ViewportSteps.select_element(driver, "mesh_0_001")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_050(args, case, driver, current_try):
    rotate_simple_scene(driver)
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
    pyautogui.dragTo(805, 420, 2, button='left') # Object coordinates
    sleep(2)
    LibrarySteps.click_library_tab(driver, 8)

def test_051(args, case, driver, current_try):
    rotate_simple_scene(driver)
    ViewportSteps.select_element(driver, "mesh_0_001")
    
    LibrarySteps.click_library_tab(driver, 2)
    utils.choose_material("Gold", driver)
    sleep(8)

    utils.choose_material("Aluminum", driver)
    sleep(3)
    LibrarySteps.click_library_tab(driver, 8)

def test_052(args, case, driver, current_try):
    rotate_simple_scene(driver)
    ViewportSteps.select_element(driver, "mesh_0_001")

    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", "-1")
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    PropertiesSteps.set(driver, "scale", "Z", "5")
    sleep(8)


def rotate_lambo_scene(driver):
    pyautogui.moveTo(1390, 240)
    pyautogui.dragTo(960, 555, 2, button='left')
    
    # move object to the top
    pyautogui.moveTo(50, 540)
    pyautogui.dragTo(50, 0, 2, button='right')

    sleep(8)


def rotate_sphere_scene(driver):
    pyautogui.moveTo(1600, 200)
    pyautogui.dragTo(1350, 450, 2, button='left')

    sleep(6)


def rotate_simple_scene(driver):
    # rotate scene
    pyautogui.moveTo(200, 200)
    pyautogui.dragTo(200, 500, 2, button='left')
    sleep(0.5)
    
    # zoom scene
    for i in range(50):
        pyautogui.scroll(1000)

    sleep(5)
