import time
from builtins import print
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.returns_dashboard import returns_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2390_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\facility_dashboard.json')
    data = json.load(testDataFile)

    def test_2390_status_verify(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.returnDashboard = returns_dashboard(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        time.sleep(2)
        barcodes = []
        for i in range(5):
            self.advance_search.change_facility_in_profile(
                self.data["facility_one"])  # this function works consistently for changing facility.
            self.packageEntry.click_package_entry()
            time.sleep(2)
            barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                         forward_branch=self.data["forward_branch"],
                                                         stop_name=self.data["stop_name"],
                                                         address_line1=self.data["address_line1"],
                                                         service_type=self.data["service_type"],
                                                         city=self.data["city"],
                                                         state=self.data["state"], zip=self.data["zip"])
            barcodes.append(barcode)
            self.returnDashboard.page_refresh_and_wait(20)
            print("barcode_" + str(i), barcodes[i])

        self.facility_dashboard.click_on_facility_dashboard()
        self.facility_dashboard.click_on_exceptions_label()

        damage_deliveryTotBef = self.facility_dashboard.get_damage_delivery_count()
        print("damage_deliveryTotBef:" + damage_deliveryTotBef)
        damage_deliveryTotBef_int = int(damage_deliveryTotBef)
        print(damage_deliveryTotBef_int)

        damage_discardBeforeTot = self.facility_dashboard.get_damage_discard_count()
        print("damage_discardBeforeTot:" + damage_discardBeforeTot)
        damage_discardBefTot_int = int(damage_discardBeforeTot)
        print(damage_discardBefTot_int)

        damage_returnBef_Tot = self.facility_dashboard.get_damage_return_count()
        print("damage_returnBef_Tot:" + damage_returnBef_Tot)
        damage_returnBefTot_int = int(damage_returnBef_Tot)
        print(damage_returnBefTot_int)

        rts_before_tot = self.facility_dashboard.get_rts_count()
        print("rts_before_tot:" + rts_before_tot)
        rts_before_tot_int = int(rts_before_tot)
        print(rts_before_tot_int)

        lost_countBef_tot = self.facility_dashboard.get_lost_count()
        print("lost_countBef_tot:" + lost_countBef_tot)
        lost_tot_bef_int = int(lost_countBef_tot)
        print(lost_tot_bef_int)

        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.facility_dashboard.click_on_facility_dashboard()
        time.sleep(2)
        self.facility_dashboard.click_on_exceptions_label()
        time.sleep(2)
        self.facility_dashboard.click_on_by_route()
        time.sleep(2)
        damage_drill_down_Tot = self.facility_dashboard.exception_drill_down_count()
        print("damage_drill_down_Tot:" + damage_drill_down_Tot)
        damage_drill_down_tot_int = int(damage_drill_down_Tot)
        print(damage_drill_down_tot_int)
        assert damage_drill_down_tot_int == 0
        time.sleep(2)
        self.facility_dashboard.verify_exception_drill_down_grid(exception_search_bar=self.data["exception_search_bar"])
        time.sleep(2)
        self.facility_dashboard.verify_item_damage_will_be_delivered(item_text=self.data["damage_delivered"])
        time.sleep(2)
        self.facility_dashboard.click_on_refresh_grid_btn()
        time.sleep(3)
        damage_deliveryTotAfter = self.facility_dashboard.get_damage_delivery_count()
        print("damage_deliveryTotAfter:" + damage_deliveryTotAfter)
        damage_deliveryTotAfter_int = int(damage_deliveryTotAfter)
        print(damage_deliveryTotAfter_int)
        assert damage_deliveryTotBef_int < damage_deliveryTotAfter_int
        time.sleep(2)
        self.facility_dashboard.verify_damage_delivery_col()
        time.sleep(6)

        self.facility_dashboard.click_on_clear_button()
        self.facility_dashboard.verify_exception_drill_down_grid(exception_search_bar=self.data["exception_search_bar"])
        time.sleep(2)
        self.facility_dashboard.verify_item_damage_will_be_delivered(item_text=self.data["damage_discarded"])
        time.sleep(2)
        self.facility_dashboard.click_on_refresh_grid_btn()
        time.sleep(3)
        damage_discardTotAfter = self.facility_dashboard.get_damage_discard_count()
        print("damage_discardTotAfter:" + damage_discardTotAfter)
        damage_discardTotAfter_int = int(damage_discardTotAfter)
        print(damage_discardTotAfter_int)
        assert damage_discardBefTot_int < damage_discardTotAfter_int
        time.sleep(2)
        self.facility_dashboard.verify_damage_discard_col()
        time.sleep(6)

        self.facility_dashboard.click_on_clear_button()
        self.facility_dashboard.verify_exception_drill_down_grid(exception_search_bar=self.data["exception_search_bar"])
        time.sleep(2)
        self.facility_dashboard.verify_item_damage_will_be_delivered(item_text=self.data["damage_returned"])
        time.sleep(2)
        self.facility_dashboard.click_on_refresh_grid_btn()
        time.sleep(3)
        damage_returnTotAfter = self.facility_dashboard.get_damage_return_count()
        print("damage_returnTotAfter:" + damage_returnTotAfter)
        damage_returnTotAfter_int = int(damage_returnTotAfter)
        print(damage_returnTotAfter_int)
        assert damage_returnBefTot_int < damage_returnTotAfter_int
        time.sleep(2)
        self.facility_dashboard.verify_damage_return_col()
        time.sleep(6)

        rts_after_tot = self.facility_dashboard.get_rts_count()
        print("rts_after_tot:" + rts_after_tot)
        rts_after_tot_int = int(rts_after_tot)
        print(rts_after_tot_int)
        assert rts_before_tot_int < rts_after_tot_int
        time.sleep(2)
        self.facility_dashboard.verify_rts_col()
        time.sleep(6)

        self.facility_dashboard.click_on_clear_button()
        self.facility_dashboard.verify_exception_drill_down_grid(exception_search_bar=self.data["exception_search_bar"])
        time.sleep(2)
        self.facility_dashboard.verify_item_damage_will_be_delivered(item_text=self.data["item_lost"])
        time.sleep(2)
        self.facility_dashboard.click_on_refresh_grid_btn()
        time.sleep(3)
        damage_lostTotAfter = self.facility_dashboard.get_lost_count()
        print("damage_lostTotAfter:" + damage_lostTotAfter)
        damage_lostTotAfter_int = int(damage_lostTotAfter)
        print(damage_lostTotAfter_int)
        assert lost_tot_bef_int < damage_lostTotAfter_int
        time.sleep(2)
        self.facility_dashboard.verify_damage_lost_col()
        time.sleep(6)
