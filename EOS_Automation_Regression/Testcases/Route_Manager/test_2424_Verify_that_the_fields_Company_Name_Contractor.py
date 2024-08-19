import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2424

class Test_2424:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2424(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.advance_search = eos_advance_search(self.driver)
        self.route_manager = eos_set_route_manager(self.driver)
        self.route_manager.verify_contract_details_fields_at_contractor_window()






