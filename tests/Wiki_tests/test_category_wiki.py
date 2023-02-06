import logging
import utilities.custom_logger as cl
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.wiki_page.wiki_page import WikiPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@mark.order(1)
@mark.regression
@mark.smoke
def test_goto_wiki_page(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_goto_wiki_page} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.wiki_icon_element.click()
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/wiki"))
    assert "wiki" in driver.current_url
    assert "workspaces" not in driver.current_url


@mark.order(2)
@mark.regression
@mark.smoke
def test_category_metric_wiki(driver):
    test_goto_wiki_page(driver)
    wiki_page = WikiPage(driver)
    wiki_page.driver.implicitly_wait(5)
    time.sleep(2)

    wiki_page.clicking_category_menu()
    time.sleep(2)
    wiki_page.clicking_metric_category_text()
    time.sleep(2)

    iter_list = wiki_page.get_max_page_num()
    if len(iter_list) == 0:
        iteration = 0
    else:
        iteration = int(iter_list[-1])
    time.sleep(1)
    print("ooooo")
    a = wiki_page.get_wiki_rows_list(iteration)
    time.sleep(1)
    print(a)
    print(len(a))






@mark.order(2)
@mark.regression
@mark.smoke
def test_category_all1_wiki(driver):
    test_category_wiki(driver)
    wiki_page = WikiPage(driver)
    #wiki_page.clicking_metric_category_text()
    time.sleep(5)
    for i in range(5):
        wiki_page.driver.find_element_by_xpath("//button[@id = 'locator_tag_pager_next']").click()
        time.sleep(5)




@mark.order(2)
@mark.regression
@mark.smoke
def test_category_metric11_wiki(driver):
    test_category_wiki(driver)
    wiki_page = WikiPage(driver)
    wiki_page.driver.implicitly_wait(5)
    time.sleep(2)

    wiki_page.clicking_category_menu()
    #wiki_page.driver.find_element_by_xpath("//mat-form-field[@id = 'locator_tag_wiki_category']").click()
    time.sleep(5)
