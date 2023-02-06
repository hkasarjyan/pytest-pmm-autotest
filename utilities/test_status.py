from traceback import print_stack

from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
               Inits CheckPoint class
        """
        self.driver = driver
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(f"--- VERIFICATION SUCCESS {result_message}")
                else:
                    self.resultList.append("FAIL")
                    self.log.error(f"--- VERIFICATION FAILED {result_message}")
                    self.screen_shot(result_message)
            else:
                self.resultList.append("FAIL")
                self.log.error(f"--- VERIFICATION FAILED {result_message}")
                self.screen_shot(result_message)
        except:
            self.resultList.append("FAIL")
            self.log.error("--- Exception occured!!! ---")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, resultMessage):
        """
               Mark the result of the verification point in a test case
        """
        self.set_result(result, resultMessage)

    def mark_final(self, test_name, result, result_message):
        """
                Mark the final result of the verification point in a test case
                This needs to be called at least once in a test case
                This should be final test status of the test case
        """
        self.set_result(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(f"{test_name} >>> FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(f"{test_name} >>> SUCCESS")
            self.resultList.clear()
            assert True == True
