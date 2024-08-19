import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup
from eospageObjects.advance_search import eos_advance_search


class Test_2393_deliveries_tab_verify_company_contractor_GPVendor_fields_added:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_2393_deliveries_tab_verify_company_contractor_GPVendor_fields_added(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.facility_dashboard.click_on_package_entry_for_facility_dashboard()
        self.facility_dashboard.deliveries_verify_that_the_fields_comp_contra_GPvendor_fields_added()
        time.sleep(3)
        self.driver.close()