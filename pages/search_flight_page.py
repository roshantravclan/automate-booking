import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class SearchFlight(BaseDriver):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_object = BaseDriver(self.driver, self.wait)

    FROM_FIELD = "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)"
    FROM_INPUT_FIELD = "//input[@id='react-select-10-input']"

    TO_FIELD = "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > p:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)"
    TO_INPUT_FIELD = "//input[@id='react-select-13-input']"

    DATE_FIELD = "//input[@id='start_date']"
    CHOOSE_DATE = "//div[@role='presentation']/button"
    PAX_FIELD = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]"
    NEXT_MONTH = "//body/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/button[2]"

    def get_from_field(self):
        return self.base_object.find_element_by_locator(By.CSS_SELECTOR, self.FROM_FIELD)

    def get_from_input_filed(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.FROM_INPUT_FIELD)

    def get_to_field(self):
        return self.base_object.find_element_by_locator(By.CSS_SELECTOR, self.TO_FIELD)

    def get_to_input_field(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.TO_INPUT_FIELD)

    def get_date_field(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.DATE_FIELD)

    def get_choose_date(self):
        return self.base_object.find_elements_by_locator(By.XPATH, self.CHOOSE_DATE)

    def get_pax_field(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.PAX_FIELD)

    def get_next_month(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.NEXT_MONTH)

    def enter_from(self, from_location):
        self.get_from_field().click()
        time.sleep(2)
        self.get_from_input_filed().send_keys(from_location)
        time.sleep(1)
        self.get_from_input_filed().send_keys(Keys.ENTER)

    def enter_to(self, to_location):
        self.get_to_field().click()
        time.sleep(3)
        self.get_to_input_field().send_keys(to_location)
        time.sleep(1)
        self.get_to_input_field().send_keys(Keys.ENTER)

    def enter_date(self, date_value, year_value):
        self.get_date_field().click()

        self.driver.find_element(By.XPATH, "//h6[contains(text(),2022)]").click()
        time.sleep(1)
        years = self.driver.find_elements(By.XPATH, "//div[contains(text(),'2021')]/following-sibling::div")
        for year in years:
            if year.text == year_value:
                year.click()
                break

        self.get_date_field().click()
        # time.sleep(2)
        # month = self.base_object.find_element_by_locator(By.XPATH, "(//p)[17]").text
        # print(month)
        #
        # time.sleep(10)
        #
        # while month_value.lower() not in month.lower():
        #     self.get_next_month().click()
        #     month = self.driver.find_element(By.XPATH, "(//p)[17]").text
        #     print(month)
        #     time.sleep(1)

        time.sleep(2)
        dates = self.driver.find_elements(By.XPATH, self.CHOOSE_DATE)
        for date in dates:
            if date_value == date.text:
                date.click()
                break

    def enter_pax(self):
        self.get_pax_field().click()
        self.driver.find_element(By.XPATH,
                                 "//div[@role='document']//div//div[1]//div[2]//div[1]//button[2]//span[1]//*[name()='svg']").click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH,
        #                          "//div[@id='simple-menu']//div[2]//div[2]//div[1]//button[2]//span[1]//*[name()='svg']").click()
        time.sleep(1)
        self.base_object.find_element_by_locator(By.XPATH,
                                                 "//body/div[@id='simple-menu']/div[3]/ul[1]/button[1]/span[1]").click()

    def click_search_flight(self):
        original_window = self.driver.current_window_handle
        # print(original_window)
        # assert len(self.driver.window_handles) == 1
        self.driver.find_element(By.XPATH, "//span[normalize-space()='SEARCH FLIGHTS']").click()
        self.wait.until(EC.number_of_windows_to_be(2))
        # print(len(self.driver.window_handles))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        # time.sleep(2)
        # self.base_object.find_element_by_locator(By.XPATH, "//span[contains(.,'One stop Flight')]").click()
        # time.sleep(3)
        # stops = self.driver.find_elements(By.XPATH, "(//div)[96]/descendant::h6[contains(text(),'top')]")
        # print(len(stops))
        # for stop in stops:
        #     assert "2 stops" in stop.text
        # self.base_object.find_element_by_locator(By.XPATH, "//span[normalize-space()='Continue']").click()
        # time.sleep(8)
        # try:
        #     self.driver.find_element(By.XPATH, "//span[contains(text(),'OK')]").click()
        # except:
        #     print("Not found")
