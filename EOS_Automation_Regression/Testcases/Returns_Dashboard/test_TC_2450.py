import time
from eospageObjects.returns_dashboard import returns_dashboard
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from eospageObjects.user_settings import UserSettings
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2450

class Test_TC_2450:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\return_dashboard.json')
    data = json.load(testDataFile)
    adv_search_testDataFile = open('.\\Data\\advance_search.json')
    adv_search_data = json.load(adv_search_testDataFile)
    def test_TC_2450(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.returnDashboard = returns_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.user_settings = UserSettings(self.driver)
        self.returnDashboard.navigate_to_return_dashbord()
        self.returnDashboard.verify_open_tab_opens_defaut()
        if self.returnDashboard.verify_all_returning_packages_are_displayed_in_package_table(self.data["package_grid_status_value"]) :
            self.advance_search.change_facility_in_profile(
                self.adv_search_data["facility_one"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.adv_search_data["customer_name"],
                                                         forward_branch=self.adv_search_data["forward_branch"],
                                                         stop_name=self.adv_search_data["stop_name"],
                                                         address_line1=self.adv_search_data["address_line1"],
                                                         city=self.adv_search_data["city"],
                                                         state=self.adv_search_data["state"], zip=self.adv_search_data["zip"])
            time.sleep(20)  # status is not being updated right away. So we need this sleep.
            self.advance_search.search_packg_in_advance_search(barcode)
            self.advance_search.set_adv_search_package_window_status_drop_down(
                self.adv_search_data["advance_package_window_status_value"], self.adv_search_data["advance_package_window_Exception_returnValue"])
            self.advance_search.close_advance_package_dialog()
            self.returnDashboard.navigate_to_return_dashbord()
            self.returnDashboard.verify_all_returning_packages_are_displayed_in_package_table(
                self.data["package_grid_status_value"])
        self.user_settings.change_landing_page("5")  # index 5 is Returns dashboard
        self.returnDashboard.verify_return_dashboard_is_launched(self.EOSURL)
