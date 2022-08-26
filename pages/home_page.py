import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_object = BaseDriver(self.driver, self.wait)

    FLIGHT_FIELD = "//a[@href='/www.systemthinking.in/flights']"

    def get_flight_field(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.FLIGHT_FIELD)

    def click_flight(self):
        self.get_flight_field().click()
        time.sleep(1)

