import json
import time

import utilities.common_util
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2422

class Test_2422:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    utilities.common_util.delete_all_files_from_downloads()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    def test_2422(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.route_manager = eos_set_route_manager(self.driver)
        # self.advance_search.change_facility(self.testDataFile["facility_three"])
        self.advance_search.change_facility_in_profile(
            self.data["facility_three"])
        self.route_manager.click_on_route_manager()
        time.sleep(6)
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button()
        self.route_manager.verify_export_excel_file()
        self.route_manager.assign_contractor_to_route(self.data["route1"],self.data["contractor"])
        self.route_manager.assign_contractor_to_route(self.data["route2"], self.data["contractor"])
        self.route_manager.assign_contractor_to_route(self.data["route3"], self.data["contractor"])
        self.route_manager.click_on_assign_preferred_type_btn()
        self.route_manager.search_with_contractor("011014D")
        time.sleep(6)
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button()
        self.route_manager.verify_export_excel_file()
        time.sleep(6)
        self.route_manager.click_on_assigned_radio_button()
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button()
        self.route_manager.verify_export_excel_file()
        time.sleep(6)
        self.route_manager.click_on_unassigned_radio_button()
        utilities.common_util.delete_all_files_from_downloads()
        self.route_manager.verify_export_excel_button()
        self.route_manager.verify_export_excel_file()













