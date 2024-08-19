import sys
import time
from _ast import Assert
import pytest
from selenium.webdriver import Keys
# sys.path.insert(1, 'C:/Users/pjarubula.EMSDOMAIN/PycharmProjects/EPCProject')
# sys.path.insert(1, 'C:/Users/skhan/Documents/EPCProject/EPCProject')

from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import custlogger
from logging import Logger
from selenium.webdriver.support.ui import Select
from datetime import datetime


# from utilities.screenshots import Screen_shots


class eos_advance_search(Custom_code):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)

    fas_fa_bars = "//*[@class='fas fa-bars']"
    advance_search_menu_id = "aAdvancedSearchDashboardLink"
    advance_search_field_id = "txtSearchTxt"
    search_type_dropdown = "ddlSearchType"
    search_button_id = "btnAdvancedSearch"
    clear_search_button_id = "btnClearAdvancedSearch"
    search_facilities_id = "cbSearchAllFacilities"
    today_only = "cbSearchTodayOnly"
    search_dropdown_id = "ddlSearchType"
    search_all_facilities = "cbSearchAllFacilities"
    # barcode1_xpath = "//a[contains(text(),'BD525D41F45EF2B64B907C')]"
    barcode1_xpath = "//*[@class='clickable viewPackageDetail']"
    status_edit_xpath = "//*[@class='fas fa-pencil-alt iconHover']"
    status_dropdown_xpath = "//*[contains(@class, 'divEditPackageStatus updatePackageStatus')]//span//button"
    status_dropdown_value_xpath = "//*[contains(@class, 'divEditPackageStatus updatePackageStatus')]//span[2]/span/span"
    status_select_dropdown = "//*[contains(@id, 'editPackageStatus') and contains(@data-role, 'dropdownlist')]"
    dropdown_ul_list_xpath = "//*[contains(@id, 'editPackageStatus') and contains(@data-role, 'staticlist')]"
    statusCodeName = "//*[contains(@id, 'statusCodeName')]"
    save_Status = "//*[contains(@id, 'savePackageStatus')]"
    cancel_Status = "//*[contains(@id, 'cancelPackageStatus')]"
    edd_date_picker = "//input[contains(@id, 'EDDdatePicker')]"
    option_out_for_delivery = "//option[@value='Out For Delivery']"
    route_on_hold_xpath = "//*[@id='AdvancedSearchGrid']//div[2]//table//tbody//tr//td[5]"
    package_refresh = "//button[contains(@id, 'btnRefreshPackage') and(@title='Refresh')]"
    attempt_field_title = "//span[contains(@id, 'spnExceptionDropDownLabel')]"

    # Delivery dropdown
    delivered_drop_dropdown_button = "//*[contains(@id, 'deliveryDetails')]//div//div/span[2]//button"
    delivered_drop_dropdown_ul_list = "//*[contains(@id, 'dropLocationDropDown') and contains(@data-role, 'staticlist')]"
    delivered_signature = "//*[@class='k-textbox txtSignature']"
    drop_location_innertext = "//*[contains(@id, 'deliveredDropLocation')]"
    # Exception dropdown
    exception_drop_dropdown_button = "//*[contains(@id, 'exceptionDetails')]//div//div/span[2]//button"
    exception_drop_dropdown_ul_list = "//*[contains(@id, 'exceptionDropDown') and contains(@data-role, 'staticlist')]"

    profile_id = "dispatcherNameMain"
    facility_dropdown = "//*[@class='facilitySelectContainer']//span//button"
    facility_dropdown2 = "//span[@aria-owns='facilitySelect_listbox']//button"
    facility_list_id = "facilitySelect_listbox"
    package_event_received = "//*[@data-gridid='PackageWindowEventsGrid']//div[2]//table//tbody//tr[2]//td[2]"

    # Route screen from advance search apge
    route_name_search_result_xpath = "//*[@id='AdvancedSearchGrid']//div[2]//table//tbody//tr//td[5]//a"
    unassigned_contractor_label = "//div[@class='yellowText inline marT5']"
    contractor_edit = "//*[contains(@id, 'routeWindowAssignContractor')]"
    contractor_id_textfield = "(//*[contains(@id, 'routeWindowContractorComplete')])[1]"
    remove_contractor = "//*[contains(@id, 'routeWindowRemoveContractor')]"
    close_window_button = "//*[@aria-label='Close']"
    ok_button_after_close_window = "(//*[@id='confirmWindowClose']//div[2]//button)[2]"
    ####
    # Type dropdown
    type_dropdown_button = "//*[contains(@aria-controls, 'ddlSearchType_listbox')]//button"
    type_dropdown_ul_list_xpath = "//*[contains(@id, 'ddlSearchType_listbox') and contains(@data-role, 'staticlist')]"
    div_notification = "//*[contains(@class, 'divNotification')]"

    edd_datepicker = "//button[contains(@aria-controls, 'EDDdatePicker')]"
    edd_datepicker_text = "//input[contains(@id, 'EDDdatePicker')]"
    door_tag = "//input[contains(@id, 'doorTag')]"
    exception_notes = "//input[contains(@id, 'txtExceptionNote')]"

    # Pick up
    status_edit_pickup_xpath = "//*[contains(@id, 'editStatusInfo')]"

    # advance search table
    advance_search_status = "//div[@class='statusWords']"

    # package window--------
    advance_search_package_window = "//div[@id='packageDrillDown']"
    advSearch_package_window_edit_icon_nextToStatus = "//div[@class='divEditContainer']//i[contains(@id,'editStatus')]"
    # advSearch_exception_value_Mechanical_breakdown ="//span[text()='Mechanical Breakdown Will Impact Delivery']"
    advSearch_package_save_button = "(//button[text()='Save'])[1]"
    advSearch_package_window_sataus = "//div[@class='divEditContainer']//span[contains(@id,'statusCodeName')]"
    advSearch_package_window_updated_eventDetails_grid = "//div[@class='divPackageEvents']//td[@role='gridcell'][3]"
    advsearch_package_window_updated_eventType_grid = "//div[@class='divPackageEvents']//td[@role='gridcell'][2]"
    advSearch_package_window_except_input_box = "(//div[contains(@class,'divException')])[2]//span[@role='listbox']"
    advsearch_package_window_except_field_value = "//div[contains(@class,'divException')]//span[@class='k-input-value-text']"
    advSearch_package_window_status_dropdown = "//div[contains(@class,'divEditPackageStatus')]//button"
    advSearch_package_window_status_dropdown_ul_list = "//ul[contains(@id,'editPackageStatus')]"
    advSearch_package_window_exception_dropdown = "(//div[contains(@class,'divException')])[2]//button"
    advSearch_package_window_exception_dropdown_ul_list = "//ul[contains(@id,'exceptionDropDown')]"
    advSearch_package_window_close_tab = "(//span[contains(@id,'packageDrillDown')]//following::a[@aria-label='Close'])[1]"
    invalid_date = "(//*[text()='Expected Delivery:'])[2]//following::span[1]//input"
    error_msg = "//*[text()='EDD is an Invalid Date']"
    def change_facility_in_profile(self, facilityName):
        time.sleep(2)
        self.click_on_element(self.profile_id)
        time.sleep(5)
        self.click_on_element(locator=self.facility_dropdown, locator_type="xpath")
        # facility_list = self.driver.find_element_by_id(self.facility_list_id)
        # facility_items = facility_list.find_elements_by_tag_name("li")
        facility_list = self.driver.find_element(By.ID, self.facility_list_id)
        facility_items = facility_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(facility_items, facilityName)
        time.sleep(5)

    def change_facility_in_profile2(self, facilityName):
        self.click_on_element(self.profile_id)
        time.sleep(3)
        self.click_on_element(self.facility_dropdown2, "xpath")
        time.sleep(2)
        # select = Select(self.driver.find_element(By.ID, "facilitySelect"))
        # select.select_by_value(facilityName)
        # self.driver.execute_script(f"return document.querySelector('select.clsSelectControl.pv').selectedValue = {facilityName}")
        time.sleep(5)

    def change_facility_in_profile3(self, facilityName):
        self.click_on_element(self.profile_id)
        time.sleep(3)
        self.click_on_element(self.facility_dropdown2, "xpath")
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//select[@id='facilitySelect']//option[25]")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("return arguments[0].removeAttribute('onkeypress');", element)
        self.driver.execute_script("return arguments[0].selected=true;", element)

    def click_on_advance_search_menu(self):
        self.click_on_element(self.fas_fa_bars)
        self.click_on_element(self.advance_search_menu_id)

    def search_packg_in_advance_search(self, value, create_new_package='no', search_type=''):
        if create_new_package.lower() == 'yes':
            time.sleep(40)
        else:
            time.sleep(5)

        self.click_on_advance_search_menu()
        self.clear_field(self.advance_search_field_id)
        if search_type != "":
            self.select_type_dropdown(search_type)
        self.send_keys_to(self.advance_search_field_id, data=value)
        self.click_on_element(self.search_all_facilities)
        time.sleep(3)
        self.click_on_element(self.search_button_id)

    def click_search_button(self):
        self.click_on_element(self.search_button_id)

    def select_type_dropdown(self, search_type=""):
        if search_type != "":
            self.click_on_element(self.type_dropdown_button, "xpath")
            # dropd_list = self.driver.find_element_by_xpath(self.dropdown_ul_list_xpath)
            # dropd_items = dropd_list.find_elements_by_tag_name("li")
            dropd_list = self.driver.find_element(By.XPATH, self.type_dropdown_ul_list_xpath)
            dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
            self.select_values_from_drop_down_textContent(dropd_items, search_type)

    def verify_search_elements_present(self):
        self.isElementPresent(self.advance_search_field_id)
        self.isElementPresent(self.clear_search_button_id)
        self.isElementPresent(self.search_facilities_id)
        self.isElementPresent(self.today_only)

    def click_barcode1(self):
        time.sleep(4)
        self.click_on_element(locator=self.barcode1_xpath, locator_type="xpath")
        time.sleep(2)

    def change_package_status(self, status, exception="", close_window="", save_status="yes"):
        self.click_on_element(self.status_edit_xpath, "xpath")
        time.sleep(3)
        self.click_on_element(self.status_dropdown_xpath, "xpath")
        time.sleep(3)
        # dropd_list = self.driver.find_element_by_xpath(self.dropdown_ul_list_xpath)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.dropdown_ul_list_xpath)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, status)
        if status == "Delivered":
            self.change_to_delivered_status(exception)
        elif status == "Exception":
            self.change_to_exception_status(exception)
        elif status == "Attempt":
            self.change_to_exception_status(exception)
        if save_status == 'yes':
            self.click_on_element(self.save_Status, "xpath")
        time.sleep(3)
        if close_window == 'no':
            pass
        else:
            #     close_xpath = self.driver.find_element_by_xpath(self.close_window_button)
            close_xpath = self.driver.find_element(By.XPATH, self.close_window_button)
            self.driver.execute_script("arguments[0].click();", close_xpath)
            # self.click_on_element(self.close_window_button, "xpath")
            try:
                # close_xpath = self.driver.find_element_by_xpath(self.close_window_button)  #there is a second window we need to close sometimes if we search for route or package in Dashboard.
                close_xpath = self.driver.find_element(By.XPATH, self.close_window_button)
                self.driver.execute_script("arguments[0].click();", close_xpath)
            except:
                pass
            try:
                self.click_on_element(self.ok_button_after_close_window, "xpath")
            except:
                pass

    def close_package_window(self):
        self.click_on_element(self.close_window_button, "xpath")
        self.click_on_element(self.ok_button_after_close_window, "xpath")

    def change_to_delivered_status(self, exception=""):
        self.click_on_element(self.delivered_drop_dropdown_button, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.delivered_drop_dropdown_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.delivered_drop_dropdown_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, exception)
        self.send_keys_to(self.delivered_signature, "xpath", "abcd")

    def change_to_exception_status(self, exception=""):
        time.sleep(3)
        self.click_on_element(self.exception_drop_dropdown_button, "xpath")
        time.sleep(2)
        # dropd_list = self.driver.find_element_by_xpath(self.exception_drop_dropdown_ul_list)
        dropd_list = self.driver.find_element(By.XPATH, self.exception_drop_dropdown_ul_list)
        time.sleep(1)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        time.sleep(1)
        self.select_values_from_drop_down_textContent(dropd_items, exception)
        time.sleep(1)
        self.click_on_element(self.attempt_field_title,
                              "xpath")  # sometimes selected exception is not set properly so we clicking something in the page.
        time.sleep(1)

    def check_drop_location(self, drop_location):
        actual_location = self.driver.find_element(By.XPATH, self.drop_location_innertext).get_attribute('textContent')
        assert actual_location == drop_location

    def verify_package_event_received(self):
        # event = self.driver.find_element_by_xpath(self.package_event_received).get_attribute('textContent')
        event = self.driver.find_element(By.XPATH, self.package_event_received).get_attribute('textContent')
        assert event == "Received"

    def assign_contractor_to_package(self, contractorId='30107'):
        time.sleep(3)
        self.click_on_element(self.route_name_search_result_xpath, "xpath")
        time.sleep(3)
        # try:
        #     self.click_on_element(self.remove_contractor, "xpath")
        # except:
        #     pass
        unassign = self.isElementPresent(self.unassigned_contractor_label, "xpath")
        if unassign:
            self.click_on_element(self.contractor_edit, "xpath")
            time.sleep(3)
            self.send_keys_to(locator=self.contractor_id_textfield, data=contractorId, locator_type="xpath")
            time.sleep(2)
            self.click_on_element("windowRoute11125")
        time.sleep(2)
        self.click_on_element(self.close_window_button, "xpath")

    def verify_status_dropdown_values(self, default_status="Received", delivered="no"):
        # Testing Status Out For Delivery START
        # status = self.driver.find_element_by_xpath(self.statusCodeName).get_attribute('textContent')
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        assert status == default_status
        self.click_on_element(self.status_edit_xpath, "xpath")
        self.click_on_element(self.status_dropdown_xpath, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.dropdown_ul_list_xpath)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.dropdown_ul_list_xpath)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        try:
            self.select_values_from_drop_down(dropd_items,
                                              "Out For Delivery")  # Out for delivery should be greyed out so it should go to Exception
            assert pytest.fail("Out For Delivery should not be able to be selected")
        except:
            pass
        # status = self.driver.find_element_by_xpath(self.statusCodeName).get_attribute('textContent')
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        assert status == default_status  # Status should remain "Received"
        # Testing out for Delivery END

        # Testing Status Delivered START
        self.click_on_element(self.status_dropdown_xpath, "xpath")
        try:
            self.select_values_from_drop_down(dropd_items,
                                              "Delivered")  # Delivered should be greyed out so it should go to Exception
            if delivered.lower() == 'no':
                assert pytest.fail("Delivered should not be able to be selected")
            else:
                pass
        except:
            pass
        # status = self.driver.find_element_by_xpath(self.statusCodeName).get_attribute('textContent')
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        assert status == default_status  # Status should remain "Received"
        # Testing Status Delivered END

        # Testing Status Exception START
        self.click_on_element(self.status_dropdown_xpath, "xpath")
        self.select_values_from_drop_down(dropd_items, "Exception")
        # Testing Status Exception END

    def verify_current_status(self, expected_status):
        # status = self.driver.find_element_by_xpath(self.statusCodeName).get_attribute('textContent')
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        assert status == expected_status

    def verify_advance_search_drill_down_grid2(self):
        time.sleep(20)
        table = self.driver.find_element(By.ID, 'AdvancedSearchGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        expected_list = ["Barcode", "EDD", "Customer", "Service", "Route", "Contractor", "Status", "Stop Name",
                         "Address",
                         "Address 2", "City", "State", "Zip", "Phone", "Notes", "Reference", "Pkg Type", "Description",
                         "Weight", "Customer Route", "Customer Stop", "Container Name", "Pallet Barcode", "Facility"]
        test_results = "F"
        actual_list = []
        for row in rows:
            head_count = row.find_elements(By.TAG_NAME, "th")
            for headers in head_count:
                actual_list.append(headers.get_attribute('textContent'))
                # elipsis = headers.find_element_by_tag_name("a")
                elipsis = headers.find_element(By.TAG_NAME, "a")
                self.driver.execute_script("arguments[0].scrollIntoView();", elipsis)
                elipsis.click()
        assert expected_list == actual_list

    def verify_search_dropdown_list(self):
        time.sleep(3)
        expected_list = ["Barcode", "Reference Number", "Deliver To", "Order Number", "Address", "Attention To",
                         "Customer Route/Stop", "Customer", "Phone", "Zip"]
        actual_list = []
        # for tag in self.driver.find_elements_by_css_selector("select[id=ddlSearchType] option"):
        for tag in self.driver.find_elements(By.CSS_SELECTOR, "select[id=ddlSearchType] option"):
            value = tag.get_attribute('textContent')
            actual_list.append(value)
        assert expected_list == actual_list

    def check_search_grid_route_on_hold(self):
        # check if Route value is "on hold" in search grid
        self.isElementPresent(self.route_on_hold_xpath, "xpath")

    def wait_and_refresh_package_view(self):
        time.sleep(30)
        self.click_on_element(self.package_refresh)

    def verify_div_notification(
            self):  # this appears when there is error validation for not entering search dropdown type
        time.sleep(1)
        self.isElementPresent(self.div_notification)

    def verify_attempt_status_fields(self):
        self.click_on_element(self.edd_datepicker_text, "xpath")
        self.isElementPresent(self.edd_datepicker, "xpath")
        self.click_on_element(self.edd_datepicker, "xpath")
        time.sleep(3)
        self.click_on_element(self.edd_datepicker, "xpath")
        time.sleep(3)
        self.isElementPresent(self.door_tag, "xpath")
        self.isElementPresent(self.exception_notes, "xpath")

    def verify_advance_search_status_in_grid(self, expected_status):
        time.sleep(30)
        if self.driver.find_element(By.ID, self.search_all_facilities).is_selected() == bool(False):
            self.click_on_element(self.search_all_facilities)
            self.click_on_element(self.search_button_id)
        time.sleep(30)
        status = self.driver.find_element(By.XPATH, self.advance_search_status).get_attribute('textContent')
        try:
            assert status == expected_status
        except:
            time.sleep(30)
            self.click_on_element(self.search_button_id)
            time.sleep(30)
            status1 = self.driver.find_element(By.XPATH, self.advance_search_status).get_attribute('textContent')
            assert status1 == expected_status

    def set_adv_search_package_window_status_drop_down(self, status_value, exception_Value):
        time.sleep(40)
        self.click_on_element(self.barcode1_xpath, "xpath")
        time.sleep(5)
        self.isElementPresent(self.advance_search_package_window, "xpath")
        self.click_on_element(self.advSearch_package_window_edit_icon_nextToStatus, "xpath")
        time.sleep(5)
        self.select_advance_search_status(status_value)
        time.sleep(5)
        self.isElementPresent(self.advSearch_package_window_except_input_box, "xpath")
        self.select_advance_search_exception(exception_Value)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.advSearch_package_save_button).click()
        time.sleep(30)

    def select_advance_search_status(self, status_option):
        self.click_on_element(self.advSearch_package_window_status_dropdown, "xpath")
        dropd_list = self.driver.find_element(By.XPATH, self.advSearch_package_window_status_dropdown_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, status_option)

    def select_values_from_drop_down_textContent(self, dropDownOptionsList, value):
        time.sleep(2)
        element_find = "N"
        for element in dropDownOptionsList:
            time.sleep(2)
            if element.get_attribute('textContent') == value:
                element.click()
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))

    def select_advance_search_exception(self, exception_name):
        self.click_on_element(self.advSearch_package_window_exception_dropdown, "xpath")
        dropd_list = self.driver.find_element(By.XPATH, self.advSearch_package_window_exception_dropdown_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, exception_name)

    def verify_advSearch_package_window_status_and_latest_event_table_detail_isUpdated(self, expected_status,
                                                                                       expected_details,
                                                                                       expeted_status_type):
        updated_status = self.driver.find_element(By.XPATH, self.advSearch_package_window_sataus).get_attribute(
            'textContent')
        assert updated_status == expected_status
        updated_event_details = self.driver.find_element(By.XPATH,
                                                         self.advSearch_package_window_updated_eventDetails_grid).get_attribute(
            'textContent')
        assert updated_event_details == expected_details
        updated_event_type = self.driver.find_element(By.XPATH,
                                                      self.advsearch_package_window_updated_eventType_grid).get_attribute(
            'textContent')
        assert updated_event_type == expeted_status_type

    def change_status_as_outofDelevery(self, status_value):
        time.sleep(20)
        self.click_on_element(self.barcode1_xpath, "xpath")
        time.sleep(5)
        self.isElementPresent(self.advance_search_package_window, "xpath")
        self.click_on_element(self.advSearch_package_window_edit_icon_nextToStatus, "xpath")
        time.sleep(5)
        self.select_advance_search_status(status_value)
        time.sleep(5)
        # self.isElementPresent(self.advSearch_package_window_except_input_box, "xpath")
        # self.select_advance_search_exception(exception_Value)
        # time.sleep(10)
        self.driver.find_element(By.XPATH, self.advSearch_package_save_button).click()
        time.sleep(20)
        self.click_on_element(self.advSearch_package_window_close_tab, "xpath")
        time.sleep(30)

    def validate_package_status_to_be(self, status_value, polling_value=10, breakT_till_value=10):
        self.click_on_element(self.search_button_id)
        time.sleep(10)
        event = self.driver.find_element(By.XPATH, self.advance_search_status).get_attribute('textContent')
        count = 0
        while count < breakT_till_value:
            if event == status_value:
                return True
            count = count + 1
            self.click_on_element(self.search_button_id)
            time.sleep(polling_value)
            event = self.driver.find_element(By.XPATH, self.advance_search_status).get_attribute('textContent')

    def change_package_status_to_business_closed(self, status_value, exception_Value):
        self.click_on_element(self.search_button_id)
        time.sleep(20)
        self.click_on_element(self.barcode1_xpath, "xpath")
        time.sleep(5)
        self.isElementPresent(self.advance_search_package_window, "xpath")
        self.click_on_element(self.advSearch_package_window_edit_icon_nextToStatus, "xpath")
        time.sleep(5)
        self.select_advance_search_status(status_value)
        time.sleep(5)
        self.select_advance_search_exception(exception_Value)
        time.sleep(10)
        self.click_on_element(self.advSearch_package_save_button, "xpath")
        time.sleep(10)

    def close_advance_package_dialog(self):
        self.click_on_element(self.advSearch_package_window_close_tab, "xpath")
        time.sleep(30)

    def verify_event_coloumn_of_package_window(self, expected_details):
        time.sleep(5)
        updated_event_details = self.driver.find_element(By.XPATH,
                                                         self.advSearch_package_window_updated_eventDetails_grid).get_attribute(
            'textContent')
        assert updated_event_details == expected_details

    def search_packg_in_all_facilities(self, value, create_new_package='no', search_type=''):
        if create_new_package.lower() == 'yes':
            time.sleep(10)
        else:
            time.sleep(5)
        self.click_on_advance_search_menu()
        self.clear_field(self.advance_search_field_id)
        if search_type != "":
            self.select_type_dropdown(search_type)
        self.send_keys_to(self.advance_search_field_id, data=value)
        if not self.driver.find_element(By.ID, self.search_all_facilities).is_selected():
            self.click_on_element(self.search_all_facilities)
        self.click_on_element(self.search_button_id)

    def search_packg_without_search_all_facilities(self, value, create_new_package='no', search_type=''):
        if create_new_package.lower() == 'yes':
            time.sleep(10)
        else:
            time.sleep(5)
        self.click_on_advance_search_menu()
        self.clear_field(self.advance_search_field_id)
        if search_type != "":
            self.select_type_dropdown(search_type)
        self.send_keys_to(self.advance_search_field_id, data=value)
        if self.driver.find_element(By.ID, self.search_all_facilities).is_selected():
            self.click_on_element(self.search_all_facilities)
        self.click_on_element(self.search_button_id)

    def change_facility(self, facilityName):
        self.wait_for_element_clickable(self.profile_id, timeOut=10)
        self.click_on_element(self.profile_id)
        self.click_on_element(locator=self.facility_dropdown, locator_type="xpath")
        # facility_list = self.driver.find_element_by_id(self.facility_list_id)
        # facility_items = facility_list.find_elements_by_tag_name("li")
        facility_list = self.driver.find_element(By.ID, self.facility_list_id)
        facility_items = facility_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_with_JS(facility_items, facilityName, timeOut=10)

    def verify_advance_search_package_status_at_package_window(self):
        time.sleep(2)
        if self.get_element("//span[contains(@id,'statusCodeName')]", "xpath").get_attribute(
                "textContent") == "Returning":
            return False
        else:
            return True

    def forward_search_packg_in_advance_search(self, value, create_new_package='no', search_type=''):
        if create_new_package.lower() == 'yes':
            time.sleep(40)
        else:
            time.sleep(5)

        self.click_on_advance_search_menu()
        self.clear_field(self.advance_search_field_id)
        if search_type != "":
            self.select_type_dropdown(search_type)
        self.send_keys_to(self.advance_search_field_id, data=value)
        self.click_on_element(self.search_all_facilities)
        time.sleep(3)
        self.click_on_element(self.search_button_id)
        time.sleep(60)
        self.click_on_element(self.search_button_id)

    def add_invalid_date(self, status_value, exception_value, expected_status):
        # for x in range(40):
        self.isElementPresent(self.advance_search_package_window, "xpath")
        self.click_on_element(self.advSearch_package_window_edit_icon_nextToStatus, "xpath")
        time.sleep(5)
        self.select_advance_search_status(status_value)
        time.sleep(5)
        self.select_advance_search_exception(exception_value)
        time.sleep(10)
        self.click_on_element(self.invalid_date, "xpath")
        time.sleep(5)
        self.clear_field(self.invalid_date, "xpath")
        time.sleep(5)
        self.send_keys_to(self.invalid_date, "21/03/2001", "xpath")
        self.click_on_element(self.advSearch_package_save_button, "xpath")
        assert self.isElementPresent(self.error_msg, "xpath")
        time.sleep(4)
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%m/%d/%Y")
        print(formatted_date)
        self.click_on_element(self.invalid_date, "xpath")
        self.clear_field(self.invalid_date, "xpath")
        time.sleep(3)
        self.send_keys_to(self.invalid_date, formatted_date, "xpath")
        time.sleep(3)
        self.click_on_element(self.advSearch_package_save_button, "xpath")
        time.sleep(20)
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        # if status == expected_status:
        self.click_on_element(self.advSearch_package_window_close_tab, "xpath")
        time.sleep(30)
        # break

    def change_status_till_next_day_delivery(self, status_value, expected_status):
        # for x in range(20):

            time.sleep(15)
            self.isElementPresent(self.advance_search_package_window, "xpath")
            self.click_on_element(self.advSearch_package_window_edit_icon_nextToStatus, "xpath")
            time.sleep(5)
            self.select_advance_search_status(status_value)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.advSearch_package_save_button).click()
            time.sleep(20)
            status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
            # if status == expected_status:
            self.click_on_element(self.advSearch_package_window_close_tab, "xpath")
            print("Changed to exception *******************************************************")
            time.sleep(30)
                # break

    first_EDD_field_of_advance_search_grid = "//div[@id='AdvancedSearchGrid']//td[2]"
    adv_package_window_expected_delivery_label = "//div[@id='packageDrillDown']//div[contains(@class,'displayEDD')]/span"

    def verify_EDD_date_and_Expected_Delivery_in_advance_search_and_adv_package_window(self):
        time.sleep(3)
        EDD_column_date_value = self.get_element(self.first_EDD_field_of_advance_search_grid,"xpath").get_attribute("textContent")
        self.click_on_element(self.barcode1_xpath,"xpath")
        time.sleep(3)
        self.wait_for_element_clickable(self.adv_package_window_expected_delivery_label,"xpath",20)
        expected_delivery_label_value = self.get_element(self.first_EDD_field_of_advance_search_grid, "xpath").get_attribute(
            "textContent")
        self.click_on_element(self.advSearch_package_window_close_tab,"xpath")
        time.sleep(3)
        assert EDD_column_date_value == expected_delivery_label_value ,"EDD date of advance search and expected delivery date of advance search package window are not equal"


