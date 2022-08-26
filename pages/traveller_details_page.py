import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class TravellerDetails(BaseDriver):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_object = BaseDriver(self.driver, self.wait)

    FIRST_NAME = "(//input[@placeholder='Enter First Name'])[1]"
    LAST_NAME = "(//input[@placeholder='Enter Last Name'])[1]"

    FIRST_NAME2 = "(//input[@placeholder='Enter First Name'])[2]"
    LAST_NAME2 = "(//input[@placeholder='Enter Last Name'])[2]"

    FIRST_NAME3 = "(//input[@placeholder='Enter First Name'])[3]"
    LAST_NAME3 = "(//input[@placeholder='Enter Last Name'])[3]"

    DATE_OF_BIRTH = "//div[@formcontrollabel='Date of Birth']//div//div//button[@type='button']"
    CONTACT_NO = "//input[@id='contactNumber']"
    EMAIL = "//input[@id='email']"
    AGREEMENT = "//span[contains(text(),'I understand and agree with the Fare Rules and the')]"

    LOGIN_NUMBER = "//body[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    REQUEST_OTP = "(//span[contains(text(),'Request Otp')])[2]"
    VERIFY_OTP = "//span[normalize-space()='VERIFY']"

    def get_first_name(self, first_name):
        return self.base_object.find_element_by_locator(By.XPATH, first_name)

    def get_last_name(self, last_name):
        return self.base_object.find_element_by_locator(By.XPATH, last_name)

    def get_contact_number(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.CONTACT_NO)

    def get_email(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.EMAIL)

    def get_agreement(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.AGREEMENT)

    def get_login_no(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.LOGIN_NUMBER)

    def get_request_otp(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.REQUEST_OTP)

    def get_verify_otp(self):
        return self.base_object.find_element_by_locator(By.XPATH, self.VERIFY_OTP)

    def enter_traveller_details(self):
        self.get_first_name(self.FIRST_NAME).send_keys("trav")
        self.get_last_name(self.LAST_NAME).send_keys("one")
        self.get_first_name(self.FIRST_NAME2).send_keys("trav")
        self.get_last_name(self.LAST_NAME2).send_keys("two")

    def info(self):
        self.get_contact_number().send_keys("8802338434")
        self.get_email().send_keys("das@gmail.com")
        self.get_agreement().click()
        self.base_object.find_element_by_locator(By.XPATH, "//span[contains(text(),'continue')]").click()

    def login(self):
        print("OTP Page")
        self.get_login_no().send_keys("8802338434")
        time.sleep(15)
        self.get_request_otp().click()
        print("Enter Otp")
        time.sleep(15)
        self.get_verify_otp().click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='continue to pay']").click()
        self.base_object.find_element_by_locator(By.XPATH, "//span[normalize-space()='pay and book now']").click()
        self.base_object.find_element_by_locator(By.XPATH, "//span[normalize-space()='Net Banking*']").click()
        self.base_object.find_element_by_locator(By.CSS_SELECTOR,
                                 "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > button:nth-child(1) > span:nth-child(1)").click()
        time.sleep(5)
        print(self.driver.page_source)
        print(len(self.driver.window_handles))
        self.base_object.find_element_by_locator(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > button:nth-child(1) > span:nth-child(1)").click()
        time.sleep(10)
