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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import utils

class FinalRenderSteps:
    def open_final_render(driver):
        utils.find_by_xpath(ViewportLocators.FINAL_RENDER, driver).click()
        sleep(2)
        utils.find_by_xpath(FinalRenderLocators.OUTPUT, driver).click()
        sleep(1)

    def set_format_to_png(driver):
        utils.find_by_xpath(FinalRenderLocators.FORMAT, driver).click()
        sleep(1)
        utils.find_by_xpath(FinalRenderLocators.PNG_FORMAT, driver).click()

    def set_resolution(driver, width, height):
        utils.find_by_xpath(FinalRenderLocators.WIDTH, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.WIDTH, driver).send_keys(width)
        utils.find_by_xpath(FinalRenderLocators.HEIGHT, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.HEIGHT, driver).send_keys(height)

    def start_render(driver):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        sleep(10)

    def return_to_viewport(driver):
        utils.find_by_xpath(FinalRenderLocators.BACK_BUTTON, driver).click()
        sleep(5)

class LibrarySteps:
    def click_library_tab(driver, sec):
        utils.find_by_xpath(LibraryLocators.LIBRARY_TAB, driver).click()
        sleep(sec)

    def select_refridgerator_element(driver):
        utils.find_by_xpath(LibraryLocators.SCENE_INDEX_TAB, driver).click()
        sleep(2)
        search = utils.find_by_xpath(LibraryLocators.SCENE_SEARCH, driver)
        search.click()
        sleep(2)
        search.send_keys("Refridgerator_1")
        sleep(1)
        utils.find_by_class("bg-yellow-700", driver, True)[0].click()
        sleep(1)
        utils.find_by_xpath(LibraryLocators.SCENE_INDEX_TAB, driver).click()
        sleep(1)

    def search_material(driver, name):
        search = utils.find_by_xpath(LibraryLocators.SEARCH_MATERIAL, driver)
        search.click()
        time.sleep(2)
        search.send_keys(name)
        sleep(4)
        materials = utils.find_by_xpath(LibraryLocators.SEARCH_MATERIAL_CARD, driver, True)
        sleep(2)
        assert len(materials) == 2 and materials[1].text == "TH Green Metal Rust", "Materials are displayed in the wrong order"

    def select_material(driver, material):
        utils.find_by_xpath(LibraryLocators.MATERIAL + str(material).capitalize() + '\"]', driver).click()
        sleep(3)

    def set_sorting(driver, key):
        utils.find_by_xpath(LibraryLocators.SORTING_BY, driver).click()
        sleep(1)
        utils.find_by_xpath(LibraryLocators.SORTING_KEY + str(key).capitalize() + '\"]', driver).click()
        sleep(5)

    def sorting_by_title(driver):
        materials = utils.find_by_xpath(LibraryLocators.MATERIAL_CARD, driver, True)
        materials_text = []
        for material in materials:
            if material.text != None:
                materials_text.append(material.text)
        materials_sorted = materials_text.copy()
        materials_sorted.sort()
        assert materials_sorted[:9] == materials_text[:9], "Materials are displayed in the wrong order"

    def test_material(driver, name):
        LibrarySteps.select_refridgerator_element(driver)
        LibrarySteps.click_library_tab(driver, 1)
        utils.choose_material(name, driver)
        sleep(3)
        LibrarySteps.click_library_tab(driver, 12)

class ViewportSteps:
    def click_tab(driver, sec, tab):
        if tab == 'scene index':
            utils.find_by_xpath(ViewportLocators.SCENE_INDEX_TAB, driver).click()
        elif tab == 'timeline':
            utils.find_by_xpath(ViewportLocators.TIMELINE_BAR, driver).click()
        elif tab == 'comments':
            utils.find_by_xpath(ViewportLocators.COMMENTS_BAR, driver).click()
        elif tab == 'settings':
            utils.find_by_xpath(ViewportLocators.SETTINGS_WINDOW, driver).click()
        elif tab == 'menu':
            utils.find_by_xpath(ViewportLocators.SCENE_MENU, driver).click()
        sleep(sec)

    def search_scene_element(driver, text):
        search = utils.find_by_xpath(ViewportLocators.SCENE_SEARCH, driver)
        search.click()
        sleep(2)
        search.send_keys(text)
        sleep(1)

    def clear_field(driver):
        utils.find_by_xpath("//div[ contains(@class, 'pl-2') ]//button", driver).click()
        sleep(3)

    def click_parent_tree(driver):
        utils.find_by_class("scene-index-prim-button-expand", driver, True)[0].click()
        sleep(2)

    def click_scene(driver):
        utils.find_by_class("bg-yellow-700", driver, True)[0].click()
<<<<<<< HEAD
    def set_samples(driver, samples):
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(samples)

    def start_render(driver):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        WebDriverWait(driver, 600).until(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        WebDriverWait(driver, 600).until_not(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        sleep(5)

    def return_to_viewport(driver):
        utils.find_by_xpath(FinalRenderLocators.BACK_BUTTON, driver).click()
        sleep(10)
        pyautogui.moveTo(500,700)
        pyautogui.dragTo(600, 700, 1, button='left')
=======
>>>>>>> 1c8c68241e7a8d54dead6f029d109cc0e7c282b9
        sleep(5)
