import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.returns_dashboard import returns_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json
from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2417_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\dispatch_search.json')
    data = json.load(testDataFile)

    def test_2417(self, setup):
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
            self.data["facility_three"])
        time.sleep(2)
        barcodes = []
        for i in range(5):
            self.advance_search.change_facility_in_profile(
                self.data["facility_three"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name1"],
                                                         forward_branch=self.data["forward_branch"],
                                                         stop_name=self.data["stop_name"],
                                                         address_line1=self.data["address_line3"],
                                                         city=self.data["city2"],
                                                         state=self.data["state2"], zip=self.data["zip2"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(25)
            print("barcode_" + str(i), barcodes[i])
        time.sleep(3)
        self.advance_search.change_facility_in_profile(self.data["facility_three"])
        time.sleep(3)
        self.advance_search.search_packg_in_advance_search(barcodes[0])
        time.sleep(30)
        route_text = self.facility_dashboard.getRouteText()
        time.sleep(3)
        self.dispatch.search_route_and_click2(route_text)
        time.sleep(4)
        self.dispatch.verify_barcode_add_vals()
