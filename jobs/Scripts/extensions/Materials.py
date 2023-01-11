from time import sleep
import sys
import os
from locators import *
from steps import LibrarySteps

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
import utils


def test_material(args, case, driver, current_try):
    if 'exact_title_match' in case:
        LibrarySteps.test_material(driver, case["material_name"], exact_title_match=case["exact_title_match"])
    else:
        LibrarySteps.test_material(driver, case["material_name"], exact_title_match=False)
