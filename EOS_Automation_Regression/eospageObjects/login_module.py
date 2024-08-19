import pytest
import time

from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from eospageObjects.user_settings import UserSettings


class eos_loginModule(Custom_code):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)

    eso_facility_dropDown = "//ul[@class='dropdown-menu']/li[1]//span[@role='listbox']"
    eso_dropdown_singleUser = "//select[@id='facilitySelect']/option[1]"
    eso_dropdown_testUser = "//select[@id='facilitySelect']/option[2]"

    def verifying_testuser(self):
        self.usersettings = UserSettings(self.driver)
        time.sleep(5)
        self.click_on_element(self.usersettings.dispatcher_name)
        time.sleep(5)
        self.click_on_element(self.eso_facility_dropDown, "xpath")
        time.sleep(5)
        assert (self.isElementPresent(self.eso_dropdown_testUser, "xpath"))
        time.sleep(5)

    def verifying_singleUser(self):
        self.usersettings = UserSettings(self.driver)
        time.sleep(5)
        self.click_on_element(self.usersettings.dispatcher_name)
        time.sleep(5)
        self.click_on_element(self.eso_facility_dropDown, "xpath")
        time.sleep(5)
        assert (self.isElementPresent(self.eso_dropdown_singleUser, "xpath"))
        time.sleep(5)
