from selenium import webdriver
import time
from time import sleep
import sys
import os
import inspect
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautogui import typewrite, press, move
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import utils

pyautogui.FAILSAFE = False

class CommonSteps:
    def element_exists(driver, locator):
        return utils.find_by_xpath(locator, driver).is_displayed()

    def select_menu_item(driver, element):
        elements = ['Home', 'Open', 'Recent', 'Save', 'Save As ...', 'Delete', 'Versions']
        if element not in elements:
            raise Exception("Unknown menu element")
        else:
            utils.find_by_xpath(ViewportLocators.file_menu(element), driver).click()
            sleep(1)

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
        sleep(0.5)

    def set_resolution(driver, width, height):
        utils.find_by_xpath(FinalRenderLocators.WIDTH, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.WIDTH, driver).send_keys(width)
        sleep(0.5)
        utils.find_by_xpath(FinalRenderLocators.HEIGHT, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.HEIGHT, driver).send_keys(height)
        sleep(0.5)

    def set_samples(driver, samples):
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(Keys.CONTROL + "a")
        utils.find_by_xpath(FinalRenderLocators.SAMPLES, driver).send_keys(samples)
        sleep(0.5)

    def start_render(driver):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        WebDriverWait(driver, 600).until(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        WebDriverWait(driver, 600).until_not(
                EC.presence_of_element_located((By.XPATH, FinalRenderLocators.RENDER_SPINNER))
            )
        sleep(5)

        return FinalRenderSteps.get_render_time(driver)

    def return_to_viewport(driver, delay=5):
        utils.find_by_xpath(FinalRenderLocators.BACK_BUTTON, driver).click()
        sleep(10)
        pyautogui.moveTo(500,700)
        pyautogui.dragTo(600, 700, 1, button='left')
        sleep(delay)

    def check_progress_bar(driver):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        sleep(1)
        style_value_1 = utils.find_by_xpath(FinalRenderLocators.PROGRESS_BAR, driver).value_of_css_property('min-width')
        sleep(4)
        style_value_2 = utils.find_by_xpath(FinalRenderLocators.PROGRESS_BAR, driver).value_of_css_property('min-width')
        assert float(style_value_2[0:-1]) >= float(style_value_1[0:-1]), "Progress bar is filling incorrectly"

    def stop_before_end(driver, restart=False):
        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        sleep(1.5)
        utils.find_by_xpath(FinalRenderLocators.STOP_RENDER, driver, True)[1].click()
        sleep(3)
        if restart:
            utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
            sleep(3)
            assert CommonSteps.element_exists(driver, FinalRenderLocators.PROGRESS_BAR), "Render didn't restart"
        else:
            assert utils.find_by_xpath(FinalRenderLocators.PROGRESS_BAR, driver, False, 2) == None, "Render didn't stop"

    def save_before_end(driver, args, case):
        image_path = os.path.abspath(os.path.join(args.output, "Color", case["case"]))

        utils.find_by_xpath(FinalRenderLocators.BEGIN_RENDER, driver).click()
        sleep(1.5)
        utils.find_by_xpath(FinalRenderLocators.DOWNLOAD_IMAGE, driver).click()
        time.sleep(0.5)
        pyautogui.typewrite(f"{image_path}.jpg")
        pyautogui.press("enter")
        time.sleep(0.5)

    def get_render_time(driver):
        raw_render_time = utils.find_by_xpath(FinalRenderLocators.TIME_TAKEN, driver, wait=0).text

        parts = raw_render_time.split()[1].split(":")
        render_hours = float(parts[0])
        render_minutes = float(parts[1])
        render_seconds = float(parts[2])

        return render_hours * 60 * 60 + render_minutes * 60 + render_seconds


class LibrarySteps:
    def click_library_tab(driver, sec):
        utils.find_by_xpath(LibraryLocators.LIBRARY_TAB, driver).click()
        sleep(sec)

    def select_element(driver, element):
        utils.find_by_xpath(LibraryLocators.SCENE_INDEX_TAB, driver).click()
        sleep(2)
        search = utils.find_by_xpath(LibraryLocators.SCENE_SEARCH, driver)
        search.click()
        sleep(2)
        if element == "sphere":
            search.send_keys("Sphere_001")
        elif element == "fridge":
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
        sleep(6)
        materials = utils.find_by_xpath(LibraryLocators.MATERIAL_CARDS, driver, True)
        utils.case_logger.info("Materials: {}".format(materials))
        return materials

    def select_material(driver, material):
        utils.find_by_xpath(LibraryLocators.MATERIAL + str(material).capitalize() + '\"]', driver).click()
        sleep(3)

    def set_sorting(driver, key):
        utils.find_by_xpath(LibraryLocators.SORTING_BY, driver).click()
        sleep(1)
        utils.find_by_xpath(LibraryLocators.SORTING_KEY + str(key).capitalize() + '\"]', driver).click()
        sleep(5)

    def sorting_by_title(driver):
        materials = utils.find_by_xpath(LibraryLocators.MATERIAL_TITLE, driver, True)
        materials_text = []
        for material in materials:
            if material.text != None:
                materials_text.append(material.text)
        materials_sorted = materials_text.copy()
        materials_sorted.sort()
        utils.case_logger.info("Materials RS: {}".format(materials_text))
        utils.case_logger.info("Materials sorted: {}".format(materials_sorted))
        assert materials_sorted == materials_text, "Materials are displayed in the wrong order"

    def test_material(driver, name, exact_title_match=False, element="sphere"):
        LibrarySteps.select_element(driver, element)
        ViewportSteps.focus_on_element(driver)
        LibrarySteps.click_library_tab(driver, 1)
        utils.choose_material(name, driver, exact_title_match)
        sleep(3)
        LibrarySteps.click_library_tab(driver, 12)
        ViewportSteps.move_scene(driver)

class ViewportSteps:
    def click_tab(driver, delay, tab):
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
        sleep(delay)

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
        utils.find_by_class("scene-index-prim-button-expand-container", driver, True)[0].click()
        sleep(2)

    def click_scene(driver):
        utils.find_by_class("bg-yellow-700", driver, True)[0].click()

    def rotate_scene(driver):
        # TODO: remove hardcoded coordinate values
        pyautogui.moveTo(800, 750)
        sleep(1)
        pyautogui.mouseDown()
        sleep(1)
        pyautogui.moveRel(-200, 100)
        sleep(1)
        pyautogui.mouseUp()
        sleep(8)

    def move_scene(driver):
        # TODO: remove hardcoded coordinate values
        pyautogui.moveTo(800, 750)
        sleep(1)
        pyautogui.mouseDown(button='right')
        sleep(1)
        pyautogui.moveRel(50, 0)
        sleep(1)
        pyautogui.mouseUp(button='right')
        sleep(8)

    def focus_on_element(driver):
        utils.find_by_xpath(ViewportLocators.FOCUS, driver).click()

    def select_element(driver, element_name):
        utils.find_by_xpath(LibraryLocators.SCENE_INDEX_TAB, driver).click()
        sleep(2)
        search = utils.find_by_xpath(LibraryLocators.SCENE_SEARCH, driver)
        search.click()
        sleep(2)
        search.send_keys(element_name)
        sleep(1)
        utils.find_by_class("bg-yellow-700", driver, True)[0].click()
        sleep(1)
        utils.find_by_xpath(LibraryLocators.SCENE_INDEX_TAB, driver).click()
        sleep(1)

    def project_view(driver):
        utils.find_by_xpath(ViewportLocators.PROJECT_VIEW, driver).click()

    def test_share_button(driver):
        utils.find_by_xpath(ViewportLocators.HAS_MENU, driver, True)[1].click()
        sleep(1)
        utils.find_by_xpath(ViewportLocators.REQUEST_LINK, driver).click()
        #pyautogui.click(970, 170)

class PropertiesSteps:
    def select_object(driver):
        utils.find_by_xpath(ViewportLocators.SCENE_INDEX_TAB, driver).click()
        sleep(0.5)
        utils.find_by_xpath(ViewportLocators.expand_node("Scene"), driver).click()
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
        sleep(0.5)
    
    def close_properties(driver):
        utils.find_by_xpath(ViewportLocators.PROPERTIES, driver).click()
        sleep(0.5)

    def lock(driver):
        utils.find_by_xpath(PropertiesLocators.LOCK_BUTTON, driver).click()
        sleep(1)

    def unlock(driver):
        utils.find_by_xpath(PropertiesLocators.UNLOCK_BUTTON, driver).click()
        sleep(1)

    def set(driver, index, axis, input):
        utils.find_by_xpath('(//h3[text()[contains(.,"Properties")]])[2]', driver).click()
        value = utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).get_attribute("value")
        if type(input) == int:
            if input > 0:
                for _ in range(input):
                    sleep(0.5)
                    utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[2], driver).click()
            else:
                for _ in range(abs(input)):
                    sleep(0.5)
                    utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[1], driver).click()
        else:
            utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).send_keys(Keys.CONTROL + "a")

            for char in input:
                utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).send_keys(char)
                sleep(0.1)

        sleep(5)
        return value
        
    def settings(driver, axis, value):
        utils.find_by_xpath(ViewportLocators.SETTINGS_WINDOW, driver).click()
        if axis == "move":
            utils.find_by_xpath(SettingsLocators.MOVE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.MOVE_INPUT, driver).send_keys(value)
        elif axis == "rotate":
            utils.find_by_xpath(SettingsLocators.ROTATE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.ROTATE_INPUT, driver).send_keys(value)
        elif axis == "scale":
            utils.find_by_xpath(SettingsLocators.SCALE_INPUT, driver).send_keys(Keys.CONTROL + "a")
            utils.find_by_xpath(SettingsLocators.SCALE_INPUT, driver).send_keys(value)
        utils.find_by_xpath(ViewportLocators.SETTINGS_WINDOW, driver).click()

    def value(driver, index, axis, value, init_value="0"):
        if int(utils.find_by_xpath(PropertiesLocators.properties_locators(index, axis)[0], driver).get_attribute("value")) - int(value) == int(init_value):
            return True
        else: return False


