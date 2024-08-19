import os

import openpyxl

from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from utilities.read_write_Data_excel import Read_Write_Data
import pandas as pd


class eos_manual_regression(Custom_code):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.read_excel = Read_Write_Data()

    profile_id = "dispatcherNameMain"
    settings_id = "btnProfileUSerSettings"
    initial_page_list = "[aria-owns='ddlLandingPage_listbox']"
    facility_list_id = "ddlLandingPage_listbox"
    settings_save_button = "//button[@id='btnUserSettingsSave']"
    settings_close_button = "//div[contains(@class,'k-window-titlebar k-hstack')]//a[@aria-label='Close']"
    facility_dashboard_deliveries = "//li[@id='dashboardTabstrip-tab-1']"
    facility_dashboard_pickups = "//li[@id='dashboardTabstrip-tab-2']"
    facility_dashboard_exceptions = "//li[@id='dashboardTabstrip-tab-3']"
    facility_id = "facilitySelect_listbox"
    facility_dropdown = "//*[@class='facilitySelectContainer']//span//button"
    dispach_dash_board = "aDispatchDashboardLink"
    search_map_button = "//input[@id='searchMapText']/..//button[1]"
    route_map_search_results = "//div[@id='collapsePackageResults']//a[@class='clickable openRouteWindow']"
    export_gps_file = "//div[@class='divRouteActions']//button[@title ='Export GPS File']//i"
    export_gps_file_radio = "radioExportGPSGPX"
    road_warrior_radio = "radioExportGPSRoadWarrior"
    circuit_route_planner_radio = "radioExportGPSCircuitPlanner"
    export_button = "//div[@id='exportGPSWindow']//button[@id='btnExportGPS']"
    search_map_input = "searchMapText"
    search_button = "//*[@title='Search']"
    route_results = "//*[@id='collapseRouteResults']//div//div//div//a"
    route_results2 = "(//*[contains(text(), 'Route Results')])[2]"
    packages_before_move = "//div[@class='divRouteStats']//span[2]/span"
    cross_button = "(//span[contains(@id,'windowRoute6512_wnd_title')]//following::a[@aria-label='Close'])[1]"
    cross_button_111_window = ("(//span[contains(@id,'windowRoute6511_wnd_title')]//following::a["
                               "@aria-label='Close'])[1]")

    def user_settings(self, facility_name):
        self.click_on_element(self.profile_id, "id")
        time.sleep(2)
        self.click_on_element(self.settings_id, "id")
        time.sleep(2)
        self.click_on_element(self.initial_page_list, "css")
        time.sleep(10)
        facility_list = self.driver.find_element(By.ID, self.facility_list_id)
        facility_items = facility_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(facility_items, facility_name)
        time.sleep(5)
        self.click_on_element(self.settings_save_button, "xpath")
        time.sleep(10)
        self.click_on_element(self.settings_close_button, "xpath")
        time.sleep(5)

    def verify_facility_dashboard(self):
        time.sleep(10)
        assert self.isElementPresent(self.facility_dashboard_deliveries, "xpath")
        assert self.isElementPresent(self.facility_dashboard_pickups, "xpath")
        assert self.isElementPresent(self.facility_dashboard_exceptions, "xpath")

    def verify_load_time(self, facility_name):

        self.click_on_element(self.profile_id, "id")
        time.sleep(5)
        self.click_on_element(locator=self.facility_dropdown, locator_type="xpath")
        facility_list = self.driver.find_element(By.ID, self.facility_id)
        facility_items = facility_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(facility_items, facility_name)
        start_time = time.time()
        time.sleep(5)

        # Wait for the page to load completely by checking the 'complete' state of the document
        timeout = 4
        while True:
            load_state = self.driver.execute_script('return document.readyState')
            if load_state == 'complete' or time.time() - start_time > timeout:
                break
            time.sleep(1)
        # Record the end time after the page has loaded
        end_time = time.time()
        # Calculate the load time
        load_time = end_time - start_time
        # Assert that the load time is less than 30 seconds
        assert load_time < 30, f"Page load time exceeded limit: {load_time:.2f} seconds"
        print(f"Page loaded in {load_time:.2f} seconds after clicking, which is within the acceptable limit.")
    def verify_dispach_routes(self, barcode, expected_column_names):
        global actual_column_names
        self.click_on_element(self.dispach_dash_board, "id")
        time.sleep(5)
        self.click_on_element(self.search_map_input, "id")
        self.send_keys_to(self.search_map_input, barcode, "id")
        time.sleep(1)
        self.click_on_element(self.search_map_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.route_map_search_results, "xpath")
        time.sleep(3)
        self.click_on_element(self.export_gps_file, "xpath")
        time.sleep(10)
        default_checked = self.driver.find_element(By.ID, self.export_gps_file_radio).get_attribute('checked')
        assert default_checked == "true"
        self.click_on_element(self.export_button, "xpath")
        time.sleep(10)
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        downloaded_gps_segment = formatted_date + "_NOR502.gpx"
        downloaded_gps_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        assert downloaded_gps_segment in downloaded_gps_name
        os.remove(os.path.join(os.path.abspath('.') + "\\Downloads", downloaded_gps_name))
        time.sleep(5)
        self.click_on_element(self.export_gps_file, "xpath")
        time.sleep(3)
        self.click_on_element(self.road_warrior_radio, "id")
        time.sleep(2)
        self.click_on_element(self.export_button, "xpath")
        time.sleep(10)
        downloaded_excel_segment = formatted_date + "_NOR502.xlsx"
        downloaded_excel_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        print(downloaded_excel_name)
        assert downloaded_excel_segment in downloaded_excel_name
        file_path = os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name
        if os.path.exists(file_path):
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            actual_column_names = [cell.value for cell in sheet[1]]
        if actual_column_names == expected_column_names:
            assert actual_column_names == expected_column_names
        os.remove(os.path.join(os.path.abspath('.') + "\\Downloads", file_path))

    def verify_circuit_route_planner_excel(self, expected_circuit_column_names):
        global actual_circuit_column_names
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        self.click_on_element(self.export_gps_file, "xpath")
        time.sleep(3)
        self.click_on_element(self.circuit_route_planner_radio, "id")
        time.sleep(2)
        self.click_on_element(self.export_button, "xpath")
        time.sleep(10)
        downloaded_circuit_excel_segment = formatted_date + "_NOR502.xlsx"
        downloaded_circuit_excel_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        assert downloaded_circuit_excel_segment in downloaded_circuit_excel_name
        file_circuit_path = os.path.abspath('.') + "\\Downloads\\" + downloaded_circuit_excel_name
        if os.path.exists(file_circuit_path):
            workbook = openpyxl.load_workbook(file_circuit_path)
            sheet = workbook.active
            actual_circuit_column_names = [cell.value for cell in sheet[1]]
        if actual_circuit_column_names == expected_circuit_column_names:
            assert actual_circuit_column_names == expected_circuit_column_names
        os.remove(os.path.join(os.path.abspath('.') + "\\Downloads", file_circuit_path))

    def getting_packages(self, route_name):
        time.sleep(10)
        self.click_on_element(self.dispach_dash_board, "id")
        time.sleep(20)
        self.send_keys_to(self.search_map_input, route_name)
        time.sleep(2)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.route_results2, "xpath")
        time.sleep(4)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(2)
        packages = self.driver.find_element(By.XPATH, self.packages_before_move).get_attribute("textContent")
        print(packages)
        self.click_on_element(self.cross_button, "xpath")
        self.clear_field(self.search_map_input, "id")
        return packages

    def verifying_packages_after_move(self, route_name, package):
        time.sleep(5)
        self.click_on_element(self.cross_button_111_window, "xpath")
        self.clear_field(self.search_map_input, "id")
        self.send_keys_to(self.search_map_input, route_name)
        time.sleep(2)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.route_results2, "xpath")
        time.sleep(4)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(2)
        packages_after_move = self.driver.find_element(By.XPATH, self.packages_before_move).get_attribute("textContent")
        print(packages_after_move)
        assert packages_after_move > package
