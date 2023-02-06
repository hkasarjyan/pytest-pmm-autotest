import logging
import os
import time
from traceback import print_stack

from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import utilities.custom_logger as cl


class SeleniumDriver:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Takes the screenshot of the current open page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        rel_filename = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, rel_filename)
        destination_directory = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info(f"Screenshot caved to {destination_file}")
        except:
            self.log.error("UNABLE TO SAVE THE SCREENSHOT")
            print_stack()

    def get_title(self):
        """
        Get the current page title
        :return:
            pageTitle
        """
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info(f"Locator type {locator_type} not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info(f"Element Found with locator {locator} and locatorType {locator_type}")
        except:
            self.log.info(f"Element NOT found with locator: {locator} and locatorType: {locator_type}")
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Use the method to get the list of elements
        :param locator:
        :param locator_type:
        :return: elements list
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info(f"Element list found with locator {locator} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {locator} and locator type {locator_type}")

        return element

    def get_elements_nested(self, parent_web_elem, child_locator, locator_type="id"):
        """
        Use the method to get elements from parent webelement
        :param parent_web_elem:
        :param child_locator:
        :param locator_type:
        :return: elements:
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            child_elements = parent_web_elem.find_elements(by_type, child_locator)
            self.log.info(f"Element list found with locator {child_elements} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {child_elements} and locator type {locator_type}")

        return child_elements

    def get_element_nested(self, parent_web_elem, child_locator, locator_type="id"):
        """
        Use the method to get element from parent webelement
        :param parent_web_elem:
        :param child_locator:
        :param locator_type:
        :return: element:
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            child_elem = parent_web_elem.find_element(by_type, child_locator)

            self.log.info(f"Element list found with locator {child_elem} and locator type {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator {child_elem} and locator type {locator_type}")

        return child_elem

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def element_double_click(self, element):
        """
        double Click on an element
        Either provide element
        :param element:
        :return:
        """
        try:
            action = ActionChains(self.driver)
            action.double_click(element).perform()
        except:
            self.log.info("Cannot Doubleclick on the element")
            print_stack()

    def clear_input_field(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info(f"The field cleaned by locator: {locator} and locatorType: {locator_type}")
        except:
            self.log.info(f"Cannot find the element to clean by locator: {locator} and locatorType: {locator_type}")
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        """
         Send keys to an element
        Either provide element or a combination of locator and locatorType
        :param data:
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        :param locator:
        :param locator_type:
        :param element:
        :param info:
        :return: text
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        :param locator:
        :param locator_type:
        :param element:
        :return: Boolean
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info(f"Element Found by {locator} and  {by_type}")
                return True
            else:
                self.log.info(f"Element not found by {locator} and {by_type}")
                return False
        except:
            self.log.info(f"Element not found by {locator} and {by_type}")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info(f"Element appeared on the web page by {locator_type}")
        except:
            self.log.info(f"Element not appeared on the web page by {locator_type}")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        Scrool the web page

        :param direction:
        :return: None
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
