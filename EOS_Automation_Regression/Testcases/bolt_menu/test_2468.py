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
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.readProperties import ReadEOSurlConfig


class Test_2468_filters:
    # self.driver = setup
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\bolt_menu.json')
    data = json.load(testDataFile)
    testDataFile1 = open('.\\Data\\dispatch_search.json')
    data1 = json.load(testDataFile1)

    def test_2468_method(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.bolt_menu = eos_bolt_menu(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)

        self.advance_search.change_facility_in_profile(
            self.data["facility_name"])
        self.dispatch.click_dispatch_dashboard()
        self.bolt_menu.verify_routes_in_dispatch_board()
        self.bolt_menu.verify_contractor_details()
        self.bolt_menu.verify_route_details()
        self.bolt_menu.verify_customer_details()
        self.bolt_menu.verify_service_details()
        self.bolt_menu.verify_status_details()
        self.packageEntry.click_package_entry()
        self.packageEntry.verify_package_entryForm(package_entry_name=self.data["package_entry_Text"])
        barcodes = []
        for i in range(5):
            self.advance_search.change_facility_in_profile(
                self.data["facility_name"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                         forward_branch=self.data["forward_branch"],
                                                         stop_name=self.data["stop_name"],
                                                         address_line1=self.data["address_line1"],
                                                         city=self.data["city"],
                                                         state=self.data["state"], zip=self.data["zip"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(20)
            print("barcode_" + str(i), barcodes[i])
        self.advance_search.change_facility_in_profile(
            self.data["facility_name"])
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcodes[0])
        time.sleep(30)
        self.packageEntry.assign_contractor(route_number=self.data1["route_number"])
        time.sleep(3)
        self.dispatch.click_on_CloseBtn()
        time.sleep(3)
        self.dispatch.verify_and_select_delivered_package_staus_vals(status=self.data1["status"])
        time.sleep(3)
        self.dispatch.click_on_CloseBtn()
        self.dispatch.click_dispatch_dashboard()
        self.bolt_menu.verify_package_routes_in_dispatch_board()
        self.bolt_menu.verify_bolt_menu_filter()
        self.bolt_menu.verify_updated_contractor()
        self.bolt_menu.verify_updated_route()
        self.bolt_menu.verify_updated_customer()
        self.bolt_menu.verify_updated_service()
        time.sleep(5)


