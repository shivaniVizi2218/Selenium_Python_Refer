import sys
import time
from _ast import Assert
import pytest
from selenium.webdriver import Keys, ActionChains

# sys.path.insert(1, 'c:/users/pjarubula/PycharmProjects/EPCProject')
# sys.path.insert(1, 'C:/Users/skhan/Documents/EPCProject/EPCProject')

from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CustomLogger import custlogger
from logging import Logger
from selenium.webdriver.support.ui import Select
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.advance_search import eos_advance_search
import random
import string
from utilities.common_util import add_days_current_date


# from utilities.screenshots import Screen_shots


class package_entry(eos_facility_dashboard):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.advance_search = None
        self.facility_dashboard = None
        self.dispatch_dashboard = None
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)

    fas_fa_bars = "//*[@class='fas fa-bars']"
    customer_ddl_button = "//*[contains(@aria-owns, 'ddlPeCustomerFormTop_listbox') and contains(@aria-labelledby, 'ddlPeCustomerFormTop_label')]//button"
    customer_ddl_ul_list = "//*[@id='ddlPeCustomerFormTop_listbox']"
    generate = "btnPeGenerateBarcode"
    validate = "btnPeValidateFormTop"
    cancel = "btnPeCancel"
    lock_form_checkbox = "cbPeLockInitialForm"
    package_image = "//*[@src='/Content/images/package_future.png']"
    package_entry = "// a[contains(text(), 'Package Entry')]"
    calendar_icon = "//*[@aria-controls='txtPeDeliveryDateFormTop_dateview']"
    address_look_up = "(//*[@data-buttonid='btnPeLookUpAddress'])[2]"
    address_look_up2 = "//button[@data-buttonid='btnPeLookUpAddress']"
    address_line1 = "txtScrubAddress"
    city = "txtScrubCity"
    zip = "txtScrubZip"
    state_button = "//*[contains(@aria-owns, 'ddlScrubState_listbox') and contains(@aria-controls, 'ddlScrubState_listbox')]//button"
    state_ul_list = "//*[@id='ddlScrubState_listbox']"
    clear_address = "btnScrubClearAddress"
    btnScrubAddressCancel = "btnScrubAddressCancel"
    btnScrubAddressValidate = "btnScrubAddressValidate"
    Search_for_Addresses_Near_Zip = "// a[contains(text(), 'Search for Addresses Near Zip')]"
    Search_for_Addresses_Near_Facility = "// a[contains(text(), 'Search for Addresses Near Facility')]"
    stop_name = "txtPeStopNameDest"
    stop_name2 = "txtPeStopNameOrig"
    btnPeSubmitPackage = "btnPeSubmitPackage"
    btnPeAddPackage = "//*[@id='btnPeAddPackage']"
    get_barcode = "//*[@style='white-space: nowrap;']"
    get_barcode_id = "txtPeBarcode"

    package_type_button = "//*[contains(@aria-owns, 'ddlPePackageType_listbox') and contains(@aria-controls, 'ddlPePackageType_listbox')]//button"
    package_type_ul_list = "//*[contains(@id, 'ddlPePackageType_listbox')]"
    service_type_button = "//*[contains(@aria-owns, 'ddlPeService_listbox') and contains(@aria-controls, 'ddlPeService_listbox')]//button"
    service_type_ul_list = "//*[contains(@id, 'ddlPeService_listbox')]"

    return_to_sender_radio = "rbPkgEntryRts"
    forward_branch_radio = "rbPkgEntryFtb"
    package_overage = "rbPkgEntryOvg"
    submit_button = "btnSubmitRtsFtb"

    customer_name_read = "//*[@aria-owns='ddlPeCustomerFormTop_listbox']//span//span"
    barcode_field_xpath = "txtPeBarcodeFormTop"
    search_map_id = "searchMapText"
    package_entry_id = "liPackageEntryDashboardLink"
    deliveries_tab_exception = "//div[@id='FacilityAggregateGrid']//table//tbody//tr//td[12]/a"
    barcode_search_field_exception = "txtSearchException_Facility"
    deliveries_tab_attempt = "//div[@id='FacilityAggregateGrid']//table//tbody//tr//td[11]/a"
    barcode_search_field_attempt = "txtSearchAttempted_Facility"
    package_txt = "//*[@id='divWrapper']/ul[1]/li[1]/div[1]/span"

    duplicate_barcode_dialog = "//div[contains(text(),'Duplicate Barcode:')]"

    elementsLoadingSpinner = "//div[@class='modalLoading']"
    pacakge_entry_txt = "(//span[contains(text(),'Package Entry')])[position()=2]"

    package_route_link = "(//tr[@class='k-master-row']/descendant::td[@role='gridcell']/descendant::a[@class='clickable openRouteWindow'])[position()=1]"
    exception_disaster = "//span[contains(text(),'Delay due to weather or natural disaster')]"
    exception_factor = "//span[contains(text(),'Delay in service due to external factors')]"
    exception_breakdown = "//span[contains(text(),'Mechanical Breakdown Will Impact Delivery')]"
    events_txt = "(//span[contains(text(),'Events')])[position()=1]"
    status_pickup_txt = "(//ul[contains(@id,'editPackageStatus')]/descendant::li/descendant::span[contains(text(),'Pickup')])[position()=1]"
    status_out_for_pickup_txt = "//ul[contains(@id,'editPackageStatus')]/descendant::li/descendant::span[contains(text(),'Out For Pickup')]"
    status_pickedup_txt = "//ul[contains(@id,'editPackageStatus')]/descendant::li/descendant::span[contains(text(),'Picked Up')]"
    status_attempt_txt = "//ul[contains(@id,'editPackageStatus')]/descendant::li/descendant::span[contains(text(),'Attempt')]"
    status_except_txt = "//ul[contains(@id,'editPackageStatus')]/descendant::li/descendant::span[contains(text(),'Exception')]"
    router_status_assign = "//i[@class='fas fa-pencil-alt inline iconHover clickable marL3']"
    router_status_label = "//span/input[contains(@id,'routeWindowContractorComplete')]"
    requested_reattempt = "//ul[contains(@id,'exceptionDropDown')]//descendant::li/span[contains(text(),'Customer Requested Re-Attempt')]"
    remove_onhold = "//ul[contains(@id,'exceptionDropDown')]//descendant::li/span[contains(text(),'Removed From On Hold')]"
    expected_delivery_date = "//input[contains(@id,'EDDdatePicker')]"
    invalid_txt = "//div[contains(text(),'EDD is an Invalid Date')]"
    attempt_column = "//*[@id='FacilityAggregateGrid']/table/tbody/descendant::tr/td[11]/a"
    attempt_col_barcode = "(//a[@class='clickable viewPackageDetail'])[position()=2]"
    exception_col = "//*[@id='FacilityAggregateGrid']/table/tbody/descendant::tr/td[13]/a"

    customer_search_field = "//input[@aria-controls='ddlPeCustomerFormTop_listbox']"
    customer_stop_field = "txtPeCustomerSequence"
    customer_route_field = "txtPeBillingRoute"

    route_dropdown_button = "span[aria-controls='ddlPeRoute_listbox'] button"
    route_input = "input[aria-controls='ddlPeRoute_listbox']"
    # destination_address_label = "// span[text() = 'Destination Address']"
    drop_status_carat = "//span[contains(@aria-owns,'dropLocationDropDown')]/descendant::button"
    drop_status_option = "//ul[contains(@id,'dropLocationDropDown')]/descendant::span[text()='BACK_DOOR']"
    delivery_column_data = "(//a[@class='clickable viewPackageDetail'])[2]"
    route_dropdown = "[aria-owns='ddlPeRoute_listbox']"
    route_ul_list = "//*[@id ='ddlPeRoute_listbox']"
    route_dropdown_button = "span[aria-controls='ddlPeRoute_listbox'] button"
    route_input = "input[aria-controls='ddlPeRoute_listbox']"

    customer_input = "(//input[@role='searchbox'])[7]"
    select_customer_midwest = "//ul[@id='ddlPeCustomerFormTop_listbox']//li[1]"
    red_barcode_window = "// div[ @ id = 'Overage_Insert_Window']"
    forward_branch_radio_button = " // input[ @ id = 'rbPkgEntryFtb']"
    destination = "//label[@id='lblMissortDestinationFacility']"
    forward_submit_button = "//button[@id='btnSubmitRtsFtb']"
    deafult_status = "(//*[text()='Transfer'])[2]"
    status_type = "//div[@data-gridid='PackageWindowEventsGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[2]//td[2]"
    event_detail = "//div[@data-gridid='PackageWindowEventsGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[2]//td[3]"

    barcode_input_area = "//input[@id='txtPeBarcodeFormTop']"
    # facility_dropdown = "//*[@class='facilitySelectContainer']//span//button"
    profile_id = "dispatcherNameMain"
    default_facility = "(//div[@class='facilitySelectContainer']//following::span)[3]"
    view_duplicate_button = "btnPeViewDuplicatePackageFormTop"
    clone_package_button = "btnPeClonePackage"
    package_detail_window = "//div[@class='k-widget k-window k-display-inline-flex k-state-focused']"
    package_detail_window_cross = "(//span[contains(@id,'packageDrillDown')]//following::a[@aria-label='Close'])[1]"
    clone_package_window = "//div[@id='clonePackageWindow']"
    barcode_text = "(//div[@id='clonePackageWindow']//following::div)[2]/span"
    clone_package_text1 = "(//div[@id='clonePackageWindow']//following::div)[1]"
    clone_package_text2 = "(//div[@id='clonePackageWindow']//following::div)[3]"
    clone_address_elements = "(//div[@id='clonePackageWindow']//following::div)[4]//input"
    clone_package_cancel_button = "//button[@id='btnCancelClonePackage']"
    clone_package_submit_button = "//button[@id='btnConfirmPackageClone']"
    package_clone_package_barcode1 = "(//*[@class='clickable viewPackageDetail'])[1]"
    package_clone_package_barcode2 = "(//*[@class='clickable viewPackageDetail'])[2]"
    package_clone_package_barcode3 = "(//*[@class='clickable viewPackageDetail'])[3]"


    exceptions_search_box = "//input[@id='txtExceptionSearch']"
    facility_dashboard_id = "aFacilityDashboardLink"
    exceptions_tab = "//span[normalize-space()='Exceptions']"
    route_window = "//div[@id='ExceptionDrillDownGrid']//tbody//td[5]/a"
    exceptions_stop_name = "//div[@data-gridid='RouteWindowStopParentGrid']/descendant::tbody//td[8]"
    settings_close_button = "//div[contains(@class,'k-window-titlebar k-hstack')]//a[@aria-label='Close']"
    deliveries_tab = "//span[normalize-space()='Deliveries']"
    exc_column = "//div[@id='FacilityAggregateGrid']//tbody//td[13]/a"
    exception_facility_input = "txtSearchException_Facility"
    exception_facility_barcode = "(//div[@id='dashboardDrilldown_Exception_Facility']/descendant::tbody//td)[2]/a"


    def click_package_entry(self):
        # self.click_on_element(self.fas_fa_bars)
        self.click_on_element(self.package_entry_id)
        self.wait_for_element_not_clickable(self.elementsLoadingSpinner,"xpath",30)

        packageTxt = self.driver.find_element(By.XPATH, self.package_txt).get_attribute('textContent')
        print("barcode: " + packageTxt)
        assert (self.isElementPresent(self.package_txt), "xpath")

    def select_customer(self, customer_name):
        self.click_on_element(self.customer_ddl_button, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.customer_ddl_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.customer_ddl_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, customer_name)

    def select_state(self, state):
        self.click_on_element(self.state_button, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.state_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.state_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, state)

    def fill_out_lookup_address(self, address_line1="1300 SW 17th Ave", city="Boynton Beach",
                                state="Florida (FL)", zip="33426"):
        # time.sleep(2)  # might not need. just in case
        # self.click_on_element(self.address_look_up, "xpath")
        time.sleep(3)
        self.isElementPresent(self.Search_for_Addresses_Near_Facility, "xpath")
        self.isElementPresent(self.Search_for_Addresses_Near_Zip, "xpath")
        self.isElementPresent(self.btnScrubAddressCancel, "id")
        self.isElementPresent(self.clear_address, "id")
        self.send_keys_to(self.address_line1, address_line1)
        self.send_keys_to(self.city, city)
        time.sleep(3)
        self.select_state(state)
        time.sleep(4)
        self.send_keys_to(self.zip, zip)
        time.sleep(1)
        self.click_on_element(self.btnScrubAddressValidate)

    def check_elements_package_entry_page1(self):
        self.isElementPresent(self.generate, "id")
        self.isElementPresent(self.validate, "id")
        self.isElementPresent(self.cancel, "id")
        self.isElementPresent(self.lock_form_checkbox, "id")
        self.isElementPresent(self.package_image, "xpath")
        self.isElementPresent(self.package_entry, "xpath")
        self.isElementPresent(self.calendar_icon, "xpath")

    def create_a_package(self, customer_name="blank", package_type="Box", service_type="Next Day Delivery",
                         return_to_sender="no", forward_branch="no", overage="yes", skip_generate="no",
                         stop_name="tc-28", address_line1="1300 SW 17TH AVE", city="Boynton Beach",
                         state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
        if customer_name != "AMAZON NON SORT (51728)":
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(7)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        # time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        self.wait_for_element_clickable(self.get_barcode, "xpath", 30)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    # this is creating a pick up service package. It works with Advances care solutions customer.
    def create_a_pick_up_package(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)", package_type="Box",
                                 service_type="Pickup", return_to_sender="no", forward_branch="no", overage="yes",
                                 skip_generate="no", stop_name="tc-1678", address_line1="1426 SKEES RD STE E",
                                 city="WEST PALM BEACH", state="Florida (FL)", zip="33411"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(3)
            self.click_on_element(self.generate)
            time.sleep(3)
            self.click_on_element(self.validate)
            time.sleep(5)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up2, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name2, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.forward_branch_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    def select_package_type(self, package_type="Box"):
        self.click_on_element(self.package_type_button, "xpath")
        time.sleep(1)
        # dropd_list = self.driver.find_element_by_xpath(self.package_type_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.package_type_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, package_type)
        time.sleep(2)

    def service_type(self, service_type="Next Day Delivery"):
        time.sleep(3)
        self.click_on_element(self.service_type_button, "xpath")
        time.sleep(3)
        # dropd_list = self.driver.find_element_by_xpath(self.service_type_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.service_type_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, service_type)
        time.sleep(2)

    def get_customer_name(self):
        time.sleep(1)
        self.click_on_element(self.search_map_id)
        time.sleep(2)
        # act_customer = self.driver.find_element_by_xpath(self.customer_name_read).get_attribute('textContent')
        # act_customer = self.driver.find_element(By.XPATH, self.customer_name_read).get_attribute('textContent')
        act_customer = self.driver.find_element(By.XPATH, self.customer_name_read).get_attribute('textContent')
        print("customer: " + act_customer)
        return act_customer

    def enter_barcode(self, barcode):
        self.click_cancel()
        self.clear_field(self.barcode_field_xpath)
        self.send_keys_to(self.barcode_field_xpath, barcode, "id")
        time.sleep(2)
        self.click_on_element(self.search_map_id)
        time.sleep(1)

    def click_cancel(self):
        self.click_on_element(self.cancel)

    def set_package_entry_as_default_landing_page(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        # element = self.driver.find_element_by_id(self.facility_dashboard_id)
        element = self.driver.find_element(By.ID, self.package_entry_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_set_landing_page()
        time.sleep(2)

    def create_a_pick_up_package_with_nextday_delivery(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                       package_type="Box",
                                                       service_type="Pickup", return_to_sender="no",
                                                       forward_branch="no", overage="yes",
                                                       skip_generate="no", stop_name="tc-1678",
                                                       address_line1="1426 SKEES RD STE E",
                                                       city="WEST PALM BEACH", state="Florida (FL)", zip="33411"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(3)
            self.click_on_element(self.generate)
            time.sleep(3)
            self.click_on_element(self.validate)
            time.sleep(3)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up2, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name2, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    def create_a_pick_up_package_with_pickup_delivery(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                      package_type="Box",
                                                      service_type="Pickup", return_to_sender="no",
                                                      forward_branch="no", overage="yes",
                                                      skip_generate="no", stop_name="tc-1678",
                                                      address_line1="1426 SKEES RD STE E",
                                                      city="WEST PALM BEACH", state="Florida (FL)", zip="33411"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(3)
            self.click_on_element(self.generate)
            time.sleep(3)
            self.click_on_element(self.validate)
            time.sleep(3)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(3)
        self.click_on_element(self.address_look_up2, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name2, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(5)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        return barcode

    def find_package_in_deliveries_exception_column(self, barcode='pass_a_barcode', drilldown_type="exception"):
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(3)
        if drilldown_type.lower() == "exception":
            self.click_on_element(self.deliveries_tab_exception, "xpath")
            time.sleep(2)
            self.click_on_element(self.barcode_search_field_exception)
            time.sleep(1)
            self.send_keys_to(self.barcode_search_field_exception, barcode)
            time.sleep(1)
            self.send_keys_to(self.barcode_search_field_exception, Keys.RETURN)
        if drilldown_type.lower() == "attempt":
            self.click_on_element(self.deliveries_tab_attempt, "xpath")
            time.sleep(2)
            self.click_on_element(self.barcode_search_field_attempt)
            time.sleep(1)
            self.send_keys_to(self.barcode_search_field_attempt, barcode)
            time.sleep(1)
            self.send_keys_to(self.barcode_search_field_attempt, Keys.RETURN)
        time.sleep(2)
        self.isElementPresent("(//a[contains(text(),'" + barcode + "')])[2]", "xpath")
        self.click_on_element("(//a[contains(text(),'" + barcode + "')])[2]", "xpath")
        time.sleep(2)



    def create_package_with_package_customer_name(self,
                                                  customer_name="Blue Apron wholly owned by Fresh Ream Inc (M7178-51687)",
                                                  package_type="Box", service_type="Non-RTS Delivery",
                                                  return_to_sender="no", forward_branch="no", overage="yes",
                                                  skip_generate="no",
                                                  stop_name="tc-28", address_line1="1300 SW 17TH AVE",
                                                  city="Boynton Beach",
                                                  state="Florida (FL)", zip="33426", used_numbers=None):

        string_value = "1LS"  # Your string value
        random_digits = [random.randint(0, 9) for _ in range(19)]
        random_code = ''.join(map(str, random_digits))
        result_string = string_value + random_code

        time.sleep(5)
        self.select_customer(customer_name)
        self.sleep3()
        self.driver.find_element(By.ID, self.barcode_field_xpath).send_keys(result_string)
        self.sleep3()
        # assert (self.isElementPresent(self.validate), "xpath")
        self.driver.find_element(By.ID, self.validate).click()
        if customer_name != "AMAZON NON SORT (51728)":
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up, "xpath")
        self.sleep3()
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(6)
        self.send_keys_to(self.stop_name, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(7)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        # time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        self.wait_for_element_clickable(self.get_barcode, "xpath", 30)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    def create_a_package_with_existing_barcode(self, customer_name="blank", barcode_existing="blank"):

        time.sleep(10)
        self.wait_for_element_not_clickable(self.elementsLoadingSpinner,"xpath",30)
        self.wait_for_element_clickable(self.customer_ddl_button, "xpath",20)
        self.select_customer(customer_name)
        self.clear_field(self.barcode_field_xpath)
        self.send_keys_to(self.barcode_field_xpath, barcode_existing, "id")
        time.sleep(2)
        self.click_on_element(self.validate)
        time.sleep(2)
        self.isElementPresent(self.duplicate_barcode_dialog, "xpath")
        time.sleep(2)
        self.click_on_element(self.forward_branch_radio)
        time.sleep(2)
        self.click_on_element(self.submit_button)
        time.sleep(10)
    def verify_package_entryForm(self, package_entry_name):
        packageEntry_Txt = self.driver.find_element(By.XPATH, self.pacakge_entry_txt).get_attribute('textContent')
        print("packageEntry_Txt: " + packageEntry_Txt)
        assert packageEntry_Txt == package_entry_name

    def perform_and_verify_barcode_status(self, exception_disaster, exception_factor, exception_breakdown):
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch_dashboard = eos_dispatch_dashboard(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_route_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dispatch_dashboard.close_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_dashboard.barcode_res, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.events_txt, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.status_change).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.status_dropdown).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.exeption_status).click()
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.edd_datepicker, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.attempt_field_title, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.door_tag, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.exception_notes, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.exception_drpdwn).click()
        time.sleep(10)
        exception_delay_txt = self.driver.find_element(By.XPATH, self.exception_disaster).get_attribute('textContent')
        print("exception_delay_txt" + exception_delay_txt)
        assert exception_delay_txt == exception_disaster
        exception_factor_txt = self.driver.find_element(By.XPATH, self.exception_factor).get_attribute('textContent')
        print("exception_factor_txt" + exception_factor_txt)
        assert exception_factor_txt == exception_factor
        exception_breakdown_txt = self.driver.find_element(By.XPATH, self.exception_breakdown).get_attribute(
            'textContent')
        print("exception_breakdown_txt" + exception_breakdown_txt)
        assert exception_breakdown_txt == exception_breakdown

    def verify_package_screen_updated_status(self, route_number):

        self.advance_search = eos_advance_search(self.driver)
        self.dispatch_dashboard = eos_dispatch_dashboard(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_route_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_assign).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_label).send_keys(route_number)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dispatch_dashboard.close_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_dashboard.barcode_res, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.events_txt, "xpath"))
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(10)
        self.facility_dashboard.verify_out_for_pickup_values()

    def verify_attempt_status_work_out_for_delivery(self, route_number):
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch_dashboard = eos_dispatch_dashboard(self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_route_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_assign).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_label).send_keys(route_number)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dispatch_dashboard.close_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_dashboard.barcode_res, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.events_txt, "xpath"))
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status="Out For Delivery")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.advance_search.save_Status).click()
        time.sleep(10)

    def verify_attempt_status_expected_delivery(self):
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status="Attempt")
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.edd_datepicker, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.attempt_field_title, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.door_tag, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.advance_search.exception_notes, "xpath"))
        time.sleep(2)
        self.facility_dashboard.click_on_attempt_drp_down()
        time.sleep(3)
        assert not (self.isElementPresent(self.requested_reattempt, "xpath"))
        time.sleep(2)
        assert not (self.isElementPresent(self.remove_onhold, "xpath"))
        time.sleep(3)
        self.facility_dashboard.verify_attempt_status_values1()

    def click_on_attempt_status(self):
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status="Attempt")
        time.sleep(2)
        self.facility_dashboard.click_on_attempt_drp_down()
        time.sleep(2)
        self.facility_dashboard.select_attempt_reason(attempt="Need More Information")

    def select_invalid_date(self, add_days=2):
        date_next_day = add_days_current_date("%d-%m-%Y", add_days)
        print("Next day:", date_next_day)
        time.sleep(2)
        expected_delivery = self.driver.find_element(By.XPATH, self.expected_delivery_date)
        expected_delivery.clear()
        expected_delivery.send_keys(date_next_day)
        # self.clear_field(self.expected_delivery_date)
        # self.send_keys_to(self.expected_delivery_date, data=date_next_day)

    def verify_invalid_date(self):
        assert (self.isElementPresent(self.invalid_txt), "xpath")

    def select_current_date(self, add_days=0):
        date_current_day = add_days_current_date("%m/%d/%Y", add_days)
        print("current day:", date_current_day)
        time.sleep(2)
        expected_delivery = self.driver.find_element(By.XPATH, self.expected_delivery_date)
        expected_delivery.clear()
        expected_delivery.send_keys(date_current_day)

    def verify_attempt_search(self, barcode):
        self.driver.find_element(By.XPATH, self.attempt_column).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.barcode_search_field_attempt).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.barcode_search_field_attempt).send_keys(barcode)
        col_att_barcode_txt = self.driver.find_element(By.XPATH, self.attempt_col_barcode).get_attribute('textContent')
        print("Col_barcode:" + col_att_barcode_txt)
        assert barcode == col_att_barcode_txt

    def verify_exception_search(self, barcode):
        self.driver.find_element(By.XPATH, self.exception_col).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.barcode_search_field_exception).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.barcode_search_field_exception).send_keys(barcode)
        col_exception_barcode_txt = self.driver.find_element(By.XPATH, self.attempt_col_barcode).get_attribute(
            'textContent')
        print("Col_barcode:" + col_exception_barcode_txt)
        assert barcode == col_exception_barcode_txt

    def close_barcode_window(self):
        self.advance_search = eos_advance_search(self.driver)
        self.driver.find_element(By.XPATH, self.advance_search.close_window_button).click()

    def create_a_package_without_select_service(self, customer_name="blank", package_type="Box", service_type="Next Day Delivery",
                         return_to_sender="no", forward_branch="no", overage="yes", skip_generate="no",
                         stop_name="tc-28", address_line1="1300 SW 17TH AVE", city="Boynton Beach",
                         state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(5)
            self.click_on_element(self.validate)
        time.sleep(2)
        self.select_package_type(package_type)
        self.click_on_element(self.address_look_up, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(7)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        # time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        self.wait_for_element_clickable(self.get_barcode, "xpath", 30)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    def select_customer_after_search(self, customer_name):
        self.click_on_element(self.customer_ddl_button, "xpath")
        self.send_keys_to(locator=self.customer_search_field, data=customer_name, locator_type="xpath")
        time.sleep(10)
        dropd_list = self.driver.find_element(By.XPATH, self.customer_ddl_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent_JS(dropd_items, customer_name, timeOut=10)

        def select_route(self, route):
            self.click_on_element(self.route_dropdown_button, "css")
            time.sleep(3)
            self.send_keys_to(self.route_input, route, "css")
            time.sleep(3)
            actionchains = ActionChains(self.driver)
            actionchains.send_keys(Keys.TAB)
            actionchains.perform()
            time.sleep(3)

    def verify_delivered_status(self, route_number):
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch_dashboard = eos_dispatch_dashboard(self.driver)
        self.package_entry = package_entry(self.driver)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_entry.package_route_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_entry.router_status_assign).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.package_entry.router_status_label).send_keys(route_number)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dispatch_dashboard.close_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.barcode_res).click()
        time.sleep(2)
        assert (self.isElementPresent(self.barcode_res, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.package_entry.events_txt, "xpath"))
        time.sleep(2)
        self.click_on_status_pencil_icon()
        time.sleep(2)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.change_the_status_to_out_for_delivery(status="Delivered")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.drop_status_carat).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.drop_status_option).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.advance_search.save_Status).click()
        time.sleep(10)

    def verify_delivery_column_vals(self, barcode):
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.driver.find_element(By.ID, self.facility_dashboard.facility_search).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.facility_dashboard.facility_search).send_keys(barcode)
        time.sleep(2)
        delivery_data_txt = self.driver.find_element(By.XPATH, self.delivery_column_data).get_attribute('textContent')
        print("delivery_data_txt:" + delivery_data_txt)
        print("barcode:" + barcode)
        assert delivery_data_txt == barcode

    def select_route(self, route):
        self.click_on_element(self.route_dropdown_button, "css")
        time.sleep(3)
        self.send_keys_to(self.route_input, route, "css")
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.TAB)
        actionchains.perform()
        time.sleep(3)

    def create_a_package_with_route(self, customer_name="blank", package_type="Box", service_type="Next Day Delivery",
                                    return_to_sender="no", forward_branch="no", overage="yes", skip_generate="no",
                                    stop_name="tc-28", address_line1="1300 SW 17TH AVE", city="Boynton Beach",
                                    state="Florida (FL)", zip="33426", route="000"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
        if customer_name != "AMAZON NON SORT (51728)":
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        self.select_route(route)
        time.sleep(7)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        # time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        self.wait_for_element_clickable(self.get_barcode, "xpath", 30)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode

    def assign_contractor(self, route_number):
        self.driver.find_element(By.XPATH, self.route_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_assign).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.router_status_label).send_keys(route_number)

    def create_package(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)", package_type="Box",
                       service_type="Pickup", return_to_sender="no", forward_branch="no", overage="no",
                       skip_generate="no", stop_name="tc-1678", address_line1="1426 SKEES RD STE E",
                       city="WEST PALM BEACH", state="Florida (FL)", zip="33411", customer_route="2218",
                       customer_stop="123"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            time.sleep(3)
            self.select_customer_after_search(customer_name)
            time.sleep(3)
            self.click_on_element(self.generate)
            time.sleep(3)
            self.click_on_element(self.validate)
            time.sleep(5)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.send_keys_to(self.customer_route_field, customer_route)
        self.send_keys_to(self.customer_stop_field, customer_stop)
        time.sleep(2)
        if "delivery" in service_type.lower():
            self.click_on_element(self.address_look_up, "xpath")
        else:
            self.click_on_element(self.address_look_up2, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        if "delivery" in service_type.lower():
            self.send_keys_to(self.stop_name, stop_name)
        else:
            self.send_keys_to(self.stop_name2, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.forward_branch_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')

    def eastern_facility_address_package(self, customer_name="blank", package_type="Box",
                                         service_type="Next Day Delivery",
                                         return_to_sender="no", forward_branch="no", overage="yes",
                                         skip_generate="no",
                                         stop_name="tc-28", address_line1="1300 SW 17TH AVE", city="Boynton Beach",
                                         state="Florida (FL)", zip="33426", route="000"):

        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer_for_midwest(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
        if customer_name != "AMAZON NON SORT (51728)":
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        time.sleep(2)
        self.click_on_element(self.address_look_up, "xpath")
        self.fill_out_lookup_address(address_line1, city, state, zip)
        time.sleep(2)
        self.send_keys_to(self.stop_name, stop_name)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        self.select_route(route)
        time.sleep(7)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        assert self.isElementPresent(self.red_barcode_window, "xpath")
        assert self.isElementPresent(self.forward_branch_radio_button, "xpath")
        assert self.isElementPresent(self.destination, "xpath")
        self.click_on_element(self.forward_branch_radio_button, "xpath")
        self.click_on_element(self.forward_submit_button, "xpath")
        self.wait_for_element_clickable(self.get_barcode, "xpath", 30)
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(1)
        self.click_on_element(self.btnPeSubmitPackage)
        print(barcode)
        return barcode


    def select_customer_for_midwest(self, customer_name):
        time.sleep(3)
        self.click_on_element(self.customer_ddl_button, "xpath")
        time.sleep(2)
        self.send_keys_to(self.customer_input, customer_name, "xpath")
        time.sleep(3)
        self.click_on_element(self.select_customer_midwest, "xpath")
        time.sleep(2)

    def verifying_status(self, value, info, event):
        default_status_option = self.driver.find_element(By.XPATH, self.deafult_status).get_attribute("textContent")
        assert default_status_option == value
        default_status_option2 = self.driver.find_element(By.XPATH, self.status_type).get_attribute("textContent")
        assert default_status_option2 == info
        default_status_option3 = self.driver.find_element(By.XPATH, self.event_detail).get_attribute("textContent")
        assert default_status_option3 == event

    def refresh_website(self, base_url):
        self.driver.get(base_url)

    def duplicate_barcode(self, value, customer_name, barcode):
        time.sleep(2)
        self.click_on_element(self.profile_id, "id")
        facility_default_option = self.driver.find_element(By.XPATH, self.default_facility).get_attribute("textContent")
        if facility_default_option == value:
            assert facility_default_option == value
            self.click_on_element(self.package_entry_id)
            time.sleep(2)
            self.select_customer_for_midwest(customer_name)
            time.sleep(2)
            self.click_on_element(self.barcode_input_area, "xpath")
            self.send_keys_to(self.barcode_input_area, barcode, "xpath")
            self.click_on_element(self.validate, "id")
            time.sleep(10)
        else:
            assert False

    def verify_duplicate_clone_package(self, barcode, info, message1):
        self.isElementPresent(self.view_duplicate_button, "id")
        self.isElementPresent(self.clone_package_button, "id")
        self.click_on_element(self.view_duplicate_button, "id")
        time.sleep(2)
        self.isElementPresent(self.package_detail_window, "xpath")
        self.click_on_element(self.package_detail_window_cross, "xpath")
        self.click_on_element(self.clone_package_button, "id")
        self.isElementPresent(self.clone_package_window, "xpath")
        time.sleep(10)
        random_barcode = barcode + "-DUP"
        print(random_barcode)
        getting_text = self.driver.find_element(By.XPATH, self.barcode_text).get_attribute("textContent")
        print(getting_text)
        assert random_barcode == getting_text
        clone_package_message1 = self.driver.find_element(By.XPATH, self.clone_package_text1).get_attribute(
            "textContent")
        assert clone_package_message1 == message1
        value_disabled = self.driver.find_element(By.XPATH, self.clone_address_elements).get_attribute("value")
        assert value_disabled == info
        input_element = self.driver.find_element(By.XPATH, self.clone_address_elements)
        assert not input_element.is_enabled()
        self.click_on_element(self.clone_package_cancel_button, "xpath")
        time.sleep(1)
        self.click_on_element(self.clone_package_button, "id")
        time.sleep(1)
        self.click_on_element(self.clone_package_submit_button, "xpath")
        time.sleep(10)

    def verify_duplicate_package_thrice(self, customer_name, barcode, info, message1):

        self.click_on_element(self.package_entry_id)
        time.sleep(2)
        self.select_customer_for_midwest(customer_name)
        time.sleep(2)
        self.click_on_element(self.barcode_input_area, "xpath")
        self.send_keys_to(self.barcode_input_area, barcode, "xpath")
        self.click_on_element(self.validate, "id")
        self.click_on_element(self.clone_package_button, "id")
        self.isElementPresent(self.clone_package_window, "xpath")
        time.sleep(10)
        random_barcode = barcode + "-DUP-3pkg"
        print(random_barcode)
        getting_text = self.driver.find_element(By.XPATH, self.barcode_text).get_attribute("textContent")
        print(getting_text)
        assert random_barcode == getting_text
        clone_package_message1 = self.driver.find_element(By.XPATH, self.clone_package_text1).get_attribute(
            "textContent")
        assert clone_package_message1 == message1
        value_disabled = self.driver.find_element(By.XPATH, self.clone_address_elements).get_attribute("value")
        assert value_disabled == info
        input_element = self.driver.find_element(By.XPATH, self.clone_address_elements)
        assert not input_element.is_enabled()
        self.click_on_element(self.clone_package_cancel_button, "xpath")
        time.sleep(1)
        self.click_on_element(self.clone_package_button, "id")
        time.sleep(1)
        self.click_on_element(self.clone_package_submit_button, "xpath")
        time.sleep(10)

    def verify_third_clone_packages_in_advance_search(self, barcode):
        duplicate_barcode = barcode + "-DUP"
        third_duplicate_barcode = barcode + "-DUP-3pkg"
        clone_package = self.driver.find_element(By.XPATH, self.package_clone_package_barcode1).get_attribute(
            "textContent")
        assert clone_package == barcode
        duplicate_package = self.driver.find_element(By.XPATH, self.package_clone_package_barcode2).get_attribute(
            "textContent")
        assert duplicate_package == duplicate_barcode
        third_duplicate_package = self.driver.find_element(By.XPATH, self.package_clone_package_barcode3).get_attribute(
            "textContent")
        assert third_duplicate_package == third_duplicate_barcode

    def verify_exceptions_results(self, stop_name):

        self.click_on_element(self.facility_dashboard_id, "id")
        time.sleep(6)
        self.click_on_element(self.exceptions_tab, "xpath")
        time.sleep(10)
        self.click_on_element(self.exceptions_search_box, "xpath")
        self.send_keys_to(self.exceptions_search_box, "401WESTA", "xpath")
        time.sleep(4)
        self.click_on_element(self.route_window, "xpath")
        time.sleep(5)
        stop_name_data = self.get_elements(self.exceptions_stop_name, "xpath")

        for element in stop_name_data:
            element_text = element.get_attribute("textContent")
            print(element_text)
            if element_text == stop_name:
                assert element_text == stop_name
                break

        self.click_on_element(self.settings_close_button, "xpath")

    def verify_deliveries_packages(self, barcode):
        time.sleep(2)
        self.click_on_element(self.deliveries_tab, "xpath")
        self.click_on_element(self.exc_column, "xpath")
        time.sleep(5)
        self.send_keys_to(self.exception_facility_input, barcode, "id")
        time.sleep(2)
        package_row = self.driver.find_element(By.XPATH, self.exception_facility_barcode).get_attribute(
            "textContent")
        print(package_row)
        assert package_row == barcode





