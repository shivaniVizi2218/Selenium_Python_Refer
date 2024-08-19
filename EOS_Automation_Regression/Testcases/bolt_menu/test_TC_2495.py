import json
import time
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.eos_bolt_menu_reports import eos_bolt_menu_report
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.common_util import delete_all_files_from_downloads


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2495
class Test_TC_2495:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    delete_all_files_from_downloads()

    def test_TC_2495(self, setup):
        self.driver = setup
        self.reports = eos_bolt_menu_report(self.driver)
        self.bolt_menu_dashboard = eos_bolt_menu(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.bolt_menu_dashboard.go_to_a_bolt_menu_view_report(self.data["Load_Manifest_By_Stop_report"])
        time.sleep(10)
        self.reports.load_manifest_stop_reports(self.data["load_manifest_stop_info"],
                                                self.data["expected_drop_down_results"],
                                                self.data["Load_Manifest_stop_word"],
                                                self.data["Load_Manifest_stop_excel"],
                                                self.data["Load_Manifest_stop_ppt"],
                                                self.data["Load_Manifest_stop_pdf"],
                                                self.data["print_dialog_text"])
