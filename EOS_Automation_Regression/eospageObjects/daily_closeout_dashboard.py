import time

from selenium.webdriver.common.by import By

from Base.custom_code import Custom_code
from utilities.common_util import add_days_current_date


class eos_daily_closeout_dashboard(Custom_code):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    left_side_toggle_bar_icon = "//a[contains(@class,'sidebar-toggle')]"
    facility_Dashboard_icon = "aFacilityDashboardLink"
    Daily_Close_Out_Dashboard_icon = "liEpcClearExceptionsDashboardLink"
    Daily_Close_Out_Dashboard_set_as_landing_page = "//ul[@id='leftSideContextMenu']//span[text()='Set as Landing Page']"
    ClearExceptionsTopSearch_Row = "//div[@class='divRow clearExceptionsTopSearch']"

    elementsLoadingSpinner = "//div[@class='modalLoading']"
    end_date_picker_id = "txtClearExceptionsEndDate"
    run_button_id = "btnClearExceptionsRun"
    current_closeouts_id = 'spnClearExceptionsTotalFacilityCount'
    expand_icon_list = "//a[@class='k-icon k-i-expand']"
    exception_type_dropdown_arrow = "//label[text()='Exception Type:']/following::span[1]"
    exception_dropdown = "(//*[text()='Exception:']/../descendant::span[@role='listbox'])[1]"
    exception_type_options = "(//*[text()='Exception:']/../descendant::span[@role='listbox'])[1]//li/span"
    exception_type_dd_text = "//span[@aria-controls='ddlClearExceptionStatusUpdateExceptionType_listbox']/span[1]"
    exception_options = "//ul[@id='ddlClearExceptionStatusUpdateException_listbox']//li/span[1]"

    any_oneexception_option = "(//*[text()='Exception:']/../descendant::span[@role='listbox'])[1]"
    notes_icon = "btnClearExceptionStatusUpdateAddNote"
    notes_text_area = "noteText"
    notes_save_button = "//ul[@class='ulExceptionButtons']//li[3]//button"
    save_button = "//ul[@class='ulSection']//button[@id='btnClearExceptionStatusUpdateSave']"
    notification_ok_button = "//div[@id='clearExceptionsStatusUpdateSaveNotification']//button"
    facility_total_exc_column = "//div[@id='FacilityAggregateGrid']//tbody//td[13]/a"
    facility_exception_report_input_bar = "txtSearchException_Facility"
    package_under_the_test_status = "//div[@id='dashboardDrilldown_Exception_Facility']/descendant::tbody//td[2]"
    route_name = "(//div[@id='dashboardDrilldown_Exception_Facility']/descendant::tbody//td[4]/a)[1]"
    facility_exception_report_close_button = "//div[@class='k-window-actions k-hstack']//a[3]"
    exceptions_tab = "//span[normalize-space()='Exceptions']"
    exceptions_search_bar = "txtExceptionSearch"
    exceptions_route = "//div[@id='ExceptionDrillDownGrid']//tbody//td[5]"
    exceptions_stop_name = "//div[@data-gridid='RouteWindowStopParentGrid']/descendant::tbody//td[8]"
    start_date_picker_id = "txtClearExceptionsStartDate"
    select_one_exception_type_option_one = "(//ul[@id='ddlClearExceptionStatusUpdateException_listbox'])[1]/descendant::span[1]"
    attempt_exception = "(//ul[@id='ddlClearExceptionStatusUpdateExceptionType_listbox']/descendant::span)[2]"
    exception_type_drop_down_icon = '[aria-owns="ddlClearExceptionStatusUpdateExceptionType_listbox"] button'
    select_one_attempt_type = "//ul[@id='ddlClearExceptionStatusUpdateException_listbox']//li[1]//span"
    any_one_exception_option = "(//ul[@id='ddlClearExceptionStatusUpdateException_listbox']/descendant::span)[1]"
    Notification_ok_Button = "//div[@id='clearExceptionsStatusUpdateSaveNotification']//button"

    facility_total_att_column = "//div[@id='FacilityAggregateGrid']//tbody//td[11]/a"
    facility_attempt_report_input_bar = "txtSearchAttempted_Facility"
    attempt_att_status = "(//div[@id='dashboardDrilldown_Attempted_Facility']/descendant::tbody//td)[1]"


    def select_set_as_landing_page_at_Daily_Close_Out_Dashboard(self):
        self.click_on_element(self.left_side_toggle_bar_icon, "xpath")
        self.context_click(self.Daily_Close_Out_Dashboard_icon, "id")
        time.sleep(1)
        self.click_on_element(self.Daily_Close_Out_Dashboard_set_as_landing_page, "xpath")
        time.sleep(3)

    def verify_Daily_Close_Out_Dashboard_is_launched(self, base_url):
        self.driver.get(base_url)
        self.wait_for_element_clickable(self.ClearExceptionsTopSearch_Row, "xpath", 50)
        assert self.isElementPresent(self.ClearExceptionsTopSearch_Row, "xpath")
        self.context_click(self.facility_Dashboard_icon, "id")
        self.click_on_element(self.Daily_Close_Out_Dashboard_set_as_landing_page, "xpath")
        time.sleep(5)

    def navigate_daily_closeout_dashboard(self):
        self.click_on_element(self.Daily_Close_Out_Dashboard_icon)
        self.wait_for_element_not_clickable(self.elementsLoadingSpinner, "xpath", 30)

    def select_end_date(self, add_days=1):
        date_next_day = add_days_current_date("%m/%d/%Y", add_days)
        print("Next day:", date_next_day)
        self.clear_field(self.end_date_picker_id)
        self.send_keys_to(self.end_date_picker_id, data=date_next_day)

    def verify_ofp_after_run(self, stop_name="tc-1678"):
        self.wait_for_element_clickable(self.run_button_id, timeOut=10)
        self.click_on_element(self.run_button_id)
        self.isElementPresent(self.current_closeouts_id)
        expand_list = []
        expand_list = self.get_elements(self.expand_icon_list, "xpath")
        for expand in expand_list:
            expand.click()
            time.sleep(10)
        self.wait_for_element_clickable(
            "//td[text()='" + stop_name + "']/../descendant::button[1]", locator_type="xpath", timeOut=10)
        self.click_on_element("//td[text()='" + stop_name + "']/../descendant::button[1]", locator_type="xpath")

    def verify_exception_type_status(self, value="Exception"):
        time.sleep(5)
        self.wait_for_element_clickable(self.exception_type_dropdown_arrow, locator_type="xpath", timeOut=10)
        self.driver.find_element(By.XPATH, self.exception_type_dropdown_arrow).click()
        time.sleep(2)
        dropd_items = self.driver.find_elements(By.XPATH, self.exception_type_options)
        time.sleep(2)
        for option in dropd_items:
            option_text = option.get_attribute('textContent')
            if option_text == value:
                option.click()
                assert option_text == value

    def verify_exception_status(self, value="Select An Exception"):
        self.click_on_element(self.exception_dropdown, "xpath")
        dropd_items = self.get_elements(self.exception_options, locator_type="xpath")
        for option in dropd_items:
            option_text = option.get_attribute('textContent')
            if option_text == value:
                assert option_text == value

    def verify_ofd_after_run(self, stop_name="tc-1678"):
        self.wait_for_element_clickable(self.run_button_id, timeOut=10)
        self.click_on_element(self.run_button_id)
        self.isElementPresent(self.current_closeouts_id)
        expand_list = []
        expand_list = self.get_elements(self.expand_icon_list, "xpath")
        for expand in expand_list:
            expand.click()
            time.sleep(10)
        self.wait_for_element_clickable(
            "//td[text()='" + stop_name + "']/../descendant::button[2]", locator_type="xpath", timeOut=10)
        self.click_on_element("//td[text()='" + stop_name + "']/../descendant::button[2]", locator_type="xpath")

    def select_one_exception_option(self, text="due to bad weather"):
        time.sleep(20)
        self.wait_for_element_clickable(self.exception_dropdown, "xpath", 6)
        self.click_on_element(self.exception_dropdown, "xpath")
        time.sleep(3)
        self.wait_for_element_clickable(self.select_one_exception_type_option_one, "xpath", 6)
        time.sleep(10)
        self.click_on_element(self.select_one_exception_type_option_one, "xpath")
        time.sleep(1)
        self.click_on_element(self.notes_icon, "id")
        time.sleep(1)
        self.click_on_element(self.notes_text_area)
        time.sleep(1)
        self.send_keys_to(self.notes_text_area, text)
        self.click_on_element(self.notes_save_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.save_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.notification_ok_button, "xpath")
        time.sleep(10)

    def verify_package_under_exc_column_of_delivery_tab(self, barcode):
        self.click_on_element(self.facility_Dashboard_icon, "id")
        time.sleep(10)
        self.click_on_element(self.facility_total_exc_column, 'xpath')
        self.clear_field(self.facility_exception_report_input_bar, "id")
        self.send_keys_to(self.facility_exception_report_input_bar, data=barcode)
        time.sleep(3)
        package_row = self.driver.find_element(By.XPATH, self.package_under_the_test_status).get_attribute(
            "textContent")
        print(package_row)
        assert package_row == barcode
        route = self.driver.find_element(By.XPATH, self.route_name).get_attribute("textContent")
        print(route)
        self.click_on_element(self.facility_exception_report_close_button, "xpath")
        time.sleep(10)
        return route

    def verify_package_under_facility_db_exceptions_tab(self, value):
        self.click_on_element(self.exceptions_tab, "xpath")
        time.sleep(4)
        self.clear_field(self.exceptions_search_bar, "id")
        time.sleep(2)
        self.send_keys_to(self.exceptions_search_bar, data=value)
        self.click_on_element(self.exceptions_route, "xpath")
        time.sleep(10)

    def verify_test_data(self, stop_name="tc-1678"):
        time.sleep(2)
        stop_name_data = self.get_elements(self.exceptions_stop_name, "xpath")
        for element in stop_name_data:
            if element == stop_name:
                assert element == stop_name
                break

    def select_start_date(self, add_days=-1):
        date_next_day = add_days_current_date("%m/%d/%Y", add_days)
        self.clear_field(self.start_date_picker_id)
        self.send_keys_to(self.start_date_picker_id, data=date_next_day)
        time.sleep(4)

    def select_one_attempt_option(self, text):
        time.sleep(4)
        self.click_on_element(self.exception_type_drop_down_icon, "css")
        time.sleep(2)
        self.click_on_element(self.attempt_exception, "xpath")

        self.wait_for_element_clickable(self.exception_dropdown, "xpath", 6)
        self.click_on_element(self.exception_dropdown, "xpath")
        time.sleep(3)
        self.wait_for_element_clickable(self.select_one_attempt_type, "xpath", 5)
        self.click_on_element(self.select_one_attempt_type, "xpath")
        time.sleep(1)
        self.click_on_element(self.notes_icon, "id")
        time.sleep(4)
        self.click_on_element(self.notes_text_area, "id")
        self.send_keys_to(self.notes_text_area, text)
        time.sleep(5)
        self.click_on_element(self.notes_save_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.save_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.notification_ok_button, "xpath")
        time.sleep(10)

    def verify_facility_dashboard_deliveries_under_att_column(self, value):
        self.click_on_element(self.facility_Dashboard_icon, "id")
        time.sleep(10)
        self.click_on_element(self.facility_total_att_column, "xpath")
        self.clear_field(self.facility_attempt_report_input_bar, "id")
        self.send_keys_to(self.facility_attempt_report_input_bar, data=value)
        time.sleep(3)
        package_row = self.driver.find_element(By.XPATH, self.attempt_att_status).get_attribute(
            "textContent")
        print(package_row)
        assert package_row == value
