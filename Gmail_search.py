from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the WebDriver with the specified path
driver = webdriver.Chrome()

# Open Gmail login page
driver.get("https://mail.google.com")

# Wait for the username input field to be visible
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "identifier"))
)

# Enter your Gmail address
username_field.send_keys("zaib4406737@cloud.neduet.edu.pk")

# Click on the "Next" button
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "identifierNext"))
)
next_button.click()

# Wait for the password input field to be visible
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "Passwd"))
)

# Enter your password
password_field.send_keys("NewOne@29")

# Click on the "Next" button to submit the password
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "passwordNext"))
)
next_button.click()

try:
    # Wait for the page to load after login
    WebDriverWait(driver, 30).until(EC.url_contains("inbox"))
    print("Login successful!")
except TimeoutException:
    print("Login failed.")

# Close the browser
driver.quit()
