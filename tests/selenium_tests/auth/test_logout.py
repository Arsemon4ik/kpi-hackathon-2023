from selenium.webdriver.common.by import By

from tests.selenium_tests.constants import BASE_URL


def test_logout(driver, login):
    driver.get(BASE_URL)
    driver.find_element(By.XPATH, "//a[contains(@href,'/sign/logout/')").click()

    assert 'Login' in driver.page_source
