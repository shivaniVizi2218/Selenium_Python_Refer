import time
from builtins import print
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.returns_dashboard import returns_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2391_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\facility_dashboard.json')
    data = json.load(testDataFile)

    def test_2391_status_verify(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.facility_dashboard.click_on_facility_dashboard()
        self.facility_dashboard.click_on_exceptions_label()
        onholdTot = self.facility_dashboard.get_on_hold_count()
        print("onholdTot:" + onholdTot)
        onholdTot_int = int(onholdTot)
        print(onholdTot_int)
        time.sleep(2)
        barcodes = []
        for i in range(5):
            self.advance_search.change_facility_in_profile(
                self.data["facility_one"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                         forward_branch=self.data["forward_branch"],
                                                         stop_name=self.data["stop_name"],
                                                         address_line1=self.data["address_line1"],
                                                         service_type=self.data["service_type"],
                                                         city=self.data["city"],
                                                         state=self.data["state"], zip=self.data["zip"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(20)
            print("barcode_" + str(i), barcodes[i])
        self.advance_search.search_packg_in_advance_search(barcodes[0])
        time.sleep(30)
        self.facility_dashboard.onhold_status_change()
        self.returnDashboard.page_refresh_and_wait(5)
        self.advance_search.search_packg_in_advance_search(barcodes[1])
        time.sleep(30)
        self.facility_dashboard.onhold_status_change()
        self.returnDashboard.page_refresh_and_wait(5)
        self.advance_search.search_packg_in_advance_search(barcodes[2])
        time.sleep(30)
        self.facility_dashboard.onhold_status_change()
        self.returnDashboard.page_refresh_and_wait(5)
        self.advance_search.search_packg_in_advance_search(barcodes[3])
        time.sleep(30)
        self.facility_dashboard.onhold_status_change()
        self.returnDashboard.page_refresh_and_wait(5)
        self.advance_search.search_packg_in_advance_search(barcodes[4])
        time.sleep(30)
        self.facility_dashboard.onhold_status_change()
        self.returnDashboard.page_refresh_and_wait(5)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.facility_dashboard.click_on_facility_dashboard()
        self.facility_dashboard.click_on_exceptions_label()
        time.sleep(3)
        onholdTot1 = self.facility_dashboard.get_on_hold_count()
        print("onholdTot1:" + onholdTot1)
        onholdTot1_int = int(onholdTot1)
        print(onholdTot1_int)
        count_val = onholdTot1_int - onholdTot_int
        print(count_val)
        assert count_val == 5
        assert onholdTot1_int > onholdTot_int
        time.sleep(3)
        self.facility_dashboard.click_and_verify_onholdCol()
        time.sleep(3)
        self.facility_dashboard.click_on_maximize_window_btn()
        self.facility_dashboard.verify_days_on_hold_ascending()



