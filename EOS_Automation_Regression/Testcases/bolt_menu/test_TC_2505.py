import json
import time
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.eos_bolt_menu_reports import eos_bolt_menu_report
from eospageObjects.bolt_menu import eos_bolt_menu
from eospageObjects.mls_bolt_menu import mls_bolt_menu
from utilities.common_util import delete_all_files_from_downloads


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2505
class Test_TC_2505:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    delete_all_files_from_downloads()

    def test_TC_2505(self, setup):
        self.driver = setup
        self.bolt_menu_dashboard = eos_bolt_menu(self.driver)
        self.mls_bolt_menu = mls_bolt_menu(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.bolt_menu_dashboard.go_to_a_bolt_menu_view_report(self.data["status_update_report"])
        time.sleep(10)
        self.mls_bolt_menu.verify_status_update_report(self.data["status_update_first_items"],
                                                       self.data["status_update_second_items"],
                                                       self.data["expected_drop_down_results"],
                                                       self.data["status_update_word"],
                                                       self.data["status_update_excel"],
                                                       self.data["status_update_ppt"],
                                                       self.data["status_update_pdf"],
                                                       self.data["print_dialog_text"])
