from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_failed_login():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://localhost:8000")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("test_user@example.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("wrong_password")
    password_field.send_keys(Keys.RETURN)

    assert "Incorrect email or password" in driver.page_source

    driver.quit()
