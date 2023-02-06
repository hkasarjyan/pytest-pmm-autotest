import logging
import utilities.custom_logger as cl
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



@mark.order(1)
@mark.regression
@mark.smoke
def test_search_workspaces(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_search_workspaces} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(5)

    ws_list_old = workspaces_page.get_workspaces_list()
    search_text = "aaaaee"
    workspaces_page.search_box_element.send_keys(search_text)
    time.sleep(2)
    ws_list = workspaces_page.get_workspaces_list()
    count_workspace = len(ws_list)
    assert count_workspace == 0, "Searching Failed"
    for i in range(len(search_text)):
        workspaces_page.search_box_element.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
    ws_list_new = workspaces_page.get_workspaces_list()
    time.sleep(3)
    assert ws_list_old == ws_list_new, "Searching Failed"

    #adding three workspaces
    adding_ws_names = ["TestHovo", "Testhovo1","TesthoVo12"]
    time.sleep(1)
    ws_name_old_list = workspaces_page.get_workspaces_list()
    time.sleep(1)
    for ws_test_name in adding_ws_names:
        if ws_test_name not in ws_name_old_list:
            time.sleep(4)
            workspaces_page.add_new_workspace(ws_test_name)
        #else:
            #time.sleep(1)
            #workspaces_page.add_new_workspace(ws_test_name*2)
    time.sleep(3)
    #define a list of "workspaces" and convert to lowercase
    ws_list = workspaces_page.get_workspaces_list()
    ws_list_lower = workspaces_page.workspaces_list_lower(ws_list)
    patterns = ["test", "hovo", "1", "2", "3"]
    # determine the number of matches with the pattern
    calc_patt = ""

    for pattern in patterns:
        workspaces_page.search_box_element.send_keys(pattern)
        time.sleep(3)
        ws_visible_list = workspaces_page.get_workspaces_list()
        num_visible_ws = len(ws_visible_list)
        time.sleep(2)
        calc_patt += pattern
        num_calc_list = workspaces_page.determine_matches_pattern(ws_list_lower, calc_patt)
        assert num_visible_ws == num_calc_list, "Searching Failed"
    num = len(calc_patt)
    print(num)
    for i in range(3, num):
        workspaces_page.search_box_element.send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        ws_visible_list = workspaces_page.get_workspaces_list()
        num_visible_ws = len(ws_visible_list)
        time.sleep(2)
        calc_patt = calc_patt[:-1]
        print(calc_patt)
        num_calc_list = workspaces_page.determine_matches_pattern(ws_list_lower, calc_patt)
        assert num_visible_ws == num_calc_list, "Searching Failed"

    #the last step: will be delete created workspaces
    for ws_name in adding_ws_names:
        workspaces_page.remove_workspace(ws_name)
        time.sleep(2)
