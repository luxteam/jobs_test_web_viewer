from time import sleep
import sys
import os
from locators import *
from steps import LibrarySteps

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_material(args, case, driver, current_try):
    LibrarySteps.test_material(driver, case["material_name"], case["scroll"])