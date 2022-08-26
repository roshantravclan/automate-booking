import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class FlightResult(BaseDriver):
    def __init__(self, driver, wait):
        self.one_stop = None
        self.non_stop = None
        self.driver = driver
        self.wait = wait
        self.base_object = BaseDriver(driver, wait)

    def filters(self, stop_filter):
        self.non_stop = self.base_object.find_element_by_locator(By.XPATH, "//input[@value='Non Stop Flight ']")
        self.one_stop = self.base_object.find_element_by_locator(By.XPATH, "//input[@value='One stop Flight']")
        time.sleep(2)
        if stop_filter == "Non Stop":
            if self.one_stop.is_selected():
                print(self.one_stop.is_selected())
                self.one_stop.click()
                self.non_stop.click()
            else:
                self.non_stop.click()

        elif stop_filter == "1 stops":
            if self.non_stop.is_selected():
                time.sleep(2)
                print(self.non_stop.is_selected())
                self.non_stop.click()
                self.one_stop.click()
            else:
                self.one_stop.click()
        time.sleep(2)
        stops = self.driver.find_elements(By.XPATH, "(//div)[96]/descendant::h6[contains(text(),'top')]")
        print(len(stops))
        for stop in stops:
            assert stop_filter in stop.text
