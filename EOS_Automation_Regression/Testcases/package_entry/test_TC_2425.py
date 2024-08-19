import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json
from utilities import DB_connection
from utilities.common_util import generate_random_string
from utilities.readProperties import ReadEOSdbConfig

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2425
from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2425_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)
    EOSserver = ReadEOSdbConfig.getEOSdb_server()
    EOSpassword = ReadEOSdbConfig.getEOSdb_pass()
    EOSuser = ReadEOSdbConfig.getEOSdb_user()

    def test_2425(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        query = "SELECT * FROM [dbo].[Facility]WHERE Active = 1 AND DivisionId = 1 ORDER BY FacilityId"
        eastern = DB_connection.execute_query(self.EOSserver, "PackageDB",
                                              self.EOSuser, self.EOSpassword,
                                              query)

        query2 = "SELECT * FROM [dbo].[Facility]WHERE Active = 1 AND DivisionId = 2 ORDER BY FacilityId"
        central = DB_connection.execute_query(self.EOSserver, "PackageDB",
                                              self.EOSuser, self.EOSpassword,
                                              query2)
        facility = central[22][4] + " " + "(085)"
        print(facility)
        self.advance_search.change_facility_in_profile(facility)  # this function works consistently for changing facility.
        stop_name_random = "tc-" + generate_random_string(8)

        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.eastern_facility_address_package(customer_name=self.data["midwest_customer"],
                                                                     forward_branch=self.data["forward_branch"],
                                                                     stop_name=stop_name_random,
                                                                     address_line1=self.data["address_line1"],
                                                                     city=self.data["city"],
                                                                     state=self.data["state"], zip=self.data["zip"],
                                                                     route=self.data["midwest_route"])
        time.sleep(20)
        self.advance_search.forward_search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.packageEntry.verifying_status(self.data["kendo_window_status"], self.data["kendo_window_type"], self.data["kendo_window_event"])
