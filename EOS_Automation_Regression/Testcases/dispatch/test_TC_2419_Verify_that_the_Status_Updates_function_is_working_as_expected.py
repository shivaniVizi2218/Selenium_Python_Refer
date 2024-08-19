import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.returns_dashboard import returns_dashboard
from Testcases.configtest import setup
import json

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2419

class Test_TC_2419:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('./Data/advance_search.json')
    data = json.load(testDataFile)
    testDataFile = open('./Data/return_dashboard.json')
    return_dashboard_data = json.load(testDataFile)
    testDataFile = open('.\\Data\\dispatch_search.json')
    dispatch_dashboard_data = json.load(testDataFile)
    def test_TC_2419(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.dispatch_dash_board = eos_dispatch_dashboard(self.driver)
        time.sleep(2)
        self.advance_search.change_facility_in_profile(self.dispatch_dashboard_data["facility_five"])  #this function works consistently for changing facility.
        self.dispatch_dash_board.clear_all_packages_in_rote(self.dispatch_dashboard_data["rout_for_dispacth_dashboard_1"],self.dispatch_dashboard_data["dispatch_backup_route"])
        for i in range(3):
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode =  self.packageEntry.create_a_package_with_route(customer_name=self.data["customer_name"], forward_branch=self.data["forward_branch"], stop_name="RD_TC_00"+str(i+1),
                                            address_line1=self.dispatch_dashboard_data["address_line2"], city=self.dispatch_dashboard_data["city1"],
                                            state=self.dispatch_dashboard_data["state1"], zip=self.dispatch_dashboard_data["zip1"],route=self.dispatch_dashboard_data["rout_for_dispacth_dashboard_1"])
            time.sleep(15)
            self.returnDashboard.page_refresh_and_wait(15)
            self.advance_search.change_facility_in_profile(self.dispatch_dashboard_data["facility_five"])  #this function works consistently for changing facility.
        self.dispatch_dash_board.click_dispatch_dashboard()
        self.dispatch_dash_board.select_route_icon_from_search_tab(self.dispatch_dashboard_data["rout_for_dispacth_dashboard_1"])
        self.dispatch_dash_board.assign_contractor_to_rout(self.dispatch_dashboard_data["contractor_for_dispatch_board"])
        self.dispatch_dash_board.verify_status_update_functionalities(self.dispatch_dashboard_data["status_update_master_row_column_headers"],self.dispatch_dashboard_data["status_update_child_row_column_headers"])
        self.dispatch_dash_board.status_update_window_input_functionality(self.dispatch_dashboard_data["status_update_time"],self.dispatch_dashboard_data["status_update_drop_value"],self.dispatch_dashboard_data["status_update_signature_value"],self.dispatch_dashboard_data["status_update_exception_value"],self.dispatch_dashboard_data["status_update_door_tag_value"])
        self.dispatch_dash_board.verify_show_PODS_and_Show_execptions_functionality()
        self.dispatch_dash_board.click_lock_icon()
        self.dispatch_dash_board.remove_contractor_id()
        self.dispatch_dash_board.move_package_to_another_route(self.dispatch_dashboard_data["dispatch_backup_route"])
        time.sleep(10)

