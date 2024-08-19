import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json
from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2415_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\dispatch_search.json')
    data = json.load(testDataFile)

    def test_2415(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.advance_search.change_facility_in_profile(self.data["facility_four"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        self.packageEntry.verify_package_entryForm(package_entry_name=self.data["package_entry_Text"])
        self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                               forward_branch=self.data["forward_branch"],
                                               stop_name=self.data["stop_name"],
                                               address_line1=self.data["address_line1"], city=self.data["city"],
                                               state=self.data["state"], zip=self.data["zip"])
        self.driver.refresh()
        time.sleep(15)
        self.advance_search.change_facility_in_profile(self.data["facility_four"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                               forward_branch=self.data["forward_branch"],
                                               stop_name=self.data["stop_name"],
                                               address_line1=self.data["address_line1"], city=self.data["city"],
                                               state=self.data["state"], zip=self.data["zip"])
        time.sleep(2)
        self.dispatch.change_route_from_manifest_tab()
        time.sleep(3)
        self.dispatch.click_on_CloseBtn()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(20)
        self.advance_search.change_facility_in_profile(self.data["facility_four"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                               forward_branch=self.data["forward_branch"],
                                               stop_name=self.data["stop_name"],
                                               address_line1=self.data["address_line1"], city=self.data["city"],
                                               state=self.data["state"], zip=self.data["zip"])
        self.driver.refresh()
        time.sleep(20)
        self.advance_search.change_facility_in_profile(self.data["facility_four"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                           forward_branch=self.data["forward_branch"],
                                           stop_name=self.data["stop_name"],
                                           address_line1=self.data["address_line1"], city=self.data["city"],
                                           state=self.data["state"], zip=self.data["zip"])
        self.driver.refresh()
        time.sleep(20)
        self.advance_search.change_facility_in_profile(self.data["facility_four"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                           forward_branch=self.data["forward_branch"],
                                           stop_name=self.data["stop_name"],
                                           address_line1=self.data["address_line1"], city=self.data["city"],
                                           state=self.data["state"], zip=self.data["zip"])
        time.sleep(3)
        routeTxt = self.dispatch.select_boltMenu_route_lst()
        time.sleep(3)
        self.dispatch.click_dispatch_dashboard()
        time.sleep(5)
        self.dispatch.search_route_and_click2(routeTxt)
        time.sleep(5)
        self.dispatch.verify_assigned_route_package()












