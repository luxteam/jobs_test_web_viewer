from selenium import webdriver
from time import sleep
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from steps import *
from locators import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_001(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'play')
    sleep(1.5)
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') != '0'


def test_002(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame')
    AnimationSteps.click_timeline_button(driver, 'first_frame')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '0'


def test_003(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '2048'


def test_004(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame', 2)
    AnimationSteps.click_timeline_button(driver, 'focus')
    sleep(8)


def test_005(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'current', '10')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '10'


def test_006(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'start', '10')
    assert utils.find_by_xpath(AnimationLocators.START_FRAME, driver).get_property('value') == '10'


def test_007(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    assert utils.find_by_xpath(AnimationLocators.END_FRAME, driver).get_property('value') == '10'


def test_008(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_arrows(driver, 'current_inc')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '1'


def test_009(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'current', '10')
    AnimationSteps.click_arrows(driver, 'current_dec')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '9'


def test_010(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_arrows(driver, 'start_inc')
    assert utils.find_by_xpath(AnimationLocators.START_FRAME, driver).get_property('value') == '1'


def test_011(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'start', '10')
    AnimationSteps.click_arrows(driver, 'start_dec')
    assert utils.find_by_xpath(AnimationLocators.START_FRAME, driver).get_property('value') == '9'


def test_012(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    AnimationSteps.click_arrows(driver, 'end_inc')
    assert utils.find_by_xpath(AnimationLocators.END_FRAME, driver).get_property('value') == '11'


def test_013(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    AnimationSteps.click_arrows(driver, 'end_dec')
    assert utils.find_by_xpath(AnimationLocators.END_FRAME, driver).get_property('value') == '9'


def test_014(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'first_frame')
    AnimationSteps.click_arrows(driver, 'current_dec')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '0'


def test_015(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame')
    AnimationSteps.click_arrows(driver, 'current_inc')
    assert utils.find_by_xpath(AnimationLocators.CURRENT_FRAME, driver).get_property('value') == '2048'


def test_016(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    sleep(8)