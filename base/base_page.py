import xml.etree.ElementTree as ET
from traceback import print_stack

import psycopg2
from selenium.webdriver.support.select import Select

from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class BasePage(SeleniumDriver):
    """
    Init Base page
    """

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title
        :param title_to_verify: Title on the page which need to verif
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def find_element_by_selector_and_text(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for domElement in selector:
                if domElement.text == text:
                    return domElement
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def find_element_by_selector_and_text_contains(self, selector, text):
        """
        Find the page element by selector and text
        :param selector: The selectors list
        :param text: The unique text by which the method can find exact element
        :return webElement: Search element
        """
        try:
            for domElement in selector:
                if text in domElement.text:
                    return domElement
        except:
            self.log.error("Failed to get element in the page")
            print_stack()
            return None

    def select_item_from_drop_down_list(self, element, option, value):
        try:
            select = Select(element)
            if option == "index":
                select.select_by_index(value)
            if option == "value":
                select.select_by_value(value)
            if option == "text":
                select.select_by_visible_text(value)
        except:
            self.log.error("Cant select from List")
            print_stack()

    def select_item_from_drop_down_list_using_loop(self, list_selector, list_item_selector, value):
        try:
            el = self.get_element(list_selector, "css")
            el.click()
            items = self.get_element_list(list_item_selector, "css")
            for item in items:
                if item.text == value:
                    item.click()
                    break
        except:
            self.log.error("Cant select from List")
            print_stack()

    def browser_logger(self, method_name):
        log_entries = self.driver.get_log("browser")
        log_file = open("browserConsoleLog.log", "a")
        for log_entry in log_entries:
            log_file.write(f"\n {method_name}<<<<<<< " +
                          "\n Log Level = " + log_entry['level'] +
                          "\n Log TimeStamp = " + str(log_entry["timestamp"]) +
                          "\n Log Message = " + log_entry['message'] +
                          "\n >>>>>>>")
        log_file.close()