class AnimationSteps:
    def click_timeline_button(driver, button, delay=0):
        if button == 'first_frame':
            utils.find_by_xpath(AnimationLocators.TIMELINE_BUTTON + '[1]', driver).click()
        elif button == 'play':
            utils.find_by_xpath(AnimationLocators.TIMELINE_BUTTON + '[2]', driver).click()
        elif button == 'last_frame':
            utils.find_by_xpath(AnimationLocators.TIMELINE_BUTTON + '[3]', driver).click()
        elif button == 'focus':
            utils.find_by_xpath(AnimationLocators.FOCUS, driver).click()
        sleep(delay)
        
    def set_frame(driver, field, value):
        if field == 'current':
            frame = utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver)
        elif field == 'start':
            frame = utils.find_by_xpath(AnimationLocators.START_FRAME, driver)
        elif field == 'end':
            frame = utils.find_by_xpath(AnimationLocators.END_FRAME, driver)
        sleep(0.5)
        action = ActionChains(driver)
        action.double_click(frame).perform()
        frame.send_keys(value)
        frame.send_keys(Keys.ENTER)

    def click_arrows(driver, arrow, clicks=1):
        for i in range(clicks):
            if arrow == 'current_inc':
                utils.find_by_xpath(AnimationLocators.CURRENT_INC, driver).click()
            elif arrow == 'current_dec':
                utils.find_by_xpath(AnimationLocators.CURRENT_DEC, driver).click()
            elif arrow == 'start_inc':
                utils.find_by_xpath(AnimationLocators.START_INC, driver).click()
            elif arrow == 'start_dec':
                utils.find_by_xpath(AnimationLocators.START_DEC, driver).click()
            elif arrow == 'end_inc':
                utils.find_by_xpath(AnimationLocators.END_INC, driver).click()
            elif arrow == 'end_dec':
                utils.find_by_xpath(AnimationLocators.END_DEC, driver).click()
            sleep(0.1)
