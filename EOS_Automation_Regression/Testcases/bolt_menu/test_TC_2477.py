import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.bolt_menu import eos_bolt_menu
from eospageObjects.bolt_menu_All_EOS_Reports import eos_bolt_menu_all_eos_reports
from utilities.common_util import generate_random_string
from utilities.common_util import delete_all_files_from_downloads


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2472

class Test_TC_2477:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    bolt_data_file = open(".\\Data\\bolt_menu.json")
    bolt_data = json.load(bolt_data_file)

    def test_TC_2477(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.bolt_menu_dashboard = eos_bolt_menu(self.driver)
        self.all_eos_reports_dashboard=eos_bolt_menu_all_eos_reports(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.bolt_menu_dashboard.go_to_a_bolt_menu_view_report(self.bolt_data["bolt_section_report_name"])
        self.all_eos_reports_dashboard.run_paginated_reports(self.bolt_data["overage_report_report_name"])
        time.sleep(20)
        self.all_eos_reports_dashboard.verify_overage_report_page(self.bolt_data["load_without_departure_start_date"],self.bolt_data["overage_report_report_section_column_header"])
        self.all_eos_reports_dashboard.verify_export_dropdown_option(self.bolt_data["export_to_file_option_files"])
        self.all_eos_reports_dashboard.verify_downloaded_reports_in_all_formate(self.bolt_data["overage_report_report_name"],self.bolt_data["file_formats_for_report_download"],self.bolt_data["file_extension_for_report_download"])
        self.all_eos_reports_dashboard.verify_print_functionality()


