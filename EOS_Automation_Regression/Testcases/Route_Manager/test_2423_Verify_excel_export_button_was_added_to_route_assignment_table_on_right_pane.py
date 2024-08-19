import json
import time

import utilities.common_util
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2423

class Test_2423:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    utilities.common_util.delete_all_files_from_downloads()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    routeDataFile = open('.\\Data\\route_manager.json')
    routeData = json.load(routeDataFile)
    def test_2423(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.route_manager = eos_set_route_manager(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.route_manager.click_on_route_manager()
        time.sleep(6)
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button_right_pane()
        self.route_manager.verify_export_excel_file_column_hedings(
            self.routeData["route_excel_sheet"],self.routeData["route_excel_file_prefix"],
            self.routeData["route_col_headings"])
        self.route_manager.verify_export_excel_file_with_UI_for_route(self.routeData["route_excel_sheet"])
        self.route_manager.click_on_assign_preferred_type_btn()
        time.sleep(6)
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button_right_pane()
        self.route_manager.verify_export_excel_file_with_UI_for_route(self.routeData["route_excel_sheet"])
        self.route_manager.search_route(self.data["route3"])
        time.sleep(2)
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button_right_pane()
        self.route_manager.verify_export_excel_file_with_UI_for_route(self.routeData["route_excel_sheet"])














