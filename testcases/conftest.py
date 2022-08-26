import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setUp(request):
    s = Service("/home/roshan/PycharmProjects/pythonProject2/drivers/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("http://s4.mytripkart.in/www.systemthinking.in")
    wait = WebDriverWait(driver, 30)
    driver.maximize_window()
    print("Launching Browser")

    request.cls.driver= driver
    request.cls.wait = wait
    # yield
    # time.sleep(2)
    # driver.quit()
