from selenium import webdriver
import time
from time import sleep
import sys
import os
import inspect
from selenium.webdriver import ActionChains
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


class ViewportSteps:
    def find_and_select_object_in_index(driver, name):
        scene_tab = utils.find_by_xpath(ViewportLocators.SCENE_INDEX, driver)
        scene_tab.click()
        sleep(2)

        search = utils.find_by_xpath(SceneIndexLocators.SEARCH_SCENE, driver)
        search.click()
        sleep(1)

        search.send_keys(name)
        sleep(2)

        utils.find_by_class("bg-yellow-700", driver, True)[0].click()
        sleep(1)

        scene_tab.click()
        sleep(1)
    

    def library_select_material(driver, mat_name):
        library = utils.find_by_xpath(ViewportLocators.LIBRARY, driver)
        library.click()
        sleep(1)

        utils.find_by_xpath("//./div[ @class='click-area' ]//h2[ text()='" + mat_name + "' ]", driver).click()
        sleep(3)

        library.click()
        sleep(8)


    def library_drag_and_drop_material_on_object(driver, material_name, object_name):
        library = utils.find_by_xpath(ViewportLocators.LIBRARY, driver)
        library.click()
        sleep(1)

        material = utils.find_by_xpath("//./div[ @class='click-area' ]//h2[ text()='" + material_name + "' ]", driver)
        obj = utils.find_by_xpath() # TODO: find out how to locate object

        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(material, obj).perform()


    def properties_set_move(driver, x:float=None, y:float=None, z:float=None):
        properties = utils.find_by_xpath(ViewportLocators.PROPERTIES, driver)
        properties.click()
        sleep(1)

        move_btn = utils.find_by_xpath(PropertiesLocators.MOVE, driver)
        move_btn.click()
        sleep(1)

        if x is not None:
            move_x_field = utils.find_by_xpath(PropertiesLocators.MOVE_X, driver)
            move_x_field.send_keys(Keys.CONTROL + "a")
            move_x_field.send_keys(str(x))

        if y is not None:
            move_y_field = utils.find_by_xpath(PropertiesLocators.MOVE_Y, driver)
            move_y_field.send_keys(Keys.CONTROL + "a")
            move_y_field.send_keys(str(y))

        if z is not None:
            move_z_field = utils.find_by_xpath(PropertiesLocators.MOVE_Z, driver)
            move_z_field.send_keys(Keys.CONTROL + "a")
            move_z_field.send_keys(str(z))

        move_btn.click()
        sleep(1)

        properties.click()


    def properties_set_rotate(driver, x:float=None, y:float=None, z:float=None):
        properties = utils.find_by_xpath(ViewportLocators.PROPERTIES, driver)
        properties.click()
        sleep(1)

        rotate_btn = utils.find_by_xpath(PropertiesLocators.ROTATE, driver)
        rotate_btn.click()
        sleep(1)

        if x is not None:
            rotate_x_field = utils.find_by_xpath(PropertiesLocators.ROTATE_X, driver)
            rotate_x_field.send_keys(Keys.CONTROL + "a")
            rotate_x_field.send_keys(str(x))

        if y is not None:
            rotate_y_field = utils.find_by_xpath(PropertiesLocators.ROTATE_Y, driver)
            rotate_y_field.send_keys(Keys.CONTROL + "a")
            rotate_y_field.send_keys(str(y))

        if z is not None:
            rotate_z_field = utils.find_by_xpath(PropertiesLocators.ROTATE_Z, driver)
            rotate_z_field.send_keys(Keys.CONTROL + "a")
            rotate_z_field.send_keys(str(z))

        rotate_btn.click()
        sleep(1)

        properties.click()


    def properties_set_scale(driver, x:float=None, y:float=None, z:float=None):
        properties = utils.find_by_xpath(ViewportLocators.PROPERTIES, driver)
        properties.click()
        sleep(1)

        scale_btn = utils.find_by_xpath(PropertiesLocators.SCALE, driver)
        scale_btn.click()
        sleep(1)

        if x is not None:
            scale_x_field = utils.find_by_xpath(PropertiesLocators.SCALE_X, driver)
            scale_x_field.send_keys(Keys.CONTROL + "a")
            scale_x_field.send_keys(str(x))

        if y is not None:
            scale_y_field = utils.find_by_xpath(PropertiesLocators.SCALE_Y, driver)
            scale_y_field.send_keys(Keys.CONTROL + "a")
            scale_y_field.send_keys(str(y))

        if z is not None:
            scale_z_field = utils.find_by_xpath(PropertiesLocators.SCALE_Z, driver)
            scale_z_field.send_keys(Keys.CONTROL + "a")
            scale_z_field.send_keys(str(z))

        scale_btn.click()
        sleep(1)

        properties.click()
