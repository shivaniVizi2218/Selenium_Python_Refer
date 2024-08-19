import json
import time
from datetime import datetime
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.bolt_menu import eos_bolt_menu
from eospageObjects.bolt_menu_All_EOS_Reports import eos_bolt_menu_all_eos_reports
from utilities.common_util import generate_random_string
from utilities.common_util import delete_all_files_from_downloads
from utilities.common_util import previous_day_current_date

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2483

class Test_TC_2483:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    bolt_data_file = open(".\\Data\\bolt_menu.json")
    bolt_data = json.load(bolt_data_file)

    def test_TC_2483(self, setup):
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
        self.all_eos_reports_dashboard.run_paginated_reports(self.bolt_data["barcode_research_report_header"])
        time.sleep(10)
        self.all_eos_reports_dashboard.verify_barcode_research(self.bolt_data["barcode_research_barcode_value"],self.bolt_data["barcode_research_report_column_headers"])
        self.all_eos_reports_dashboard.verify_export_dropdown_option(self.bolt_data["export_to_file_option_files"])
        self.all_eos_reports_dashboard.verify_downloaded_reports_in_all_formate(self.bolt_data["barcode_research_report_header"],self.bolt_data["file_formats_for_report_download_1"],self.bolt_data["file_extension_for_report_download_1"])
        self.all_eos_reports_dashboard.verify_print_functionality()


