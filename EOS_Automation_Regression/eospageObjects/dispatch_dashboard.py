import sys
import time
from _ast import Assert
import pytest
from selenium.webdriver import Keys

sys.path.insert(1, 'C:/Users/pjarubula/Documents/EPCProject/EPCProject')
from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
# from utilities.CustomLogger import custlogger
from logging import Logger
from selenium.webdriver.support.ui import Select
from eospageObjects.bolt_menu import eos_bolt_menu
from eospageObjects.route_manager import eos_set_route_manager
from eospageObjects.facility_dashboard import eos_facility_dashboard
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class eos_dispatch_dashboard(Custom_code):
    # LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.facility_dashboard = None
        self.route_manager = None
        # self.screen_shot = Screen_shots(self.driver)

    dispatch_dashboard_id = "aDispatchDashboardLink"
    route_W952B = "//*[@id='route_11125']//span"
    # = "(//*[contains(text(),'1LSCXNU0031590')])[2]"
    search_map_input = "searchMapText"
    search_button = "//*[@title='Search']"
    collapse_route_results = "//*[@href='#collapseRouteResults']//div//span"
    route_results = "//*[@id='collapseRouteResults']//div//div//div//a"
    route_results2 = "(//*[contains(text(), 'Route Results')])[2]"
    route_WPB8 = "(//a[contains(@data-routeid, '179808') and contains(@class, 'clickable openRouteWindow')])[6]"
    expand_route_stop = "//*[contains(@id, 'iconRouteStopExpand')]"
    fas_fa_bars = "//*[@class='fas fa-bars']"
    contractor_edit_pencil = "//*[contains(@id, 'routeWindowAssignContractor')]"
    contractor_edit = "//*[contains(@id, 'routeWindowAssignContractor')]"
    stop_value = "//*[contains(@id, 'stopsRouteVals')]"
    route_window_maximize = "(//a[@aria-label='window-Maximize'])[2]"
    stops = "(//*[@class='divRouteStats']//span)[1]"
    stops_value = "//*[contains(@id, 'stopsRouteVals')]"
    packages = "//*[@class='divRouteStats']//span[2]"
    packages_value = "//*[contains(@id, 'totalRouteVals')]"
    pickup = "//*[@class='divRouteStats']//span[3]"
    pickup_value = "//*[contains(@id, 'pickupRouteVals')]"
    received = "//*[@class='divRouteStats']//span[4]"
    received_value = "//*[contains(@id, 'receivedRouteVals')]"
    loaded = "//*[@class='divRouteStats']//span[5]"
    loaded_value = "//*[contains(@id, 'loadedRouteVals')]"
    delivered = "//*[@class='divRouteStats']//span[6]"
    delivered_value = "//*[contains(@id, 'deliveredRouteVals')]"
    picked_up = "//*[@class='divRouteStats']//span[7]"
    picked_up_value = "//*[contains(@id, 'pickedUpRouteVals')]"
    attempts = "//*[@class='divRouteStats']//span[8]"
    attempts_value = "//*[contains(@id, 'attemptsRouteVals')]"
    exceptions = "//*[@class='divRouteStats']//span[9]"
    exceptions_value = "//*[contains(@id, 'exceptionsRouteVals')]"
    weight = "//*[@class='divRouteStats']//span[10]"
    weight_value = "//*[contains(@id, 'weightRouteVals')]"
    first_stop_in_route = "(//a[contains(@id, 'iconRouteStopExpand')])[1]"
    seq_column = "//th[(@data-title='Seq') and (@data-index='1')]//span//span//span"
    address_column = "//th[(@data-title='Address') and (@data-index='2')]//span//span//span"
    address2_column = "//th[(@data-title='Address 2') and (@data-index='3')]//span//span//span"
    city_column = "//th[(@data-title='City') and (@data-index='4')]//span//span//span"
    zip_column = "//th[(@data-title='Zip') and (@data-index='5')]//span//span//span"
    stopName_column = "//th[(@data-title='Stop Name') and (@data-index='6')]//span//span//span"
    attentionTo_column = "//th[(@data-title='Attention To') and (@data-index='7')]//span//span//span"
    customers_column = "//th[(@data-title='Customers') and (@data-index='8')]//span//span//span"
    weight_column = "//th[(@data-title='Weight') and (@data-index='9')]//span//span//span"
    scheduled_column = "//th[(@data-title='# Scheduled') and (@data-index='10')]//span//span//span"
    received_column = "//th[(@data-title='# Received') and (@data-index='11')]//span//span//span"
    duedate_column = "//th[(@data-title='Due Date') and (@data-index='12')]//span//span//span"
    custRoute_column = "//th[(@data-title='Cust Route') and (@data-index='13')]//span//span//span"
    custStop_column = "//th[(@data-title='Cust Stop') and (@data-index='14')]//span//span//span"
    coordinates_column = "//th[(@data-title='Coordinates') and (@data-index='15')]//span//span//span"
    status_column = "//th[(@data-title='Status') and (@data-index='16')]//span//span//span"
    first_stop_in_route_xpath = "(//a[contains(@id, 'iconRouteStopExpand')])[1]"

    barcode = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Barcode')]"
    customer = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Customer')]"
    service = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Service')]"
    description = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Description')]"
    status = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Status')]"
    originalEOD = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Original EDD')]"
    weight2 = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Weight')]"
    custRoute = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Cust Route')]"
    custStop = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Cust Stop')]"
    originalRoute = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'Original Route')]"
    references = "//div[@data-gridid='RouteWindowStopDetailGrid']//span//span//span[contains(text(), 'References')]"

    add_monitor = "//button[@title='Add Monitor']"
    lock = "//button[@title='Lock']"
    map_directions = "//button[@title='Map Directions']"
    export_gps_file = "//button[@title='Export GPS File']"
    barcodes_button = "//button[@title='Barcodes']"
    status_updates = "//button[@title='Status Updates']"
    manifest_button = "//button[@title='Manifest']"
    auto_sequence = "//button[@title='Auto Sequence']"
    sequence_button = "//*[contains(@id, 'btnSubmitAutosequence')]"
    select_all = "//input[@title='Select All']"
    specefic_address = "//*[contains(@id, 'rbStartSpecificAddress')]"
    editAddressStart = "//*[contains(@id, 'editAddressStart')]"
    editCityStart = "//*[contains(@id, 'editCityStart')]"
    editStateStart = "//*[contains(@id, 'editStateStart')]"
    editZipStart = "//*[contains(@id, 'editZipStart')]"
    auto_sequence_close_button = "//*[contains(@id, 'AutoSequence_Window_wnd_title')]//..//a"

    events_tab = "//li[contains(@id, 'routeTabstrip')]//*[contains(text(), ' Events')]"
    events_date = "//th[@data-field='EventDateTime']//span//span//span"
    events_stop_name = "(//th[@data-field='StopPointName']//span//span//span)[5]"
    events_barcode = "//div[@data-gridid='RouteEvents']//thead//tr//th[3]//span//span//span"
    events_type = "(//th[@data-field='EventCodeType']//span//span//span)[1]"
    events_detail = "(//th[@data-field='EventCode']//span//span//span)[1]"
    events_created_on = "(//th[@data-field='CreatedOn']//span//span//span)[3]"

    manifest_type = "//select[@id='ddlManifestType']"
    route_link = "//a[@class='clickable openRouteWindow'][position()=1]"
    # route_list_link = "//td[@role='gridcell']//a[contains(text(),'Z')]"
    route_list_link = "(//a[contains(@id,'lnkRouteFilter')])[position()=1]"
    click_route_menu = "//strong[contains(text(),'Route')]"
    select_route = "(//span[contains(text(),'Select a Route')])[position()=2]"
    select_route_dropdownlst = "//ul[contains(@id,'ddlMoveStopsSelectRoute')]/li[1]/span"
    select_route_dropdownlst1 = "//ul[contains(@id,'ddlMoveStopsSelectRoute')]/li[3]/span"
    routedropDownText = "//span[contains(@aria-owns,'ddlMoveStopsSelectRoute')]/descendant::span[2]"
    move_stopBtn = "//button[contains(@id,'btnMoveStops')]"
    dispatch_routeNum = "(//div[contains(@id,'route')]//span)[position()=2]"
    routeNum_txt = "//span[contains(@aria-controls,'ddlMoveStopsSelectRoute')]//span[@class='k-input-value-text']"
    package_txt = "(//td[@role='gridcell']//a[contains(@class,'clickable aTagWideSelector')])[position()=1]"
    select_first = "(//input[contains(@id,'routeStopPoint')])[position()=1]"
    route_movepopup = "//div[contains(text(),'Packages moved Successfully')]"
    close_btn = "//a[@aria-label='Close']"

    route_icon_on_dispatch_dashboard_modal_xpath = "(//span[text()='code'])[1]/parent::div[1]"
    rote_window_preffered_contract_id_field = "//div[contains(@id,'contractorAssignedToRoute')]/a"
    route_window_remove_contractor = "//i[contains(@id,'routeWindowRemoveContractor')]"
    route_window_close = "(//a[@aria-label='Close'])[2]"
    route_window_close1 = "(//a[@aria-label='Close'])[1]"
    unassigned_symbol = "//div[text()='Unassigned']"
    contractor_edit_dispatch = "//*[contains(@id, 'routeWindowAssignContractor')]"
    contractor_id_textfield_dispatch = "(//*[contains(@id, 'routeWindowContractorComplete')])[1]"
    route_lock_confirm_alert_id = "lockRouteConfirm"
    route_lock_confir_accept_btn_id = "btnConfirmYes"
    dynamic_route_stop_expand = "((//td[text()='stop_name'])[1]/..//a[1])[1]"
    dynamic_barcode_link = "((//td[text()='stop_name'])[1]/following::a[contains(@class,'viewPackageDetail')])[1]"
    route_window_button = "(//div[@class='divRouteWindowActionsContainer']//button[1])[1]"
    route_window_input = "//input[contains(@aria-controls,'ddlMoveStopsSelectRoute')]"
    move_stop_button = "//button[contains(@id,'btnMoveStops')]"
    lock_button = "//button[@title='Lock']//i[contains(@class,'fa-lock')]"
    
    master_row_time_picker_field = "(//div[@data-gridid='StatusUpdateGrid']//input[contains(@id,'timePicker')])[1]"
    child_row_time_picker_field = "(//div[@data-gridid='StatusUpdateChildGrid']//input[contains(@id,'timePicker')])[1]"
    status_update_drop_btn = "(//div[@data-gridid='StatusUpdateGrid']//button[contains(@class,'k-select')])[1]"
    master_row_time_picker = "(//button[contains(@aria-controls,'timePicker')])[1]"
    child_row_drop_field = "(//div[@data-gridid='StatusUpdateChildGrid']//span[@class='k-input-value-text'])[1]"
    unique_list_li = "//ul[@aria-hidden='false']/li"
    master_row_signature_field = "(//div[@data-gridid='StatusUpdateGrid']//input[contains(@id,'signature_')])[1]"
    child_row_signature_field = "(//div[@data-gridid='StatusUpdateChildGrid']//input[contains(@id,'signature_')])[1]"
    master_row_exception_optn_button = "(//div[@data-gridid='StatusUpdateGrid']//button[contains(@class,'k-select')])[3]"
    child_row_exception_option_field = "(//div[@data-gridid='StatusUpdateChildGrid']//span[@class='k-input-value-text'])[3]"
    master_door_tag = "(//div[@data-gridid='StatusUpdateGrid']//input[contains(@id,'doorTag')])[1]"
    child_door_tag = "(//div[@data-gridid='StatusUpdateChildGrid']//input[contains(@id,'doorTag')])[1]"
    second_master_row_time_picker = "(//button[contains(@aria-controls,'timePicker')])[3]"
    second_master_row_drop_btn = "(//div[@data-gridid='StatusUpdateGrid']//button[contains(@class,'k-select')])[7]"
    second_master_row_signature_field = "(//div[@data-gridid='StatusUpdateGrid']//input[contains(@id,'signature_')])[3]"
    submit_update_status = "btnSubmitStopStatuses"
    green_color_delivered_package_row = "(//tr[@class='k-master-row PODStatus'])[1]"
    orange_color_exception_row = "(//tr[@class='k-master-row ExceptionStatus'])[1]"
    status_update_button_cancel_button = "//div[contains(@id,'statusUpdate')]//button[normalize-space()='Cancel']"
    status_update_close_window_confirm_pop_up = "confirmWindowClose"
    status_update_ok_button = "//div[@id='confirmWindowClose']//button[text()='OK']"
    route_window_select_all_check_box = "[title='Select All']"
    route_monitor_auto_sequence_icon = "[title='Auto Sequence']"
    auto_sequence_widge_popup = ".divAutoSequenceStartEndLocation"
    submit_auto_sequence_btn = "//button[contains(@id,'btnSubmitAutosequence')]"
    route_monitor_lock_icon = "[title='Lock']"
    route_lock_confirm_alert_id = "lockRouteConfirm"
    route_lock_confir_accept_btn_id = "btnConfirmYes"
    route_monitor_status_update_icon = "[title='Status Updates']"
    status_update_window_header_modal_xpath = "//div[@data-gridid='StatusUpdateGrid']//thead//span[text()='temp_header']"
    show_pod_check_box_id = "chkShowPODStatuses"
    show_exception_check_box_id = "chkShowExceptionStatuses"
    status_update_expand_one_btn = "(//div[@data-gridid='StatusUpdateGrid']//a[@aria-label='Expand'])[1]"
    status_update_window_child_row_header_model_xpath = "//div[contains(@id,'statusChildGrid')]//th[text()='temp_header']"
    map_direction_button = "[title='Map Directions']"
    directions_dash_board_window_print_btn = "button[onclick='window.print()']"
    directions_dashboard_toggle_sequence_btn = "btnToggleSequence"
    directions_dashboard_toggle_directions_btn = "btnToggleDirections"
    directions_dash_board_map_picture = "printDirectionsMap"
    directions_container_section = "directionsContainer"
    directions_destination_address = "(//div[@id='directionsContainer']//strong)[1]"
    directions_blue_color_stop_icon = "[class='stopSequence']"

    windows_barcode1 = "(//*[contains(@id,'svgBarcode')]/descendant::*[@text-anchor='middle'])[1]"
    windows_customer1 = "//div[@class='barcodeRecord'][1]/descendant::div[1]"
    windows_address1 = "//div[contains(@id,'divAddress')][1]"
    route_seq1 = "(//span[contains(text(),'Route:')]/parent::div)[1]"

    expand_route_stop1 = "(//*[contains(@id, 'iconRouteStopExpand')])[1]"
    expand_route_stop2 = "(//*[contains(@id, 'iconRouteStopExpand')])[2]"
    expand_route_stop3 = "(//*[contains(@id, 'iconRouteStopExpand')])[3]"

    route_add_txt1 = "//tr[contains(@id, 'RouteDraggable')][1]/descendant::td[4]"
    route_stop_txt1 = "//tr[contains(@id, 'RouteDraggable')][1]/descendant::td[8]"
    route_customer_txt1 = "//tr[contains(@id, 'RouteDraggable')][1]/descendant::td[10]"

    route_barcode_txt1 = "(//*[contains(@id,'RouteDataList_Child')]/descendant::tbody/descendant::td[1])[1]"

    route_num_txt1 = "(//*[contains(@id,'RouteDataList_Child')]/descendant::tbody/descendant::td)[10]"
    lock_confirm_msg = "//div[@id='lockRouteConfirm']/descendant::div[1]"
    yellow_status_bar = "//div[@class='statusBar yellowStatus']"
    green_status_bar = "//div[@class='statusBar greenStatus']"
    red_status_bar = "//div[@class='statusBar redStatus']"
    route_close = "(//a[@aria-label='Close'])[2]"
    event_time_icon = "(//button[@aria-label='Open the time view'])[2]"
    event_time_drop_down_select = "//ul[contains(@id,'dateTimePicker')]/descendant::li[5]/span"
    no_route_found_section = "//div[text()='No Results Found']"
    open_lock_icon = "//button[@title='Lock']//i[contains(@class,'fa-lock-open')]"

    def click_dispatch_dashboard(self):
        self.click_on_element(self.fas_fa_bars, "xpath")
        self.click_on_element(self.dispatch_dashboard_id)

    def click_route_w952b(self):
        self.click_on_element(self.route_W952B)

    def click_barcode_in_dashboard(self):
        # self.get_element("(//*[contains(text(),'1LSCXNU0031590')])[2]")
        self.click_on_element("(//*[contains(text(),'1LSCXNU0031590')])[2]", "xpath")

    def search_route_and_click(self, route_name):
        self.send_keys_to(self.search_map_input, route_name)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(1)
        self.click_on_element(self.collapse_route_results, "xpath")
        time.sleep(1)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(1)
        self.click_on_element(self.expand_route_stop, "xpath")
        time.sleep(1)
        self.click_on_element("(//*[contains(text(),'1LSCXNU0037925')])[2]", "xpath")

    def search_and_open_package(self, barcode):
        self.send_keys_to(self.search_map_input, barcode)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(5)
        self.click_on_element("(//*[contains(text(),'" + barcode + "')])[2]", "xpath")
        time.sleep(3)

    def click_contractor_edit_pencil(self):
        self.click_on_element(self.click_contractor_edit_pencil(), "xpath")
        self.send_keys_to(self.contractor_edit, "30310", "xpath")
        self.click_on_element(self.stop_value, "xpath")

    def click_auto_sequence(self):
        self.click_on_element(self.select_all, "xpath")
        time.sleep(1)
        self.click_on_element(self.auto_sequence, "xpath")
        time.sleep(1)
        self.click_on_element(self.sequence_button, "xpath")
        time.sleep(2)

    def validate_autosequence_specific_address(self):
        self.click_on_element(self.auto_sequence, "xpath")
        time.sleep(1)
        self.click_on_element(self.specefic_address, "xpath")
        time.sleep(1)
        # editAddressStart_actual = self.driver.find_element_by_xpath(self.editAddressStart).get_attribute('textContent')
        editAddressStart_actual = self.driver.find_element(By.XPATH, self.editAddressStart).get_attribute('textContent')
        print("editAddressStart_actual: " + editAddressStart_actual)
        assert editAddressStart_actual == "362 N HAVERHILL RD"
        # editCityStart_actual = self.driver.find_element_by_xpath(self.editCityStart).get_attribute('textContent')
        editCityStart_actual = self.driver.find_element(By.XPATH, self.editCityStart).get_attribute('textContent')
        assert editCityStart_actual == "WEST PALM BEACH"
        # editStateStart_actual = self.driver.find_element_by_xpath(self.editStateStart).get_attribute('textContent')
        editStateStart_actual = self.driver.find_element(By.XPATH, self.editStateStart).get_attribute('textContent')
        assert editStateStart_actual == "FL"
        # editZipStart_actual = self.driver.find_element_by_xpath(self.editZipStart).get_attribute('textContent')
        editZipStart_actual = self.driver.find_element(By.XPATH, self.editZipStart).get_attribute('textContent')
        assert editZipStart_actual == "33415-2032"
        self.click_on_element(self.click_on_element(self.auto_sequence_close_button, "xpath"))
        # the actual addresses are not in html tree so we cant really use this function

    def click_manifest(self):
        self.click_on_element(self.manifest_button, "xpath")

    def click_manifest_type(self):
        # self.click_on_element(self.manifest_type, "xpath")
        # self.select_values_from_drop_down()
        # select = Select(self.driver.find_element_by_xpath(self.manifest_type))
        select = Select(self.driver.find_element(By.XPATH, self.manifest_type))
        select.select_by_visible_text("Manifest Condensed")
        time.sleep(1)
        select.select_by_visible_text("Load")
        time.sleep(1)
        select.select_by_visible_text("Load Condensed")
        time.sleep(1)
        select.select_by_visible_text("Manifest")

    def search_route_and_click2(self, route_name):
        time.sleep(5)
        self.send_keys_to(self.search_map_input, route_name)
        time.sleep(2)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.route_results2, "xpath")
        time.sleep(4)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(2)
        self.click_on_element(self.route_window_maximize, "xpath")
        time.sleep(2)

    def verify_route_stats_are_present(self):
        assert (self.isElementPresent(self.stops, "xpath"))
        assert (self.isElementPresent(self.stops_value, "xpath"))
        assert (self.isElementPresent(self.packages, "xpath"))
        assert (self.isElementPresent(self.packages_value, "xpath"))
        assert (self.isElementPresent(self.pickup, "xpath"))
        assert (self.isElementPresent(self.pickup_value, "xpath"))
        assert (self.isElementPresent(self.received, "xpath"))
        assert (self.isElementPresent(self.received_value, "xpath"))
        assert (self.isElementPresent(self.loaded, "xpath"))
        assert (self.isElementPresent(self.loaded_value, "xpath"))
        assert (self.isElementPresent(self.delivered, "xpath"))
        assert (self.isElementPresent(self.delivered_value, "xpath"))
        assert (self.isElementPresent(self.picked_up, "xpath"))
        assert (self.isElementPresent(self.picked_up_value, "xpath"))
        assert (self.isElementPresent(self.attempts, "xpath"))
        assert (self.isElementPresent(self.attempts_value, "xpath"))
        assert (self.isElementPresent(self.exceptions, "xpath"))
        assert (self.isElementPresent(self.exceptions_value, "xpath"))
        assert (self.isElementPresent(self.weight, "xpath"))
        assert (self.isElementPresent(self.weight_value, "xpath"))

    def verify_elements_in_manifest(self):
        self.click_on_element(self.seq_column, "xpath")
        assert (self.isElementPresent(self.address_column, "xpath"))
        assert (self.isElementPresent(self.address2_column, "xpath"))
        assert (self.isElementPresent(self.city_column, "xpath"))
        assert (self.isElementPresent(self.zip_column, "xpath"))
        assert (self.isElementPresent(self.stopName_column, "xpath"))
        assert (self.isElementPresent(self.attentionTo_column, "xpath"))
        assert (self.isElementPresent(self.customers_column, "xpath"))
        assert (self.isElementPresent(self.weight_column, "xpath"))
        assert (self.isElementPresent(self.scheduled_column, "xpath"))
        assert (self.isElementPresent(self.received_column, "xpath"))
        assert (self.isElementPresent(self.duedate_column, "xpath"))
        assert (self.isElementPresent(self.custRoute_column, "xpath"))
        assert (self.isElementPresent(self.custStop_column, "xpath"))
        assert (self.isElementPresent(self.coordinates_column, "xpath"))
        assert (self.isElementPresent(self.status_column, "xpath"))

    def verify_elements_in_package_drilldown(self):
        self.click_on_element(self.first_stop_in_route_xpath, "xpath")
        assert (self.isElementPresent(self.barcode, "xpath"))
        assert (self.isElementPresent(self.customer, "xpath"))
        assert (self.isElementPresent(self.service, "xpath"))
        assert (self.isElementPresent(self.description, "xpath"))
        assert (self.isElementPresent(self.status, "xpath"))
        assert (self.isElementPresent(self.originalEOD, "xpath"))
        assert (self.isElementPresent(self.weight2, "xpath"))
        assert (self.isElementPresent(self.custRoute, "xpath"))
        assert (self.isElementPresent(self.custStop, "xpath"))
        assert (self.isElementPresent(self.originalRoute, "xpath"))
        assert (self.isElementPresent(self.references, "xpath"))

    def verify_route_actions_buttons(self):
        assert (self.isElementPresent(self.add_monitor, "xpath"))
        assert (self.isElementPresent(self.lock, "xpath"))
        assert (self.isElementPresent(self.map_directions, "xpath"))
        assert (self.isElementPresent(self.export_gps_file, "xpath"))
        assert (self.isElementPresent(self.barcodes_button, "xpath"))
        assert (self.isElementPresent(self.status_updates, "xpath"))
        assert (self.isElementPresent(self.auto_sequence, "xpath"))

    def verify_events_tab_columns(self):
        self.click_on_element(self.events_tab, "xpath")
        time.sleep(2)
        assert (self.isElementPresent(self.events_date, "xpath"))
        assert (self.isElementPresent(self.events_stop_name, "xpath"))
        assert (self.isElementPresent(self.events_barcode, "xpath"))
        assert (self.isElementPresent(self.events_type, "xpath"))
        assert (self.isElementPresent(self.events_detail, "xpath"))
        assert (self.isElementPresent(self.events_created_on, "xpath"))

    def change_route_from_manifest_tab(self):
        self.eos_bolt_menu = eos_bolt_menu(self.driver)
        self.click_on_element(self.eos_bolt_menu.bolt_menu)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_route_menu).click()
        self.driver.find_element(By.XPATH, self.route_list_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_all).click()
        self.driver.find_element(By.XPATH, self.select_route).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_route_dropdownlst).click()
        self.driver.find_element(By.XPATH, self.move_stopBtn).click()

    def select_boltMenu_route_lst(self):
        self.eos_bolt_menu = eos_bolt_menu(self.driver)
        time.sleep(2)
        self.click_on_element(self.eos_bolt_menu.bolt_menu)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_route_menu).click()
        self.driver.find_element(By.XPATH, self.route_list_link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_all).click()
        self.driver.find_element(By.XPATH, self.select_route).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_route_dropdownlst1).click()
        time.sleep(5)
        routetext = self.driver.find_element(By.XPATH, self.routedropDownText).get_attribute('textContent')
        self.driver.find_element(By.XPATH, self.move_stopBtn).click()
        self.driver.find_element(By.XPATH, self.close_btn).click()
        return routetext

    def click_on_CloseBtn(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_assigned_route_package(self):
        self.driver.find_element(By.XPATH, self.select_all).click()
        packageAddbefore = self.driver.find_element(By.XPATH, self.package_txt).get_attribute('textContent')
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_route).click()
        self.driver.find_element(By.XPATH, self.select_route_dropdownlst1).click()
        get_package = self.driver.find_element(By.XPATH, self.route_link).get_attribute('textContent')
        self.search_route_and_click2(get_package)
        packageAddAfter = self.driver.find_element(By.XPATH, self.package_txt).get_attribute('textContent')
        if packageAddbefore == packageAddAfter:
            print("Values match as expected")
        else:
            print("Values do not match as expected")

    def verify_route_icon_color(self, route, preffered_contractor_id):
        self.click_on_element(self.dispatch_dashboard_id)
        time.sleep(10)
        assert self.get_element(self.route_icon_on_dispatch_dashboard_modal_xpath.replace("code", route),
                                "xpath").value_of_css_property('background-color') == "rgba(0, 165, 79, 0.7)"
        self.send_keys_to(self.search_map_input, route)
        time.sleep(5)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(2)
        self.click_on_element(self.collapse_route_results, "xpath")
        time.sleep(2)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(5)
        assert self.get_element(self.rote_window_preffered_contract_id_field, "xpath").get_attribute(
            "textContent") == preffered_contractor_id
        self.click_on_element(self.route_window_remove_contractor, "xpath")
        time.sleep(3)
        self.click_on_element(self.route_window_close, "xpath")
        time.sleep(2)
        self.click_on_element(self.route_window_close1, "xpath")
        time.sleep(3)

    def navigate_to_dispatch_dashboard(self):
        self.click_on_element(self.dispatch_dashboard_id)
        time.sleep(10)

    def select_route_icon_from_search_tab(self, route):
        time.sleep(10)
        self.send_keys_to(self.search_map_input, route)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(15)
        self.click_on_element(self.collapse_route_results, "xpath")
        time.sleep(3)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(3)

    def assign_contractor_to_rout(self, contractorId):
        if self.isElementPresent(self.unassigned_symbol, "xpath"):
            self.click_on_element(self.contractor_edit_dispatch, "xpath")
            time.sleep(2)
            self.send_keys_to(locator=self.contractor_id_textfield_dispatch, data=contractorId, locator_type="xpath")
            time.sleep(3)
            action = ActionChains(self.driver)
            action.send_keys(Keys.TAB)
            action.perform()
            time.sleep(3)

    def click_lock_icon(self):
        self.click_on_element(self.select_all, "xpath")
        time.sleep(1)
        self.click_on_element(self.lock, "xpath")
        time.sleep(2)
        assert self.isElementPresent(self.route_lock_confirm_alert_id)
        self.click_on_element(self.route_lock_confir_accept_btn_id)
        time.sleep(2)

    def open_advance_search_barcode_from_dispatch_board(self, stop_name):
        time.sleep(5)
        self.click_on_element(self.dynamic_route_stop_expand.replace("stop_name", stop_name), "xpath")
        time.sleep(2)
        self.click_on_element(self.dynamic_barcode_link.replace("stop_name", stop_name), "xpath")
        time.sleep(10)

    def close_both_windows(self):
        time.sleep(2)
        self.click_on_element(self.route_window_close, "xpath")
        time.sleep(2)
        self.click_on_element(self.route_window_close1, "xpath")

    def remove_contractor_id(self):
        time.sleep(3)
        self.click_on_element(self.route_window_remove_contractor, "xpath")
        time.sleep(3)

    def move_package_to_another_route(self, route):
        self.click_on_element(self.select_all, "xpath")
        time.sleep(1)
        if not self.get_element(self.select_all, "xpath").is_selected():
            self.click_on_element(self.select_all, "xpath")
            time.sleep(1)
        self.click_on_element(self.route_window_button, "xpath")
        time.sleep(2)
        self.send_keys_to(locator=self.route_window_input, data=route, locator_type="xpath")
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(3)
        self.click_on_element(self.move_stop_button, "xpath")
        time.sleep(5)

    def verify_route_lock_status(self):
        if self.isElementPresent("//div[text()='No Results Found']", "xpath"):
            self.click_on_element(self.route_window_close1, "xpath")
        if self.isElementPresent(self.lock_button, "xpath"):
            self.click_lock_icon()
            self.close_both_windows()

    def click_on_barcode(self):
        self.driver.find_element(By.XPATH, self.barcodes_button).click()
        self.click_on_element(self.barcodes_button)

    def verify_barcode_add_vals(self):
        self.driver.find_element(By.XPATH, self.expand_route_stop1).click()
        route_address_txt1 = self.driver.find_element(By.XPATH, self.route_add_txt1).get_attribute('textContent')
        print("route_address_txt1:" + route_address_txt1)
        route_customerTxt1 = self.driver.find_element(By.XPATH, self.route_customer_txt1).get_attribute('textContent')
        print("route_customerTxt1:" + route_customerTxt1)
        route_barcodeTxt1 = self.driver.find_element(By.XPATH, self.route_barcode_txt1).get_attribute('textContent')
        print("route_barcodeTxt1:" + route_barcodeTxt1)
        route_numberTxt1 = self.driver.find_element(By.XPATH, self.route_num_txt1).get_attribute('textContent')
        print("route_numberTxt1:" + route_numberTxt1)
        time.sleep(3)
        self.click_on_barcode()
        time.sleep(20)
        all_windows = self.driver.window_handles
        # Switch to the new window
        time.sleep(10)
        self.driver.switch_to.window(all_windows[1])
        time.sleep(3)
        window_customerTxt1 = self.driver.find_element(By.XPATH, self.windows_customer1).get_attribute('textContent')
        print("window_customerTxt1:" + window_customerTxt1)
        time.sleep(3)
        assert route_customerTxt1.strip() == window_customerTxt1.strip()
        time.sleep(2)
        window_add1 = self.driver.find_element(By.XPATH, self.windows_address1).get_attribute('textContent')
        window_addT1 = window_add1.split()[0]
        window_addT2 = window_add1.split()[1]
        window_addT3 = window_add1.split()[2]
        window_addT4 = window_addT1 + " " + window_addT2 + " " + window_addT3
        print("window_add1:" + window_addT4)
        assert route_address_txt1.strip() == window_addT4
        time.sleep(2)
        route_seq_txt1 = self.driver.find_element(By.XPATH, self.route_seq1).get_attribute('textContent')
        route_seq_txtT1 = route_seq_txt1.split()[1]
        print("route_seq_txt1:" + route_seq_txtT1)
        assert route_numberTxt1.strip() == route_seq_txtT1.strip()
        time.sleep(2)
        windows_barcode_txt1 = self.driver.find_element(By.XPATH, self.windows_barcode1).get_attribute('textContent')
        print("windows_barcode_txt1:" + windows_barcode_txt1)
        assert route_barcodeTxt1.strip() == windows_barcode_txt1.strip()

    def search_and_open_route_maps(self, route_name):
        time.sleep(5)
        self.send_keys_to(self.search_map_input, route_name)
        time.sleep(2)
        self.click_on_element(self.search_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.route_results2, "xpath")
        time.sleep(4)
        self.click_on_element(self.route_results, "xpath")
        time.sleep(2)

    def verify_and_add_monitor(self, saved_popup):
        self.route_manager = eos_set_route_manager(self.driver)
        assert (self.isElementPresent(self.add_monitor, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_monitor).click()
        self.driver.find_element(By.XPATH, self.add_monitor).click()
        self.wait_for_element_clickable(self.route_manager.alert_notification_css, "css", 30)
        popup_alert_txt = self.get_element(self.route_manager.alert_notification_css, "css").get_attribute(
            'textContent')
        print("popup_alert_txt:" + popup_alert_txt)
        print("saved_popup:" + saved_popup)
        assert saved_popup == popup_alert_txt

    def click_check_all_and_sequence_lock(self, confirm_msg):
        time.sleep(2)
        self.click_auto_sequence()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.lock).click()
        time.sleep(2)
        lock_confirm_txt = self.driver.find_element(By.XPATH, self.lock_confirm_msg).get_attribute('textContent')
        print("lock_confirm_txt:" + lock_confirm_txt)
        print("lock_confirm_txt1:" + confirm_msg)
        assert confirm_msg == lock_confirm_txt
        time.sleep(2)
        self.driver.find_element(By.ID, self.route_lock_confir_accept_btn_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.lock).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.route_lock_confir_accept_btn_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.route_close).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_and_select_delivered_package_staus_vals(self, status="blank"):
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        print("status:" + status)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.drop_down_status_arrow).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.drop_down_status_text).click()
        time.sleep(2)
        self.facility_dashboard.click_on_save_button()
        time.sleep(10)

    def verify_and_select_attempt_package_staus_vals(self, status_out="blank", status="blank", drop="blank"):
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(6)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        print("staus0:" + status_out)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status_out)
        time.sleep(2)
        self.facility_dashboard.click_on_save_button()
        time.sleep(10)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        print("status:" + status)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.event_time_icon).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.event_time_drop_down_select).click()
        time.sleep(2)
        self.facility_dashboard.click_on_attempt_drp_down()
        time.sleep(3)
        self.facility_dashboard.select_attempt_reason(drop)
        print("attempt:" + drop)
        self.facility_dashboard.click_on_save_button()
        time.sleep(15)

    def verify_and_select_exception_staus_vals(self, status="blank", drop="blank"):
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.facility_dashboard.barcode_res).click()
        time.sleep(2)
        self.facility_dashboard.click_on_status_pencil_icon()
        time.sleep(2)
        self.facility_dashboard.click_on_status_drop_down()
        time.sleep(2)
        print("status:" + status)
        self.facility_dashboard.change_the_status_to_out_for_delivery(status)
        time.sleep(2)
        self.facility_dashboard.click_on_attempt_drp_down()
        time.sleep(2)
        self.facility_dashboard.select_attempt_reason(drop)
        print("attempt:" + drop)
        self.facility_dashboard.click_on_save_button()
        time.sleep(10)

    def verify_green_status_bar(self):
        assert (self.isElementPresent(self.green_status_bar), "xpath")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_yellow_status_bar(self):
        assert (self.isElementPresent(self.yellow_status_bar), "xpath")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def verify_red_status_bar(self):
        assert (self.isElementPresent(self.red_status_bar), "xpath")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.close_btn).click()

    def select_route_from_boult_menu(self, rout_name):
        self.eos_bolt_menu = eos_bolt_menu(self.driver)
        time.sleep(2)
        self.click_on_element(self.eos_bolt_menu.bolt_menu)
        time.sleep(3)
        self.click_on_element(self.click_route_menu,'xpath')
        time.sleep(3)
        self.click_on_element(rout_name, "link")
        time.sleep(5)
        self.click_on_element(self.eos_bolt_menu.bolt_menu)
        time.sleep(3)

    def verify_status_update_functionalities(self,items_to_validate,child_row_coloumns):
        self.click_on_element(self.route_window_select_all_check_box,"css")
        time.sleep(2)
        self.click_on_element(self.route_monitor_auto_sequence_icon, "css")
        time.sleep(3)
        assert self.isElementPresent(self.auto_sequence_widge_popup,"css")
        time.sleep(3)
        self.click_on_element(self.submit_auto_sequence_btn,"xpath")
        time.sleep(3)
        self.click_on_element(self.route_window_select_all_check_box, "css")
        time.sleep(2)
        self.click_on_element(self.route_monitor_lock_icon, "css")
        time.sleep(2)
        assert self.isElementPresent(self.route_lock_confirm_alert_id)
        self.click_on_element(self.route_lock_confir_accept_btn_id)
        time.sleep(2)
        assert self.isElementPresent(self.route_monitor_status_update_icon,"css")
        self.click_on_element(self.route_monitor_status_update_icon,"css")
        time.sleep(5)
        for x in items_to_validate:
            assert self.isElementPresent(self.status_update_window_header_modal_xpath.replace("temp_header", x),"xpath"),"Coloumn "+x+" was not present"
        assert self.isElementPresent(self.show_pod_check_box_id) , "Show POD check box was not present"
        assert self.isElementPresent(self.show_exception_check_box_id) , "Show Exception Check box was not present"
        self.click_on_element(self.status_update_expand_one_btn,"xpath")
        time.sleep(5)
        for x in child_row_coloumns:
            assert self.isElementPresent(self.status_update_window_child_row_header_model_xpath.replace("temp_header", x),"xpath"),"Coloumn "+x+" was not present"

    def status_update_window_input_functionality(self,event_time,drop_location,signature,exception_value,door_tag):
        time.sleep(3)
        self.click_on_element(self.master_row_time_picker,"xpath")
        time.sleep(5)
        all_times = self.get_elements(self.unique_list_li,"xpath")
        self.select_values_from_drop_down(all_times,event_time)
        self.click_on_element(self.status_update_drop_btn,"xpath")
        time.sleep(3)
        all_drop_list=self.get_elements(self.unique_list_li,"xpath")
        self.select_values_from_drop_down(all_drop_list,drop_location)
        time.sleep(3)
        self.send_keys_to(self.master_row_signature_field,signature,"xpath")
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(3)
        child_time = self.get_element(self.child_row_time_picker_field, "xpath").get_attribute("value")
        child_drop_value = self.get_element(self.child_row_drop_field, "xpath").get_attribute("textContent")
        child_signature_field = self.get_element(self.child_row_signature_field, "xpath").get_attribute("value")
        assert child_time == event_time
        assert child_drop_value == drop_location
        assert child_signature_field == signature
        time.sleep(5)
        self.click_on_element(self.master_row_exception_optn_button,"xpath")
        time.sleep(3)
        all_exception = self.get_elements(self.unique_list_li, "xpath")
        self.select_values_from_drop_down(all_exception,exception_value)
        self.send_keys_to(self.master_door_tag,door_tag,"xpath")
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(4)
        child_exception_val = self.get_element(self.child_row_exception_option_field, "xpath").get_attribute(
            "textContent")
        child_door_value = self.get_element(self.child_door_tag, "xpath").get_attribute("value")
        assert child_exception_val == exception_value
        assert child_door_value == door_tag
        self.click_on_element(self.status_update_expand_one_btn, "xpath")
        time.sleep(5)
        self.click_on_element(self.second_master_row_time_picker,'xpath')
        time.sleep(5)
        all_times = self.get_elements(self.unique_list_li, "xpath")
        self.select_values_from_drop_down(all_times, event_time)
        self.click_on_element(self.second_master_row_drop_btn, "xpath")
        time.sleep(3)
        all_drop_list = self.get_elements(self.unique_list_li, "xpath")
        self.select_values_from_drop_down(all_drop_list, drop_location)
        time.sleep(3)
        self.send_keys_to(self.second_master_row_signature_field, signature, "xpath")
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(5)
        self.click_on_element(self.submit_update_status)
        time.sleep(10)

    def verify_show_PODS_and_Show_execptions_functionality(self):
        self.click_on_element(self.route_monitor_status_update_icon, "css")
        time.sleep(5)
        self.click_on_element(self.show_pod_check_box_id)
        time.sleep(5)
        assert self.isElementPresent(self.green_color_delivered_package_row,"xpath") , "green color row was not displayed"
        time.sleep(5)
        self.click_on_element(self.show_pod_check_box_id)
        time.sleep(5)
        self.click_on_element(self.show_exception_check_box_id)
        time.sleep(5)
        assert self.isElementPresent(self.orange_color_exception_row,
                                     "xpath"), "orange color row was not displayed"
        self.click_on_element(self.status_update_button_cancel_button,"xpath")
        time.sleep(3)
        assert self.isElementPresent(self.status_update_close_window_confirm_pop_up) ,"The Confirm Close popup was not appeared"
        self.click_on_element(self.status_update_ok_button,'xpath')

    def click_on_map_directions_button(self):
        self.click_on_element(self.map_direction_button,"css")
        time.sleep(5)

    def validate_map_direction_tab(self,address1,city,zip_code):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(10)
        assert self.driver.title == "Directions" ,"Directions tab should be open"
        assert self.isElementPresent(self.directions_dash_board_window_print_btn,"css"),"Directions tab should have Print btn"
        assert self.isElementPresent(self.directions_dashboard_toggle_sequence_btn),"Directions tab should have Hide sequence button"
        assert self.isElementPresent(self.directions_dashboard_toggle_directions_btn),"Directions tab should have Hide directions button"
        assert self.isElementPresent(self.directions_dash_board_map_picture),"Directions tab should have map section"
        assert self.isElementPresent(self.directions_container_section) , "direction tab should have drrections sections"
        destination_address_text = self.get_element(self.directions_destination_address,"xpath").get_attribute("textContent")
        assert address1 in destination_address_text ,"destination address was not correct"
        assert city in destination_address_text,"destination address was not correct"
        assert zip_code in destination_address_text,"destination address was not correct"
        self.click_on_element(self.directions_dashboard_toggle_sequence_btn)
        time.sleep(5)
        assert self.get_element(self.directions_dashboard_toggle_sequence_btn).get_attribute("textContent") == "Show Sequence" ,"Hide sequence button name was not changed"
        assert not self.get_element(self.directions_blue_color_stop_icon,"css").is_displayed() , "stop sequence bue mark was not disappeared"
        self.click_on_element(self.directions_dashboard_toggle_sequence_btn)
        time.sleep(5)
        assert self.get_element(self.directions_dashboard_toggle_sequence_btn).get_attribute("textContent") == "Hide Sequence" ,"Show sequence button name was not changed"
        assert self.get_element(self.directions_blue_color_stop_icon,
                                    "css").is_displayed(), "stop sequence bue mark was not Present"
        self.click_on_element(self.directions_dashboard_toggle_directions_btn)
        time.sleep(2)
        assert self.get_element(self.directions_dashboard_toggle_directions_btn).get_attribute(
            "textContent") == "Show Directions", "Hide Directions button name was not changed"
        assert not self.get_element(self.directions_container_section).is_displayed(), "Direction section was not disappeared"
        self.click_on_element(self.directions_dashboard_toggle_directions_btn)
        time.sleep(2)
        assert self.get_element(self.directions_dashboard_toggle_directions_btn).get_attribute(
            "textContent") == "Hide Directions", "Show Directions button name was not changed"
        assert self.get_element(self.directions_container_section).is_displayed(), "Direction section was not Present"

    def clear_all_packages_in_rote(self,route,backup_route):
        try:
            self.navigate_to_dispatch_dashboard()
            self.select_route_icon_from_search_tab(route)
            if self.isElementPresent(self.no_route_found_section, "xpath"):
                self.click_on_element(self.route_window_close1, "xpath")
                return
        except:
            self.click_on_element(self.route_window_close1,"xpath")
            return
        try:
            if not self.isElementPresent(self.open_lock_icon, "xpath"):
                self.click_lock_icon()
            self.move_package_to_another_route(backup_route)
            time.sleep(10)
            self.close_both_windows()
        except:
            self.close_both_windows()










