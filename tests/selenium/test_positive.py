from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def test_successful_login():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://localhost:8000")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("admin@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("adminadmin")
    password_field.send_keys(Keys.RETURN)

    assert "Додати новий предмет" in driver.page_source

    driver.quit()
