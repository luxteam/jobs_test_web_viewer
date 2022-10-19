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
from locators import *
from steps import *

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils

def test_001(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)

def test_002(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.close_properties(driver)

def test_003(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.set(driver, "move", "X", 1)
    assert PropertiesSteps.value(driver, "move", "X", "0") == True, "Properties can be changed while being unlocked"

def test_004(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", 1)
    assert PropertiesSteps.value(driver, "move", "X", "1") == True, "Properties are not changing after locking"

def test_005(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.unlock(driver)
    PropertiesSteps.set(driver, "move", "X", 1)
    assert PropertiesSteps.value(driver, "move", "X", "0") == True, "Properties can be changed while being unlocked"

def test_006(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", "10")
    assert PropertiesSteps.value(driver, "move", "X", "10") == True, "Incorrect field value"

def test_007(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", "-10")
    assert PropertiesSteps.value(driver, "move", "X", "10") == True, "Incorrect field value"

def test_008(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Y", "10")
    assert PropertiesSteps.value(driver, "move", "Y", "10") == True, "Incorrect field value"

def test_009(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Y", "-10")
    assert PropertiesSteps.value(driver, "move", "Y", "10") == True, "Incorrect field value"

def test_010(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Z", "10")
    assert PropertiesSteps.value(driver, "move", "Z", "10") == True, "Incorrect field value"

def test_011(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Z", "-10")
    assert PropertiesSteps.value(driver, "move", "Z", "-10") == True, "Incorrect field value"

def test_012(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.select_object(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "X", "10")
    assert PropertiesSteps.value(driver, "rotate", "X", "10") == True, "Incorrect field value"

def test_013(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "X", "-10")
    assert PropertiesSteps.value(driver, "rotate", "X", "-10") == True, "Incorrect field value"

def test_014(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Y", "10")
    assert PropertiesSteps.value(driver, "rotate", "Y", "10") == True, "Incorrect field value"

def test_015(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Y", "-10")
    assert PropertiesSteps.value(driver, "rotate", "Y", "-10") == True, "Incorrect field value"

def test_016(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Z", "10")
    assert PropertiesSteps.value(driver, "rotate", "Z", "10") == True, "Incorrect field value"

def test_017(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Z", "-10")
    assert PropertiesSteps.value(driver, "rotate", "Z", "-10") == True, "Incorrect field value"
    

def test_018(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "X", "10")
    assert PropertiesSteps.value(driver, "scale", "X", "10") == True, "Incorrect field value"

def test_019(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "X", "-10")
    assert PropertiesSteps.value(driver, "scale", "X", "-10") == True, "Incorrect field value"

def test_020(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Y", "10")
    assert PropertiesSteps.value(driver, "scale", "Y", "10") == True, "Incorrect field value"

def test_021(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Y", "-10")
    assert PropertiesSteps.value(driver, "scale", "Y", "-10") == True, "Incorrect field value"

def test_022(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Z", "10")
    assert PropertiesSteps.value(driver, "scale", "Z", "10") == True, "Incorrect field value"

def test_023(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Z", "-10")
    assert PropertiesSteps.value(driver, "scale", "Z", "-10") == True, "Incorrect field value"

def test_024(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", 10)
    assert PropertiesSteps.value(driver, "move", "X", "10") == True, "Incorrect field value"

def test_025(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", -10)
    assert PropertiesSteps.value(driver, "move", "X", "-10") == True, "Incorrect field value"

def test_026(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Y", 10)
    assert PropertiesSteps.value(driver, "move", "Y", "10") == True, "Incorrect field value"

def test_027(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Y", -10)
    assert PropertiesSteps.value(driver, "move", "Y", "-10") == True, "Incorrect field value"

def test_028(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Z", 10)
    assert PropertiesSteps.value(driver, "move", "Z", "10") == True, "Incorrect field value"

def test_029(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "Z", -10)
    assert PropertiesSteps.value(driver, "move", "Z", "-10") == True, "Incorrect field value"

def test_030(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "X", 10)
    assert PropertiesSteps.value(driver, "rotate", "X", "10") == True, "Incorrect field value"

def test_031(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "X", -10)
    assert PropertiesSteps.value(driver, "rotate", "X", "-10") == True, "Incorrect field value"

def test_032(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Y", 10)
    assert PropertiesSteps.value(driver, "rotate", "Y", "10") == True, "Incorrect field value"

def test_033(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Y", -10)
    assert PropertiesSteps.value(driver, "rotate", "Y", "-10") == True, "Incorrect field value"

def test_034(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Z", 10)
    assert PropertiesSteps.value(driver, "rotate", "Z", "10") == True, "Incorrect field value"

def test_035(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "rotate", "Z", -10)
    assert PropertiesSteps.value(driver, "rotate", "Z", "-10") == True, "Incorrect field value"

def test_036(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "X", 10)
    assert PropertiesSteps.value(driver, "scale", "X", "10") == True, "Incorrect field value"

def test_037(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "X", -10)
    assert PropertiesSteps.value(driver, "scale", "X", "-10") == True, "Incorrect field value"

def test_038(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Y", 10)
    assert PropertiesSteps.value(driver, "scale", "Y", "10") == True, "Incorrect field value"

def test_039(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Y", -10)
    assert PropertiesSteps.value(driver, "scale", "Y", "-10") == True, "Incorrect field value"

def test_040(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Z", 10)
    assert PropertiesSteps.value(driver, "scale", "Z", "10") == True, "Incorrect field value"

def test_041(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "scale", "Z", -10)
    assert PropertiesSteps.value(driver, "scale", "Z", "-10") == True, "Incorrect field value"

def test_042(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.set(driver, "move", "X", "abc")
    assert CommonSteps.element_exists(driver, PropertiesLocators.NOT_A_NUMBER_TOOLTIP) == True, "Invalid imput tooltip does not appear"

def test_043(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "X", -10)
    assert PropertiesSteps.value(driver, "move", "X", "-50") == True, "Incorrect field value"

def test_044(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "X", 10)
    assert PropertiesSteps.value(driver, "move", "X", "50") == True, "Incorrect field value"

def test_045(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "Y", -10)
    assert PropertiesSteps.value(driver, "move", "Y", "-50") == True, "Incorrect field value"

def test_046(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "Y", 10)
    assert PropertiesSteps.value(driver, "move", "Y", "50") == True, "Incorrect field value"

def test_047(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "Z", -10)
    assert PropertiesSteps.value(driver, "move", "Z", "-50") == True, "Incorrect field value"

def test_048(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "move", "5")
    PropertiesSteps.set(driver, "move", "Z", 10)
    assert PropertiesSteps.value(driver, "move", "Z", "50") == True, "Incorrect field value"

def test_049(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "X", -10)
    assert PropertiesSteps.value(driver, "rotate", "X", "-50") == True, "Incorrect field value"

def test_050(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "X", 10)
    assert PropertiesSteps.value(driver, "rotate", "X", "50") == True, "Incorrect field value"

def test_051(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "Y", -10)
    assert PropertiesSteps.value(driver, "rotate", "Y", "-50") == True, "Incorrect field value"

def test_052(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "Y", 10)
    assert PropertiesSteps.value(driver, "rotate", "Y", "50") == True, "Incorrect field value"

def test_053(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "Z", -10)
    assert PropertiesSteps.value(driver, "rotate", "Z", "-50") == True, "Incorrect field value"

def test_054(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "rotate", "5")
    PropertiesSteps.set(driver, "rotate", "Z", 10)
    assert PropertiesSteps.value(driver, "rotate", "Z", "50") == True, "Incorrect field value"

def test_055(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "X", -10)
    assert PropertiesSteps.value(driver, "scale", "X", "-50") == True, "Incorrect field value"

def test_056(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "X", 10)
    assert PropertiesSteps.value(driver, "scale", "X", "50") == True, "Incorrect field value"

def test_057(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "Y", -10)
    assert PropertiesSteps.value(driver, "scale", "Y", "-50") == True, "Incorrect field value"

def test_058(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "Y", 10)
    assert PropertiesSteps.value(driver, "scale", "Y", "50") == True, "Incorrect field value"

def test_059(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "Z", -10)
    assert PropertiesSteps.value(driver, "scale", "Z", "-50") == True, "Incorrect field value"

def test_060(args, case, driver, current_try):
    PropertiesSteps.select_object(driver)
    PropertiesSteps.open_properties(driver)
    PropertiesSteps.lock(driver)
    PropertiesSteps.settings(driver, "scale", "5")
    PropertiesSteps.set(driver, "scale", "Z", 10)
    assert PropertiesSteps.value(driver, "scale", "Z", "50") == True, "Incorrect field value"