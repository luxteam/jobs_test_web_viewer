import os
import logging
import pyautogui
from selenium import webdriver
import time
import win32gui
import win32con
from selenium.webdriver.common.by import By
from pyautogui import typewrite, press
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from psutil import Popen, NoSuchProcess
from subprocess import PIPE, CREATE_NEW_CONSOLE
import sys
import traceback

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import local_config


pyautogui.FAILSAFE = False


# Logger for current test case
case_logger = None
# Streamer process (only for desktop version)
streamer_process = None


def close_process(process):
    try:
        child_processes = process.children()
        case_logger.info(f"Child processes: {child_processes}")
        for ch in child_processes:
            try:
                ch.kill()
                status = ch.status()
                case_logger.error(f"Process is alive: {ch}. Name: {ch.name()}. Status: {status}")
            except NoSuchProcess:
                case_logger.info(f"Process is killed: {ch}")

        try:
            process.kill()
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

        win32gui.ShowWindow(window_hwnd, win32con.SW_MAXIMIZE)
    else:
        driver = driver_web()
        driver.get(local_config.domain)

    return driver


def driver_desktop():
    global streamer_process
    streamer_process = Popen(["C:\\Program Files\\AMD\\AMD RenderStudio\\services\\WebUsdStreamServer\\Run.bat", "--webrtc-port", "10000", "--rest-port", "10001"], creationflags=CREATE_NEW_CONSOLE)
    time.sleep(2)

    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\AMD\\AMD RenderStudio\\AMD RenderStudio.exe"
    options.add_argument("--url-streamer=ws://localhost:10000")
    options.add_argument("--url-rest-streamer=http://localhost:10001")
    driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\jobs_test_web_viewer\\jobs\\driver\\100\\chromedriver.exe', options=options)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    return driver


def driver_web():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\jobs_test_web_viewer\\jobs\\driver\\105\\chromedriver.exe', options=options)
    
    return driver


def post_action(case, mode, driver):
    if mode == "desktop":   

        close_process(streamer_process)

    if driver:
        driver.close()


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


def load_scene(args, case, driver):
    if args.mode == "desktop":
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

    for i in range(60):
        try:
            loading_element= find_by_xpath("//div[ text() = 'Loading' ]", driver, False, 0)
            time.sleep(1)
        except:
            loading_element = None
            break

    if loading_element is not None:
        raise Exception("Can't detect scene loading")

    load_scene_time = time.time() - start_time

    time.sleep(case["viewport_render_delay"])

    return load_scene_time


def switch_window(driver):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)


def save_screen(screen_path, driver, extension = "jpg"):
    driver.save_screenshot(f"{screen_path}.{extension}")


def choose_material(material_name, driver):
    search = find_by_xpath("//input[ @placeholder='Search' ]", driver)
    search.click()
    time.sleep(2)
    search.send_keys(material_name)

    material_cards = find_by_class("material-card", driver, True)

    for card in material_cards:
        found_name = card.find_element(By.TAG_NAME, "h2").text

        if found_name == material_name:
            card.click()
            break
    else:
        assert False