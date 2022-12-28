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
    AnimationSteps.click_timeline_button(driver, 'play', 0)
    sleep(8)


def test_002(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame', 0)
    AnimationSteps.click_timeline_button(driver, 'first_frame', 0)
    sleep(8)


def test_003(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame', 0)
    sleep(8)


def test_004(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame', 2)
    AnimationSteps.click_timeline_button(driver, 'focus', 0)
    sleep(8)


def test_005(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'current', '10')
    sleep(8)


def test_006(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'start', '10')
    sleep(8)


def test_007(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    sleep(8)


def test_008(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_arrows(driver, 'current_inc')
    sleep(8)


def test_009(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'current', '10')
    AnimationSteps.click_arrows(driver, 'current_dec')
    sleep(8)


def test_010(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_arrows(driver, 'start_inc')
    sleep(8)


def test_011(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'start', '10')
    AnimationSteps.click_arrows(driver, 'start_dec')
    sleep(8)


def test_012(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    AnimationSteps.click_arrows(driver, 'end_inc')
    sleep(8)


def test_013(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.set_frame(driver, 'end', '10')
    AnimationSteps.click_arrows(driver, 'end_dec')
    sleep(8)


def test_014(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'first_frame', 0)
    AnimationSteps.click_arrows(driver, 'current_dec')
    sleep(8)


def test_015(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    AnimationSteps.click_timeline_button(driver, 'last_frame', 0)
    AnimationSteps.click_arrows(driver, 'current_inc')
    sleep(8)


def test_016(args, case, driver, current_try):
    ViewportSteps.click_tab(driver, 2, 'timeline')
    sleep(8)