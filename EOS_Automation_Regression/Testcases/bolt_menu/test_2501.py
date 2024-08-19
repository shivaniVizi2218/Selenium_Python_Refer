import json
import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.returns_dashboard import returns_dashboard
from eospageObjects.mls_bolt_menu import mls_bolt_menu
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.readProperties import ReadEOSurlConfig


class Test_2501_Reports:
    # self.driver = setup
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\bolt_menu.json')
    data = json.load(testDataFile)

    def test_2501_method(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.advance_search = eos_advance_search(self.driver)
        self.bolt_menu = eos_bolt_menu(self.driver)
        self.mls_bolt_menu = mls_bolt_menu(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_name1"])
        self.bolt_menu.go_to_a_bolt_menu_view_report(report_name="MOSD_by_facility")
        self.mls_bolt_menu.validating_MOSD_by_facility()
        self.mls_bolt_menu.export_drop_down_validation()
        self.mls_bolt_menu.validating_print_text_vals(expected_texts=self.data["expected_texts"],
                                                      word_file=self.data["word_file"],
                                                      excel_file_name=self.data["excel_file_name"],
                                                      pdf_name=self.data["pdf_name"],
                                                      power_point_name=self.data["power_point_name"],
                                                      text=self.data["print_dialog_text"])


