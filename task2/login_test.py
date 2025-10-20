from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service('/Users/florencendinda/Desktop/PLP/AI_FOR_SOFTWARE/week4/task2/chromedriver'))
driver.get("file:///Users/florencendinda/Desktop/PLP/AI_FOR_SOFTWARE/week4/task2/login.html")


def test_login(username, password, expected_message, screenshot_name):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "message").text
    driver.save_screenshot(f"screenshots/{screenshot_name}")
    print(f"Test with ({username}, {password}) → {result}")
    assert result == expected_message

# Valid credentials
test_login("admin", "1234", "Login successful!", "valid_login.png")

# Invalid credentials
test_login("user", "wrongpass", "Invalid credentials.", "invalid_login.png")

driver.quit()
