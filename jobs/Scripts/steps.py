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

    def set_samples(driver, samples):
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(samples)

    def start_render(driver):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        WebDriverWait(driver, 500).until(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        WebDriverWait(driver, 500).until_not(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        sleep(5)

    def return_to_viewport(driver):
        utils.find_by_xpath(FinalRenderLocators.BACK_BUTTON, driver).click()
        sleep(10)
        pyautogui.moveTo(500,700)
        pyautogui.dragTo(600, 700, 1, button='left')
        sleep(5)