import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2441
# Prerequisite is to assign contractor to route 401WESTA

class Test_TC_2441:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    def test_TC_2441(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        time.sleep(2)
        self.advance_search.change_facility_in_profile(self.data["facility_one"])  #this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"], forward_branch=self.data["forward_branch"], stop_name=self.data["stop_name"],
                                            address_line1=self.data["address_line1"], city=self.data["city"],
                                            state=self.data["state"], zip=self.data["zip"])
        time.sleep(20)  # status is not being updated right away. So we need this sleep.
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_of_delivery_value"])
        if(self.advance_search.validate_package_status_to_be("Out For Delivery",10,20)!=True):
            self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_of_delivery_value"])
            self.advance_search.validate_package_status_to_be("Out For Delivery", 10, 10)
        self.advance_search.change_package_status_to_business_closed(self.data["advance_package_window_status_attempt_value"], self.data["advance_package_window_attempt_value_business_closed"])
        self.advance_search.verify_advSearch_package_window_status_and_latest_event_table_detail_isUpdated(self.data["advance_barcode_status_one"], self.data["advance_package_window_attempt_value_business_closed"], self.data["advance_package_window_status_attempted_value"])