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

class CommonSteps:
    def element_exists(driver, locator):
        return utils.find_by_xpath(locator, driver).is_displayed()

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
        sleep(5)

class PropertiesSteps:
    def select_object(driver):
        utils.find_by_xpath(ViewportLocators.SCENE_INDEX, driver).click()
        sleep(0.5)
        utils.find_by_xpath(ViewportLocators.expand_node("Kitchen_set"), driver).click()
        utils.find_by_xpath(ViewportLocators.expand_node("Props_grp"), driver).click()
        utils.find_by_xpath(ViewportLocators.expand_node("North_grp"), driver).click()
        utils.find_by_xpath(ViewportLocators.expand_node("FridgeArea_grp"), driver).click()
        utils.find_by_xpath(ViewportLocators.expand_node("Refridgerator_1"), driver).click()
        utils.find_by_xpath(ViewportLocators.expand_node("Geom"), driver).click()
        utils.find_by_xpath(ViewportLocators.FRIDGE, driver).click()

    def open_properties(driver):
        utils.find_by_xpath(ViewportLocators.PROPERTIES, driver).click()
        sleep(0.5)
        utils.find_by_xpath(PropertiesLocators.MOVE, driver).click()
        utils.find_by_xpath(PropertiesLocators.ROTATE, driver).click()
        utils.find_by_xpath(PropertiesLocators.SCALE, driver).click()
    
    def close_properties(driver):
        utils.find_by_xpath(ViewportLocators.PROPERTIES, driver).click()
        sleep(0.5)

    def lock(driver):
        utils.find_by_xpath(PropertiesLocators.LOCK_BUTTON, driver).click()

    def unlock(driver):
        utils.find_by_xpath(PropertiesLocators.UNLOCK_BUTTON, driver).click()

    def set(driver, index, axis, input):
        value = utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).get_attribute("value")
        if type(input) == int:
            if input > 0:
                for _ in range(input):
                    utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[2], driver).click()
            else:
                for _ in range(abs(input)):
                    utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[1], driver).click()
        else:
            utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).send_keys(input)
        sleep(5)
        return value
        
    def settings(driver, axis, value):
        utils.find_by_xpath(ViewportLocators.SETTING, driver).click()
        if axis == "move":
            utils.find_by_xpath(SettingsLocators.MOVE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.MOVE_INPUT, driver).send_keys(value)
        elif axis == "rotate":
            utils.find_by_xpath(SettingsLocators.ROTATE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.ROTATE_INPUT, driver).send_keys(value)
        elif axis == "scale":
            utils.find_by_xpath(SettingsLocators.SCALE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.SCALE_INPUT, driver).send_keys(value)
        utils.find_by_xpath(ViewportLocators.SETTING, driver).click()

    def value(driver, index, axis, value, init_value="0"):
        if int(utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).get_attribute("value")) - int(value) == int(init_value):
            return True
        else: return False