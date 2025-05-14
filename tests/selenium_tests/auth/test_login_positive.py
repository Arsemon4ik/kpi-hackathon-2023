import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.selenium_tests.constants import BASE_URL


def test_successful_login(driver):
    driver.get(BASE_URL)

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("admin@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("adminadmin")
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)
    assert "Додати новий предмет" in driver.page_source

    driver.quit()
