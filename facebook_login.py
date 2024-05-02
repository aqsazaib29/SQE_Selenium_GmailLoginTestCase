from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver with the specified path
driver = webdriver.Chrome()

# Open Facebook login page
driver.get("https://www.facebook.com")

# Wait for the email/phone input field to be visible
email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "email"))
)

# Enter your email/phone number
email_field.send_keys("zaibiaqsa@gmail.com")


# Wait for the password input field to be visible
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "pass"))
)

# Enter your password
password_field.send_keys("@ise_aam#06fb")


# Click on the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "login"))
)
login_button.click()

# Wait for the page to load after login
WebDriverWait(driver, 30).until(
    EC.url_contains("facebook.com")
)

# Check if login was successful by looking for an element unique to the logged-in page
if "facebook.com" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

# Close the browser
driver.quit()
