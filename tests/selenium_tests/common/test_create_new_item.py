from selenium.webdriver.common.by import By

from conftest import BASE_URL


def test_authorized_page_access(driver, login):
    driver.get(BASE_URL)
    assert "Додати новий предмет" in driver.page_source


def test_create_new_item(driver, login):
    driver.get(BASE_URL)

    driver.find_element(By.NAME, "theme").send_keys("Новий предмет")
    driver.find_element(By.NAME, "description").send_keys("Опис нового предмету")
    driver.find_element(By.NAME, "max_score").send_keys("100")

    driver.find_element(By.NAME, "btn-subject").click()

    success_message = driver.find_element(By.XPATH, "//td[contains(text(), 'Новий предмет')]")
    assert success_message.is_displayed()
