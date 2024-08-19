import os
import time
from datetime import datetime
from logging import Logger
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.CustomLogger import custlogger

class Custom_code():
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "partial link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.LOG.info("locator type not supported")
            return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.LOG.info("Element found with locator: " + locator +
                          " and  locatorType: " + locator_type)
            return element
        except:
            self.LOG.warning("Element not found with locator: " + locator +
                             " and locatorType: " + locator_type)
            return element

        # except NoSuchElementException:
        #     self.LOG.warning("Element {0} not found".format(locator))

    # def click_on_element(self, locator, locator_type="id"):
    #     element = self.get_element(locator, locator_type)
    #     time.sleep(10)
    #     element.click()

    def click_on_element(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.LOG.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.LOG.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)

    def clear_field(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            self.LOG.info("Cleared field with locator:" + locator +
                          " locatorType: " + locator_type)
        except:
            self.LOG.info("Cannot clear the field with locator:" + locator +
                          "locatorType:" + locator_type)

    def send_keys_to(self, locator, data="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.LOG.info("Sent data on element with locator:" + locator + "locatorType:" + locator_type)
        except:
            self.LOG.info("Cannot send data on the element with locator: " + locator + "locatorType:" + locator_type)

        # element = self.get_element(locator, locator_type)
        # element.send_keys(data)

    def take_screenshot(self, driver, testcase_name="", module_name=""):
        test_name = testcase_name.replace(" ", "_")
        test_name = test_name.replace(" ", "_")
        date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        date = date.replace('', "_")
        date = date.replace(':', "_")
        date = date.replace(',', '')
        date = "_DATE_" + date

        fileDir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.dirname(fileDir) + \
                    "\\Screenshots\\" + module_name + "\\" + testcase_name + date + '.png'

        print(file_path)
        driver.save_screenshot(file_path)

    def select_values_from_drop_down(self, dropDownOptionsList, value):
        # print(len(dropDownOptionsList))

        element_find = "N"
        for element in dropDownOptionsList:
            # print(element.text)
            if element.text == value:
                element.click()
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        # print(element_find)
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            if element is not None:
                self.LOG.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.LOG.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def ElementPresent_and_click(self, locator="", locatorType="id", element=None):

        try:
            if locator:
                element = self.get_element(locator, locatorType)
            if element is not None:
                element.click()
                self.LOG.info("Element clickble with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.LOG.info("Element not present with locatorhhhh: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not Found")
            return False

    def sleep1(self):
        time.sleep(1)

    def sleep2(self):
        time.sleep(2)

    def sleep3(self):
        time.sleep(3)

    def sleep5(self):
        time.sleep(5)

    def imp_wait_20(self):
        self.driver.implicitly_wait(20)

    def imp_wait_20_and_then_sleep1(self):
        self.imp_wait_20()
        self.sleep1()

    def imp_wait_20_and_then_sleep2(self):
        self.imp_wait_20()
        self.sleep2()

    def imp_wait_8_and_then_sleep2(self):
        self.driver.implicitly_wait(10)

    def imp_wait_5_and_then_sleep2(self):
        self.driver.implicitly_wait(5)
        self.sleep2()

    def select_values_from_drop_down_textContent(self, dropDownOptionsList, value):
        # shafiul added this on 04/15/2022. In EOS some dropdowns text not readable with element.text.
        # I needed to use element.get_attirbute('textContent')
        # "Status:Out for delivery option not working
        time.sleep(2)
        print(len(dropDownOptionsList))
        element_find = "N"
        for element in dropDownOptionsList:
            time.sleep(3)
            # print(element.get_attribute('textContent'))
            if element.get_attribute('textContent') == value:
                element.click()
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        # print(element_find)
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))

    def select_values_from_drop_down_index(self, dropDownOptionsList, value):
        # shafiul added this on 04/28/2022.

        print(len(dropDownOptionsList))
        element_find = "N"
        for element in dropDownOptionsList:
            print(element.get_attribute('data-offset-index'))
            if element.get_attribute('data-offset-index') == value:
                element.click()
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        # print(element_find)
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))
    def wait_for_element_clickable(self, locator, locator_type="id", timeOut=10):
        WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable( (self.get_by_type(locator_type), locator)))

    def wait_for_element_not_clickable(self, locator, locator_type="id", timeOut=10):
        WebDriverWait(self.driver, timeOut).until_not(EC.element_to_be_clickable( (self.get_by_type(locator_type), locator)))

    def context_click(self,locator, locator_type="id"):
        action = ActionChains(self.driver)
        action.context_click(self.get_element(locator, locator_type)).perform()
        time.sleep(1)

    def get_elements(self, locator, locator_type="id"):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.LOG.info("Elements found with locator: " + locator +
                          " and  locatorType: " + locator_type)
            return elements
        except:
            self.LOG.warning("Elements not found with locator: " + locator +
                             " and locatorType: " + locator_type)
            return elements
    def page_refresh_and_wait(self, timeOut=5):
        self.driver.refresh()
        time.sleep(timeOut)

    def select_values_from_drop_down_with_JS(self, dropDownOptionsList, value, timeOut=10):
        # Facility:Columbus (083) selection not working
        element_find = "N"
        for element in dropDownOptionsList:
            if element.text == value:
                WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable(element))
                self.driver.execute_script("arguments[0].click();", element)
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        # print(element_find)
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))

    def select_values_from_drop_down_textContent_JS(self, dropDownOptionsList, value, timeOut=10):
        # "Status:Out for delivery option not working
        time.sleep(2)
        print(len(dropDownOptionsList))
        element_find = "N"
        for element in dropDownOptionsList:
            time.sleep(3)
            # print(element.get_attribute('textContent'))
            if element.get_attribute('textContent') == value:
                # WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable(element))
                self.driver.execute_script("arguments[0].click();", element)
                element_find = "y"
                self.LOG.info("Selected value from dropdown: " + "value:" + value)
                break
        if element_find == "N":
            self.LOG.warning("Cannot select value from dropdown: " + "value:" + str(value))