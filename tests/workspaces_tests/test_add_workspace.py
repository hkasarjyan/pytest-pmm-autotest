import logging
import utilities.custom_logger as cl
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@mark.order(1)
@mark.regression
@mark.smoke
def test_add_workspace_non_existing(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_add_workspace_non_existing} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(5)
    ws_list = workspaces_page.get_workspaces_list()
    ws_name1 = ws_list[0] + 'wWWw'                               #New workspace name
    workspaces_page.add_new_workspace(ws_name1)                  #Adding new workspace
    ws_name_new_list = workspaces_page.get_workspaces_list()     #New workspaces list
    assert ws_name1 in ws_name_new_list, "WS Created Failed"

    #adding new workspace in upper keys
    ws_name2 = ws_list[0] + 'WWWw'                               #New workspace name
    workspaces_page.add_new_workspace(ws_name2)                  #Adding new workspace
    ws_name_new_list = workspaces_page.get_workspaces_list()     #New workspaces list
    assert ws_name2 in ws_name_new_list, "WS Created Failed"

    #will be delete created workspaces
    workspaces_page.remove_workspace(ws_name1)
    time.sleep(1)
    ws_name_new_list = workspaces_page.get_workspaces_list()
    time.sleep(1)
    assert ws_name1 not in ws_name_new_list, "WS Deleted Failed"
    workspaces_page.remove_workspace(ws_name2)
    time.sleep(1)
    ws_name_new_list = workspaces_page.get_workspaces_list()
    time.sleep(1)
    assert ws_name2 not in ws_name_new_list, "WS Deleted Failed"

@mark.order(2)
@mark.regression
@mark.smoke
def test_add_workspace_with_existing_name(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_add_workspace_with_existing_name} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(5)

    ws_list = workspaces_page.get_workspaces_list()      #list of workspaces names
    new_ws = ws_list[0]
    workspaces_page.add_new_workspace(new_ws)           #let's try to add a workspace with an already existing name
    ws_new_list = workspaces_page.get_workspaces_list() #new list of workspaces names
    count_new_ws = ws_new_list.count(new_ws)            #displaying the number of workspace with name is new_ws
    time.sleep(1)
    assert count_new_ws == 1, "created two workspaces with same name"












