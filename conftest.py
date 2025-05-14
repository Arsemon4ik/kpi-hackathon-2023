import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from tests.selenium_tests.constants import BASE_URL


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(BASE_URL)

    username_input = driver.find_element(By.NAME, "email")
    username_input.send_keys("admin@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("adminadmin")

    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    time.sleep(2)
    assert "Додати новий предмет" in driver.page_source