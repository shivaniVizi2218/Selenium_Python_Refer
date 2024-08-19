import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.common_util import generate_random_string


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2515

class Test_TC_2515:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    bolt_data_file = open(".\\Data\\bolt_menu.json")
    bolt_data = json.load(bolt_data_file)

    def test_TC_2515(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.bolt_menu_dashboard = eos_bolt_menu(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        stop_name_random = "tc-" + generate_random_string(8)

        barcode = self.packageEntry.create_a_package_with_route(customer_name=self.data["customer_name"],
                                                                forward_branch=self.data["forward_branch"],
                                                                stop_name=stop_name_random,
                                                                address_line1=self.data["address_line1"],
                                                                city=self.data["city"],
                                                                state=self.data["state"], zip=self.data["zip"],
                                                                route=self.data["route"])
        print(barcode)
        time.sleep(20)  # status is
        self.bolt_menu_dashboard.verify_cost_area_adjustment_elements(barcode, self.bolt_data["cost_area"])
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package()
        self.advance_search.click_barcode1()
        self.bolt_menu_dashboard.verify_cost_area_updated(self.bolt_data["cost_area"])
