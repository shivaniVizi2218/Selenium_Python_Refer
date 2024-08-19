import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.returns_dashboard import returns_dashboard
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from Testcases.configtest import setup
import json
from utilities.common_util import delete_all_files_from_downloads


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2455

class Test_TC_2455:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    testDataFile = open('.\\Data\\return_dashboard.json')
    return_dashboard_data = json.load(testDataFile)
    delete_all_files_from_downloads()
    def test_TC_2455(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.dispatch_board =eos_dispatch_dashboard(self.driver)
        time.sleep(2)
        self.advance_search.change_facility_in_profile(self.data["facility_one"])
        try:
            self.dispatch_board.navigate_to_dispatch_dashboard()
            self.dispatch_board.select_route_icon_from_search_tab(self.return_dashboard_data["route_name_one"])
            self.dispatch_board.verify_route_lock_status()
        except:
            print("Nothing went wrong")
        self.packageEntry.click_package_entry()
        time.sleep(2)
        barcode = self.packageEntry.create_a_package_with_route(customer_name=self.data["customer_name"], forward_branch=self.data["forward_branch"], stop_name="RD_TC_0001",
                                            address_line1=self.data["address_line1"], city=self.data["city"],
                                            state=self.data["state"], zip=self.data["zip"],route="022370")
        self.dispatch_board.navigate_to_dispatch_dashboard()
        self.dispatch_board.select_route_icon_from_search_tab(self.return_dashboard_data["route_name_one"])
        self.dispatch_board.assign_contractor_to_rout(self.return_dashboard_data["contractor_id_one"])
        self.dispatch_board.click_auto_sequence()
        self.dispatch_board.click_lock_icon()
        self.dispatch_board.open_advance_search_barcode_from_dispatch_board(self.return_dashboard_data["stop_name_one"])
        for i in range(20):
            self.advance_search.change_package_status(self.return_dashboard_data["package_window_status_attempt"],self.return_dashboard_data["package_window_exception_value_one"],close_window='no')
            time.sleep(5)
            if not self.advance_search.verify_advance_search_package_status_at_package_window():
                if i ==19 :
                    assert False ,"status not changed to return"
                break
        self.advance_search.close_advance_package_dialog()
        self.dispatch_board.close_both_windows()
        self.returnDashboard.navigate_to_return_dashbord()
        self.returnDashboard.verify_open_tab_opens_defaut()
        self.returnDashboard.verify_package_with_barcode_filter(barcode)
        self.dispatch_board.navigate_to_dispatch_dashboard()
        self.dispatch_board.select_route_icon_from_search_tab(self.return_dashboard_data["route_name_one"])
        self.dispatch_board.open_advance_search_barcode_from_dispatch_board(self.return_dashboard_data["stop_name_one"])
        self.advance_search.change_package_status(self.return_dashboard_data["package_window_status_exeption"], self.return_dashboard_data["package_window_exception_value_two"],close_window='no')
        self.advance_search.close_advance_package_dialog()
        self.dispatch_board.close_both_windows()
        self.returnDashboard.navigate_to_return_dashbord()
        self.returnDashboard.verify_open_tab_opens_defaut()
        self.returnDashboard.verify_package_with_barcode_filter(barcode)
        self.dispatch_board.navigate_to_dispatch_dashboard()
        self.dispatch_board.select_route_icon_from_search_tab(self.return_dashboard_data["route_name_one"])
        self.dispatch_board.open_advance_search_barcode_from_dispatch_board(self.return_dashboard_data["stop_name_one"])
        self.advance_search.change_package_status(self.return_dashboard_data["package_window_status_exeption"], self.return_dashboard_data["package_window_exception_value_three"],close_window='no')
        self.advance_search.close_advance_package_dialog()
        self.dispatch_board.click_lock_icon()
        self.dispatch_board.close_both_windows()
        self.returnDashboard.navigate_to_return_dashbord()
        self.returnDashboard.verify_open_tab_opens_defaut()
        self.returnDashboard.verify_package_with_barcode_filter(barcode)
        self.returnDashboard.verify_returns_dashboard_components()
        self.returnDashboard.verify_returns_dashboard_excel()
        self.returnDashboard.verify_returns_dashboard_print_grid(self.return_dashboard_data["return_dash_board_print_grid_coloumn_headers"])
        # following methods were added to move packages to another route
        self.returnDashboard.switch_to_previous_window()
        self.dispatch_board.navigate_to_dispatch_dashboard()
        self.dispatch_board.select_route_icon_from_search_tab(self.return_dashboard_data["route_name_one"])
        # self.dispatch_board.click_lock_icon()
        self.dispatch_board.remove_contractor_id()
        self.dispatch_board.move_package_to_another_route(self.return_dashboard_data["route_name_two"])
        time.sleep(10)
