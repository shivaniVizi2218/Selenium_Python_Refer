import random
import string
import sys
import time
from idlelib import browser

from EOS_Excelcode.excel_code import ExcelTest

# sys.path.insert(1, 'c:/users/pjarubula/PycharmProjects/EPCProject')
from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from utilities.CustomLogger import custlogger
from utilities.read_write_Data_excel import Read_Write_Data
from logging import Logger
from EOS_Excelcode.read_test_data import read_EOS_values
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from eospageObjects.advance_search import eos_advance_search
from Testcases.configtest import setup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from utilities.screenshots import Screen_shots


class eos_facility_dashboard(Custom_code):
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.screen_shot = Screen_shots(self.driver)
        self.row = 0
        self.excel = ExcelTest()
        self.excel = self.excel.return_data(file_path=self.excel.get_file_path_for_excel_file('Westpalmbeach_address'))
        self.address_values = read_EOS_values()

    stp_orig = 0
    pkg_orig = 0
    short_orig = 0
    stp_value_orig = 0
    pkg_value_orig = 0
    short_value_orig = 0
    stp_exp = 0
    pkg_exp = 0
    short_exp = 0
    route_values = {}
    package_barcode = ""
    route = ""
    package_barcode2 = ""

    facility_dashboard_id = "aFacilityDashboardLink"
    facility_dashboard_xpath = "//span[.='Facility Dashboard']"
    deliveries_label_id = "dashboardTabstrip-tab-1"
    pickups_label_id = "dashboardTabstrip-tab-2"
    exceptions_label_id = "dashboardTabstrip-tab-3"
    mls_grid_xpath = "//div[@id='FacilityAggregateGrid']/table/tbody/tr/td[7]/a"
    route_dropdown_id = "ddlMovePackagesSelectReportMLS_Facility"
    move_package_id = "btnMovePackagesMLS_Facility"
    refresh_id = "btnRefreshDashboardValues"
    pickup_refresh_id = "btnRefreshPage"
    export_button_id = "btnExportDashboard"
    print_button_id = "btnPrintDashboard"
    contractor_radio_id = "radioDashboardByContractor"
    route_radio_id = "radioDashboardByRoute"
    customer_radio_id = "radioDashboardByCustomer"
    service_radio_id = "radioDashboardByService"
    pickups_customer_radio_button = "radioPickupsByCustomer"
    pickups_service_radio_button = "radioPickupsByService"
    exceptions_tab_contractor_id = "radioExceptionsByContractor"
    exceptions_tab_route_id = "radioExceptionsByRoute"
    exceptions_tab_customer_id = "radioExceptionsByCustomer"
    exceptions_tab_service_id = "radioExceptionsByService"
    toggle_bar_xpath = "//i[@class='fas fa-bars']"
    set_as_landing_page_xpath = "//ul[@id='leftSideContextMenu']/li[2]/span"
    dispatcher_name_id = "dispatcherNameMain"
    settings_button_id = "btnProfileUSerSettings"
    landing_page_xpath = "//div[@id='userSettingsWindow']/div/div[2]/span"
    save_settings_button_id = "btnUserSettingsSave"
    # package_entry_id = "aPackageEntryDashboardLink"
    cust_drop_down_xpath = "//div[@id='divWrapper']/ul[1]/li[3]/ul/li[2]/span"
    generate_button_id = "btnPeGenerateBarcode"
    validate_button_id = "btnPeValidateFormTop"
    package_type_drop_down_xpath = "//div[@id='divWrapper']/ul[1]/li[4]/ul[1]/li[2]/span"
    look_up_address_xpath = "//ul[@id='ulPeAddressDest']/li[1]/div[2]/button"
    address1_id = "txtScrubAddress"
    city_id = "txtScrubCity"
    state_drop_down_id = "ddlScrubState"
    zipcode_id = "txtScrubZip"
    validate2_button_id = "btnScrubAddressValidate"
    stop_name_id = "txtPeStopNameDest"
    add_package_id = "btnPeAddPackage"
    submit_button_id = "btnSubmitRtsFtb"
    submit_packages_id = "btnPeSubmitPackage"
    route_id = "ddlPeRoute"
    search_id = "searchMapText"
    route_manager_id = "aRouteManagerDashboardLink"
    package_input_xpath = "//div[@class='k-filter-menu-container']/span[2]/input[1]"
    drilldown_exception = "//div[@data-gridid='pickupDashboardAggregateGrid']//table//tbody//tr//td[7]/a"
    attempt_exception = "//div[@data-gridid='pickupDashboardAggregateGrid']//table//tbody//tr//td[6]/a"
    deliveries_tab_attempt = "//div[@id='FacilityAggregateGrid']//table//tbody//tr//td[11]/a"
    deliveries_tab_exception = "//div[@id='FacilityAggregateGrid']//table//tbody//tr//td[12]/a"
    barcode_search_field_exception = "txtSearchException_Facility"
    barcode_search_field_attempt = "txtSearchAttempted_Facility"
    # package_entry_id = "aPackageEntryDashboardLink"
    customer_ddl_button = "//*[contains(@aria-owns, 'ddlPeCustomerFormTop_listbox') and contains(@aria-labelledby, 'ddlPeCustomerFormTop_label')]//button"
    customer_ddl_ul_list = "//*[@id='ddlPeCustomerFormTop_listbox']"
    generate = "btnPeGenerateBarcode"
    validate = "btnPeValidateFormTop"
    cancel = "btnPeCancel"
    lock_form_checkbox = "cbPeLockInitialForm"
    package_image = "//*[@src='/Content/images/package_future.png']"
    package_entry = "// a[contains(text(), 'Package Entry')]"
    calendar_icon = "//*[@aria-controls='txtPeDeliveryDateFormTop_dateview']"
    address_look_up = "//*[@id='ulPeAddressOrig']/li[1]/div[2]/button"
    address_look_up1 = "//ul[@id='ulPeAddressDest']/li[1]/div[2]/button"
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
    stop_name = "txtPeStopNameOrig"
    stop_name1 = "txtPeStopNameDest"
    btnPeSubmitPackage = "btnPeSubmitPackage"
    btnPeAddPackage = "//*[@id='btnPeAddPackage']"
    get_barcode = "//*[@style='white-space: nowrap;']"
    get_barcode_id = "txtPeBarcode"

    package_type_button = "//*[contains(@aria-owns, 'ddlPePackageType_listbox') and contains(@aria-controls, 'ddlPePackageType_listbox')]//button"
    package_type_ul_list = "//*[contains(@id, 'ddlPePackageType_listbox')]"
    # service_type_button = "//*[contains(@aria-owns, 'ddlPeService_listbox') and contains(@aria-controls, 'ddlPeService_listbox')]//button"
    service_type_button = "//div[@id='divWrapper']/ul[1]/li[4]/ul[2]/li[1]/span[1]"
    service_type_ul_list = "//*[contains(@id, 'ddlPeService_listbox')]"

    return_to_sender_radio = "rbPkgEntryRts"
    submit_button = "btnSubmitRtsFtb"

    customer_name_read = "//*[@aria-owns='ddlPeCustomerFormTop_listbox']//span//span"
    barcode_field_xpath = "txtPeBarcodeFormTop"
    search_map_id = "searchMapText"
    advance_search_menu_id = "aAdvancedSearchDashboardLink"
    advance_search_field_id = "txtSearchTxt"
    search_type_dropdown = "ddlSearchType"
    search_button_id = "btnAdvancedSearch"
    clear_search_button_id = "btnClearAdvancedSearch"
    search_facilities_id = "cbSearchAllFacilities"
    today_only = "cbSearchTodayOnly"
    search_dropdown_id = "ddlSearchType"
    search_all_facilities = "cbSearchAllFacilities"
    package_route_xpath = "//div[@id='AdvancedSearchGrid']/div[2]/table/tbody/tr/td[5]/a"
    barcode_xpath = "//div[@id='AdvancedSearchGrid']/div[2]/table/tbody/tr/td[1]/a"

    package_entry_id = "liPackageEntryDashboardLink"
    status_dropdown = "//*[contains(@id, 'packageStatus')]/div[2]/span[2]/button"
    # drop_dropdown = "//*[contains( @id, 'deliveryDetailsDrop')]/span[2]/button"
    statusCodeName = "//*[contains(@id, 'statusCodeName')]"
    attempt_drop_down_xpath = "//*[contains(@id, 'exceptionDetails')]/div/div[1]/span[2]/button"

    onhold_total = "//*[@id='FacilityAggregateGrid']/table/tbody/tr/td[13]/a"
    onhold_total1 = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[8]/a"

    barcode_res = "//a[@class='clickable viewPackageDetail']"
    verify_code = "//div[@class='inlineB']/strong"
    status_change = "//i[@class='fas fa-pencil-alt iconHover']"
    exeption_status = "//*[contains(@id,'editPackageStatus')]/li//span[text()='Exception']"
    exception_drpdwn = "//*[contains(@id, 'exceptionDetails')]/div[1]//span[2]/button[1]"
    exception_searchBar = "(//*[contains(@aria-controls,'exceptionDropDown')])[2]"
    lasership_data = "//ul[contains(@id,'exceptionDropDown')]"
    save_btn = "//button[contains(@id,'savePackageStatus')]"
    close_btn = "//a[@aria-label='Close']"
    on_hold_reportTab = "//span[@id='exDashDrilldown_OnHold_Facility_wnd_title']/div"
    barcode_res1 = "//*[@id='exceptionDashboardDrilldown_OnHold_Facility']/div[2]/table/tbody/tr[1]/td[2]/a"
    events_tab = "//*[contains(@id,'packageDetailTabstrip')]/div/ul/li[1]/span[2]"
    status_change1 = "//i[@class='fas fa-pencil-alt iconHover']"
    drop_dropdown1 = "(//*[contains(@id,'packageStatus')]/div[2]/span[2]/button)[1]"
    exeption_status1 = "//*[contains(@id,'editPackageStatus')]/li[2]"
    exception_drpdwn1 = "//*[contains(@id,'exceptionDetails')]/div/div[1]/span[2]/button"
    exception_statusTxt1 = "//*[contains(@id,'exceptionDropDown')]/li[1]/span"
    exception_statusTxt2 = "//*[contains(@id,'exceptionDropDown')]/li[2]/span"
    exception_statusTxt3 = "//*[contains(@id,'exceptionDropDown')]/li[3]/span"
    text_searchonhold_facility = "txtSearchExceptionOnHold_Facility"
    onhold_facility_checkbox1 = "(//input[contains(@id,'chkReportSelectionOnHold_Facility')])[position()=1]"
    onhold_facility_checkbox2 = "(//input[contains(@id,'chkReportSelectionOnHold_Facility')])[position()=2]"
    onhold_facility_checkbox3 = "(//input[contains(@id,'chkReportSelectionOnHold_Facility')])[position()=3]"
    apply_event_btn = "btnApplyEventExceptionDrilldownOnHold_Facility"
    select_event_arrow = "//div[@id='exApplyEvent_OnHold_Facility']/descendant::div[2]/span/button"
    exceed_on_hold_days_discard = "//option[contains(text(),'Exceeded On Hold Days, Discard')]"
    exceed_on_hold_days_rts = "//span[contains(text(),'Exceeded On-Hold Days, RTS')]"
    lost_by_laserShip = "//span[contains(text(),'Item has been lost by LaserShip')]"
    remove_from_onhold = "//span[contains(text(),'Removed From On Hold')]"

    status_update = "//button[contains(@id,'btnStatusUpdate')]"
    master_row_top = "//*[contains(@id,'statusGrid')]/table/tbody/descendant::tr[1]/descendant::td[1]/a"
    time_picker = "//div[@data-gridid='StatusUpdateGrid']/descendant::tbody/tr[1]/td[3]/descendant::button"
    time_picker_field = "(//input[contains(@id,'timePicker')])[1]"
    time_picker_dropdown = "//*[@id='timePicker_178397725_option_selected']/span"
    drop_down_carat = "//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/descendant::td[4]/span/button"
    route_link = "//div[@id='AdvancedSearchGrid']/div[2]/descendant::table/descendant::td[5]/a"
    drop_down_val = "(//span[text()='DESK'])[1]"
    signature_txt = "(//input[contains(@id,'signature')])[position()=1]"
    status_update_icon = "//button[contains(@id,'btnStatusUpdate')]"
    # master header Status
    sequence_txt = "(//span[contains(text(),'Seq')])[position()=2]"
    time_txt = "//span[contains(text(),'Time')]"
    drop_txt = "//span[contains(text(),'Drop')]"
    signature_Txt = "//span[contains(text(),'Signature')]"
    picked_up_txt = "(//span[contains(text(),'Picked Up')])[position()=2]"
    exceptionTyp_txt = "//span[contains(text(),'Exception Type')]"
    exception_txt = "(//thead[@class='k-grid-header'])[4]//descendant::th[8]//span[contains(text(),'Exception')]"
    door_tag = "//span[contains(text(),'Door Tag')]"
    edd_txt = "(//span[contains(text(),'EDD')])[position()=2]"
    stop_name_txt = "(//span[contains(text(),'Stop Name')])[position()=1]"
    address_txt = "(//thead[@class='k-grid-header'])[4]/descendant::th[12]/descendant::span[contains(text(),'Address')]"
    hash_txt = "(//thead[@class='k-grid-header'])[4]/descendant::th[13]/descendant::span[contains(text(),'#')]"
    status_txt = "(//span[contains(text(),'Status')])[6]"
    cust_route_txt = "(//span[contains(text(),'Cust Route')])[2]"
    cust_stop_txt = "(//span[contains(text(),'Cust Stop')])[2]"
    service_txt = "(//thead[@class='k-grid-header'])[4]/descendant::th[18]/descendant::span[contains(text(),'Service')]"
    show_POD_checkbox = "chkShowPODStatuses"
    show_exception_checkbox = "chkShowExceptionStatuses"
    # child header status
    time_status_txt = "(//thead[@class='k-grid-header'])[5]//tr/th[contains(text(),'Time')]"
    drop_status_txt = "//th[contains(text(),'Drop')]"
    signature_status_txt = "//th[contains(text(),'Signature')]"
    picked_up_status_txt = "//th[contains(text(),'Picked Up')]"
    exception_type_txt = "//th[contains(text(),'Exception Type')]"
    exception_status_txt = "(//th[contains(text(),'Exception')])[2]"
    door_tag_txt = "//th[contains(text(),'Door Tag')]"
    edd_status_txt = "//th[contains(text(),'EDD')]"
    barcode_status_txt = "(//thead[@class='k-grid-header'])[5]/descendant::tr/th[contains(text(),'Barcode')]"
    status_txt_type = "(//thead[@class='k-grid-header'])[5]/descendant::tr/th[contains(text(),'Status')]"
    cust_route_status = "(//thead[@class='k-grid-header'])[5]/descendant::tr/th[contains(text(),'Cust Route')]"
    cust_stop_status = "(//thead[@class='k-grid-header'])[5]/descendant::tr/th[contains(text(),'Cust Stop')]"
    service_status_txt = "(//thead[@class='k-grid-header'])[5]/descendant::tr/th[contains(text(),'Service')]"
    master_body = "(//div[contains(@class,'statusUpdatGrid')]/descendant::tr)[2]"
    # master status text values
    master_time_text_val = "//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/descendant::input[1]"
    master_drop_down_txt_val = "//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/td[4]/descendant::span[3]"
    master_signature_txt_val = "//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/td[5]/descendant::input"
    # child satus text values
    child_time_text_val = "//div[@data-gridid='StatusUpdateChildGrid']/descendant::tbody/descendant::tr[1]/descendant::input[1]"
    child_drop_down_txt_val1 = "//div[@data-gridid='StatusUpdateChildGrid']/descendant::tbody/tr[1]/td[2]/descendant::span[3]"
    child_drop_down_txt_val = "(//div[@data-gridid='StatusUpdateChildGrid']/descendant::span[contains(@class,'statusUpdateDropdown')]/descendant::span[text()='DESK'])[1]"
    child_signature_txt_val = "//div[@data-gridid='StatusUpdateChildGrid']/descendant::tbody/tr[1]/td[3]/descendant::input"

    # exception_carat_button = "(//div[@data-gridid='StatusUpdateChildGrid']/descendant::tbody/tr[1]/td[6]/descendant::button)[1]"
    exception_carat_button = "(//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/td[8]/descendant::button)[1]"
    search_box = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::input"
    # Exception Drop Down Vals
    delay_natural_disaster = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Delay due to weather or natural disaster')]"
    delay_external_factors = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Delay in service due to external factors')]"
    exceed_discarded = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Delay in service due to external factors')]"
    exceed_rts = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Exceeded max attempts, RTS')]"
    item_damaged_delivered = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Item damaged and will be delivered')]"
    item_damaged_discarded = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Item damaged and will be discarded')]"
    item_damaged_returned = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Item damaged and will be returned')]"
    item_lost_laser = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Item has been lost by LaserShip')]"
    late_line_haul = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Late Line Haul')]"
    left_on_dock = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Late Line Haul')]"
    mechanical_break_down = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Mechanical Breakdown Will Impact Delivery')]"
    on_hold_laser = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'On Hold at LaserShip')]"
    return_request_customer_shipper = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'On Hold at LaserShip')]"

    exception_type_carat_button = "//div[@data-gridid='StatusUpdateGrid']/table/tbody/descendant::tr[1]/td[7]/descendant::button"
    exception_attempt_drop_down = "(//li[@role='option']/span[text()='Attempt'])[1]"
    # exception Drop down
    already_picked_up = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Already Picked Up']"
    need_more_info = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Need More Information']"
    recipient_refuse_damage = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Recipient refused as damaged']"
    recipient_refuse_delivery = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Recipient refused delivery']"
    secure_building_no_access = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Secure Building No Access']"
    unable_to_leave_parcel = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[text()='Unable to Leave Parcel']"
    delivery_column_link = "(//a[@data-reporttype='Delivered'])[1]"
    facility_search = "txtSearchDelivered_Facility"
    mechanical_break_down_txt = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Mechanical Breakdown Will Impact Delivery')]"
    master_attempt_status = "//div[@data-gridid='StatusUpdateGrid']/descendant::tbody/tr[1]/td[7]/descendant::span[text()='Attempt']"
    child_attempt_status = "(//div[@data-gridid='StatusUpdateChildGrid']/descendant::tbody/descendant::span[text()='Attempt'])[1]"
    picked_up_check_box = "//div[@data-gridid='StatusUpdateGrid']/descendant::tbody/tr[1]/td[6]/input[contains(@id,'pickedUp_')]"
    business_closed_status = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Business Closed')]"
    customer_kept_return_status = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Customer Kept Return')]"
    return_unavailable_pickup = "//div[@class='k-popup k-group k-reset k-state-border-up']/descendant::div[@class='k-list-content k-list-scroller']/descendant::li/span[contains(text(),'Return unavailable for Pickup')]"
    days_on_hold_header = "//span[text()='Days on Hold']"
    days_on_hold_text_bef = "//div[@id='exceptionDashboardDrilldown_OnHold_Facility']/div[2]/descendant::table/tbody/descendant::tr[1]/td[14]"
    days_on_hold_text_after = "//div[@id='exceptionDashboardDrilldown_OnHold_Facility']/div[2]/descendant::table/tbody/descendant::tr[1]/td[14]"
    maximize_window_btn = "[aria-label='window-Maximize']"
    damage_delivery_col = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[4]/a"
    damage_discard_col = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[5]/a"
    damage_return_col = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[6]/a"
    rts_col = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[9]/a"
    lost_col = "//*[contains(@id,'ExceptionAggregateGrid')]/table/tbody/tr/td[10]/a"
    exception_drill_down_grid1 = "(//div[@id='ExceptionDrillDownGrid']/descendant::tbody/tr[1]/descendant::td[@class='rightText']/a)[1]"
    exception_drill_down_grid2 = "(//div[@id='ExceptionDrillDownGrid']/descendant::tbody/tr[1]/descendant::td[@class='rightText']/a)[2]"
    exception_search_txt = "txtExceptionSearch"
    exception_route_link = "//*[@id='ExceptionDrillDownGrid']/div[2]/descendant::table/descendant::tbody/tr/descendant::td[5]/a"
    green_status_bar = "//div[@class='statusBar greenStatus']"
    route_tab_expand1 = "(//a[@aria-label='Expand'])[1]"
    exception_by_route = "radioExceptionsByRoute"
    route_tab_barcode = "//div[contains(@id,'RouteDataList_Child')]/table/tbody/descendant::tr[1]/descendant::td[1]/a"
    grid_refresh_btn = "btnRefreshExceptionValues"
    facility_damage_del_txt = "//div[text()='Facility DamageDelivered Report']"
    facility_discard_del_txt = "//div[text()='Facility DamageDiscard Report']"
    facility_return_del_txt = "//div[text()='Facility DamageReturn Report']"
    facility_lost_del_txt = "//div[text()='Facility Lost Report']"
    facility_rts_del_txt = "//div[text()='Facility RTS Report']"
    button_clear_search = "btnClearExceptionSearch"
    drop_down_status_arrow = "//span[contains(@aria-owns,'dropLocationDropDown')]/descendant::button[1]"
    drop_down_status_text = "//div[contains(@id,'dropLocationDropDown')]/descendant::ul[1]/descendant::li[1]/span"
    #window_maximize = "(//a[@aria-label='window-Maximize'])[3]"


    def click_on_facility_dashboard(self):
        self.click_on_element(self.facility_dashboard_id)

    def randombarcode(self, length=20):
        letters = string.ascii_lowercase
        # return_str = ''.join(random.choice(letters, length))
        self.package_barcode2 = ''.join((random.choice(letters) for i in range(length)))
        print(self.package_barcode2)

    def click_on_package_route(self):
        self.click_on_element(self.package_route_xpath, locator_type="xpath")

    def click_on_dashboard(self):
        self.click_on_element(self.facility_dashboard_xpath, locator_type="xpath")

    def click_on_advance_search(self):
        self.click_on_element(self.advance_search_menu_id)

    def click_on_deliveries_label(self):
        # self.isElementPresent(self.deliveries_label_id)
        # time.sleep(1)
        # self.driver.execute_script("document.getElementById('dashboardTabstrip-tab-1').click()")
        self.ElementPresent_and_click(self.deliveries_label_id)

    def click_on_pickups_label(self):
        self.driver.execute_script("document.getElementById('dashboardTabstrip-tab-2').click()")
        # self.ElementPresent_and_click(self.pickups_label_id)

    def click_on_exceptions_label(self):
        self.driver.execute_script("document.getElementById('dashboardTabstrip-tab-3').click()")
        # self.ElementPresent_and_click(self.exceptions_label_id)

    def click_on_route_dropdown(self):
        self.driver.execute_script("document.getElementById('ddlMovePackagesSelectReportMLS_Facility').click()")

    def click_on_attempt_drp_down(self):
        self.click_on_element(self.attempt_drop_down_xpath, locator_type="xpath")

    def click_on_move_package(self):
        self.click_on_element(self.move_package_id)

    def click_on_status_drop_down(self):
        status_drop_down = self.driver.find_element(By.XPATH,
                                                    "//*[contains(@id, 'packageStatus')]/div[2]/span[2]/button")

        status_drop_down.click()

    def click_on_drop_drop_down(self):
        drop_drop_down = self.driver.find_element(By.XPATH,
                                                  "//*[contains( @id, 'deliveryDetailsDrop')]/span[2]/button")
        drop_drop_down.click()

    def verify_status_drop_down_values(self, status):
        drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div/ul")
        list_values = drop_down.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(list_values, status)
        print(len(list_values))
        # print(100/0)

    def verify_delivered_status_drop_down_values(self, status):
        drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'dropLocationDropDown')]/div/ul")
        list_values = drop_down.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(list_values, status)
        print(len(list_values))
        # print(100/0)

    def change_the_status_to_out_for_delivery(self, status):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div[2]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(list_values1, status)
        print(len(list_values1))

    def select_attempt_reason(self, attempt):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'exceptionDropDown')]/div[3]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(list_values1, attempt)
        print(len(list_values1))

    def verify_picked_up_values(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        if list_values1[0].text == "Returning" and list_values1[1].text == "Exception":
            assert True
        else:
            assert False

        print(len(list_values1))
        print(list_values1[1].text)

        # print(100/0)

    def verify_out_for_pickup_values(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div[2]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        out_for_pickup_drop_down_values = ["Out For Pickup", "Picked Up", "Attempt", "Exception"]
        pickvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print(list_value.text)
            print(out_for_pickup_drop_down_values[j])
            if list_value.text == out_for_pickup_drop_down_values[j]:
                pickvalues_matched = "Y"
            else:
                pickvalues_matched = "N"
                break
            j = j + 1
        print(pickvalues_matched)

    def verify_attempt_status_values(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'exceptionDropDown')]/div[3]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        attempt_drop_down_values = ["Already Picked Up", "Business Closed", "Customer Kept Return",
                                    "Need More Information", "Return unavailable for Pickup",
                                    "Secure Building No Access"]
        print("test12121")
        print(len(list_values1))
        attemptvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print(list_value.text)
            print(attempt_drop_down_values[j])
            if list_value.text == attempt_drop_down_values[j]:
                attemptvalues_matched = "Y"
            else:
                attemptvalues_matched = "N"
                assert False
                # break
            j = j + 1
        print(attemptvalues_matched)
        # print(100/0)

    def verify_attempt_status_values1(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'exceptionDropDown')]/div[3]/ul/li")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "span")
        attempt_drop_down_values = ["Business Closed",
                                    "Need More Information",
                                    "Recipient refused as damaged",
                                    "Recipient refused delivery"
                                    "Secure Building No Access",
                                    "Unable to Leave Parcel"]
        print("test12121")
        print(len(list_values1))
        attemptvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print("listvals:" + list_value.text)
            print("dropdownvals:" + attempt_drop_down_values[j])
            if list_value.text == attempt_drop_down_values[j]:
                attemptvalues_matched = "Y"
            else:
                attemptvalues_matched = "N"
                assert False
                # break
            j = j + 1
        print(attemptvalues_matched)
        # print(100/0)

    def verify_exception_status_values(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'exceptionDropDown')]/div[3]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        exception_drop_down_values = ["Delay due to weather or natural disaster",
                                      "Delay in service due to external factors", "Exceeded max attempts, discarded",
                                      "Exceeded max attempts, RTS", "Item damaged and will be delivered",
                                      "Item damaged and will be discarded",
                                      "Item damaged and will be returned", "Item has been lost by LaserShip",
                                      "Late Line Haul", "Left on Dock - will not attempt",
                                      "Mechanical Breakdown Will Impact Delivery", "On Hold at LaserShip",
                                      "Return requested by customer/shipper"]
        print("test12121")
        print(len(list_values1))
        exceptionvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print(list_value.text)
            print(exception_drop_down_values[j])
            if list_value.text == exception_drop_down_values[j]:
                exceptionvalues_matched = "Y"
            else:
                exceptionvalues_matched = "N"
                assert False
                # break
            j = j + 1
        print(exceptionvalues_matched)

    def verify_pick_up_values(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div[2]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        pickup_drop_down_values = ["Pickup", "Out For Pickup", "Picked Up", "Attempt", "Exception"]
        pickvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print(list_value.text)
            print(pickup_drop_down_values[j])
            if list_value.text == pickup_drop_down_values[j]:
                pickvalues_matched = "Y"
            else:
                pickvalues_matched = "N"
                break
            j = j + 1
        print(pickvalues_matched)
        self.change_the_status_to_out_for_delivery(status="Out For Pickup")
        time.sleep(3)
        self.click_on_save_button()
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(2)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.verify_out_for_pickup_values()
        time.sleep(2)
        self.change_the_status_to_out_for_delivery(status="Attempt")
        time.sleep(2)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.select_attempt_reason(attempt="Business Closed")
        time.sleep(2)
        self.click_on_save_button()
        time.sleep(2)
        # self.click_on_close_button1()
        # time.sleep(2)
        self.click_on_pickup_refresh_grid()
        time.sleep(2)

    def verify_pick_up_values_and_change_the_status_to_exception(self):
        status_drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div[2]/ul")
        list_values1 = status_drop_down.find_elements(By.TAG_NAME, "li")
        pickup_drop_down_values = ["Pickup", "Out For Pickup", "Picked Up", "Attempt", "Exception"]
        pickvalues_matched = "N"
        j = 0
        for list_value in list_values1:
            print(list_value.text)
            print(pickup_drop_down_values[j])
            if list_value.text == pickup_drop_down_values[j]:
                pickvalues_matched = "Y"
            else:
                pickvalues_matched = "N"
                break
            j = j + 1
        print(pickvalues_matched)
        self.change_the_status_to_out_for_delivery(status="Exception")
        time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.select_attempt_reason(attempt="Delay due to weather or natural disaster")
        time.sleep(2)
        self.click_on_save_button()
        time.sleep(2)
        # self.click_on_close_button1()
        # time.sleep(2)
        self.click_on_pickup_refresh_grid()
        time.sleep(5)

    def verify_delivered_status_values(self):
        drop_down = self.driver.find_element(By.XPATH, "//*[contains(@id, 'editPackageStatus')]/div/ul")
        list_values2 = drop_down.find_elements(By.TAG_NAME, "li")
        if list_values2[0].text == "Delivered" and list_values2[1].text == "Exception":
            assert True
        else:
            assert False

    def click_on_save_button(self):
        save_button = self.driver.find_element(By.XPATH, "//*[contains(@id, 'savePackageStatus')]")
        save_button.click()

    def select_route_value_from_drop_down(self, route_values):
        # route_list = self.driver.find_element_by_id("ddlMovePackagesSelectReportMLS_Facility_listbox")
        # route_items = route_list.find_elements_by_tag_name("li")
        route_list = self.driver.find_element(By.ID, "ddlMovePackagesSelectReportMLS_Facility_listbox")
        route_items = route_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(route_items, value=route_values)

    def click_on_refresh_grid(self):
        self.click_on_element(self.refresh_id)

    def click_on_pickup_refresh_grid(self):
        self.click_on_element(self.pickup_refresh_id)

    def click_on_export_button(self):
        self.click_on_element(self.export_button_id)

    def click_on_print_button(self):
        self.click_on_element(self.print_button_id)

    def click_on_mls_grid(self):
        self.click_on_element(self.mls_grid_xpath, locator_type="xpath")
        time.sleep(2)
        # check = self.driver.find_elements(By.XPATH, "//div[@id='dashboardDrilldown_MLS_Facility']"
        #                                            "/div[2]/table/tbody/tr/td[1]")
        # print(len(check))
        # checkboxes = self.driver.execute_script("document.getElementsByClassName('cb_MLS_FacilitycheckForShiftDrilldown')")
        # checkbox1 = self.driver.find_element_by_xpath(
        #     "//div[@id='dashboardDrilldown_MLS_Facility']/div[2]/table/tbody/tr/td[1]")
        checkbox1 = self.driver.find_element(By.XPATH,
                                             "//div[@id='dashboardDrilldown_MLS_Facility']/div[2]/table/tbody/tr/td[1]")
        checkbox1.click()
        # checkbox2 = self.driver.find_element_by_xpath("//div[@id='dashboardDrilldown_MLS_Facility']"
        #                                               "/div[2]/table/tbody/tr[2]/td[1]")
        checkbox2 = self.driver.find_element(By.XPATH, "//div[@id='dashboardDrilldown_MLS_Facility']"
                                                       "/div[2]/table/tbody/tr[2]/td[1]")
        checkbox2.click()
        # checkbox3 = self.driver.find_element_by_xpath("//div[@id='dashboardDrilldown_MLS_Facility']"
        #                                               "/div[2]/table/tbody/tr[3]/td[1]")
        checkbox3 = self.driver.find_element(By.XPATH, "//div[@id='dashboardDrilldown_MLS_Facility']"
                                                       "/div[2]/table/tbody/tr[3]/td[1]")
        checkbox3.click()
        time.sleep(2)
        self.click_on_route_dropdown()
        time.sleep(5)
        self.select_route_value_from_drop_down(route_values="000")
        time.sleep(5)
        self.click_on_move_package()
        time.sleep(2)
        test = self.driver.execute_script("document.getElementsByClassName('divNotification')[0].innerText")
        if test != "Packages Moved Successfully to Route 000":
            assert True
        else:
            print("test passed")
            assert False

    def verify_STP_column(self):
        table = self.driver.find_element(By.ID, 'FacilityAggregateGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")

        header_lables = ["STP", "PKG", "SHORT", "REC", "RTBD", "LOAD", "MLS", "OFD", "DEL",
                         "MAN", "ATT", "NMI", "EXC", "REDEL", "%"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            # print(len(head_count))
            j = 0
            for headers in head_count:
                # print(headers.text)
                if headers.text == header_lables[j]:
                    test_results = "T"
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False
                j = j + 1
            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_facility_drill_down_grid(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["IC", "NAME", "RTE", "STP", "PKG", "SHORT", "REC", "RTBD", "LOAD",
                         "MLS", "OFD", "DEL", "MAN", "ATT", "EXC", "REDEL", "LBS", "EVENT", "DUE", "%", "COMP",
                         "VEND", "TYPE", "NMI"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_delivery_by_route_grid(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["IC", "NAME", "RTE", "STP", "PKG", "SHORT", "REC", "RTBD", "LOAD",
                         "MLS", "OFD", "DEL", "MAN", "ATT", "EXC", "REDEL", "LBS", "EVENT", "DUE", "%", "COMP",
                         "VEND", "TYPE", "NMI"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == "":
                    print(headers.text + ":is empty")
                elif headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def filter_by_route_value(self):

        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        header_lables = ["RTE"]
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # print(rows)
        # cells = table.find_elements_by_tag_name("td")
        cells = table.find_elements(By.TAG_NAME, "td")
        # print(cells)
        for cell in cells:
            # print(cell.text)
            # if cell == "WPB25":
            #     cell.click()
            # td_links = cell.find_elements_by_tag_name("a")
            td_links = cell.find_elements(By.TAG_NAME, "a")
            # print("My hubby is Awesome")
            # print(len(td_links))
            for tdlink in td_links:
                if tdlink.text == self.route_values[0]:
                    # print(tdlink.text)
                    tdlink.click()
                    time.sleep(5)

    def filter_by_route_value_for_values_validation(self):
        route_id_lbl = "RTE"
        pickup_id_lbl = "PU"
        route_id = 0
        pickup_id = 0
        i = 0
        table = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == route_id_lbl:
                route_id = i
            if header.text == pickup_id_lbl:
                pickup_id = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        is_route_row = "N"
        is_pu_click = "N"
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.route in col.text:
                    print("route id found")
                    is_route_row = "Y"
                    # pu_links = col.find_elements(By.TAG_NAME, 'a')

                if j == pickup_id and is_route_row == "Y":
                    print("PU column found")
                    pu_links = col.find_elements(By.TAG_NAME, 'a')
                    for pu_link in pu_links:
                        pu_link.click()
                        is_pu_click = "Y"
                        break
                j = j + 1
            if is_pu_click == "Y":
                break

            # print(self.route)
            # print(cols[route_id].text)

    def click_onhold_hyperlink(self):
        # route_id_lbl = "RTE"
        # pickup_id_lbl = "PU"
        onhold_id_lbl = "On Hold"
        route_id = 0
        pickup_id = 0
        onhold_id = 0
        i = 0
        table = self.driver.find_element(By.XPATH, "//div[@id='ExceptionAggregateGrid']")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            print(header.text)
            # print(100/0)
            # if header.text == onhold_id_lbl:
            #     route_id = i
            if header.text == onhold_id_lbl:
                onhold_id = i
            i = i + 1
        print(onhold_id)
        table1 = self.driver.find_element(By.XPATH, "//div[@id='ExceptionAggregateGrid']/table/tbody")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        # is_route_row = "N"
        is_onhold_click = "N"
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)

                if j == onhold_id:
                    print("PU column found")
                    onhold_links = col.find_elements(By.TAG_NAME, 'a')
                    for onhold_link in onhold_links:
                        onhold_link.click()
                        is_onhold_click = "Y"
                        break
                j = j + 1
            if is_onhold_click == "Y":
                break

    def filter_by_route_value_for_attempt_values_validation(self):
        route_id_lbl = "RTE"
        attempt_id_lbl = "ATT"
        route_id = 0
        attemp_id = 0
        i = 0
        table = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == route_id_lbl:
                route_id = i
            if header.text == attempt_id_lbl:
                attemp_id = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        is_route_row = "N"
        is_attempt_click = "N"
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.route in col.text:
                    print("route id found")
                    is_route_row = "Y"
                    # pu_links = col.find_elements(By.TAG_NAME, 'a')

                if j == attemp_id and is_route_row == "Y":
                    print("PU column found")
                    pu_links = col.find_elements(By.TAG_NAME, 'a')
                    for pu_link in pu_links:
                        pu_link.click()
                        is_attempt_click = "Y"
                        break
                j = j + 1
            if is_attempt_click == "Y":
                break

    def filter_by_route_value_for_package_values_validation(self):
        route_id_lbl = "RTE"
        package_id_lbl = "PKG"
        route_id = 0
        package_id = 0
        i = 0
        table = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == route_id_lbl:
                route_id = i
            if header.text == package_id_lbl:
                package_id = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        is_route_row = "N"
        is_package_click = "N"
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.route in col.text:
                    print("route id found")
                    is_route_row = "Y"
                    # pu_links = col.find_elements(By.TAG_NAME, 'a')

                if j == package_id and is_route_row == "Y":
                    print("PU column found")
                    pu_links = col.find_elements(By.TAG_NAME, 'a')
                    for pu_link in pu_links:
                        pu_link.click()
                        is_package_click = "Y"
                        break
                j = j + 1
            if is_package_click == "Y":
                break

    def filter_by_route_value_for_exception_values_validation(self):
        route_id_lbl = "RTE"
        exc_id_lbl = "EXC"
        route_id = 0
        exc_id = 0
        i = 0
        table = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == route_id_lbl:
                route_id = i
            if header.text == exc_id_lbl:
                exc_id = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH, "//div[@id='PickupDrillDownGrid']/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        is_route_row = "N"
        is_exc_click = "N"
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.route in col.text:
                    print("route id found")
                    is_route_row = "Y"
                    # pu_links = col.find_elements(By.TAG_NAME, 'a')

                if j == exc_id and is_route_row == "Y":
                    print("PU column found")
                    pu_links = col.find_elements(By.TAG_NAME, 'a')
                    for pu_link in pu_links:
                        pu_link.click()
                        is_exc_click = "Y"
                        break
                j = j + 1
            if is_exc_click == "Y":
                break

    def filter_by_barcode_and_click_on_barcode(self):
        barcode_value = ""
        is_barcode_click = ""
        i = 0
        table = self.driver.find_element(By.XPATH, "//*[contains(@id, 'dashboardDrilldown_Pickup_Contractor')]/div[1]")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == "Barcode":
                barcode_value = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH,
                                          "//*[contains(@id,  'dashboardDrilldown_Pickup_Contractor')]/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.package_barcode == col.text:
                    # print("Barcode id found")
                    barcode_links = col.find_elements(By.TAG_NAME, 'a')
                    for barcode_link in barcode_links:
                        barcode_link.click()
                        is_barcode_click = "Y"
                        break
                j = j + 1
                if is_barcode_click == "Y":
                    break
            if is_barcode_click == "Y":
                break

            # print(self.route)
            # print(cols[route_id].text)

        # print(100 / 0)

    def package_filter_by_barcode_and_click_on_barcode(self):
        barcode_value = ""
        is_barcode_click = ""
        i = 0
        table = self.driver.find_element(By.XPATH,
                                         "//*[contains(@id, 'facDashDrilldown_Packages_Contractor')]/div[1]")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == "Barcode":
                barcode_value = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH,
                                          "//*[contains(@id, 'facDashDrilldown_Packages_Contractor')]/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.package_barcode == col.text:
                    # print("Barcode id found")
                    barcode_links = col.find_elements(By.TAG_NAME, 'a')
                    for barcode_link in barcode_links:
                        barcode_link.click()
                        is_barcode_click = "Y"
                        break
                j = j + 1
                if is_barcode_click == "Y":
                    break
            if is_barcode_click == "Y":
                break

    def attemp_filter_by_barcode_and_click_on_barcode(self):
        barcode_value = ""
        is_barcode_click = ""
        i = 0
        table = self.driver.find_element(By.XPATH,
                                         "//*[contains(@id, 'dashboardDrilldown_Attempted_Contractor')]/div[1]")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == "Barcode":
                barcode_value = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH,
                                          "//*[contains(@id, 'dashboardDrilldown_Attempted_Contractor')]/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.package_barcode == col.text:
                    # print("Barcode id found")
                    barcode_links = col.find_elements(By.TAG_NAME, 'a')
                    for barcode_link in barcode_links:
                        barcode_link.click()
                        is_barcode_click = "Y"
                        break
                j = j + 1
                if is_barcode_click == "Y":
                    break
            if is_barcode_click == "Y":
                break

    def OnHold_filter_by_barcode_and_click_on_barcode(self):
        barcode_value = ""
        is_barcode_click = ""
        i = 0
        table = self.driver.find_element(By.XPATH,
                                         "//*[contains(@id, 'exDashDrilldown_OnHold_Facility')]/div/div[1]")
        headers = table.find_elements(By.TAG_NAME, "th")
        print(len(headers))

        for header in headers:

            print(header.text)

            if header.text == "Barcode":
                barcode_value = i
            i = i + 1

        table1 = self.driver.find_element(By.XPATH,
                                          "//*[contains(@id, 'exDashDrilldown_OnHold_Facility')]/div/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        print(len(rows))
        print(self.package_barcode2)
        # print(100 / 0)
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                print(col.text)
                if self.package_barcode2 == col.text:

                    print("Barcode id found")
                    barcode_links = col.find_elements(By.TAG_NAME, 'a')
                    for barcode_link in barcode_links:
                        barcode_link.click()
                        is_barcode_click = "Y"
                        break
                j = j + 1
                if is_barcode_click == "Y":
                    break
            if is_barcode_click == "Y":
                break

        print(100 / 0)

    def exc_filter_by_barcode_and_click_on_barcode(self):
        barcode_value = ""
        is_barcode_click = ""
        i = 0
        table = self.driver.find_element(By.XPATH,
                                         "//*[contains(@id, 'facDashDrilldown_Exception_Contractor')]/div[1]")
        headers = table.find_elements(By.TAG_NAME, "th")

        for header in headers:
            # print(header.text)
            if header.text == "Barcode":
                barcode_value = i
            i = i + 1
        table1 = self.driver.find_element(By.XPATH,
                                          "//*[contains(@id, 'facDashDrilldown_Exception_Contractor')]/div[2]")
        rows = table1.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                # print(col.text)
                if self.package_barcode == col.text:
                    # print("Barcode id found")
                    barcode_links = col.find_elements(By.TAG_NAME, 'a')
                    for barcode_link in barcode_links:
                        barcode_link.click()
                        is_barcode_click = "Y"
                        break
                j = j + 1
                if is_barcode_click == "Y":
                    break
            if is_barcode_click == "Y":
                break

    def verify_stp_value(self):

        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # print(rows)
        # cells = table.find_elements_by_tag_name("td")
        cells = table.find_elements(By.TAG_NAME, "td")
        # print(cells)
        for cell in cells:
            # print(cell.text)
            # if cell == "WPB25":
            #     cell.click()
            # td_links = cell.find_elements_by_tag_name("a")
            td_links = cell.find_elements(By.TAG_NAME, "a")
            # print("My hubby is Awesome")
            # print(len(td_links))
            for tdlink in td_links:
                if tdlink.text == self.route_values[0]:
                    # print(tdlink.text)
                    tdlink.click()
                    time.sleep(5)

    def verify_delivery_by_customer_grid(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # header_lables = ["CUST", "STP", "PKG", "SHORT", "REC", "RTBD", "LOAD", "MLS", "OFD", "DEL", "MAN",
        #                  "!EXC!", "EXC", "REDEL", "LBS", "EVENT", "DUE", "%"]
        header_lables = ["CUST", "STP", "PKG", "SHORT", "REC", "RTBD", "LOAD", "MLS", "OFD", "DEL", "MAN",
                         "ATT", "EXC", "REDEL", "LBS", "EVENT", "DUE", "%", "NMI"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            # for headers in head_count:
            for headers in head_count:
                print(j)
                print(headers.text)

                if headers.text == "":
                    print(headers.text + ":is empty")
                elif headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                # if headers.text == header_lables[j]:
                #     j = j + 1
                #     test_results = "T"
                #
                # elif headers.text == "":
                #     print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_delivery_by_service_grid(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["SRV", "STP", "PKG", "SHORT", "REC", "RTBD", "LOAD", "MLS", "OFD", "DEL", "MAN",
                         "ATT", "EXC", "REDEL", "LBS", "EVENT", "DUE", "%", "NMI"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == "":
                    print(headers.text + ":is empty")
                elif headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_customer_facility_grid(self):
        table = self.driver.find_element(By.ID, 'PickupDrillDownGrid')
        # table = self.driver.find_element(By.XPATH, '//div[@id="PickupDrillDownGrid"]')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["CUST", "STP", "PKG", "PU", "OFP", "PU'D", "ATT", "EXC", "REDEL"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_service_facility_grid(self):
        table = self.driver.find_element(By.ID, 'PickupDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["SRV", "STP", "PKG", "PU", "OFP", "PU'D", "ATT", "EXC", "REDEL"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                # print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_pickups_route_facility_drill_down(self):
        def verify_service_facility_grid(self):
            table = self.driver.find_element(By.ID, 'PickupDrillDownGrid')
            # rows = table.find_elements_by_tag_name("tr")
            rows = table.find_elements(By.TAG_NAME, "tr")
            header_lables = ["IC", "Name", "RTE", "STP", "PKG", "PU", "OFP", "PU'D", "ATT", "EXC", "REDEL", "COMP",
                             "TYPE", "VEND"]
            test_results = "F"
            for row in rows:
                # head_count = row.find_elements_by_tag_name("th")
                head_count = row.find_elements(By.TAG_NAME, "th")
                print(len(head_count))
                j = 0
                for headers in head_count:
                    # print(headers.text)
                    # print(header_lables[j])
                    if headers.text == header_lables[j]:
                        j = j + 1
                        test_results = "T"

                    elif headers.text == "":
                        print(headers.text + ":is empty")
                    else:
                        test_results = "F"
                        self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                        assert False

                if test_results == "T":
                    self.LOG.info("FacilityAggregateGrid verification success")
                break

    def verify_exceptions_tab_facility_aggregate_grid(self):
        table = self.driver.find_element(By.ID, 'ExceptionAggregateGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["Overages (Reconciled)", "Overages (Non Reconciled)", "Shortages",
                         "Damaged (Delivered)", "Damaged (Discarded)", "Damaged (Returned)",
                         "FTB", "On Hold", "RTS", "Lost", "MisSort"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def select_by_contractor_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.contractor_radio_id)
        c_radio_button = self.driver.find_element(By.ID, self.contractor_radio_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_route_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.route_radio_id)
        c_radio_button = self.driver.find_element(By.ID, self.route_radio_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def pickups_select_by_route_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.route_radio_id)
        c_radio_button = self.driver.find_element(By.ID, "radioPickupsByRoute")
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def exceptions_select_by_route_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.route_radio_id)
        c_radio_button = self.driver.find_element(By.ID, "radioExceptionsByRoute")
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_customer_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.customer_radio_id)
        c_radio_button = self.driver.find_element(By.ID, self.customer_radio_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_pickup_customer_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.pickups_customer_radio_button)
        c_radio_button = self.driver.find_element(By.ID, self.pickups_customer_radio_button)
        if c_radio_button.is_selected():
            self.LOG.info("Custlomer radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_exceptions_customer_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.pickups_customer_radio_button)
        c_radio_button = self.driver.find_element(By.ID, "radioExceptionsByCustomer")
        if c_radio_button.is_selected():
            self.LOG.info("Custlomer radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_pickup_service_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.pickups_service_radio_button)
        c_radio_button = self.driver.find_element(By.ID, self.pickups_service_radio_button)
        if c_radio_button.is_selected():
            self.LOG.info("service radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_exception_service_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.pickups_service_radio_button)
        c_radio_button = self.driver.find_element(By.ID, "radioExceptionsByService")
        if c_radio_button.is_selected():
            self.LOG.info("service radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def select_by_service_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.service_radio_id)
        c_radio_button = self.driver.find_element(By.ID, self.service_radio_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def exceptions_tab_select_by_contractor_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.exceptions_tab_contractor_id)
        c_radio_button = self.driver.find_element(By.ID, self.exceptions_tab_contractor_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def exceptions_tab_select_by_route_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.exceptions_tab_route_id)
        c_radio_button = self.driver.find_element(By.ID, self.exceptions_tab_route_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def exceptions_tab_select_by_customer_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.exceptions_tab_customer_id)
        c_radio_button = self.driver.find_element(By.ID, self.exceptions_tab_customer_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def click_on_barcode(self):
        self.click_on_element(self.barcode_xpath, locator_type="xpath")

    def exceptions_tab_select_by_service_radio_button(self):
        # c_radio_button = self.driver.find_element_by_id(self.exceptions_tab_service_id)
        c_radio_button = self.driver.find_element(By.ID, self.exceptions_tab_service_id)
        if c_radio_button.is_selected():
            self.LOG.info("Contractor radio button is already selected with locator")
        else:
            c_radio_button.click()
            self.LOG.info("Checkbox is selected with locator")

    def service_type(self, service_type):
        time.sleep(3)
        self.click_on_element(self.service_type_button, "xpath")
        time.sleep(3)
        # dropd_list = self.driver.find_element_by_xpath(self.service_type_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.service_type_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, service_type)
        time.sleep(2)

    def verify_exceptions_tab_contractor_facility_aggregate_grid(self):
        table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["Contractor", "Company", "Vendor Id", "Contractor Type", "Route", "Shortages",
                         "Damaged (Delivered)", "Damaged (Discarded)",
                         "Damaged (Returned)", "FTB", "On Hold", "RTS", "Lost", "MisSort"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_exceptions_tab_route_facility_aggregate_grid(self):
        table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["Contractor", "Company", "Vendor Id", "Contractor Type", "Route", "Shortages",
                         "Damaged (Delivered)", "Damaged (Discarded)",
                         "Damaged (Returned)", "FTB", "On Hold", "RTS", "Lost", "MisSort"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_exceptions_tab_customer_facility_aggregate_grid(self):
        table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["Customer", "Shortages", "Damaged (Delivered)", "Damaged (Discarded)",
                         "Damaged (Returned)", "FTB", "On Hold", "RTS", "Lost", "MisSort"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def verify_exceptions_tab_service_facility_aggregate_grid(self):
        table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        header_lables = ["Service", "Shortages", "Damaged (Delivered)", "Damaged (Discarded)",
                         "Damaged (Returned)", "FTB", "On Hold", "RTS", "Lost", "MisSort"]
        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == header_lables[j]:
                    j = j + 1
                    test_results = "T"

                elif headers.text == "":
                    print(headers.text + ":is empty")
                else:
                    test_results = "F"
                    self.LOG.info("FacilityAggregateGrid verification failed at: " + headers.text)
                    assert False

            if test_results == "T":
                self.LOG.info("FacilityAggregateGrid verification success")
            break

    def facility_dashboard(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(5)
        self.verify_STP_column()
        time.sleep(2)
        self.click_on_refresh_grid()
        time.sleep(5)
        self.click_on_export_button()
        time.sleep(5)
        self.click_on_print_button()
        time.sleep(5)

    def test_facility(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(5)
        self.verify_STP_column()
        time.sleep(5)
        time.sleep(2)
        self.click_on_mls_grid()
        time.sleep(5)
        # self.take_screenshot(self.driver, testcase_name="test_001_open_mls_drill_down_window",
        #                      module_name="Facility_Dashboard")
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(5)
        self.click_on_exceptions_label()
        time.sleep(2)

    def facility_dashboard_facility_drill_down(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.select_by_contractor_radio_button()
        time.sleep(2)
        self.select_by_route_radio_button()
        time.sleep(2)
        self.select_by_customer_radio_button()
        time.sleep(2)
        self.select_by_service_radio_button()
        time.sleep(2)
        self.select_by_contractor_radio_button()
        time.sleep(15)
        self.verify_facility_drill_down_grid()
        time.sleep(2)

    def cust_facility_dashboard_facility_drill_down(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.select_by_pickup_customer_radio_button()
        time.sleep(2)
        self.verify_customer_facility_grid()
        time.sleep(2)

    def ser_facility_dashboard_facility_drill_down(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.select_by_pickup_service_radio_button()
        time.sleep(2)
        self.verify_service_facility_grid()
        time.sleep(2)

    def delivery_by_route(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(2)
        self.select_by_route_radio_button()
        time.sleep(10)
        self.verify_delivery_by_route_grid()
        time.sleep(2)

    def delivery_by_customer(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(2)
        self.select_by_customer_radio_button()
        time.sleep(10)
        self.verify_delivery_by_customer_grid()
        time.sleep(2)

    def click_on_barcode_field(self, barcode1):
        # barcode_elm = self.driver.execute_script("document.getElementById('txtPeBarcodeFormTop')")
        barcode_elm = self.driver.find_element(By.ID, "txtPeBarcodeFormTop")
        # barcode_elm.text = self.package_barcode2
        # time.sleep(5)
        self.send_keys_to("txtPeBarcodeFormTop", barcode1)

    def enter_random_barcode(self, barcode1):
        self.send_keys_to(self.barcode_field_xpath, barcode1, locator_type="xpath")

    def delivery_by_service(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(2)
        self.select_by_service_radio_button()
        time.sleep(10)
        self.verify_delivery_by_service_grid()
        time.sleep(2)

    def pickups_by_route(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(2)
        self.select_by_route_radio_button()
        time.sleep(10)
        self.verify_pickups_route_facility_drill_down()
        time.sleep(2)

    def exceptions_tab_facility_aggregate_grid(self):
        self.click_on_facility_dashboard()
        time.sleep(10)
        self.click_on_exceptions_label()
        time.sleep(15)
        self.verify_exceptions_tab_facility_aggregate_grid()
        time.sleep(2)

    def exceptions_tab_contractor_facility_aggregate_grid(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(8)
        self.exceptions_tab_select_by_contractor_radio_button()
        time.sleep(15)
        self.verify_exceptions_tab_contractor_facility_aggregate_grid()
        time.sleep(2)

    def exceptions_tab_route_facility_aggregate_grid(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(8)
        self.exceptions_tab_select_by_route_radio_button()
        time.sleep(15)
        self.verify_exceptions_tab_route_facility_aggregate_grid()
        time.sleep(2)

    def exceptions_tab_customer_facility_aggregate_grid(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(8)
        self.exceptions_tab_select_by_customer_radio_button()
        time.sleep(15)
        self.verify_exceptions_tab_customer_facility_aggregate_grid()
        time.sleep(2)

    def exceptions_tab_service_facility_aggregate_grid(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(8)
        self.exceptions_tab_select_by_service_radio_button()
        time.sleep(15)
        self.verify_exceptions_tab_service_facility_aggregate_grid()
        time.sleep(2)

    def click_on_toggle_bar(self):
        self.click_on_element(self.toggle_bar_xpath, locator_type="xpath")

    def click_on_set_landing_page(self):
        self.click_on_element(self.set_as_landing_page_xpath, locator_type="xpath")

    def facility_dashboard_as_default_landing_page(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        # element = self.driver.find_element_by_id(self.facility_dashboard_id)
        element = self.driver.find_element(By.ID, self.facility_dashboard_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_set_landing_page()
        time.sleep(2)

    def move_packages_from_mls_drill_down_window(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_deliveries_label()
        time.sleep(5)
        self.click_on_mls_grid()
        time.sleep(4)

    def click_on_user(self):
        self.click_on_element(self.dispatcher_name_id)

    def click_on_settings_button(self):
        self.click_on_element(self.settings_button_id)

    def click_on_landing_page(self):
        self.click_on_element(self.landing_page_xpath, locator_type="xpath")

    def select_landing_page_from_drop_down(self, landingpage_value):
        # landingpage_list = self.driver.find_element_by_id("ddlLandingPage_listbox")
        # landingpage_items = landingpage_list.find_elements_by_tag_name("li")
        landingpage_list = self.driver.find_element(By.ID, "ddlLandingPage_listbox")
        landingpage_items = landingpage_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(landingpage_items, value=landingpage_value)

    def select_package_entry_customer_from_drop_down(self, customer_value):
        # customer_list = self.driver.find_element_by_id("ddlPeCustomerFormTop_listbox")
        # customer_items = customer_list.find_elements_by_tag_name("li")
        customer_list = self.driver.find_element(By.ID, "ddlPeCustomerFormTop_listbox")
        customer_items = customer_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(customer_items, value=customer_value)

    def click_on_save_settings(self):
        self.click_on_element(self.save_settings_button_id)

    def set_the_facility_dashboard_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Facility Dashboard")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(2)

    def set_the_dispatch_dashboard_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Dispatch Dashboard")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def set_the_route_manager_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Route Manager")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def set_the_package_entry_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Package Entry")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def set_the_advanced_search_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Advanced Search")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def set_the_RTS_FTB_DD_Dashboard_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="RTS-FTB-DD Dashboard")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def set_the_daily_closeout_dashboard_as_landing_page(self):
        self.click_on_user()
        time.sleep(2)
        self.click_on_settings_button()
        time.sleep(2)
        self.click_on_landing_page()
        time.sleep(2)
        self.select_landing_page_from_drop_down(landingpage_value="Daily Closeout Dashboard")
        time.sleep(2)
        self.click_on_save_settings()
        time.sleep(4)

    def click_on_package_entry(self):
        self.driver.execute_script("document.getElementById('aPackageEntryDashboardLink').click()")

    def click_on_customer_drop_down(self):
        self.click_on_element(self.cust_drop_down_xpath, locator_type="xpath")

    def click_on_generate_button(self):
        self.click_on_element(self.generate_button_id)

    def click_on_validate_button(self):
        self.click_on_element(self.validate_button_id)

    def deliveries_tab_values(self):
        table = self.driver.find_element(By.ID, 'FacilityAggregateGrid')
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                print(col.text)
                if j == 0:
                    self.stp_orig = col.text
                    print("stp Value:" + self.stp_orig)
                elif j == 1:
                    self.pkg_orig = col.text
                    print("pkg Value:" + self.pkg_orig)
                elif j == 2:
                    self.short_orig = col.text
                    print("short Value:" + self.short_orig)
                j = j + 1
            # print(j / j)

    def deliveries_original_tab_values(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:
                print(col.text)
                if j == 0:
                    self.stp_value_orig = col.text
                    print("stp Value:" + self.stp_value_orig)
                elif j == 1:
                    self.pkg_value_orig = col.text
                    print("pkg Value:" + self.pkg_value_orig)
                elif j == 2:
                    self.short_value_orig = col.text
                    print("short Value:" + self.short_value_orig)
                j = j + 1
            # print(j / j)

    def deliveries_tab_expected_values(self):
        self.click_on_facility_dashboard()
        time.sleep(5)
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        rows = table.find_elements(By.TAG_NAME, "tr")
        print("jsfksdfhsfhjsf")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            j = 0
            for col in cols:

                if j == 4:
                    self.stp_exp = col.text
                    print("stp exp Value:" + self.stp_exp)
                    print(col.text)
                elif j == 5:
                    self.pkg_exp = col.text
                    print("pkg exp Value:" + self.pkg_exp)
                    print(col.text)
                elif j == 6:
                    self.short_exp = col.text
                    print("short exp Value:" + self.short_exp)
                    print(col.text)
                j = j + 1
        # x = 0
        # i = 9
        # print(i / x)

    def click_on_package_type_drop_down(self):
        self.click_on_element(self.package_type_drop_down_xpath, locator_type="xpath")

    def select_package_type_from_drop_down(self, package_value):
        # package_list = self.driver.find_element_by_id("ddlPePackageType_listbox")
        # package_items = package_list.find_elements_by_tag_name("li")
        package_list = self.driver.find_element(By.ID, "ddlPePackageType_listbox")
        package_items = package_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(package_items, value=package_value)

    def select_state_value_from_drop_down(self, state_value):
        # state_list = self.driver.find_element_by_id("ddlScrubState_listbox")
        # state_items = state_list.find_elements_by_tag_name("li")
        state_list = self.driver.find_element(By.ID, "ddlScrubState_listbox")
        state_items = state_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(state_items, value=state_value)

    def select_package_route_value_from_drop_down(self, route_value):
        # route_list = self.driver.find_element_by_id("ddlPeRoute-list")
        # route_items = route_list.find_elements_by_tag_name("li")
        route_list = self.driver.find_element(By.ID, "ddlPeRoute-list")
        route_items = route_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(route_items, value=route_value)

    def click_on_package_route_drop_down(self):
        self.driver.execute_script("document.getElementById('ddlPeRoute_label').click()")

    def click_on_look_up_address(self):
        self.click_on_element(self.look_up_address_xpath, locator_type="xpath")

    def enter_address1(self, address):
        self.send_keys_to(self.address1_id, address)

    def enter_city(self, city):
        self.send_keys_to(self.city_id, city)

    def enter_zipcode(self, zipcode):
        self.send_keys_to(self.zipcode_id, zipcode)

    def click_on_state_drop_down(self):
        self.driver.execute_script("document.getElementById('ddlScrubState').click()")

    def click_on_address_validate_button(self):
        self.click_on_element(self.validate2_button_id)

    def enter_stop_name(self):
        self.send_keys_to(self.stop_name_id, data="Test")

    def click_on_add_package(self):
        self.click_on_element(self.add_package_id)

    def click_on_submit_button(self):
        self.click_on_element(self.submit_button_id)

    def click_on_submit_packages(self):
        self.click_on_element(self.submit_packages_id)

    def search_with_route(self):
        self.click_on_element(self.search_id)
        time.sleep(2)
        self.send_keys_to(self.search_id, data="WPB25")

    def click_on_route_pencil_icon(self):
        # route_pencil = self.driver.find_element_by_xpath('//*[contains(@id, "routeWindowAssignContractor")]')
        route_pencil = self.driver.find_element(By.XPATH, '//*[contains(@id, "routeWindowAssignContractor")]')
        route_pencil.click()

    def click_on_status_pencil_icon(self):
        # route_pencil = self.driver.find_element_by_xpath('//*[contains(@id, "routeWindowAssignContractor")]')
        route_pencil1 = self.driver.find_element(By.XPATH, '//*[contains(@id, "editStatusInfo")]')
        route_pencil1.click()

    def click_on_route_manager(self):
        self.click_on_element(self.route_manager_id)

    def click_on_packages(self):
        element = self.driver.find_element(By.XPATH, "//div[@id="
                                                     "'routeAssignmentTable']/div[1]/div/table/thead/tr/th[4]/span/a")

        element.click()

    def click_on_package_value_dropdown(self):
        element1 = self.driver.find_element(By.XPATH, "//div[@class='k-filter-menu-container']/span[1]/button")
        element1.click()

    def select_customer(self, customer_name):
        self.click_on_element(self.customer_ddl_button, "xpath")
        # dropd_list = self.driver.find_element_by_xpath(self.customer_ddl_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.customer_ddl_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, customer_name)

    def filter_package(self, package_value):
        # package_list = self.driver.find_element_by_xpath("//div[@class='k-animation-container']/div/div/div[2]/ul")
        # package_items = package_list.find_elements_by_tag_name("li")
        package_list = self.driver.find_element(By.XPATH, "//div[@class='k-animation-container']/div/div/div[2]/ul")
        package_items = package_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down(package_items, value=package_value)

    def enter_package_input(self, value):
        element = self.driver.find_element(By.XPATH, "//div[@class='k-filter-menu-container']/span[2]/input[1]")
        element.click()

    def click_on_increase_value(self):
        increase_element = self.driver.find_element(By.XPATH, "//*[@aria-label='Increase value']")
        increase_element.click()

    def click_on_decrease_value(self):
        increase_element = self.driver.find_element(By.XPATH, "//*[@aria-label='Decrease value']")
        increase_element.click()

    def click_on_filter_button(self):
        filter_button = self.driver.find_element(By.XPATH, "//span[.='Filter']")
        filter_button.click()

    def get_the_route_value(self):
        # print(" nee abba")
        self.route_values[0] = self.driver.find_element(By.XPATH,
                                                        "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[1]/td[1]/a").text
        self.route_values[1] = self.driver.find_element(By.XPATH,
                                                        "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[2]/td[1]/a").text
        self.route_values[2] = self.driver.find_element(By.XPATH,
                                                        "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[3]/td[1]/a").text
        self.route_values[3] = self.driver.find_element(By.XPATH,
                                                        "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[4]/td[1]/a").text
        self.route_values[4] = self.driver.find_element(By.XPATH,
                                                        "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[5]/td[1]/a").text
        # print(self.route_values)
        #
        # route_value = self.driver.find_element_by_xpath(
        #     "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[2]/td[1]/a")
        #
        # print(route_value.text)
        # route_value = self.driver.find_element_by_xpath(
        #     "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[3]/td[1]/a")
        #
        # print(route_value.text)

    # def enter_package_value(self, value):
    #     self.send_keys_to(self.package_input_xpath, value, locator_type="xpath")

    def get_route_with_no_packages(self):
        # route_table = self.driver.find_element_by_id("routeAssignmentTable")
        # rows = route_table.find_elements_by_tag_name("tr")
        route_table = self.driver.find_element(By.ID, "routeAssignmentTable")
        rows = route_table.find_elements(By.TAG_NAME, "tr")
        columns = rows.find_elements(By.TAG_NAME, "th")
        # print(len(columns))
        # print(columns)
        # print("Shiva")
        # print(actual + rows)

    def assign_route_value(self):
        # route_text_box = self.driver.find_element_by_xpath('//*[contains(@id, "routeWindowContractorComplete")]')
        route_text_box = self.driver.find_element(By.XPATH, '//*[contains(@id, "routeWindowContractorComplete")]')
        time.sleep(3)
        route_text_box.clear()
        time.sleep(3)
        route_text_box.send_keys("30109")
        time.sleep(3)

    def click_on_undo_button(self):
        undo_buttton = self.driver.find_element(By.XPATH, '//*[contains(@id, "routeWindowUndoContractor")]')
        undo_buttton.click()

    def click_on_close_button(self):
        # close_button = self.driver.find_element_by_xpath("//*[@aria-label='Close']")
        close_button = self.driver.find_element(By.XPATH, "//*[@aria-label='Close']")
        close_button.click()

    def click_on_close_button1(self):
        # close_button = self.driver.find_element_by_xpath("//*[@aria-label='Close']")
        close_button = self.driver.find_element(By.XPATH, "/html/body/div[28]/div[1]/div/a[3]")
        close_button.click()

    def click_on_close_button2(self):
        # close_button = self.driver.find_element_by_xpath("//*[@aria-label='Close']")
        close_button = self.driver.find_element(By.XPATH, "/html/body/div[27]/div[1]/div/a[3]]")
        close_button.click()

    def click_on_advance_search_menu_and_search_with_barcode(self):
        # time.sleep(7)
        # self.click_on_element(self.fas_fa_bars)
        time.sleep(5)
        self.click_on_element(self.advance_search_menu_id)
        time.sleep(5)
        self.clear_field(self.advance_search_field_id)
        time.sleep(5)
        self.send_keys_to(self.advance_search_field_id, data=self.package_barcode)
        time.sleep(5)
        self.click_on_element(self.search_all_facilities)
        time.sleep(5)
        self.click_on_element(self.search_button_id)
        time.sleep(5)

    def click_on_advance_search_menu_and_search_with_random_barcode(self, random_barcode):
        # time.sleep(7)
        # self.click_on_element(self.fas_fa_bars)
        time.sleep(5)
        self.click_on_element(self.advance_search_menu_id)
        time.sleep(5)
        self.clear_field(self.advance_search_field_id)
        time.sleep(5)
        self.send_keys_to(self.advance_search_field_id, random_barcode)
        time.sleep(5)
        self.click_on_element(self.search_all_facilities)
        time.sleep(5)
        self.click_on_element(self.search_button_id)
        time.sleep(5)

    def create_package(self, j):

        self.select_package_entry_customer_from_drop_down(customer_value="SMITH DRUG (M7025-51465)")
        time.sleep(5)
        self.click_on_generate_button()
        time.sleep(2)
        self.click_on_validate_button()
        time.sleep(2)
        self.click_on_validate_button()
        time.sleep(2)
        self.click_on_package_type_drop_down()
        time.sleep(2)
        self.select_package_type_from_drop_down(package_value="Box")
        time.sleep(2)
        self.click_on_look_up_address()
        time.sleep(2)
        self.enter_address1(address=self.excel['Palmbeach_address']['Address'][j])
        time.sleep(2)
        self.enter_city(city=self.excel['Palmbeach_address']['City'][j])
        time.sleep(3)
        self.click_on_state_drop_down()
        time.sleep(2)
        self.select_state_value_from_drop_down(state_value=self.excel['Palmbeach_address']['State'][j])
        time.sleep(2)
        self.enter_zipcode(zipcode=str(self.excel['Palmbeach_address']['Zip'][j]))
        time.sleep(2)
        self.click_on_address_validate_button()
        time.sleep(2)
        self.enter_stop_name()
        time.sleep(2)
        self.click_on_package_route_drop_down()
        time.sleep(5)
        # self.select_package_route_value_from_drop_down(route_value="WPB25")
        self.select_package_route_value_from_drop_down(route_value=self.route_values[0])
        time.sleep(2)
        self.click_on_add_package()
        time.sleep(2)
        self.click_on_submit_button()
        time.sleep(3)
        self.click_on_submit_packages()
        time.sleep(3)

    def verify_exceptions_tab_comp_contra_vendorID(self):
        table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # header_lables = ["Company", "Vendor Id", "Contractor Type"]
        comp_text = "Company"
        vendor_text = "Vendor Id"
        contractor_text = "Contractor Type"
        comp_text_exist = "F"
        vendor_text_exist = "F"
        contractor_text_exist = "F"

        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == comp_text:
                    comp_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == vendor_text:
                    vendor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == contractor_text:
                    contractor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
            if comp_text_exist == "T" and vendor_text_exist == "T" and contractor_text_exist == "T":
                test_results = "T"
            # print(test_results)
            # print(100/0)

            if test_results == "T":
                self.LOG.info("exception tab verification success")
            break

    def verify_deiveries_tab_comp_contra_vendorID(self):
        table = self.driver.find_element(By.ID, 'FacilityDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # header_lables = ["Company", "Vendor Id", "Contractor Type"]
        comp_text = "COMP"
        vendor_text = "VEND"
        contractor_text = "TYPE"
        comp_text_exist = "F"
        vendor_text_exist = "F"
        contractor_text_exist = "F"

        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == comp_text:
                    comp_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == vendor_text:
                    vendor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == contractor_text:
                    contractor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
            if comp_text_exist == "T" and vendor_text_exist == "T" and contractor_text_exist == "T":
                test_results = "T"
            # print(test_results)
            # print(100/0)

            if test_results == "T":
                self.LOG.info("exception tab verification success")
            break

    def verify_pickups_tab_comp_contra_vendorID(self):
        table = self.driver.find_element(By.ID, 'PickupDrillDownGrid')
        # rows = table.find_elements_by_tag_name("tr")
        rows = table.find_elements(By.TAG_NAME, "tr")
        # header_lables = ["Company", "Vendor Id", "Contractor Type"]
        comp_text = "COMP"
        vendor_text = "VEND"
        contractor_text = "TYPE"
        comp_text_exist = "F"
        vendor_text_exist = "F"
        contractor_text_exist = "F"

        test_results = "F"
        for row in rows:
            # head_count = row.find_elements_by_tag_name("th")
            head_count = row.find_elements(By.TAG_NAME, "th")
            print(len(head_count))
            j = 0
            for headers in head_count:
                print(headers.text)
                # print(header_lables[j])
                if headers.text == comp_text:
                    comp_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == vendor_text:
                    vendor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                elif headers.text == contractor_text:
                    contractor_text_exist = "T"
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
                    headers.click()
                    time.sleep(5)
            if comp_text_exist == "T" and vendor_text_exist == "T" and contractor_text_exist == "T":
                test_results = "T"
            # print(test_results)
            # print(100/0)

            if test_results == "T":
                self.LOG.info("exception tab verification success")
            break

    #
    # def verify_exceptions_tab_comp_contra_vendorID(self):
    #     table = self.driver.find_element(By.ID, 'ExceptionDrillDownGrid')
    #     # rows = table.find_elements_by_tag_name("tr")
    #     rows = table.find_elements(By.TAG_NAME, "tr")
    #     # header_lables = ["Company", "Vendor Id", "Contractor Type"]
    #     comp_text = "COMP"
    #     vendor_text = "VEND"
    #     contractor_text = "TYPE"
    #     comp_text_exist = "F"
    #     vendor_text_exist = "F"
    #     contractor_text_exist = "F"
    #
    #     test_results = "F"
    #     for row in rows:
    #         # head_count = row.find_elements_by_tag_name("th")
    #         head_count = row.find_elements(By.TAG_NAME, "th")
    #         print(len(head_count))
    #         j = 0
    #         for headers in head_count:
    #             print(headers.text)
    #             # print(header_lables[j])
    #             if headers.text == comp_text:
    #                 comp_text_exist = "T"
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #             elif headers.text == vendor_text:
    #                 vendor_text_exist = "T"
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #             elif headers.text == contractor_text:
    #                 contractor_text_exist = "T"
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #                 headers.click()
    #                 time.sleep(5)
    #         if comp_text_exist == "T" and vendor_text_exist == "T" and contractor_text_exist == "T":
    #             test_results = "T"
    #         # print(test_results)
    #         # print(100/0)
    #
    #         if test_results == "T":
    #             self.LOG.info("exception tab verification success")
    #         break

    def verify_if_the_values_are_correct_deliveries_tab(self):
        # self.deliveries_tab_values()
        # stp_value = self.driver.find_element_by_xpath("//div[@id='FacilityAggregateGrid']/table/tbody/tr/td[1]")
        # print(stp_value)
        time.sleep(5)
        # self.deliveries_original_tab_values()
        time.sleep(5)
        self.click_on_toggle_bar()
        time.sleep(5)
        self.click_on_route_manager()
        time.sleep(5)
        self.click_on_packages()
        time.sleep(5)
        self.click_on_package_value_dropdown()
        time.sleep(5)
        self.filter_package(package_value="Equal To")
        time.sleep(5)
        self.click_on_increase_value()
        time.sleep(5)
        self.click_on_decrease_value()
        time.sleep(5)
        self.click_on_filter_button()
        time.sleep(10)
        self.get_the_route_value()
        time.sleep(10)
        self.click_on_package_entry()
        time.sleep(3)
        self.click_on_customer_drop_down()
        time.sleep(5)
        i = 0
        while (i < 2):
            self.create_package(i)
            i = i + 1

        time.sleep(5)
        # self.search_with_route()
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.filter_by_route_value()
        time.sleep(5)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_undo_button()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(10)
        time.sleep(5)
        self.deliveries_tab_expected_values()
        time.sleep(5)
        time.sleep(2)

    def click_on_package_entry_for_facility_dashboard(self):
        self.click_on_element(self.package_entry_id)

    def select_package_type(self, package_type="Box"):
        time.sleep(3)
        self.click_on_element(self.package_type_button, "xpath")
        time.sleep(3)
        # dropd_list = self.driver.find_element_by_xpath(self.package_type_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.package_type_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, package_type)
        time.sleep(2)

    def select_state(self, state):
        time.sleep(2)
        self.click_on_element(self.state_button, "xpath")
        time.sleep(1)
        # dropd_list = self.driver.find_element_by_xpath(self.state_ul_list)
        # dropd_items = dropd_list.find_elements_by_tag_name("li")
        dropd_list = self.driver.find_element(By.XPATH, self.state_ul_list)
        dropd_items = dropd_list.find_elements(By.TAG_NAME, "li")
        self.select_values_from_drop_down_textContent(dropd_items, state)

    def fill_out_lookup_address(self, stop_name="tc-28", address_line1="1300 SW 17th Ave", city="Boynton Beach",
                                state="Florida (FL)", zip="33426"):
        time.sleep(1)  # might not need. just in case
        self.click_on_element(self.address_look_up, "xpath")
        time.sleep(1)
        self.isElementPresent(self.Search_for_Addresses_Near_Facility, "xpath")
        self.isElementPresent(self.Search_for_Addresses_Near_Zip, "xpath")
        self.isElementPresent(self.btnScrubAddressCancel, "id")
        self.isElementPresent(self.clear_address, "id")
        self.send_keys_to(self.address_line1, address_line1)
        self.send_keys_to(self.city, city)
        self.select_state(state)
        self.send_keys_to(self.zip, zip)
        self.click_on_element(self.btnScrubAddressValidate)
        time.sleep(1)
        self.send_keys_to(self.stop_name, stop_name)

    def fill_out_lookup_address1(self, stop_name="tc-28", address_line1="1300 SW 17th Ave", city="Boynton Beach",
                                 state="Florida (FL)", zip="33426"):
        time.sleep(1)  # might not need. just in case
        self.click_on_element(self.address_look_up1, "xpath")
        time.sleep(1)
        self.isElementPresent(self.Search_for_Addresses_Near_Facility, "xpath")
        self.isElementPresent(self.Search_for_Addresses_Near_Zip, "xpath")
        self.isElementPresent(self.btnScrubAddressCancel, "id")
        self.isElementPresent(self.clear_address, "id")
        self.send_keys_to(self.address_line1, address_line1)
        self.send_keys_to(self.city, city)
        self.select_state(state)
        self.send_keys_to(self.zip, zip)
        self.click_on_element(self.btnScrubAddressValidate)
        time.sleep(1)
        self.send_keys_to(self.stop_name1, stop_name)

    def create_a_pick_up_package(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)", package_type="Box",
                                 service_type="Pickup", return_to_sender="no", forward_branch="no", overage="yes",
                                 skip_generate="no", stop_name="test", address_line1="1301 SW 17TH AVE",
                                 city="Boynton Beach", state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(5)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(5)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_barcode()
        time.sleep(7)
        self.click_on_status_pencil_icon()
        time.sleep(4)
        self.click_on_status_drop_down()
        time.sleep(3)
        self.verify_status_drop_down_values(status="Picked Up")
        time.sleep(5)
        self.click_on_save_button()
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.verify_picked_up_values()
        time.sleep(2)

    def verify_current_status(self, expected_status):
        # status = self.driver.find_element_by_xpath(self.statusCodeName).get_attribute('textContent')
        status = self.driver.find_element(By.XPATH, self.statusCodeName).get_attribute('textContent')
        print(status)
        assert status == expected_status

    def exceptions1_verify_that_the_fields_comp_contra_GPvendor_fields_added(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(15)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(5)
        self.exceptions_tab_select_by_route_radio_button()
        time.sleep(5)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(5)
        self.exceptions_tab_select_by_customer_radio_button()
        time.sleep(8)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(8)
        self.exceptions_tab_select_by_service_radio_button()
        time.sleep(8)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(5)

    def deliveries_verify_that_the_fields_comp_contra_GPvendor_fields_added(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_deliveries_label()
        time.sleep(8)
        # self.exceptions_tab_select_by_contractor_radio_button()
        time.sleep(15)
        self.verify_deiveries_tab_comp_contra_vendorID()
        time.sleep(5)
        self.select_by_route_radio_button()
        time.sleep(8)
        self.verify_deiveries_tab_comp_contra_vendorID()
        time.sleep(8)
        self.select_by_customer_radio_button()
        time.sleep(8)
        self.verify_deiveries_tab_comp_contra_vendorID()
        time.sleep(8)
        self.select_by_service_radio_button()
        time.sleep(8)
        self.verify_deiveries_tab_comp_contra_vendorID()
        time.sleep(8)

    def pickups_verify_that_the_fields_comp_contra_GPvendor_fields_added(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_pickups_label()
        time.sleep(8)
        # self.exceptions_tab_select_by_contractor_radio_button()
        time.sleep(15)
        self.verify_pickups_tab_comp_contra_vendorID()
        time.sleep(5)
        self.pickups_select_by_route_radio_button()
        time.sleep(5)
        self.verify_pickups_tab_comp_contra_vendorID()
        time.sleep(5)
        self.select_by_pickup_service_radio_button()
        time.sleep(5)
        self.verify_pickups_tab_comp_contra_vendorID()
        time.sleep(8)
        self.select_by_pickup_customer_radio_button()
        time.sleep(5)
        self.verify_pickups_tab_comp_contra_vendorID()
        time.sleep(8)
        # self.select_by_pickup_service_radio_button()
        # time.sleep(5)
        # self.verify_pickups_tab_comp_contra_vendorID()
        # time.sleep(8)

    def exceptions_verify_that_the_fields_comp_contra_GPvendor_fields_added(self):
        self.click_on_facility_dashboard()
        time.sleep(8)
        self.click_on_exceptions_label()
        time.sleep(8)
        # self.exceptions_tab_select_by_contractor_radio_button()
        time.sleep(15)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(5)
        self.exceptions_select_by_route_radio_button()
        time.sleep(5)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(5)
        self.select_by_exception_service_radio_button()
        time.sleep(5)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(8)
        self.select_by_exceptions_customer_radio_button()
        time.sleep(5)
        self.verify_exceptions_tab_comp_contra_vendorID()
        time.sleep(8)
        # self.select_by_pickup_service_radio_button()
        # time.sleep(5)
        # self.verify_pickups_tab_comp_contra_vendorID()
        # time.sleep(8)

    def create_package_with_delivered_status(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)", package_type="Box",
                                             service_type="Next Day Delivery", return_to_sender="no",
                                             forward_branch="no",
                                             overage="yes",
                                             skip_generate="no", stop_name="test", address_line1="1301 SW 17TH AVE",
                                             city="Boynton Beach", state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address1(stop_name, address_line1, city, state, zip)
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
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_barcode()
        time.sleep(7)
        self.click_on_status_pencil_icon()
        time.sleep(4)
        self.click_on_status_drop_down()
        time.sleep(3)
        self.verify_status_drop_down_values(status="Delivered")
        time.sleep(5)
        self.click_on_drop_drop_down()
        time.sleep(5)
        self.verify_delivered_status_drop_down_values(status="DOOR_PERSON")
        time.sleep(5)
        self.click_on_save_button()
        time.sleep(5)
        # self.click_on_status_pencil_icon()
        # time.sleep(5)
        # self.click_on_status_drop_down()
        # time.sleep(2)
        # self.verify_status_drop_down_values(status="Delivered")
        # time.sleep(5)
        # self.click_on_drop_drop_down()
        # time.sleep(5)
        # self.verify_delivered_status_drop_down_values(status="DOOR_PERSON")
        # time.sleep(5)
        # self.click_on_save_button()
        # time.sleep(10)
        self.click_on_close_button()
        time.sleep(10)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_barcode()
        # time.sleep(5)
        # self.click_on_status_pencil_icon()
        # time.sleep(5)
        # self.click_on_status_drop_down()
        # time.sleep(2)
        # self.verify_status_drop_down_values(status="Delivered")
        # time.sleep(5)
        # self.click_on_drop_drop_down()
        # time.sleep(5)
        # self.verify_delivered_status_drop_down_values(status="DOOR_PERSON")
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.verify_delivered_status_values()
        time.sleep(2)

    def verify_if_the_values_are_correct_in_the_pickup_tab(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                           package_type="Box", service_type="Pickup",
                                                           return_to_sender="no", forward_branch="no", overage="yes",
                                                           skip_generate="no", stop_name="test",
                                                           address_line1="1301 SW 17TH AVE", city="Boynton Beach",
                                                           state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        route_value = self.driver.find_element(By.XPATH, "//div[@id='divWrapper']/ul[3]/li/ul/li/div[1]/span")
        self.route = route_value.text
        print(self.route)
        time.sleep(3)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        time.sleep(2)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.filter_by_route_value_for_values_validation()
        time.sleep(2)
        self.filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.verify_current_status(expected_status="Pickup")
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(5)
        self.verify_pick_up_values()
        time.sleep(5)
        self.filter_by_route_value_for_attempt_values_validation()
        time.sleep(5)
        self.attemp_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        time.sleep(5)
        self.verify_current_status(expected_status="Pickup")
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(5)
        self.verify_pick_up_values_and_change_the_status_to_exception()
        time.sleep(5)
        self.filter_by_route_value_for_package_values_validation()
        time.sleep(5)
        self.package_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.click_on_refresh_grid()
        time.sleep(5)
        self.filter_by_route_value_for_attempt_values_validation()
        time.sleep(5)
        self.attemp_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.click_on_refresh_grid()
        time.sleep(5)
        self.filter_by_route_value_for_exception_values_validation()
        time.sleep(5)
        self.exc_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)

    def test_barcode(self):
        self.click_on_package_entry()
        time.sleep(7)
        self.select_customer(customer_name="Blue Apron wholly owned by Fresh Ream Inc (M7178-51687)")
        time.sleep(5)
        self.randombarcode()
        print(self.package_barcode2)
        time.sleep(2)
        self.click_on_barcode_field(barcode1=self.package_barcode2)
        time.sleep(2)
        self.click_on_validate_button()
        time.sleep(5)
        self.service_type(service_type="Non-RTS Delivery")
        time.sleep(2)
        time.sleep(3)
        self.select_package_type(package_type="Box")
        time.sleep(2)
        self.click_on_look_up_address()
        time.sleep(5)
        self.fill_out_lookup_address1()
        time.sleep(5)
        self.click_on_add_package()
        time.sleep(5)
        self.click_on_submit_packages()
        time.sleep(5)
        self.click_on_advance_search()
        time.sleep(5)
        self.click_on_advance_search_menu_and_search_with_random_barcode(random_barcode=self.package_barcode2)
        time.sleep(5)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_barcode()
        time.sleep(7)
        self.click_on_status_pencil_icon()
        time.sleep(4)
        self.click_on_status_drop_down()
        time.sleep(3)
        self.verify_status_drop_down_values(status="Exception")
        time.sleep(5)
        # self.change_the_status_to_out_for_delivery(status="Exception")
        # time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.select_attempt_reason(attempt="On Hold at LaserShip")
        time.sleep(5)
        self.click_on_save_button()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(5)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_exceptions_label()
        time.sleep(5)
        self.click_onhold_hyperlink()
        # self.click_on_element("//div[@id='ExceptionAggregateGrid']/table/tbody/tr/td[8]/a", locator_type="xpath")
        time.sleep(5)
        self.OnHold_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)

    def check_statuses_of_picked_up(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                    package_type="Box", service_type="Pickup",
                                    return_to_sender="no", forward_branch="no", overage="yes",
                                    skip_generate="no", stop_name="test",
                                    address_line1="1301 SW 17TH AVE", city="Boynton Beach",
                                    state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        route_value = self.driver.find_element(By.XPATH, "//div[@id='divWrapper']/ul[3]/li/ul/li/div[1]/span")
        self.route = route_value.text
        print(self.route)
        time.sleep(3)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        time.sleep(2)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.filter_by_route_value_for_values_validation()
        time.sleep(2)
        self.filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.verify_current_status(expected_status="Pickup")
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(5)
        self.verify_pick_up_values()
        time.sleep(5)
        self.filter_by_route_value_for_attempt_values_validation()
        time.sleep(5)
        self.attemp_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        time.sleep(5)
        self.verify_current_status(expected_status="Pickup")
        time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(5)
        self.verify_pick_up_values_and_change_the_status_to_exception()
        time.sleep(5)
        self.filter_by_route_value_for_package_values_validation()
        time.sleep(5)
        self.package_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.click_on_refresh_grid()
        time.sleep(5)
        self.filter_by_route_value_for_attempt_values_validation()
        time.sleep(5)
        self.attemp_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        self.click_on_refresh_grid()
        time.sleep(5)
        self.filter_by_route_value_for_exception_values_validation()
        time.sleep(5)
        self.exc_filter_by_barcode_and_click_on_barcode()
        time.sleep(5)

    def find_package_in_pickup_exception_column(self, barcode='pass_a_barcode', drilldown_type="exception"):
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(3)
        self.click_on_pickups_label()
        time.sleep(3)
        if drilldown_type.lower() == "exception":
            self.click_on_element(self.drilldown_exception, "xpath")
        if drilldown_type.lower() == "attempt":
            self.click_on_element(self.attempt_exception, "xpath")
        time.sleep(2)
        # self.isElementPresent("(//a[contains(text(),'70AE14A21EBAB4A94A8D91')])[2]", "xpath")
        self.isElementPresent("(//a[contains(text(),'" + barcode + "')])[2]", "xpath")
        self.click_on_element("(//a[contains(text(),'" + barcode + "')])[2]", "xpath")
        time.sleep(2)

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

    def verify_that_attempt_status_works_as_expected(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                     package_type="Box", service_type="Pickup",
                                                     return_to_sender="no", forward_branch="no", overage="yes",
                                                     skip_generate="no", stop_name="test",
                                                     address_line1="1301 SW 17TH AVE", city="Boynton Beach",
                                                     state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        route_value = self.driver.find_element(By.XPATH, "//div[@id='divWrapper']/ul[3]/li/ul/li/div[1]/span")
        self.route = route_value.text
        print(self.route)
        time.sleep(3)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        time.sleep(2)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.filter_by_route_value_for_values_validation()
        time.sleep(2)
        self.filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        # self.verify_current_status(expected_status="Pickup")
        # time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.change_the_status_to_out_for_delivery(status="Attempt")
        time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.verify_attempt_status_values()
        # self.verify_pick_up_values()
        # time.sleep(5)
        # self.filter_by_route_value_for_attempt_values_validation()
        # time.sleep(5)
        # self.attemp_filter_by_barcode_and_click_on_barcode()
        # time.sleep(5)
        # time.sleep(5)
        # self.verify_current_status(expected_status="Pickup")
        # time.sleep(5)
        # self.click_on_status_pencil_icon()
        # time.sleep(5)
        # self.click_on_status_drop_down()
        # time.sleep(5)
        # self.verify_pick_up_values_and_change_the_status_to_exception()
        time.sleep(5)

    def verify_that_exception_status_works_as_expected(self, customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                       package_type="Box",
                                                       service_type="Next Day Delivery", return_to_sender="no",
                                                       forward_branch="no",
                                                       overage="yes",
                                                       skip_generate="no", stop_name="test",
                                                       address_line1="1301 SW 17TH AVE",
                                                       city="Boynton Beach", state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address1(stop_name, address_line1, city, state, zip)
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
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_barcode()
        time.sleep(7)
        self.click_on_status_pencil_icon()
        time.sleep(4)
        self.click_on_status_drop_down()
        time.sleep(3)
        self.change_the_status_to_out_for_delivery(status="Exception")
        time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(5)
        self.verify_exception_status_values()
        time.sleep(3)

    def verify_that_all_of_the_attempt_statuses_are_working_as_expected(self,
                                                                        customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                                        package_type="Box", service_type="Pickup",
                                                                        return_to_sender="no", forward_branch="no",
                                                                        overage="yes",
                                                                        skip_generate="no", stop_name="test",
                                                                        address_line1="1301 SW 17TH AVE",
                                                                        city="Boynton Beach",
                                                                        state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_type need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        route_value = self.driver.find_element(By.XPATH, "//div[@id='divWrapper']/ul[3]/li/ul/li/div[1]/span")
        self.route = route_value.text
        print(self.route)
        time.sleep(3)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        time.sleep(2)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.filter_by_route_value_for_values_validation()
        time.sleep(2)
        self.filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        # self.verify_current_status(expected_status="Pickup")
        # time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.change_the_status_to_out_for_delivery(status="Out For Delivery")
        time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.verify_attempt_status_values()

    def Nextdaydelivery_verify_that_attempt_status_works_as_expected(self,
                                                                     customer_name="ADVANCED CARE SOLUTIONS (M7034)",
                                                                     package_type="Box",
                                                                     service_type="Next Day Delivery",
                                                                     return_to_sender="no", forward_branch="no",
                                                                     overage="yes",
                                                                     skip_generate="no", stop_name="test",
                                                                     address_line1="1301 SW 17TH AVE",
                                                                     city="Boynton Beach",
                                                                     state="Florida (FL)", zip="33426"):
        if skip_generate.lower() == 'yes':
            self.click_on_element(self.validate)
        else:
            self.select_customer(customer_name)
            time.sleep(2)
            self.click_on_element(self.generate)
            time.sleep(2)
            self.click_on_element(self.validate)
            self.service_type(service_type)  # service_ty_pe need to selected before package_type
            self.select_package_type(package_type)
            time.sleep(2)
        self.fill_out_lookup_address(stop_name, address_line1, city, state, zip)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.btnPeAddPackage)
        time.sleep(4)
        route_value = self.driver.find_element(By.XPATH, "//div[@id='divWrapper']/ul[3]/li/ul/li/div[1]/span")
        self.route = route_value.text
        print(self.route)
        time.sleep(3)
        self.click_on_element(self.btnPeAddPackage, "xpath")
        time.sleep(2)
        if return_to_sender.lower() == "yes":  ##if you need to click "return to sender" option then set this to "yes" in parameters #few tests need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)
        if forward_branch.lower() == "yes":  # if you need to click "forward branch" option then set this to "yes" in parameters #TC178 need this
            self.click_on_element(self.return_to_sender_radio)
            self.click_on_element(self.submit_button)

        if overage.lower() == "yes":  # if you need to click "overage" option then set this to "yes" in parameters #TC177 need this
            # self.click_on_element(self.package_overage)
            self.click_on_element(self.submit_button)
        time.sleep(2)
        # barcode = self.driver.find_element_by_xpath(self.get_barcode).get_attribute('textContent')
        barcode = self.driver.find_element(By.XPATH, self.get_barcode).get_attribute('textContent')
        print("barcode: " + barcode)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        self.click_on_element(self.btnPeSubmitPackage)
        time.sleep(2)
        print(barcode)
        self.package_barcode = barcode
        time.sleep(5)
        time.sleep(2)
        self.click_on_advance_search_menu_and_search_with_barcode()
        time.sleep(2)
        self.click_on_package_route()
        time.sleep(2)
        self.click_on_route_pencil_icon()
        time.sleep(5)
        self.assign_route_value()
        time.sleep(5)
        self.click_on_close_button()
        time.sleep(2)
        self.click_on_facility_dashboard()
        time.sleep(5)
        self.click_on_pickups_label()
        time.sleep(2)
        self.filter_by_route_value_for_values_validation()
        time.sleep(2)
        self.filter_by_barcode_and_click_on_barcode()
        time.sleep(5)
        # self.verify_current_status(expected_status="Pickup")
        # time.sleep(5)
        self.click_on_status_pencil_icon()
        time.sleep(5)
        self.click_on_status_drop_down()
        time.sleep(2)
        self.change_the_status_to_out_for_delivery(status="Attempt")
        time.sleep(5)
        self.click_on_attempt_drp_down()
        time.sleep(2)
        self.verify_attempt_status_values()
        # self.verify_pick_up_values()
        # time.sleep(5)
        # self.filter_by_route_value_for_attempt_values_validation()
        # time.sleep(5)
        # self.attemp_filter_by_barcode_and_click_on_barcode()
        # time.sleep(5)
        # time.sleep(5)
        # self.verify_current_status(expected_status="Pickup")
        # time.sleep(5)
        # self.click_on_status_pencil_icon()
        # time.sleep(5)
        # self.click_on_status_drop_down()
        # time.sleep(5)
        # self.verify_pick_up_values_and_change_the_status_to_exception()
        time.sleep(5)

    def changing_onHoldStatus(self, barcode):
        exception_name = "On Hold at LaserShip"
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.barcode_res).click()
        time.sleep(3)
        assert (self.isElementPresent(self.verify_code), "xpath")
        self.driver.find_element(By.XPATH, self.status_change).click()
        assert (self.isElementPresent(self.verify_code), "xpath")
        self.driver.find_element(By.XPATH, self.status_dropdown).click()
        assert (self.isElementPresent(self.status_dropdown), "xpath")
        self.driver.find_element(By.XPATH, self.exeption_status).click()
        self.driver.find_element(By.XPATH, self.exception_drpdwn).click()

        self.driver.find_element(By.XPATH, self.exception_searchBar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).send_keys(exception_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.lasership_data).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.save_btn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.close_btn).click()
        assert (self.isElementPresent(self.facility_dashboard_id), "xpath")
        self.click_on_element(self.facility_dashboard_id)
        self.click_on_exceptions_label()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.onhold_total1).click()
        assert (self.isElementPresent(self.on_hold_reportTab), "xpath")
        time.sleep(3)
        self.driver.find_element(By.ID, self.text_searchonhold_facility).click()
        self.driver.find_element(By.ID, self.text_searchonhold_facility).send_keys(barcode)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.barcode_res1).click()
        time.sleep(3)
        eventTxt = self.driver.find_element(By.XPATH, self.events_tab).get_attribute('textContent')
        eventTab = self.driver.find_element(By.XPATH, self.events_tab)
        assert (self.isElementPresent(eventTab.text), eventTxt)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.status_change1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.drop_dropdown1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exeption_status1).click()
        self.driver.find_element(By.XPATH, self.exception_statusTxt1).get_attribute(
            'textContent')
        exception_stat1 = self.driver.find_element(By.XPATH, self.exception_statusTxt1)
        assert (self.isElementPresent(exception_stat1.text), exception_stat1)
        self.driver.find_element(By.XPATH, self.exception_statusTxt2).get_attribute(
            'textContent')
        exception_stat2 = self.driver.find_element(By.XPATH, self.exception_statusTxt2)
        assert (self.isElementPresent(exception_stat1.text), exception_stat2)
        self.driver.find_element(By.XPATH, self.exception_statusTxt3).get_attribute(
            'textContent')
        exception_stat3 = self.driver.find_element(By.XPATH, self.exception_statusTxt3)
        assert (self.isElementPresent(exception_stat1.text), exception_stat3)

    def verify_status_displayed_onhold_package(self, exceed_on_hold_days_discard, exceed_on_hold_days_rts,
                                               lost_by_laserShip, remove_from_onhold):
        exception_name = "On Hold at LaserShip"
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.barcode_res).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.status_change).click()
        assert (self.isElementPresent(self.verify_code), "xpath")
        self.driver.find_element(By.XPATH, self.status_dropdown).click()
        assert (self.isElementPresent(self.status_dropdown), "xpath")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.exeption_status).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_drpdwn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).send_keys(exception_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.lasership_data).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.save_btn).click()
        time.sleep(5)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.close_btn).click()
        self.click_on_element(self.facility_dashboard_id)
        assert (self.isElementPresent(self.deliveries_label_id))
        assert (self.isElementPresent(self.pickups_label_id))
        self.driver.find_element(By.ID, self.exceptions_label_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.onhold_total1).click()
        assert (self.isElementPresent(self.on_hold_reportTab, "xpath"))
        self.driver.find_element(By.XPATH, self.onhold_facility_checkbox1).click()
        self.driver.find_element(By.XPATH, self.onhold_facility_checkbox2).click()
        self.driver.find_element(By.XPATH, self.onhold_facility_checkbox3).click()
        assert (self.isElementPresent(self.apply_event_btn))
        self.driver.find_element(By.ID, self.apply_event_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_event_arrow).click()
        time.sleep(5)
        assert (self.isElementPresent(self.exceed_on_hold_days_discard), exceed_on_hold_days_discard)
        assert (self.isElementPresent(self.exceed_on_hold_days_rts), exceed_on_hold_days_rts)
        assert (self.isElementPresent(self.lost_by_laserShip), lost_by_laserShip)
        assert (self.isElementPresent(self.remove_from_onhold), remove_from_onhold)

    def getRouteText(self):
        route_text = self.driver.find_element(By.XPATH, self.route_link).get_attribute('textContent')
        print("routeTxt:" + route_text)
        return route_text

    def verify_master_header_status(self):
        time.sleep(2)
        assert (self.isElementPresent(self.sequence_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.time_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.drop_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.signature_Txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.picked_up_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.exceptionTyp_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.exception_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.door_tag, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.edd_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.stop_name_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.address_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.hash_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.status_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.cust_route_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.cust_stop_txt, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.service_txt, "xpath"))

    def verify_checkbox_types(self):
        assert (self.isElementPresent(self.show_POD_checkbox))
        assert (self.isElementPresent(self.show_exception_checkbox))

    def verify_child_header_status(self):
        assert (self.isElementPresent(self.time_status_txt, "xpath"))
        assert (self.isElementPresent(self.drop_status_txt, "xpath"))
        assert (self.isElementPresent(self.signature_status_txt, "xpath"))
        assert (self.isElementPresent(self.picked_up_status_txt, "xpath"))
        assert (self.isElementPresent(self.exception_type_txt, "xpath"))
        assert (self.isElementPresent(self.exception_status_txt, "xpath"))
        assert (self.isElementPresent(self.door_tag_txt, "xpath"))
        assert (self.isElementPresent(self.edd_status_txt, "xpath"))
        assert (self.isElementPresent(self.barcode_status_txt, "xpath"))
        assert (self.isElementPresent(self.status_txt_type, "xpath"))
        assert (self.isElementPresent(self.cust_route_status, "xpath"))
        assert (self.isElementPresent(self.cust_stop_status, "xpath"))

    def verify_master_child_time_vals(self):
        master_time_val = self.driver.find_element(By.XPATH, self.master_time_text_val).get_attribute('textContent')
        time.sleep(3)
        child_time_val = self.driver.find_element(By.XPATH, self.child_time_text_val).get_attribute('textContent')
        time.sleep(3)
        assert master_time_val == child_time_val

    def verify_master_child_dropdown_vals(self):
        master_drop_down_val = self.driver.find_element(By.XPATH, self.master_drop_down_txt_val).get_attribute(
            'textContent')
        time.sleep(3)
        print("masterDrop:" + master_drop_down_val)
        child_drop_down_val = self.driver.find_element(By.XPATH, self.child_drop_down_txt_val).get_attribute(
            'textContent')
        time.sleep(3)
        print("childDrop:" + child_drop_down_val)
        assert master_drop_down_val == child_drop_down_val

    def verify_master_child_signature_vals(self):
        master_sign_val = self.driver.find_element(By.XPATH, self.master_signature_txt_val).get_attribute('textContent')
        child_sign_val = self.driver.find_element(By.XPATH, self.child_signature_txt_val).get_attribute('textContent')
        assert master_sign_val == child_sign_val

    def verify_drop_down_signature_vals(self):
        time.sleep(4)
        child_dropdown_val = self.driver.find_element(By.XPATH, self.child_drop_down_txt_val1).get_attribute(
            'textContent')
        assert child_dropdown_val.strip() == ""
        time.sleep(4)
        child_sign_val = self.driver.find_element(By.XPATH, self.child_signature_txt_val).get_attribute('textContent')
        assert child_sign_val.strip() == ""

    def verify_exception_dropdown_vals(self):
        assert (self.isElementPresent(self.delay_natural_disaster, "xpath"))
        assert (self.isElementPresent(self.delay_external_factors, "xpath"))
        assert (self.isElementPresent(self.exceed_discarded, "xpath"))
        assert (self.isElementPresent(self.exceed_rts, "xpath"))
        assert (self.isElementPresent(self.item_damaged_delivered, "xpath"))
        assert (self.isElementPresent(self.item_damaged_discarded, "xpath"))
        assert (self.isElementPresent(self.item_damaged_returned, "xpath"))
        assert (self.isElementPresent(self.item_lost_laser, "xpath"))
        assert (self.isElementPresent(self.late_line_haul, "xpath"))
        assert (self.isElementPresent(self.left_on_dock, "xpath"))
        assert (self.isElementPresent(self.mechanical_break_down, "xpath"))
        assert (self.isElementPresent(self.on_hold_laser, "xpath"))
        assert (self.isElementPresent(self.return_request_customer_shipper, "xpath"))

    def verify_exception_type_drop_down_vals(self):
        assert (self.isElementPresent(self.already_picked_up), "xpath")
        assert (self.isElementPresent(self.need_more_info), "xpath")
        assert (self.isElementPresent(self.recipient_refuse_damage), "xpath")
        assert (self.isElementPresent(self.recipient_refuse_delivery), "xpath")
        assert (self.isElementPresent(self.secure_building_no_access), "xpath")
        assert (self.isElementPresent(self.unable_to_leave_parcel), "xpath")

    def verify_PU_exception_dropdown_vals(self):
        assert (self.isElementPresent(self.delay_natural_disaster, "xpath"))
        assert (self.isElementPresent(self.delay_external_factors, "xpath"))
        assert (self.isElementPresent(self.mechanical_break_down_txt), "xpath")

    def verify_PU_attempt_dropdown_vals(self):
        assert (self.isElementPresent(self.already_picked_up), "xpath")
        assert (self.isElementPresent(self.need_more_info), "xpath")
        assert (self.isElementPresent(self.business_closed_status), "xpath")
        assert (self.isElementPresent(self.customer_kept_return_status), "xpath")
        assert (self.isElementPresent(self.return_unavailable_pickup), "xpath")
        assert (self.isElementPresent(self.secure_building_no_access), "xpath")

    def verify_PU_attempt_status(self):
        master_attempt_txt = self.driver.find_element(By.XPATH, self.master_attempt_status).get_attribute(
            'textContent')
        print("master_attempt_txt:" + master_attempt_txt)
        time.sleep(3)
        child_attempt_txt = self.driver.find_element(By.XPATH, self.child_attempt_status).get_attribute(
            'textContent')
        print("child_attempt_txt:" + child_attempt_txt)
        assert master_attempt_txt == child_attempt_txt

    def verify_RD_status_update(self, signature, time_format, exception_test):
        time.sleep(5)
        assert (self.isElementPresent(self.status_update_icon, "xpath"))
        self.driver.find_element(By.XPATH, self.status_update).click()
        time.sleep(3)
        self.verify_master_header_status()
        time.sleep(3)
        self.verify_checkbox_types()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.master_row_top).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.time_picker_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.time_picker_field).send_keys(time_format)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.master_body).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.drop_down_carat).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drop_down_val).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.signature_txt).send_keys(signature)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.master_body).click()
        time.sleep(3)
        self.verify_child_header_status()
        time.sleep(3)
        self.verify_master_child_time_vals()
        time.sleep(3)
        self.verify_master_child_dropdown_vals()
        time.sleep(3)
        self.verify_master_child_signature_vals()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.master_body).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.search_box).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_box).send_keys(exception_test)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.search_box).send_keys(Keys.ENTER)
        time.sleep(3)
        self.verify_drop_down_signature_vals()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(2)
        self.verify_exception_dropdown_vals()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.exception_type_carat_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_attempt_drop_down).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(2)
        self.verify_exception_type_drop_down_vals()

    def click_on_delivery_column(self):
        self.driver.find_element(By.XPATH, self.delivery_column_link).click()

    def verify_PU_status_update(self, signature, time_format, exception_test):
        time.sleep(5)
        assert (self.isElementPresent(self.status_update_icon, "xpath"))
        self.driver.find_element(By.XPATH, self.status_update).click()
        time.sleep(3)
        self.verify_master_header_status()
        time.sleep(3)
        self.verify_checkbox_types()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.master_row_top).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.time_picker_field).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.time_picker_field).send_keys(time_format)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.master_body).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.signature_txt).send_keys(signature)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.master_body).click()
        time.sleep(3)
        assert (self.isElementPresent(self.picked_up_check_box, "xpath"))
        self.verify_child_header_status()
        time.sleep(3)
        self.verify_master_child_time_vals()
        time.sleep(3)
        self.verify_master_child_signature_vals()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.search_box).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_box).send_keys(exception_test)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.search_box).send_keys(Keys.ENTER)
        time.sleep(3)
        # self.verify_drop_down_signature_vals()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(2)
        self.verify_PU_exception_dropdown_vals()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.exception_type_carat_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_attempt_drop_down).click()
        time.sleep(3)
        self.verify_PU_attempt_status()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_carat_button).click()
        time.sleep(2)
        self.verify_PU_attempt_dropdown_vals()

    def get_on_hold_count(self):
        onholdTot = self.driver.find_element(By.XPATH, self.onhold_total1).get_attribute(
            'textContent')
        print("onholdTot:" + onholdTot)
        return onholdTot

    def onhold_status_change(self):
        exception_name = "On Hold at LaserShip"
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.barcode_res).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.status_change).click()
        assert (self.isElementPresent(self.verify_code), "xpath")
        self.driver.find_element(By.XPATH, self.status_dropdown).click()
        self.driver.find_element(By.XPATH, self.exeption_status).click()
        self.driver.find_element(By.XPATH, self.exception_drpdwn).click()
        self.driver.find_element(By.XPATH, self.exception_searchBar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).send_keys(exception_name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.lasership_data).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.save_btn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def click_and_verify_onholdCol(self):
        self.driver.find_element(By.XPATH, self.onhold_total1).click()
        assert (self.isElementPresent(self.on_hold_reportTab), "xpath")

    def click_on_maximize_window_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.maximize_window_btn).click()

    def verify_days_on_hold_ascending(self):
        days_on_hold_before_click = self.driver.find_element(By.XPATH, self.days_on_hold_text_bef).get_attribute(
            'textContent')
        print("days_on_hold_before_click:" + days_on_hold_before_click)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.days_on_hold_header).click()
        days_onhold_ascending_data_bef = self.driver.find_element(By.XPATH, self.days_on_hold_text_bef).get_attribute(
            'textContent')
        print("days_onhold_ascending_data_bef:" + days_onhold_ascending_data_bef)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.days_on_hold_header).click()
        time.sleep(2)
        days_onhold_ascending_data_after = self.driver.find_element(By.XPATH,
                                                                    self.days_on_hold_text_after).get_attribute(
            'textContent')
        print("days_onhold_ascending_data_after:" + days_onhold_ascending_data_after)
        assert days_onhold_ascending_data_bef < days_onhold_ascending_data_after

        assert days_onhold_ascending_data_after > days_onhold_ascending_data_bef

        self.driver.find_element(By.XPATH, self.days_on_hold_header).click()

        days_on_hold_after_click = self.driver.find_element(By.XPATH, self.days_on_hold_text_bef).get_attribute(
            'textContent')
        print("dasy_on_hold_after_click:" + days_on_hold_after_click)

        assert days_on_hold_before_click == days_on_hold_after_click

    def get_damage_delivery_count(self):
        damageDelTot = self.driver.find_element(By.XPATH, self.damage_delivery_col).get_attribute(
            'textContent')
        print("onholdTot:" + damageDelTot)
        return damageDelTot

    def get_damage_discard_count(self):
        damageDiscardTot = self.driver.find_element(By.XPATH, self.damage_discard_col).get_attribute(
            'textContent')
        print("onholdTot:" + damageDiscardTot)
        return damageDiscardTot

    def get_damage_return_count(self):
        damageDiscardTot = self.driver.find_element(By.XPATH, self.damage_return_col).get_attribute(
            'textContent')
        print("onholdTot:" + damageDiscardTot)
        return damageDiscardTot

    def get_rts_count(self):
        rtsTot = self.driver.find_element(By.XPATH, self.rts_col).get_attribute(
            'textContent')
        print("onholdTot:" + rtsTot)
        return rtsTot

    def get_lost_count(self):
        lostCountTot = self.driver.find_element(By.XPATH, self.lost_col).get_attribute(
            'textContent')
        print("onholdTot:" + lostCountTot)
        return lostCountTot

    def click_on_by_route(self):
        self.driver.find_element(By.ID, self.exception_by_route).click()

    def exception_drill_down_count(self):
        drill_down_count = self.driver.find_element(By.XPATH, self.exception_drill_down_grid1).get_attribute(
            'textContent')
        print("onholdTot:" + drill_down_count)
        return drill_down_count

    def verify_exception_drill_down_grid(self, exception_search_bar):
        time.sleep(2)
        self.driver.find_element(By.ID, self.exception_search_txt).click()
        time.sleep(4)
        self.driver.find_element(By.ID, self.exception_search_txt).send_keys(exception_search_bar)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_route_link).click()

    def verify_item_damage_will_be_delivered(self, item_text="blank"):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.route_tab_expand1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.route_tab_barcode).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.status_change).click()
        assert (self.isElementPresent(self.verify_code), "xpath")
        self.driver.find_element(By.XPATH, self.status_dropdown).click()
        self.driver.find_element(By.XPATH, self.exeption_status).click()
        self.driver.find_element(By.XPATH, self.exception_drpdwn).click()
        self.driver.find_element(By.XPATH, self.exception_searchBar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).send_keys(item_text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.exception_searchBar).send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.save_btn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.close_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def click_on_refresh_grid_btn(self):
        self.driver.find_element(By.ID, self.grid_refresh_btn).click()

    def click_on_clear_button(self):
        self.driver.find_element(By.ID, self.button_clear_search).click()

    def verify_damage_delivery_col(self):
        self.driver.find_element(By.XPATH, self.damage_delivery_col).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_damage_del_txt), "xpath")
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_damage_discard_col(self):
        self.driver.find_element(By.XPATH, self.damage_discard_col).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_discard_del_txt), "xpath")
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_damage_return_col(self):
        self.driver.find_element(By.XPATH, self.damage_return_col).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_return_del_txt), "xpath")
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_damage_lost_col(self):
        self.driver.find_element(By.XPATH, self.lost_col).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_lost_del_txt), "xpath")
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_rts_col(self):
        self.driver.find_element(By.XPATH, self.rts_col).click()
        time.sleep(2)
        assert (self.isElementPresent(self.facility_rts_del_txt), "xpath")
        self.driver.find_element(By.XPATH, self.close_btn).click()
