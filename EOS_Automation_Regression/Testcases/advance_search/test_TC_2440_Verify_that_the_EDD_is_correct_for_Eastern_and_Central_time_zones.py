import time
import os
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig,ReadEOSdbConfig
from utilities.common_util import change_system_time_zone,get_system_time_zone
from Testcases.configtest import setup
import json
from utilities import DB_connection


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2440

class Test_TC_2440:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOS_DB_SERVER = ReadEOSdbConfig.getEOSdb_server()
    EOS_DB_DATABASE = ReadEOSdbConfig.getEOSdb_database()
    EOS_DB_USER = ReadEOSdbConfig.getEOSdb_user()
    EOS_DB_PASS = ReadEOSdbConfig.getEOSdb_pass()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)

    def test_TC_2440(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        current_time_zone =get_system_time_zone()
        db_query_for_facility_code = "SELECT * FROM [dbo].[Facility] WHERE TimeZone = 'America/Chicago'"
        query_results = DB_connection.execute_query(self.EOS_DB_SERVER, "PackageDB", self.EOS_DB_USER,
                                                       self.EOS_DB_PASS, db_query_for_facility_code)
        facility_code = query_results[0][3]
        facility_name = query_results[0][4]
        facility_code = str(facility_code)
        facility_code_modified = facility_code if len(facility_code) == 3 else "00" + facility_code
        facility = facility_name+" ("+facility_code_modified[-3:]+")"
        print(facility)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        time.sleep(2)
        self.advance_search.change_facility_in_profile(facility)  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                     forward_branch=self.data["forward_branch"],
                                                     stop_name=self.data["stop_name"],
                                                     address_line1=self.data["address_line1_two"], city=self.data["city_1"],
                                                     state=self.data["state_1"], zip=self.data["zip_1"])
        time.sleep(100)  # status is not being updated right away. So we need this sleep.
        self.advance_search.search_packg_in_all_facilities(barcode)
        self.advance_search.verify_EDD_date_and_Expected_Delivery_in_advance_search_and_adv_package_window()
        change_system_time_zone(self.data["time_zone_name_for_UTC_minus_06_00_Central_Time"])
        time.sleep(5)
        self.advance_search.search_packg_in_all_facilities(barcode)
        self.advance_search.verify_EDD_date_and_Expected_Delivery_in_advance_search_and_adv_package_window()
        change_system_time_zone(self.data["time_zone_name_for_UTC_minus_05_00_eastern_Time"])
        time.sleep(5)
        self.advance_search.search_packg_in_all_facilities(barcode)
        self.advance_search.verify_EDD_date_and_Expected_Delivery_in_advance_search_and_adv_package_window()
        # following method was added to change system time zone to default time zone
        change_system_time_zone(current_time_zone)
        time.sleep(5)

