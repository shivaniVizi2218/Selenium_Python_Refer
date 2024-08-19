import json
import time

from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig

from Testcases.configtest import setup


class Test_4920_un_assign_IC_from_route:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_4920_un_assign_route_ID(self, setup):
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
        self.route_manager.assign_route_by_using_contractor_ID(contractorID=self.data["route_number"])
        time.sleep(5)
        self.route_manager.click_on_unassigned_btn()
        time.sleep(2)
        self.route_manager.verify_unassigned_status()
        self.driver.close()


