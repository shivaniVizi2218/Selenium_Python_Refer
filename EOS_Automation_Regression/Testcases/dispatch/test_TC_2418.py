import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from eospageObjects.returns_dashboard import returns_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json
from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2418_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\dispatch_search.json')
    data = json.load(testDataFile)

    def test_2418(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_five"])
        barcodes = []
        for i in range(3):
            self.advance_search.change_facility_in_profile(
                self.data["facility_five"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                                         forward_branch=self.data["forward_branch"],
                                                         stop_name=self.data["stop_name"],
                                                         address_line1=self.data["address_line2"],
                                                         city=self.data["city1"],
                                                         state=self.data["state1"], zip=self.data["zip1"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(20)
            print("barcode_" + str(i), barcodes[i])
        time.sleep(20)
        self.advance_search.change_facility_in_profile(
            self.data["facility_five"])
        time.sleep(2)
        self.advance_search.search_packg_in_advance_search(barcodes[0])
        time.sleep(30)
        route_text = self.facility_dashboard.getRouteText()
        time.sleep(3)
        self.packageEntry.assign_contractor(route_number=self.data["route_number"])
        time.sleep(3)
        self.dispatch.click_on_CloseBtn()
        time.sleep(3)
        self.dispatch.search_and_open_route_maps(route_text)
        time.sleep(6)
        self.dispatch.verify_and_add_monitor(saved_popup=self.data["saved_popup"])
        time.sleep(3)
        self.dispatch.click_check_all_and_sequence_lock(confirm_msg=self.data["confirm_msg"])
        time.sleep(3)
        self.advance_search.search_packg_in_advance_search(barcodes[0])
        time.sleep(30)
        self.dispatch.verify_and_select_delivered_package_staus_vals(status=self.data["status"])
        time.sleep(3)
        self.dispatch.verify_green_status_bar()
        time.sleep(2)
        self.advance_search.search_packg_in_advance_search(barcodes[1])
        time.sleep(30)
        self.dispatch.verify_and_select_attempt_package_staus_vals(status_out=self.data["status0"],
                                                                   status=self.data["status1"],
                                                                   drop=self.data["drop1"])
        time.sleep(2)
        self.dispatch.verify_yellow_status_bar()
        time.sleep(2)
        self.advance_search.search_packg_in_advance_search(barcodes[2])
        time.sleep(30)
        self.dispatch.verify_and_select_exception_staus_vals(status=self.data["status2"], drop=self.data["drop2"])
        time.sleep(2)
        self.dispatch.verify_red_status_bar()







