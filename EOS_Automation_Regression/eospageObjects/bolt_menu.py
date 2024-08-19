import sys
import time
from _ast import Assert
import pytest
from selenium.webdriver import Keys

sys.path.insert(1, 'c:/users/pjarubula/PycharmProjects/EPCProject')
# sys.path.insert(1, 'C:/Users/skhan/Documents/EPCProject/EPCProject')
from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

# from utilities.CustomLogger import custlogger
from logging import Logger
from selenium.webdriver.support.ui import Select
from utilities import DB_connection


# from utilities.screenshots import Screen_shots


class eos_bolt_menu(Custom_code):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)

    fas_fa_bars = "//*[@class='fas fa-bars']"
    bolt_menu = 'iconBoltMenu'
    bolt_menu_reports = "//a[@href='#control-sidebar-report-tab']"
    bolt_settings_menu = "//*[@href='#control-sidebar-settings-tab']"
    multi_sequence = "hlMultiSequence"
    route_image = "//*[@src='Content/images/route.png']"
    sequence_options = "//div[contains(text(),' Sequence Options ')]"
    multi_seq_faq = "icoMultiSequenceFAQ"
    faq0 = "//*[@href='#collapseFAQ0']"
    faq1 = "//*[@href='#collapseFAQ1']"
    faq2 = "//*[@href='#collapseFAQ2']"
    second_close_window_button = "(//*[@aria-label='Close'])[2]"
    all_routes = "btnSequenceRoutes"
    service_routes = "btnSequenceAddServiceRoutes"
    select_routes = "(//*[@aria-controls='ddlSequenceRoutes_listbox'])[2]"
    btnSequenceRoute = "btnSequenceRoute"
    btnCancelSequence = "btnCancelSequence"
    btnSequenceSwitch = "btnSequenceSwitch"
    btnSequenceContractor = "btnSequenceContractor"
    endpoint_dropd_ul_list = "//*[contains(@id, 'ddlSequenceEndLocationRoute_listbox') and contains(@data-role, 'staticlist')]"
    endpoint_dropd_xpath = "//*[@aria-controls='ddlSequenceEndLocationRoute_listbox']//button"
    select_route_input = "//input[@aria-controls='ddlSequenceRoutes_listbox']"
    # switch sequence contractor page
    all_contractors = "btnSequenceContractor"
    contractor_image = "//img[@src='Content/images/ic_male.png']"
    select_contractor_input = "//input[@aria-controls='ddlSequenceContractors_listbox']"
    iframe_contractor = "//iframe[@ng-show='!failureReason']"

    mass_event_applicator = "hlEventApplicator"
    mass_event_barcode_input = "//*[@class='k-spreadsheet-cell k-spreadsheet-active-cell k-left k-top k-right k-single']"

    akb_stop_notes = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/AKB%20Stop%20Notes%20By%20Facility']"
    all_eos_reports = "//a[@href='http://dev.reports.lasership.com/ngreports/browse/NEXTGEN/']"
    alerts_report = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Notification%20Report']"
    load_manifest_with_received = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Load%20Manifest%20With%20Rec']"
    location_services = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Location%20Services%20OFF%20-%20ALL%20Deliveries']"
    missing_load_scan = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/MLS%20(Missing%20Load%20Scan)']"
    mls_by_facility_and_route = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/MLS%20by%20Facility%20and%20Route']"
    mls_by_facility_and_zip = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/MLS%20By%20Facility%20and%20Zip']"
    MOSD_by_facility = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/MOSD%20By%20Facility']"
    past_edd = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Past%20EDD']"
    attempts_not_redelivered = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Attempts%20not%20Redelivered']"
    status_update = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Status%20Update']"
    unable_to_deliver_exceptions = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Unable%20to%20Deliver%20Exceptions%20(LOD%20404%20423)']"
    attempt_by_facility = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Attempt%20By%20Facility']"
    driver_summary = "//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Driver%20Summary']"
    load_manifest_barcode="//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Load%20Manifest%20By%20Barcode']"
    load_manifest_stop ="//a[@href='http://dev.reports.lasership.com/ngreports/report/NEXTGEN/Load%20Manifest%20By%20Stop']"
    save_button = "ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg"
    word = "//a[@title='Word']"
    excel = "//a[@title='Excel']"
    powerpoint = "//a[@title='PowerPoint']"
    pdf = "//a[@title='PDF']"
    tiff_file = "//a[@title='TIFF file']"
    mhtml = "//a[@title='MHTML (web archive)']"
    csv = "//a[@title='CSV (comma delimited)']"
    csv_delimit = "//a[@title='CSV (PIPE Delimited)']"
    csv_noheader = "//a[@title='CSV (No Header)']"
    tab_delimit = "//a[@title='TAB Delimited']"
    xml_file = "//a[@title='XML file with report data']"
    data_feed = "//a[@title='Data Feed']"

    arrival_scan = "//a[@href='report/NEXTGEN/Arrival%20Scan']"

    mass_delay_link = "hlOpenMassDelay"
    facility_element = "//*[text()='Scheduled Delays']/../descendant::span[2]"
    customer_element = "//*[text()='Scheduled Delays']/../descendant::span[5]"
    service_element = "//*[text()='Scheduled Delays']/../descendant::span[8]"
    route_element = "//*[text()='Scheduled Delays']/../descendant::span[11]"
    contractor_element = "//*[text()='Scheduled Delays']/../descendant::span[14]"
    New_edd_element = "//*[text()='Scheduled Delays']/../descendant::span[20]"
    New_event_element = "//*[text()='Scheduled Delays']/../descendant::span[29]"
    scheduled_time_element = "//*[text()='Scheduled Delays']/../descendant::span[32]"

    Reason_field = "//*[text()='Event Data']/../descendant::span[1]"
    scheduled_time_field = "//*[text()='Event Data']/../descendant::span[5]"
    new_edd_field = "//*[text()='Event Data']/../descendant::span[8]"

    default_option_in_Reason_field = "//*[text()='Event Data']/../descendant::span[3]"
    Reason_field_dropdown = "[aria-owns='ddlMassDelayReason_listbox']"
    Reason_field_options = "//ul[@id='ddlMassDelayReason_listbox']//li/span"

    facility_field = "//*[text()='Facility Data']/../descendant::span[2]"
    facility_field_default_option = "//*[text()='Facility Data']/../descendant::span[2]"
    facilities_field = "//*[text()='Facility Data']/../descendant::input[3]"
    facility_field_dropdown = "[aria-owns='ddlMassDelayFacilityType_listbox']"
    facility_field_options = "//*[@id='ddlMassDelayFacilityType_listbox']/descendant::span"
    by_contractor_radio_button = "radioMassDelayByContractor"
    by_route_radio_button = "radioMassDelayByRoute"
    by_customer_radio_button = "radioMassDelayByCustomer"
    select_customers = "ddlMassDelayCustomers_taglist"
    select_services = "ddlMassDelayServices_taglist"
    all_customers_button = "btnMassDelaySelectAllCustomers"
    all_services_button = "btnMassDelaySelectAllServices"
    mass_delay_cancel_button = "//button[@id='btnCancelMassDelay'][1]"
    mass_delay_submit_button = "//button[@id='btnConfirmMassDelay'][1]"
    cost_area_adjustments_link = "hlCostAreas"
    un_route = "//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]/td[4]/a"
    cost_area_barcode_element = "(//*[text()='Barcode'])[7]"
    cost_area_cost_area_element = "//*[text()='Cost Area']"
    cost_area_route_element = "(//*[text()='Route'])[6]"
    cost_area_customer_element = "(//*[text()='Customer'])[6]"
    cost_area_address = "(//*[text()='Customer'])[6]"
    cost_area_city = "(//*[text()='Customer'])[4]"
    cost_area_state = "(//*[text()='Customer'])[4]"
    cost_area_zip = "(//*[text()='Customer'])[4]"
    check_box = "//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]//input"
    New_input_area_text_box = "//*[text() ='New Cost Area:']/..//input"
    New_input_area_option = "//ul[@id ='txtCostArea_listbox']/li[1]"
    cost_area_submit_button = "//button[@id ='btnUpdateCostArea'][1]"
    cost_area_yes_button = "//button[@id='btnConfirmYes'][1]"
    cost_area_barcode = "//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]/td[2]/a"
    cost_area_cancel_button = "//button[@id='btnCancelCostArea'][1]"
    package_other_tab = "//span[normalize-space()='Other']"
    updated_cost_area_in_other_tab = "//*[text() ='Package Info']//following-sibling::div[2]//div[5]"

    mass_delay_by_customer_radio_button = "//input[@id='radioMassDelayByCustomer']"
    mass_delay_select_customer = "ddlMassDelayCustomers_taglist"
    mass_delay_select_customer_input = "//div[@id='ddlMassDelayCustomers_taglist']/input"
    mass_delay_select_customer_option = "//ul[@id='ddlMassDelayCustomers_listbox']//li[1]"
    mass_delay_select_service = "ddlMassDelayServices_taglist"
    mass_delay_select_service_input = "//div[@id='ddlMassDelayServices_taglist']/input"
    mass_delay_select_service_option = "//ul[@id='ddlMassDelayServices_listbox']//li[1]"
    mass_delay_yes_button = "//button[@id='btnConfirmYes'][1]"
    mass_delay_window = "//div[@class='statusBar yellowStatus']"
    package_detail_kendo_window = "(//*[text()='Customer'])[1]"
    mass_delay_event = "//div[@data-gridid='PackageWindowEventsGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]//td[3]"

    # cost_area_adjustments_link = "hlCostAreas"
    # un_route = "//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]/td[4]/a"
    # cost_area_barcode_element = "(//*[text()='Barcode'])[7]"
    # cost_area_cost_area_element = "//*[text()='Cost Area']"
    # cost_area_route_element = "(//*[text()='Route'])[6]"
    # cost_area_customer_element = "(//*[text()='Customer'])[6]"
    # cost_area_address = "(//*[text()='Customer'])[6]"
    # cost_area_city = "(//*[text()='Customer'])[4]"
    # cost_area_state = "(//*[text()='Customer'])[4]"
    # cost_area_zip = "(//*[text()='Customer'])[4]"
    # check_box = "//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]//input"
    # New_input_area_text_box = "//*[text() ='New Cost Area:']/..//input"
    # New_input_area_option = "//ul[@id ='txtCostArea_listbox']/li[1]"
    # cost_area_submit_button = "//button[@id ='btnUpdateCostArea'][1]"
    # cost_area_yes_button = "//button[@id='btnConfirmYes'][1]"
    # cost_area_barcode ="//div[@id='costAreaGrid']//div[@class='k-grid-content k-auto-scrollable']//tr[1]/td[2]/a"
    # cost_area_cancel_button = "//button[@id='btnCancelCostArea'][1]"
    # package_other_tab = "//span[normalize-space()='Other']"
    # updated_cost_area_in_other_tab = "//*[text() ='Package Info']//following-sibling::div[2]//div[5]"

    # filters
    dispatch_route_mark_icon = "(//div[@class='routeMarkerBackground  routeMarkerAssigned']/span)[1]"
    contractor_panel = "//strong[text()='Contractor']"
    contractor_filter_deselect = "filterContractorGridDeselect"
    contractor_un_assigned_routes = "//span[text()='Unassigned Routes']"
    contractor_filter_icon = "//div[@id='filterContractorGrid']/descendant::th[1]"
    contactor_monitor = "//div[@id='filterContractorGrid']/descendant::th[2]"
    contractor_code = "//div[@id='filterContractorGrid']/descendant::th[3]/descendant::span[text()='Code']"
    contractor_name = "//div[@id='filterContractorGrid']/descendant::th[4]/descendant::span[text()='Name']"
    contractor_info = "//div[@id='filterContractorGrid']/descendant::tbody/tr[1]"

    route_panel = "//strong[text()='Route']"
    route_deselect = "//div[@id='filterRouteGridDeselect']/a[text()='Deselect All']"
    show_empty_checkbox = "//div[@id='filterRouteGridDeselect']/descendant::span[text()=' Show Empty']"

    route_filter = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[1]/descendant::span/i"
    route_monitor = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[2]/descendant::span/i"
    route_text = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[3]/descendant::span[text()='Route']"
    route_contractor = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[4]/descendant::span[text()='Contractor']"
    route_packages = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[5]/descendant::span[text()='# Packages']"
    route_stops = "//div[@id='filterRouteGrid']/descendant::table/thead/descendant::th[6]/descendant::span[text()='# Stops']"
    route_info = "//div[@id='filterRouteGrid']/descendant::tbody/tr[1]"

    customer_panel = "//div[@id='ParentCollapseEvent']/descendant::strong[text()='Customer']"
    customer_deselect_all = "//div[@id='customerGridDeselect']/a[text()='Deselect All']"
    customer_filter = "//div[@id='customerGrid']/descendant::thead/tr/th[1]/descendant::span/i"
    customer_name = "//div[@id='customerGrid']/descendant::thead/tr/th[2]/descendant::span[text()='Customer Name']"
    customer_package = "//div[@id='customerGrid']/descendant::thead/tr/th[3]/descendant::span[text()='# Packages']"
    customer_stop = "//div[@id='customerGrid']/descendant::thead/tr/th[4]/descendant::span[text()='# Stops']"
    customer_info = "//div[@id='customerGrid']/div/descendant::table/descendant::tbody/tr[1]"

    service_panel = "//div[@id='ParentCollapseService']/descendant::strong[text()='Service']"
    service_deselect_all = "//div[@id='serviceGridDeselect']/a[text()='Deselect All']"
    service_filter = "//div[@id='serviceGrid']/descendant::table/descendant::thead/tr[1]/th[1]/descendant::span/i"
    service_name = "//div[@id='serviceGrid']/descendant::table/descendant::thead/tr[1]/th[2]/descendant::span[text()='Name']"
    service_package = "//div[@id='serviceGrid']/descendant::table/descendant::thead/tr[1]/th[3]/descendant::span[text()='# Packages']"
    service_stops = "//div[@id='serviceGrid']/descendant::table/descendant::thead/tr[1]/th[4]/descendant::span[text()='# Stops']"
    service_info = "//div[@id='ParentCollapseService']/descendant::tbody/tr[1]"

    status_panel = "//div[@id='ParentCollapseStatus']/descendant::div/descendant::strong[text()='Status']"
    status_deselect = "filterStatusGridDeselect"
    status_filter = "//div[@id='collapseStatus']/descendant::table/thead/tr[1]/th[1]/descendant::span/i"
    status_text = "//div[@id='collapseStatus']/descendant::table/thead/tr[1]/th[2]/descendant::span[text()='Status']"
    status_info = "//div[@id='collapseStatus']/descendant::table/tbody/tr[1]"

    status_not_received_checkbox = "statusFilterGrid_0"
    status_out_for_delivery_checkbox = "statusFilterGrid_1"
    status_delivered_check_box = "statusFilterGrid_3"
    status_exception_check_box = "statusFilterGrid_4"
    status_low_quality_check_box = "statusFilterGrid_5"
    default_filter = "//li[@title='Filters']/a"


    def verify_multi_sequence_elements(self):
        self.click_on_element(self.bolt_menu)
        self.click_on_element(self.bolt_settings_menu, "xpath")
        self.click_on_element(self.multi_sequence)
        self.isElementPresent(self.route_image, "xpath")
        self.isElementPresent(self.sequence_options, "xpath")
        self.isElementPresent(self.all_routes)
        self.isElementPresent(self.service_routes)
        self.isElementPresent(self.select_routes)
        self.isElementPresent(self.btnCancelSequence)
        self.isElementPresent(self.btnSequenceRoute)
        self.click_on_element(self.multi_sequence)
        self.isElementPresent(self.faq0)
        self.isElementPresent(self.faq1)
        self.isElementPresent(self.faq2)
        self.click_on_element(self.second_close_window_button, "xpath")
        self.click_on_element(self.select_route_input, "xpath")
        self.click_on_element(self.route_image, "xpath")
        self.verify_endpoint_dropdown_list()

        self.click_on_element(self.btnSequenceSwitch)
        self.isElementPresent(self.all_contractors)
        self.isElementPresent(self.sequence_options, "xpath")
        self.isElementPresent(self.btnCancelSequence)
        self.isElementPresent(self.btnSequenceRoute)
        self.isElementPresent(self.btnSequenceSwitch)
        self.click_on_element(self.select_contractor_input, "xpath")
        self.click_on_element(self.contractor_image, "xpath")
        self.verify_endpoint_dropdown_list()

    def verify_endpoint_dropdown_list(self):
        time.sleep(3)
        self.click_on_element(self.endpoint_dropd_xpath, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.endpoint_dropd_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.endpoint_dropd_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(dropd_items, "Furthest Stop")
        time.sleep(1)
        self.select_values_from_drop_down(dropd_items, "Facility")

    def enter_barcode_in_mass_applicator(self, barcode):
        # self.driver.execute_script("document.querySelector('#searchMapText').value=1234")
        self.click_on_element(self.bolt_menu)
        self.click_on_element(self.bolt_settings_menu, "xpath")
        self.click_on_element(self.mass_event_applicator)
        # cell = self.driver.find_element_by_xpath("//*[@class='k-spreadsheet-cell k-spreadsheet-active-cell k-left k-top k-right k-single']")
        ##spreadsheetBarcodes > div.k-spreadsheet-view > div.k-spreadsheet-fixed-container > div.k-spreadsheet-pane.k-top.k-left > div.k-spreadsheet-data > div.k-spreadsheet-cell.k-spreadsheet-active-cell.k-left.k-top.k-right.k-single
        self.driver.execute_script(
            "document.querySelector('#spreadsheetBarcodes > div.k-spreadsheet-view > div.k-spreadsheet-fixed-container > div.k-spreadsheet-pane.k-top.k-left > div.k-spreadsheet-data > div.k-spreadsheet-cell.k-spreadsheet-active-cell.k-left.k-top.k-right.k-single').value=1234")
        # self.driver.execute_script("document.cell.value='"+barcode+"'")

        # self.driver.execute_script("document.getElementByXpath('//*[@class='k-spreadsheet-cell k-spreadsheet-active-cell k-left k-top k-right k-single']').value='"+barcode+"'")
        # checkbox3 = self.driver.find_element_by_xpath("//div[@id='dashboardDrilldown_MLS_Facility']"
        # "/div[2]/table/tbody/tr[3]/td[1]")
        # self.click_on_element(self.mass_event_barcode_input, "xpath")
        # self.click_on_element(self.mass_event_barcode_input, "xpath")
        # self.send_keys_to(self.mass_event_barcode_input, barcode, "xpath")

    def get_day_formatted(self, days_to_subtract=0):
        d = datetime.today() - timedelta(days=days_to_subtract)
        d2 = d.strftime("%m/%d/%y")
        d3 = str(d2)[:10]
        return str(d3)

    def check_download_file_formats(self):
        time.sleep(2)
        self.click_on_element(self.save_button)
        time.sleep(2)
        self.isElementPresent(self.word, "xpath")
        self.isElementPresent(self.excel, "xpath")
        self.isElementPresent(self.powerpoint, "xpath")
        self.isElementPresent(self.pdf, "xpath")
        self.isElementPresent(self.tiff_file, "xpath")
        self.isElementPresent(self.mhtml, "xpath")
        self.isElementPresent(self.csv, "xpath")
        self.isElementPresent(self.csv_delimit, "xpath")
        self.isElementPresent(self.csv_noheader, "xpath")
        self.isElementPresent(self.tab_delimit, "xpath")
        self.isElementPresent(self.xml_file, "xpath")
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.isElementPresent(self.data_feed, "xpath")

    def go_to_a_bolt_menu_view_report(self, report_name="akb_stop_notes",user_name="skhan",password="@Miami33067"):
        time.sleep(2)
        self.click_on_element(self.bolt_menu)
        time.sleep(2)
        self.click_on_element(self.bolt_menu_reports, "xpath")
        if report_name == "all_eos_reports":
            self.click_on_element(self.all_eos_reports, "xpath")
        if report_name == "akb_stop_notes":
            self.click_on_element(self.akb_stop_notes, "xpath")
        if report_name == "alerts_report":
            self.click_on_element(self.alerts_report, "xpath")
        if report_name == "attempt_by_facility":
            self.click_on_element(self.attempt_by_facility, "xpath")
        if report_name == "Driver_Summary":
            self.click_on_element(self.driver_summary, "xpath")
        if report_name == "Load_Manifest_By_Barcode":
            self.click_on_element(self.load_manifest_barcode, "xpath")
        if report_name == "Load_Manifest_By_Stop":
            self.click_on_element(self.load_manifest_stop, "xpath")
        if report_name == "load_manifest_with_received":
            self.click_on_element(self.load_manifest_with_received, "xpath")
        if report_name == "location_services":
            self.click_on_element(self.location_services, "xpath")
        if report_name == "missing_load_scan":
            self.click_on_element(self.missing_load_scan, "xpath")
        if report_name == "mls_by_facility_and_route":
            self.click_on_element(self.mls_by_facility_and_route, "xpath")
        if report_name == "mls_by_facility_and_zip":
            self.click_on_element(self.mls_by_facility_and_zip, "xpath")
        if report_name == "MOSD_by_facility":
            self.click_on_element(self.MOSD_by_facility, "xpath")
        if report_name == "past_edd":
            self.click_on_element(self.past_edd, "xpath")
        if report_name == "attempts_not_redelivered":
            self.click_on_element(self.attempts_not_redelivered, "xpath")
        if report_name == "status_update":
            self.click_on_element(self.status_update, "xpath")
        if report_name == "unable_to_deliver_exceptions":
            self.click_on_element(self.unable_to_deliver_exceptions, "xpath")
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        url1 = self.driver.current_url
        time.sleep(4)
        list1 = url1.split("//", 1)
        url2 = list1[1]
        url3 = "https://"+user_name+":"+password+"@" + url2
        print("url3: " + url3)
        self.driver.get(url3)
        time.sleep(10)
        # if report_name != "All_EOS_Reports":        #view_all_ssrs_reports page does not have iframe. Other reports does.
        #    iframe_elem = self.get_element(self.iframe_contractor, "xpath")
        #    self.driver.switch_to.frame(iframe_elem)

    def akb_stop_notes_report(self, facility_name="Akron"):
        # time.sleep()
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl05_ddValue"))
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")
        time.sleep(5)

    def verify_alerts_report(self, facility_name="Akron", start_date="", end_date=""):
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_ddValue")
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl03_ddValue"))
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl11_txtValue")
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl11_divDropDown_ctl00")
        # ActionChains.send_keys("all").perform()
        # action = ActionChains(self.driver)
        # action.send_keys("all")
        # action.perform()
        # self.click_on_element(self.dropdown_in_reports1)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_txtValue")
        self.send_keys_to("ReportViewerControl_ctl04_ctl05_txtValue", start_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_txtValue")
        self.send_keys_to("ReportViewerControl_ctl04_ctl07_txtValue", end_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl09_txtValue")  # dismissed only
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl09_divDropDown_ctl00")  # select all
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")
        time.sleep(3)

    def verify_load_manifest_received_report(self, facility_name, delivery_date):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")  # delivery date
        self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl05_ddValue"))  # facility
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(6)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # delivery dropdown
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_divDropDown_ctl02")  # select all
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # deliver dropdown again
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(5)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")
        time.sleep(3)

    def verify_location_services_report(self, delivery_date):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")  # delivery date
        self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddDropDownButton")  # faclity input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_divDropDown_ctl02")  # faclity name
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddDropDownButton")  # faclity input
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(6)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")
        time.sleep(3)

    def verify_missing_load_scan(self, delivery_date):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        # self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")  # delivery date
        # self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddDropDownButton")  # faclity input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_divDropDown_ctl02")  # faclity name
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddDropDownButton")  # faclity input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_divDropDown_ctl00")  # Customer name
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(5)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")
        time.sleep(3)

    def verify_MLS_by_facility_and_route(self, delivery_date, facility_name):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")  # delivery date
        self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl05_ddValue"))  # facility
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_txtValue")  # Click delivery date
        time.sleep(2)
        self.send_keys_to("ReportViewerControl_ctl04_ctl07_divDropDown_ctl00", "all")
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(5)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")
        time.sleep(3)

    def verify_MOSD_by_facility(self, facility_name):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(4)
        # self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")  # delivery date
        # self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl05_ddValue"))  # facility
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_divDropDown_ctl00")  # Customer name
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(5)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(5)
        self.click_on_element("//a[@title='PDF']", "xpath")

    def verify_attempts_not_redelivered(self, facility_name, delivery_date):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_ddValue")  # faclity
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_ddValue")  # faclity
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl03_ddValue"))  # facility
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_txtValue")  # delivery date
        self.send_keys_to("ReportViewerControl_ctl04_ctl05_txtValue", delivery_date)
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddValue")  # report type
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl07_ddValue"))  # report type
        select.select_by_visible_text("Redelivery")  # select by visible text
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")

    def verify_status_update(self, facility_name):
        time.sleep(3)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl05_ddValue")  # faclity
        time.sleep(2)
        select = Select(self.driver.find_element_by_id("ReportViewerControl_ctl04_ctl05_ddValue"))  # facility
        select.select_by_visible_text(facility_name)  # select by visible text
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_divDropDown_ctl00")  # Customer name
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl07_ddDropDownButton")  # Customer input
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl09_ddDropDownButton")  # Service input
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl09_divDropDown_ctl00")  # Service name
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl09_ddDropDownButton")  # Service input
        time.sleep(4)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")  # view report
        time.sleep(5)
        self.click_on_element("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown")  # click save report
        time.sleep(2)
        self.click_on_element("//a[@title='PDF']", "xpath")

    def verify_arrival_scan_report(self, delivery_date):
        time.sleep(2)
        self.click_on_element(self.arrival_scan, "xpath")
        time.sleep(5)
        iframe_elem = self.get_element("//iframe[@ng-show='!failureReason']", "xpath")
        self.driver.switch_to.frame(iframe_elem)
        time.sleep(2)
        self.click_on_element("ReportViewerControl_ctl04_ctl03_txtValue")
        self.send_keys_to("ReportViewerControl_ctl04_ctl03_txtValue", delivery_date)
        time.sleep(3)
        self.click_on_element("ReportViewerControl_ctl04_ctl00")
        time.sleep(9)  # this report is very slow

    def verify_mass_delay_elements(self):
        self.click_on_element(self.bolt_menu)
        self.click_on_element(self.bolt_settings_menu, "xpath")
        self.click_on_element(self.mass_delay_link, "id")
        assert self.isElementPresent(self.facility_element, "xpath")
        assert self.isElementPresent(self.customer_element, "xpath")
        assert self.isElementPresent(self.service_element, "xpath")
        assert self.isElementPresent(self.route_element, "xpath")
        assert self.isElementPresent(self.contractor_element, "xpath")
        assert self.isElementPresent(self.New_edd_element, "xpath")
        assert self.isElementPresent(self.New_event_element, "xpath")
        assert self.isElementPresent(self.scheduled_time_element, "xpath")
        assert self.isElementPresent(self.Reason_field, "xpath")
        assert self.isElementPresent(self.scheduled_time_field, "xpath")
        assert self.isElementPresent(self.new_edd_field, "xpath")
        assert self.isElementPresent(self.by_contractor_radio_button, "id")
        assert self.isElementPresent(self.by_route_radio_button, "id")
        assert self.isElementPresent(self.by_customer_radio_button, "id")
        assert self.isElementPresent(self.select_customers, "id")
        assert self.isElementPresent(self.select_services, "id")
        assert self.isElementPresent(self.all_customers_button, "id")
        assert self.isElementPresent(self.all_services_button, "id")
        assert self.isElementPresent(self.mass_delay_cancel_button, "id")
        assert self.isElementPresent(self.mass_delay_submit_button, "id")

    def verify_reason_field_options(self, value):

        self.click_on_element(self.Reason_field_dropdown, "css")
        time.sleep(2)
        dropitems = self.get_elements(self.Reason_field_options, "xpath")
        for option in dropitems:
            option_text = option.get_attribute('textContent')
            if option_text == value:
                assert option_text == value
            break

    def verify_reason_field_default_option(self, value):
        default_option = self.driver.find_element(By.XPATH, self.default_option_in_Reason_field).get_attribute(
            "textContent")
        assert default_option == value

    def verify_facility_data_and_type(self, value):
        assert self.isElementPresent(self.facility_field, "xpath")
        assert self.isElementPresent(self.facilities_field, "xpath")
        self.click_on_element(self.facility_field_dropdown, "css")
        facility_list = self.get_elements(self.facility_field_options, "xpath")
        for option in facility_list:
            option_text = option.get_attribute('textContent')
            assert option_text in value

    def verify_facility_field_default_option(self, value):
        default_option = self.driver.find_element(By.XPATH, self.facility_field_default_option).get_attribute("textContent")
        assert default_option == value


    def verify_cost_area_adjustment_elements(self, barcode, value):
        self.click_on_element(self.bolt_menu, "id")
        self.click_on_element(self.bolt_settings_menu, "xpath")
        self.click_on_element(self.cost_area_adjustments_link, "id")
        # self.click_on_element(self.un_route, "xpath")
        assert self.isElementPresent(self.cost_area_barcode_element, "xpath")
        assert self.isElementPresent(self.cost_area_cost_area_element, "xpath")
        assert self.isElementPresent(self. cost_area_route_element, "xpath")
        assert self.isElementPresent(self.cost_area_customer_element, "xpath")
        assert self.isElementPresent(self.cost_area_address, "xpath")
        assert self.isElementPresent(self.cost_area_city, "xpath")
        assert self.isElementPresent(self.cost_area_state, "xpath")
        assert self.isElementPresent(self.cost_area_zip, "xpath")

        self.click_on_element("//a[text()='" + barcode + "']/../preceding-sibling::td/input", "xpath" )
        self.click_on_element(self.New_input_area_text_box, "xpath")
        time.sleep(10)
        self.send_keys_to(self.New_input_area_text_box, value, "xpath")
        time.sleep(2)
        self.click_on_element(self.New_input_area_option, "path")
        time.sleep(10)
        self.click_on_element(self.cost_area_submit_button, "xpath")
        self.click_on_element(self.cost_area_yes_button, "xpath")
        cost_area_adjustment_barcode = self.driver.find_element(By.XPATH, self.cost_area_barcode).get_attribute(
            "textContent")
        assert cost_area_adjustment_barcode != barcode
        time.sleep(3)
        self.click_on_element(self.cost_area_cancel_button, "xpath")
        time.sleep(6)

    def verify_cost_area_updated(self, value):
        self.click_on_element(self.package_other_tab, "xpath")
        updated_cost_area = self.driver.find_element(By.XPATH, self.updated_cost_area_in_other_tab).get_attribute(
            "textContent")
        assert updated_cost_area == value

    def select_customer_service_facility_as_package(self, value, info, base_url,
                                                    server, user, password):
        self.click_on_element(self.bolt_menu, "id")
        self.click_on_element(self.bolt_settings_menu, "xpath")
        self.click_on_element(self.mass_delay_link, "id")
        time.sleep(6)
        self.click_on_element(self.mass_delay_by_customer_radio_button, "xpath")
        self.click_on_element(self.mass_delay_select_customer, "xpath")
        time.sleep(2)
        self.send_keys_to(self.mass_delay_select_customer_input, value, "xpath")
        time.sleep(3)
        self.click_on_element(self.mass_delay_select_customer_option, "xpath")
        self.click_on_element(self.mass_delay_select_service, "xpath")
        time.sleep(2)
        self.send_keys_to(self.mass_delay_select_service_input, info, "xpath")
        time.sleep(3)
        self.click_on_element(self.mass_delay_select_service_option, "xpath")
        self.click_on_element(self.mass_delay_window, "xpath")
        self.click_on_element(self.mass_delay_submit_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.mass_delay_yes_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.mass_delay_cancel_button, "xpath")
        time.sleep(5)

        rows = DB_connection.execute_query(server, "PackageDB",
                                           user, password,
                                           "SELECT ProcessedOn, * FROM [MassDelaySchedule]WHERE CAST(CREATEDON AS "
                                           "DATE) = CAST(GETDATE() AS DATE)")

        print(len(rows))
        for row in rows:
            print(row)
        print("Waiting for 5 minutes...")
        time.sleep(300)

        rows_data = DB_connection.execute_query(server, "PackageDB", user, password,
                                                "SELECT ProcessedOn, * FROM [MassDelaySchedule]WHERE CAST(CREATEDON AS "
                                                "DATE) = CAST(GETDATE() AS DATE)")

        print(len(rows_data))
        for row in rows_data:
            print(row)
        self.driver.get(base_url)

    def verify_actual_event(self, value):
        kendo_window_event = self.driver.find_element(By.XPATH, self.mass_delay_event).get_attribute("textContent")
        assert kendo_window_event == value
        time.sleep(20)

    def verify_routes_in_dispatch_board(self):
        time.sleep(3)
        assert not self.isElementPresent(self.dispatch_route_mark_icon, "xpath")

    def verify_contractor_details(self):
        time.sleep(3)
        self.driver.find_element(By.ID, self.bolt_menu).click()
        time.sleep(3)
        assert self.isElementPresent(self.contractor_panel, "xpath")
        self.driver.find_element(By.XPATH, self.contractor_panel).click()
        assert self.isElementPresent(self.contractor_filter_deselect, "id")
        assert self.isElementPresent(self.contractor_un_assigned_routes, "xpath")
        assert self.isElementPresent(self.contractor_filter_icon, "xpath")
        assert self.isElementPresent(self.contactor_monitor, "xpath")
        assert self.isElementPresent(self.contractor_code, "xpath")
        assert self.isElementPresent(self.contractor_name, "xpath")
        assert not self.isElementPresent(self.contractor_info, "xpath")

    def verify_route_details(self):
        assert self.isElementPresent(self.route_panel, "xpath")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.route_panel).click()
        time.sleep(3)
        assert self.isElementPresent(self.route_deselect, "xpath")
        assert self.isElementPresent(self.show_empty_checkbox, "xpath")
        assert self.isElementPresent(self.route_filter, "xpath")
        assert self.isElementPresent(self.route_monitor, "xpath")
        assert self.isElementPresent(self.route_text, "xpath")
        assert self.isElementPresent(self.route_contractor, "xpath")
        assert self.isElementPresent(self.route_packages, "xpath")
        assert self.isElementPresent(self.route_stops, "xpath")
        assert not self.isElementPresent(self.route_info, "xpath")

    def verify_customer_details(self):
        time.sleep(3)
        assert self.isElementPresent(self.customer_panel, "xpath")
        self.driver.find_element(By.XPATH, self.customer_panel).click()
        time.sleep(3)
        assert self.isElementPresent(self.customer_filter, "xpath")
        assert self.isElementPresent(self.customer_name, "xpath")
        assert self.isElementPresent(self.customer_package, "xpath")
        assert self.isElementPresent(self.customer_stop, "xpath")
        assert not self.isElementPresent(self.customer_info, "xpath")

    def verify_service_details(self):
        time.sleep(2)
        assert self.isElementPresent(self.service_panel, "xpath")
        self.driver.find_element(By.XPATH, self.service_panel).click()
        time.sleep(3)
        assert self.isElementPresent(self.service_deselect_all, "xpath")
        assert self.isElementPresent(self.service_filter, "xpath")
        assert self.isElementPresent(self.service_name, "xpath")
        assert self.isElementPresent(self.service_package, "xpath")
        assert self.isElementPresent(self.service_stops, "xpath")
        assert not self.isElementPresent(self.service_info, "xpath")

    def verify_status_details(self):
        time.sleep(3)
        assert self.isElementPresent(self.status_panel, "xpath")
        self.driver.find_element(By.XPATH, self.status_panel).click()
        time.sleep(3)
        assert self.isElementPresent(self.status_deselect, "id")
        assert self.isElementPresent(self.status_filter, "xpath")
        assert self.isElementPresent(self.status_text, "xpath")

        assert self.isElementPresent(self.status_not_received_checkbox, "id")
        assert self.isElementPresent(self.status_out_for_delivery_checkbox, "id")
        assert self.isElementPresent(self.status_delivered_check_box, "id")
        assert self.isElementPresent(self.status_exception_check_box, "id")
        assert self.isElementPresent(self.status_low_quality_check_box, "id")

    def verify_bolt_menu_filter(self):
        time.sleep(3)
        self.driver.find_element(By.ID, self.bolt_menu).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.default_filter).click()

    def verify_updated_contractor(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.contractor_panel).click()
        time.sleep(2)
        assert self.isElementPresent(self.contractor_info, "xpath")

    def verify_updated_route(self):
        self.driver.find_element(By.XPATH, self.route_panel).click()
        time.sleep(2)
        assert self.isElementPresent(self.route_info, "xpath")

    def verify_updated_customer(self):
        self.driver.find_element(By.XPATH, self.customer_panel).click()
        time.sleep(2)
        assert self.isElementPresent(self.customer_info, "xpath")

    def verify_updated_service(self):
        self.driver.find_element(By.XPATH, self.service_panel).click()
        time.sleep(2)
        assert self.isElementPresent(self.service_info, "xpath")

    def verify_package_routes_in_dispatch_board(self):
        time.sleep(3)
        assert self.isElementPresent(self.dispatch_route_mark_icon, "xpath")

    def verify_routes_received_not_received(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.status_panel).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.status_not_received_checkbox).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.status_not_received_checkbox).click()
        time.sleep(2)
        assert self.isElementPresent(self.dispatch_route_mark_icon, "xpath")
