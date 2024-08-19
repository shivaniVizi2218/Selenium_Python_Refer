import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities import DB_connection
from utilities.readProperties import ReadEOSurlConfig, ReadEOSdbConfig
from Testcases.configtest import setup
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.daily_closeout_dashboard import eos_daily_closeout_dashboard
from utilities.common_util import generate_random_string

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2457

class Test_TC_2457:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOS_DB_SERVER = ReadEOSdbConfig.getEOSdb_server()
    EOS_DB_DATABASE = ReadEOSdbConfig.getEOSdb_database()
    EOS_DB_USER = ReadEOSdbConfig.getEOSdb_user()
    EOS_DB_PASS = ReadEOSdbConfig.getEOSdb_pass()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    testDataFile2 = open('.\\Data\\daily_closeout.json')
    daily_closeout_dashboard_data = json.load(testDataFile2)

    def test_TC_2457(self, setup):
        rows = DB_connection.execute_query(server=self.EOS_DB_SERVER, database=self.EOS_DB_DATABASE,
                                           username=self.EOS_DB_USER, password=self.EOS_DB_PASS,
                                          query= "SELECT CF.MaxDeliveryAttempt, SC.Description, C.CustomerName, F.FacilityName, * FROM CustomerFacilityService AS CF"
                                            +" JOIN [ServiceCode] AS SC ON CF.ServiceCodeId = SC.Id JOIN Customer AS C ON CF.CustomerId = C.CustomerId"
                                            +" JOIN Facility AS F ON CF.FacilityId = F.FacilityId WHERE ServiceCodeId IN (11, 12) AND F.FacilityName='Columbus' AND C.Active<>0")
        customer_drop_down_option = []
        for row in rows:
            customer_drop_down_option.append(str(row[2])+" ("+str(row[40])+")")

        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.dailyClouseout = eos_daily_closeout_dashboard(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        time.sleep(10)
        self.advance_search.change_facility(self.data["facility_four"])
        self.packageEntry.click_package_entry()
        time.sleep(2)
        stop_name_random = "tc-"+generate_random_string(8)
        barcode = self.packageEntry.create_package(customer_name=str(customer_drop_down_option[0]),
                                                   package_type=self.daily_closeout_dashboard_data["Package_Type"],
                                                   service_type=self.daily_closeout_dashboard_data["Service_Type1"],
                                                   stop_name=stop_name_random,
                                                   address_line1=self.daily_closeout_dashboard_data["Address_Line1"],
                                                   city=self.daily_closeout_dashboard_data["City"],
                                                   state=self.daily_closeout_dashboard_data["State"],
                                                   zip=self.daily_closeout_dashboard_data["Zip"]) # 411EASTA
        time.sleep(45)
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package(contractorId=self.daily_closeout_dashboard_data["ContractorId"])
        self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_for_pickup_value"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_package_window_status_Out_for_pickup_value"],
                                                              10, 20) != True):
            self.advance_search.change_status_as_outofDelevery(self.data["advance_package_window_status_Out_for_pickup_value"])
            self.advance_search.validate_package_status_to_be(self.data["advance_package_window_status_Out_for_pickup_value"],
                                                              10, 10)
        self.dailyClouseout.navigate_daily_closeout_dashboard()
        self.dailyClouseout.select_end_date()
        self.dailyClouseout.verify_ofp(stop_name=stop_name_random)
        self.dailyClouseout.verify_grid_columns()

        self.packageEntry.click_package_entry()
        time.sleep(2)
        stop_name_random2 = "tc-" + generate_random_string(8)
        barcode2 = self.packageEntry.create_package(customer_name=str(customer_drop_down_option[0]),
                                                   package_type=self.daily_closeout_dashboard_data["Package_Type"],
                                                   service_type=self.daily_closeout_dashboard_data["Service_Type2"],
                                                   stop_name=stop_name_random2,
                                                   address_line1=self.daily_closeout_dashboard_data["Address_Line1"],
                                                   city=self.daily_closeout_dashboard_data["City"],
                                                   state=self.daily_closeout_dashboard_data["State"],
                                                   zip=self.daily_closeout_dashboard_data["Zip"])  # 411EASTA
        time.sleep(45)
        self.advance_search.search_packg_in_advance_search(barcode2)
        self.advance_search.assign_contractor_to_package()
        self.advance_search.change_status_as_outofDelevery(
            self.data["advance_package_window_status_Out_for_delivery_value"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_package_window_status_Out_for_delivery_value"],
                                                              10, 20) != True):
            self.advance_search.change_status_as_outofDelevery(
                self.data["advance_package_window_status_Out_for_delivery_value"])
            self.advance_search.validate_package_status_to_be(self.data["advance_package_window_status_Out_for_delivery_value"],
                                                              10, 10)
        self.dailyClouseout.navigate_daily_closeout_dashboard()
        self.dailyClouseout.select_end_date()
        self.dailyClouseout.verify_ofd(stop_name=stop_name_random2)
        self.dailyClouseout.verify_grid_columns()