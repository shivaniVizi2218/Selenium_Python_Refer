import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.returns_dashboard import returns_dashboard
from Testcases.configtest import setup
import json


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2452

class Test_TC_2452:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    testDataFile = open('.\\Data\\return_dashboard.json')
    return_dashboard_data = json.load(testDataFile)
    def test_TC_2452(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        time.sleep(2)
        barcodes = []
        for i in range(4):
            self.advance_search.change_facility_in_profile(self.data["facility_one"])  #this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"], forward_branch=self.data["forward_branch"], stop_name=self.data["stop_name"],
                                                address_line1=self.data["address_line1"], city=self.data["city"],
                                                state=self.data["state"], zip=self.data["zip"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(15)
            print("barcode_"+str(i), barcodes[i])
        self.advance_search.change_facility_in_profile(self.data["facility_three"])
        self.advance_search.search_packg_in_all_facilities(barcodes[0])
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(self.data["advance_package_window_status_value"], self.data["advance_package_window_Exception_Item_damaged_return_value"])
        if(self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"],10,20)!=True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(self.data["advance_package_window_status_value"], self.data["advance_package_window_Exception_Item_damaged_return_value"])
            self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10, 10)
        self.advance_search.search_packg_in_all_facilities(barcodes[1])
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(
            self.data["advance_package_window_status_value"], self.data["advance_package_window_Exception_Item_damaged_return_value"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10,
                                                              20) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(
                self.data["advance_package_window_status_value"], self.data["advance_package_window_Exception_Item_damaged_return_value"])
            self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10, 10)
        self.advance_search.search_packg_in_all_facilities(barcodes[2])
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(
            self.data["advance_package_window_status_value"], self.data["advance_package_window_Execption_Exceeded_max_attempts"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10,
                                                              20) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(
                self.data["advance_package_window_status_value"], self.data["advance_package_window_Execption_Exceeded_max_attempts"])
            self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10, 10)
        self.advance_search.search_packg_in_all_facilities(barcodes[3])
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(
            self.data["advance_package_window_status_value"], self.data["advance_package_window_Execption_Exceeded_max_attempts"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10,
                                                              20) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(
                self.data["advance_package_window_status_value"], self.data["advance_package_window_Execption_Exceeded_max_attempts"])
            self.advance_search.validate_package_status_to_be(self.data["advance_search_retrun_value"], 10, 10)
        self.returnDashboard.navigate_to_return_dashbord()
        self.returnDashboard.verify_open_tab_opens_defaut()
        self.returnDashboard.create_new_container(self.return_dashboard_data["return_dashboard_third_party_traking_container_type"],"TEST_CONTAINER_001")
        self.returnDashboard.scan_barcode(barcodes[0])
        self.returnDashboard.scan_barcode(barcodes[1])
        self.returnDashboard.scan_barcode(barcodes[2])
        self.returnDashboard.scan_barcode(barcodes[3])
        self.returnDashboard.save_return_dashboard()
        self.returnDashboard.click_on_barcode_in_return_dashboard(barcodes[0])
        self.advance_search.verify_event_coloumn_of_package_window(self.data["advance_search_package_window_Palletize_value"])
        self.advance_search.change_package_status(self.data["advance_package_window_status_value"], self.data["advance_package_window_Exception_value"])
        self.returnDashboard.refresh_return_dash_board()
        self.returnDashboard.click_on_barcode_in_return_dashboard(barcodes[1])
        self.advance_search.verify_event_coloumn_of_package_window(self.data["advance_search_package_window_Palletize_value"])
        self.advance_search.change_package_status(self.data["advance_package_window_status_value"],
                                                  self.data["advance_package_window_Exception_value"])
        self.returnDashboard.refresh_return_dash_board()
        self.returnDashboard.click_on_barcode_in_return_dashboard(barcodes[2])
        self.advance_search.verify_event_coloumn_of_package_window(self.data["advance_search_package_window_Palletize_value"])
        self.advance_search.change_package_status(self.data["advance_package_window_status_value"],
                                                  self.data["advance_package_window_Exception_value"])
        self.returnDashboard.refresh_return_dash_board()
        self.returnDashboard.click_on_barcode_in_return_dashboard(barcodes[3])
        self.advance_search.verify_event_coloumn_of_package_window(self.data["advance_search_package_window_Palletize_value"])
        self.advance_search.change_package_status(self.data["advance_package_window_status_value"],
                                                  self.data["advance_package_window_Exception_value"])


