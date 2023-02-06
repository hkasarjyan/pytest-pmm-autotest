from base.base_page import BasePage
import utilities.custom_logger as cl
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
import time
import re


class WikiPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def clicking_category_menu(self):
        result = self.driver.find_element_by_xpath("//mat-form-field[@id = 'locator_tag_wiki_category']").click()
        return result

    def clicking_all_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_All']").click()
        return result

    def clicking_metric_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_Metric']").click()
        return result

    def clicking_trigger_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_Trigger']").click()
        return result

    def clicking_alert_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_Alert']").click()
        return result

    def clicking_manual_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_Manual']").click()
        return result

    def clicking_configuration_category_text(self):
        result = self.driver.find_element_by_xpath(f"//mat-option[@id = 'locator_tag_wiki_category_Configuration']").click()
        return result

    def clicking_page_num_element(self, page_num):
        result = self.driver.find_element_by_xpath(f"//div[@id = 'locator_tag_pager_{page_num}']").click()
        return result

    def left_single_arrow_element(self):
        result = self.driver.find_element_by_xpath(f"//button[@id = 'locator_tag_pager_previous']").click()
        return result

    def left_double_arrow_element(self):
        result = self.driver.find_element_by_xpath(f"//button[@id = 'locator_tag_pager_first']").click()
        return result

    def right_single_arrow_element(self):
        result = self.driver.find_element_by_xpath(f"//button[@id = 'locator_tag_pager_next']").click()
        return result

    def right_double_arrow_element(self):
        result = self.driver.find_element_by_xpath(f"//button[@id = 'locator_tag_pager_last']").click()
        return result

    def verify_active_page_number(self, page_num):
        active_page_number = self.driver.find_element_by_xpath(f"//div[@id = 'locator_tag_pager_{page_num}']")
        result = active_page_number.get_attribute("class")
        return result


    def get_wiki_rows_list(self, iteration):
        self.wiki_rows_names = []
        print(iteration)
        i = 0
        while i < iteration:
            existing_wiki_rows = self.driver.find_elements_by_xpath("//div[@class = 'row ng-star-inserted']/div/p[1]")
            time.sleep(1)
            print("i=", i)

            for wiki_rows in existing_wiki_rows:
                time.sleep(1)
                wiki_rows_text = wiki_rows.text
                self.wiki_rows_names.append(wiki_rows_text)
                time.sleep(1)
                print(self.wiki_rows_names)
            time.sleep(1)
            i += 1
            if i == iteration:
                break
            self.driver.find_element_by_xpath("//button[@id = 'locator_tag_pager_next']").click()
            time.sleep(1)
        return self.wiki_rows_names

    def existing_wiki_pages_list(self):
        self.page_number = []
        existing_wiki_pages = self.driver.find_elements_by_xpath("//div[@class = 'page-number']/div")
        for page_nums in existing_wiki_pages:
            time.sleep(2)
            wiki_page_item = page_nums.text
            time.sleep(2)
            self.page_number.append(wiki_page_item)
        return self.page_number
