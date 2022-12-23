import os
import logging
import pyautogui
from selenium import webdriver
import time
import win32gui
import win32api
import win32con
import zipfile
import requests
import wget
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautogui import typewrite, press
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from psutil import Popen, NoSuchProcess
from subprocess import PIPE, CREATE_NEW_CONSOLE
import sys
import traceback
from locators import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import local_config


pyautogui.FAILSAFE = False


# Logger for current test case
case_logger = None
# Streamer process (only for desktop version)
streamer_process = None
# Storage server process (only for desktop version)
storage_server_process = None


def close_process(process):
    try:
        child_processes = process.children()
        case_logger.info(f"Child processes: {child_processes}")
        for ch in child_processes:
            try:
                ch.kill()
            except NoSuchProcess:
                case_logger.info(f"Process is killed: {ch}")

        try:
            process.kill()
        except NoSuchProcess:
            case_logger.info(f"Process is killed: {process}")

        time.sleep(0.5)

        for ch in child_processes:
            try:
                status = ch.status()
                case_logger.error(f"Process is alive: {ch}. Name: {ch.name()}. Status: {status}")
            except NoSuchProcess:
                case_logger.info(f"Process is killed: {ch}")

        try:
            status = process.status()
            case_logger.error(f"Process is alive: {process}. Name: {process.name()}. Status: {status}")
        except NoSuchProcess:
            case_logger.info(f"Process is killed: {process}")
    except Exception as e:
        case_logger.error(f"Failed to close process: {str(e)}")
        case_logger.error(f"Traceback: {traceback.format_exc()}")


def pre_action(case, mode):
    if mode == "desktop":
        driver = driver_desktop()

        window_hwnd = None

        for window in pyautogui.getAllWindows():
            if "Web USD Viewer" in window.title:
                window_hwnd = window._hWnd
                break

        if not window_hwnd:
            raise Exception("Render Studio window not found")

        pyautogui.hotkey("win", "m")
        time.sleep(1)
        win32gui.ShowWindow(window_hwnd, win32con.SW_MAXIMIZE)
        time.sleep(1)
    else:
        driver = driver_web()
        driver.get(local_config.domain)

    return driver


def driver_desktop():
    install_chromedriver("desktop")

    global streamer_process, storage_server_process
    storage_server_process = Popen(["C:\\Program Files\\AMD\\AMD RenderStudio\\services\\WebUsdStorageServer\\WebUsdStorageServer.exe", "--port", "11000", "--local-mode",
        "--db-uri", "sqlite+aiosqlite:///C:\\Users\\user\\AppData\\Roaming\\AMDRenderStudio\\WebUsdStorageServer\\storage.db",
        "--storage-dir", "C:\\Users\\user\\AppData\\Roaming\\AMDRenderStudio\\WebUsdStorageServer\\.storage",
        "--storage-preset-dir", "C:\\Program Files\\AMD\\AMD RenderStudio\\services\\WebUsdStorageServer\\storage-preset"], creationflags=CREATE_NEW_CONSOLE)
    streamer_process = Popen(["C:\\Program Files\\AMD\\AMD RenderStudio\\services\\WebUsdStreamServer\\Run.bat", "--webrtc-port", "10000", "--rest-port", "10001", "--storage-service-url", "http://localhost:11000"], creationflags=CREATE_NEW_CONSOLE)
    time.sleep(2)

    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\AMD\\AMD RenderStudio\\AMD RenderStudio.exe"
    options.add_argument("--url-streamer=ws://localhost:10000")
    options.add_argument("--url-rest-streamer=http://localhost:10001")
    options.add_argument("--url-storage=http://localhost:11000")
    driver = webdriver.Chrome('..\\driver\\chromedriver.exe', options=options)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    return driver


def driver_web():
    install_chromedriver("web")

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome('..\\driver\\chromedriver.exe', options=options)
    
    return driver


def get_chrome_version():
    file = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    info = win32api.GetFileVersionInfo(file, "\\")
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = "{0}.{1}.{2}.{3}".format(win32api.HIWORD(ms), win32api.LOWORD (ms), win32api.HIWORD (ls), win32api.LOWORD (ls))
    case_logger.info("Chrome version: {}".format(version))
    return version


def install_chromedriver(mode):
    try:
        try:
            with open('..\\driver\\version.json') as json_file:
                version = json.load(json_file)['Chromedriver version']
        except FileNotFoundError:
            version = None
        if mode == "desktop":
            driver_version = "100.0.4896.60"
            if version != driver_version:
                driver_zip = wget.download('https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip'.format(driver_version), 'chromedriver.zip')
                with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
                    zip_ref.extractall('..\\driver')
                os.remove(driver_zip)
                data = {"Chromedriver version": driver_version}
                with open('..\\driver\\version.json', 'w') as f:
                    f.write(json.dumps(data))
                case_logger.info("Driver is installed. Version: {}".format(driver_version))
            else:
                case_logger.info("Driver is already installed")
        elif mode == "web":
            chrome_version = get_chrome_version()
            chrome_version = chrome_version.split('.')[0]
            driver_version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{}'.format(chrome_version)).text
            if version != driver_version:
                driver_zip = wget.download('https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip'.format(driver_version), 'chromedriver.zip')
                with zipfile.ZipFile(driver_zip, 'r') as zip_ref:
                    zip_ref.extractall('..\\driver')
                os.remove(driver_zip)
                data = {"Chromedriver version": driver_version}
                with open('..\\driver\\version.json', 'w') as f:
                    f.write(json.dumps(data))
                case_logger.info("Driver is installed. Version: {}".format(driver_version))
            else:
                case_logger.info("Driver is already installed")
    except Exception as e:
        case_logger.error(f"Failed to download chromedriver: {str(e)}")
        case_logger.error(f"Traceback: {traceback.format_exc()}")


