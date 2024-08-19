import sys
import time
from _ast import Assert
import pytest
from selenium.webdriver import Keys
#sys.path.insert(1, 'C:/Users/pjarubula/Documents/EPCProject/EPCProject')
from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from utilities.CustomLogger import custlogger
from logging import Logger
from selenium.webdriver.support.ui import Select

# from utilities.screenshots import Screen_shots


class UserSettings(Custom_code):
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)

    #user settings locators
    landing_page_dropdown = "//*[@id='userSettingsWindow']//div//div[2]//span//button"
    landing_page_dropdown_ul_list = "//*[contains(@id, 'ddlLandingPage_listbox') and contains(@data-role, 'staticlist')]"
    user_setting_save_button = "btnUserSettingsSave"
    dispatcher_name = "dispatcherNameMain"
    user_settings = "btnProfileUSerSettings"
    user_settings_close_button = "//*[contains(@role, 'button') and contains(@aria-label, 'Close')]"

    def change_landing_page(self, index_no):
        self.click_on_element(self.dispatcher_name)
        self.click_on_element(self.user_settings)
        time.sleep(2)
        self.click_on_element(self.landing_page_dropdown, "xpath")
        time.sleep(1)
        dropd_list = self.driver.find_element(By.XPATH, self.landing_page_dropdown_ul_list)
        time.sleep(1)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        #self.select_values_from_drop_down_textContent(dropd_items, page_name)
        self.select_values_from_drop_down_index(dropd_items, index_no)
        self.click_on_element(self.user_setting_save_button)
        time.sleep(3)
        self.click_on_element(self.user_settings_close_button)



