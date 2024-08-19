import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.alerts import alerts_page
from eospageObjects.returns_dashboard import returns_dashboard
from Testcases.configtest import setup
import json

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2464

class Test_TC_2464:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    testDataFile = open('.\\Data\\alerts.json')
    alerts_data = json.load(testDataFile)

    def test_TC_2464(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.alerts_page = alerts_page(self.driver)
        self.returns_dashboard = returns_dashboard(self.driver)
        time.sleep(2)
        self.packageEntry.click_package_entry()
        time.sleep(2)
        barcode = self.packageEntry.create_a_package_without_select_service(customer_name=self.alerts_data["customer_name_for_alert"], forward_branch=self.data["forward_branch"], stop_name=self.data["stop_name"],
                                                address_line1=self.data["address_line1"], city=self.data["city"],
                                                state=self.data["state"], zip=self.data["zip"])
        self.advance_search.search_packg_without_search_all_facilities(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(self.alerts_data["package_status_one"], self.alerts_data[
            "drop_value_one"])
        if (self.advance_search.validate_package_status_to_be(self.alerts_data["package_status_one"], 10,
                                                              10) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(self.alerts_data["package_status_one"], self.alerts_data[
                "drop_value_one"])
            self.advance_search.validate_package_status_to_be(self.alerts_data["package_status_one"], 10, 10)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(self.alerts_data["status_value_exception"], self.alerts_data[
            "Exception_value_On_hold_at_lasership"])
        if (self.advance_search.validate_package_status_to_be(self.alerts_data["adv_search_hold_status"], 10,
                                                              10) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(self.alerts_data["status_value_exception"], self.alerts_data[
                "Exception_value_On_hold_at_lasership"])
            self.advance_search.validate_package_status_to_be(self.alerts_data["adv_search_hold_status"], 10, 10)
        self.returns_dashboard.page_refresh_and_wait(15)
        self.alerts_page.navigate_to_alert_window()
        self.alerts_page.validating_notification_type_coloumn(barcode, self.alerts_data["alert_notification_type_Event_After_Delivery"])
        self.alerts_page.click_on_resolver_icon_of_current_barcode(barcode)
        self.alerts_page.resolve_the_alert_notification(self.alerts_data["alert_resolve_action_type_Contractor_Notified"], self.alerts_data["alert_resolve_result_Manual_Closeout"])
        self.alerts_page.close_alert_window()
        self.advance_search.search_packg_without_search_all_facilities(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(self.alerts_data["status_value_exception"],self.alerts_data["exception_value_removed_from_on_hold"])
        if (self.advance_search.validate_package_status_to_be(self.data["advance_barcode_status_one"], 10,
                                                              10) != True):
            self.advance_search.click_barcode1()
            self.advance_search.change_package_status(self.alerts_data["status_value_exception"],self.alerts_data["exception_value_removed_from_on_hold"])
            self.advance_search.validate_package_status_to_be(self.data["advance_barcode_status_one"], 10, 10)
        self.returns_dashboard.page_refresh_and_wait(15)
        self.alerts_page.navigate_to_alert_window()
        self.alerts_page.verify_event_is_not_created_for_barcode(barcode)
        time.sleep(10)


