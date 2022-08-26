from selenium.webdriver.support import expected_conditions as EC


class BaseDriver():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def find_element_by_locator(self, locator, locator_path):
        element = self.wait.until(EC.presence_of_element_located((locator, locator_path)))
        return element

    def find_elements_by_locator(self, locator, locator_path):
        elements = self.wait.until(EC.presence_of_all_elements_located((locator, locator_path)))
        return elements
