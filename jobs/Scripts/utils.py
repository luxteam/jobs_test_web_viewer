import logging
import pyautogui
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pyautogui import typewrite, press
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE


pyautogui.FAILSAFE = False


# Logger for current test case
case_logger = None
# Streamer process (only for desktop version)
streamer_process = None


def pre_action(case, mode):
    if mode == "desktop":
        driver = driver_init_desktop()
        driver.switch_to.window(driver_init.window_handles[0])
    else
        driver = driver_init_web()

    return driver


def driver_init_desktop():
    global streamer_process
    streamer_process = Popen(["C:\\Program Files\\AMD\\AMD RenderStudio\\services\\WebUsdStreamServer\\Run.bat", "--webrtc-port", "10000", "--rest-port", "10001"], creationflags=CREATE_NEW_CONSOLE)
    sleep(2)

    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\AMD\\AMD RenderStudio\\AMD RenderStudio.exe"
    options.add_argument("--url-streamer=ws://localhost:10000")
    options.add_argument("--url-rest-streamer=http://localhost:10001")

    driver = webdriver.Chrome('..\\drivers\\chromedriver.exe', options=options)
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    return driver


def driver_init_web():
    options = webdriver.ChromeOptions()
    for flag in conf['chromeArguments']:
        options.add_argument(flag)
    preferences = conf['chromeSettings']
    options.add_experimental_option("prefs", preferences)
    self.driver = webdriver.Chrome('..\\drivers\\chromedriver.exe', options=options)
    
    return driver


def post_action(case, mode, driver):
    if mode == "desktop":   
        streamer_process.kill()

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


def is_case_skipped(case, render_platform, is_inventor=None):
    if case['status'] == 'skipped':
        return True

    return sum([render_platform & set(x) == set(x) for x in case.get('skip_on', '')])


def find_by_xpath(xpath, driver_init, many=False, wait=10):
    if not many:
        element = WebDriverWait(driver_init, wait).until(
            lambda d: d.find_element(By.XPATH, xpath)
        )
        return element
    else:
        try:
            elements = WebDriverWait(driver_init, wait).until(
                lambda d: d.find_elements(By.XPATH, xpath)
            )
            return elements
        except TimeoutException:
            return []


def find_by_class(class_name, driver_init, many=False, wait=10):
    if not many:
        element = WebDriverWait(driver_init, wait).until(
            lambda d: d.find_element(By.CLASS_NAME, class_name)
        )
        return element
    else:
        try:
            elements = WebDriverWait(driver_init, wait).until(
                lambda d: d.find_elements(By.CLASS_NAME, class_name)
            )
            return elements
        except TimeoutException:
            return []


def find_by_tag(tag_name, driver_init, many=False, wait=10):
    if not many:
        element = WebDriverWait(driver_init, wait).until(
            lambda d: d.find_element(By.TAG_NAME, tag_name)
        )
        return element
    else:
        try:
            elements = WebDriverWait(driver_init, wait).until(
                lambda d: d.find_elements(By.TAG_NAME, tag_name)
            )
            return elements
        except TimeoutException:
            return []


def load_scene(path, open_time, driver_init):
    find_by_class("p-2", driver_init=driver_init).click()
    sleep(1)
    pyautogui.typewrite(path)
    pyautogui.press("enter")
    sleep(open_time)


def switch_window(driver_init):
    driver_init.switch_to.window(driver_init.window_handles[1])
    sleep(1)
