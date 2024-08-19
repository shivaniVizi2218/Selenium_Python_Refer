import json
import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.route_manager import eos_set_route_manager
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig ,ReadEOSdbConfig
from Testcases.configtest import setup
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from utilities import DB_connection

# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2420

class Test_2420:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOS_DB_SERVER = ReadEOSdbConfig.getEOSdb_server()
    EOS_DB_DATABASE = ReadEOSdbConfig.getEOSdb_database()
    EOS_DB_USER = ReadEOSdbConfig.getEOSdb_user()
    EOS_DB_PASS = ReadEOSdbConfig.getEOSdb_pass()
    testDataFile = open('.\\Data\\package_entry_search.json')
    package_entry_data = json.load(testDataFile)

    def test_2420(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.advance_search = eos_advance_search(self.driver)
        self.route_manager = eos_set_route_manager(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.dispatch_dashboard =eos_dispatch_dashboard(self.driver)
        db_query_for_facility_code = "SELECT * FROM [dbo].[Facility] WHERE FacilityName LIKE '%"+self.package_entry_data["facility_one"][:-6]+"%'"
        facility_details = DB_connection.execute_query(self.EOS_DB_SERVER, "PackageDB", self.EOS_DB_USER, self.EOS_DB_PASS, db_query_for_facility_code)
        facility_code =facility_details[0][0]
        print(facility_code)
        db_query_for_rout_and_contract = "SELECT R.RouteName, C.ContractorCode, * FROM Route AS R JOIN CONTRACTOR AS C ON R.PreferredContractorId = C.ContractorId WHERE R.FacilityId = "+str(facility_code)+" AND C.FacilityId = "+str(facility_code)+" AND R.PreferredContractorId IS NOT NULL AND C.Active = 1"
        rows = DB_connection.execute_query(self.EOS_DB_SERVER, "PackageDB", self.EOS_DB_USER, self.EOS_DB_PASS, db_query_for_rout_and_contract)
        route_name =rows[2][0]
        contractor_id = rows[2][1]
        route_name = route_name.replace(" ","")
        contractor_id = contractor_id.replace(" ","")
        self.advance_search.change_facility_in_profile(self.package_entry_data["facility_one"])
        self.packageEntry.click_package_entry()
        time.sleep(5)
        self.packageEntry.create_a_package_with_route(customer_name=self.package_entry_data["customer_name"],
                                                         stop_name=self.package_entry_data["stop_name"],
                                                         address_line1=self.package_entry_data["address_line1"],
                                                         city=self.package_entry_data["city"],
                                                         state=self.package_entry_data["state"], zip=self.package_entry_data["zip"],route=route_name)
        self.route_manager.add_preferred_contract_id_to_route(route_name,contractor_id)
        self.dispatch_dashboard.verify_route_icon_color(route_name,contractor_id)
        self.route_manager.add_preferred_contractor_from_assign_preferred_btn(route_name)











