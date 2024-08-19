import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.daily_closeout_dashboard import eos_daily_closeout_dashboard
from utilities.common_util import generate_random_string

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2459

class Test_TC_2459:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    testDataFile2 = open('.\\Data\\daily_closeout.json')
    daily_closeout_dashboard_data = json.load(testDataFile2)

    def test_TC_2459(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.dailyClouseout = eos_daily_closeout_dashboard(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        stop_name_random = "tc-"+generate_random_string(8)
        barcode = self.packageEntry.create_a_pick_up_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)",stop_name=stop_name_random) # 411EASTA
        time.sleep(45)
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package()
        self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_for_pickup_value"])
        if (self.advance_search.validate_package_status_to_be("Out For Pickup", 10, 20) != True):
            self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_for_pickup_value"])
            self.advance_search.validate_package_status_to_be("Out For Pickup", 10, 10)
        self.dailyClouseout.navigate_daily_closeout_dashboard()
        self.dailyClouseout.select_end_date()
        self.dailyClouseout.verify_ofp_after_run(stop_name=stop_name_random)
        self.dailyClouseout.verify_exception_type_status(self.daily_closeout_dashboard_data["exception_type_option_1"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Exception_Option_1"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Exception_Option_2"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Exception_Option_3"])

        self.dailyClouseout.verify_exception_type_status(self.daily_closeout_dashboard_data["exception_type_option_2"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Attempt_Option_1"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Attempt_Option_2"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Attempt_Option_3"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Attempt_Option_4"])
        self.dailyClouseout.verify_exception_status(self.daily_closeout_dashboard_data["Attempt_Option_5"])


