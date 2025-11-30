from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.selenium_tests.constants import BASE_URL


def test_failed_login(driver):
    driver.get(BASE_URL)

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("test_user@example.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("wrong_password")
    password_field.send_keys(Keys.RETURN)

    assert "Incorrect email or password" in driver.page_source

    driver.quit()