def post_action(case, mode, driver):
    try:
        if mode == "desktop":   
            close_process(streamer_process)
            close_process(storage_server_process)

        if driver:
            driver.close()
    except Exception as e:
        case_logger.error(f"Failed to do post actions: {str(e)}")
        case_logger.error(f"Traceback: {traceback.format_exc()}")


def create_case_logger(case, log_path):
    formatter = logging.Formatter(fmt=u'[%(asctime)s] #%(levelname)-6s [F:%(filename)s L:%(lineno)d] >> %(message)s')

    file_handler = logging.FileHandler(filename=os.path.join(log_path, f"{case['case']}.log"), mode='a')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger(f"{case['case']}")
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    global case_logger
    case_logger = logger


def is_case_skipped(case, render_platform):
    if case['status'] == 'skipped':
        return True

    return sum([render_platform & set(x) == set(x) for x in case.get('skip_on', '')])


def find_by_xpath(xpath, driver, many=False, wait=10):
    if not many:
        try:
            element = WebDriverWait(driver, wait).until(
                lambda d: d.find_element(By.XPATH, xpath)
            )
            return element
        except TimeoutException:
            return None
    else:
        try:
            elements = WebDriverWait(driver, wait).until(
                lambda d: d.find_elements(By.XPATH, xpath)
            )
            return elements
        except TimeoutException:
            return []


def find_by_class(class_name, driver, many=False, wait=10):
    if not many:
        try:
            element = WebDriverWait(driver, wait).until(
                lambda d: d.find_element(By.CLASS_NAME, class_name)
            )
            return element
        except TimeoutException:
            return None
    else:
        try:
            elements = WebDriverWait(driver, wait).until(
                lambda d: d.find_elements(By.CLASS_NAME, class_name)
            )
            return elements
        except TimeoutException:
            return []


def find_by_tag(tag_name, driver, many=False, wait=10):
    if not many:
        try:
            element = WebDriverWait(driver, wait).until(
                lambda d: d.find_element(By.TAG_NAME, tag_name)
            )
            return element
        except TimeoutException:
            return None
    else:
        try:
            elements = WebDriverWait(driver, wait).until(
                lambda d: d.find_elements(By.TAG_NAME, tag_name)
            )
            return elements
        except TimeoutException:
            return []


def load_scene(args, case, driver, max_load_time=60):
    if args.mode == "desktop":
        try:
            # try to find scene in recently viewed items
            find_by_xpath(ViewportLocators.get_recently_viewed_item_locator(case["scene_path"]), driver=driver).click()
            time.sleep(1)
        except:
            # else open new scene through files browser
            find_by_class("p-2", driver=driver).click()
            time.sleep(1)
            scene_path = os.path.join(args.res_path, case["scene_path"])
            pyautogui.typewrite(scene_path)
            pyautogui.press("enter")
    else:
        scene_name = case['scene_name']
        find_by_xpath(f"//div[ @class = 'project-card-text' ]//div[ text() = '{scene_name}' ]", driver=driver).click()

    start_time = time.time()
    loading_element = find_by_xpath("//div[ text() = 'Loading' ]", driver)

    for i in range(max_load_time):
        case_logger.info(loading_element)

        loading_element= find_by_xpath("//div[ text() = 'Loading' ]", driver, False, 0)

        if loading_element == None:
            break
        else:
            time.sleep(1)

    if loading_element is not None:
        raise Exception("Can't detect scene loading")

    load_scene_time = time.time() - start_time

    if "viewport_render_delay" in case:
        time.sleep(case["viewport_render_delay"])

    return load_scene_time


def switch_window(driver):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)


def save_screen(screen_path, driver, extension = "jpg", save_final_render_image = False):
    if save_final_render_image:
        find_by_xpath(FinalRenderLocators.DOWNLOAD_IMAGE, driver).click()
        time.sleep(0.5)
        pyautogui.typewrite(f"{screen_path}.{extension}")
        pyautogui.press("enter")
        time.sleep(0.5)
    else:
        driver.save_screenshot(f"{screen_path}.{extension}")


def choose_material(material_name, driver, scroll = False, click = True):
    search = find_by_xpath(LibraryLocators.SEARCH_MATERIAL, driver)
    search.click()
    time.sleep(2)
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(material_name)

    # cards with materials can be reloaded few times, wait a bit
    time.sleep(2)

    if scroll:
        first_material = find_by_xpath(LibraryLocators.MATERIAL_CARD, driver)
        first_material.click() # focus on the materials table 
        ActionChains(driver)\
        .key_down(Keys.END)\
        .perform() # scroll down to load all materials

        needed_material = find_by_xpath(LibraryLocators.MATERIAL + material_name + '\"]', driver)
        driver.execute_script("arguments[0].scrollIntoView();", needed_material)
        needed_material.click()

    else:
        material_cards = find_by_xpath(LibraryLocators.MATERIAL_CARDS, driver, True)

        for card in material_cards:
            found_name = card.find_element(By.XPATH, LibraryLocators.MATERIAL_TITLE).text

            if found_name == material_name:
                if click:
                    card.click()

                break
        else:
            raise Exception("Material not found")
