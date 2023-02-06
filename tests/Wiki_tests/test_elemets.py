import logging
import utilities.custom_logger as cl
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.wiki_page.wiki_page import WikiPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Wiki_tests.test_category_wiki import test_goto_wiki_page
import time



@mark.order(1)
@mark.regression
@mark.smoke
def test_left_single_arrow(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_left_single_arrow} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)

    #take the third element from the list and click on it,
    page_num = wiki_page.existing_wiki_pages_list()[2]  #should be [-1]
    wiki_page.clicking_page_num_element(page_num)
    #check the page is active
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "left single arrow not work"

    wiki_page.left_single_arrow_element()
    time.sleep(1)
    page_num = int(page_num)-1
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "left single arrow not work"

    wiki_page.left_single_arrow_element()
    time.sleep(1)
    page_num = int(page_num)-1
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "left single arrow not work"


@mark.order(2)
@mark.regression
@mark.smoke
def test_left_double_arrow(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_left_double_arrow} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)


    page_num = wiki_page.existing_wiki_pages_list()[2]
    wiki_page.clicking_page_num_element(page_num)
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "left double arrow not work"

    wiki_page.left_double_arrow_element()
    time.sleep(1)
    page_num = 1
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "left double arrow not work"



@mark.order(3)
@mark.regression
@mark.smoke
def test_right_single_arrow(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_right_single_arrow} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)


    wiki_page.right_single_arrow_element()
    page_num = 2
    wiki_page.clicking_page_num_element(page_num)
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "right single arrow not work"

    wiki_page.right_single_arrow_element()
    time.sleep(1)
    page_num = 3
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "right single arrow not work"


@mark.order(4)
@mark.regression
@mark.smoke
def test_right_double_arrow(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_right_double_arrow} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)

    wiki_page.right_double_arrow_element()
    page_num = wiki_page.existing_wiki_pages_list()[-1]

    assert wiki_page.verify_active_page_number(page_num) in ("ng-star-inserted active", "active ng-star-inserted") , "right double arrow not work"


@mark.order(5)
@mark.regression
@mark.smoke
def test_pager_exact_number(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_pager_exact_number} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)

    page_num = 3
    wiki_page.clicking_page_num_element(page_num)
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "pager exact number not work"

    page_num = 5
    wiki_page.clicking_page_num_element(page_num)
    assert wiki_page.verify_active_page_number(page_num) == "ng-star-inserted active", "pager exact number not work"


@mark.order(6)
@mark.regression
@mark.smoke
def test_validate_pager_switching(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    log = cl.custom_logger(logging.DEBUG)
    log.info(f"{test_validate_pager_switching} >>>>>>>>>>>>>>>>> started")
    wiki_page.driver.implicitly_wait(5)

    page_num = 3
    wiki_page.clicking_page_num_element(page_num)
    time.sleep(2)
    page_num = 5
    wiki_page.clicking_page_num_element(page_num)
    time.sleep(2)
    wiki_pages_list = wiki_page.existing_wiki_pages_list()
    number_pages = ['3', '4', '5', '6', '7']

    for number in number_pages:
        if number not in wiki_pages_list:
            result = "pager not switching correctly"
        else:
            result = "pager switching correctly"
    assert result == "pager switching correctly", "pager switching correctly"

