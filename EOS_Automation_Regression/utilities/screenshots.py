import datetime
import os
from logging import Logger
import time
from utilities.CustomLogger import custlogger


class Screen_shots():
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, driver, testcase_name="", module_name=""):
        test_name = testcase_name.replace(" ", "_")
        test_name = test_name.replace(" ", "_")
        date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        date = date.replace('', "_")
        date = date.replace(':', "_")
        date = date.replace(',', '')
        date = "_DATE_" + date
        screen_shot_folder_path = os.path.abspath('.') + "\\reports" + "\\Screenshots"
        if not os.path.exists(screen_shot_folder_path):
            os.makedirs(screen_shot_folder_path)
        file_path = os.path.abspath('.') + "\\reports\\Screenshots\\" + testcase_name + module_name + date + '.png'
        print(file_path)
        driver.save_screenshot(file_path)
        return ".\\Screenshots\\" + testcase_name + module_name + date + '.png'
