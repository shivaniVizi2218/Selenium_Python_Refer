import json
import time

from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig

from Testcases.configtest import setup


class Test_4921_assigned_all_preferred_IC_table:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    route_testDataFile = open('.\\Data\\route_manager.json')
    route_data = json.load(route_testDataFile)

    def test_4921_assigned_all_preferred_IC(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.advance_search = eos_advance_search(self.driver)
        self.route_manager = eos_set_route_manager(self.driver)
        self.route_manager.verify_eso_name()
        time.sleep(2)
        self.route_manager.verify_user_name()
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.route_manager.verify_preferred_IC()
        self.route_manager.verify_package_greater_than_zero()
        time.sleep(2)
        self.route_manager.set_assigned_filter_and_preferred_IC()
        time.sleep(2)
        self.route_manager.verify_disabled_preferred_contractor()
        time.sleep(2)
        self.route_manager.verify_user_settings_alerts(saved_popup=self.route_data["saved_settings_popup"])








