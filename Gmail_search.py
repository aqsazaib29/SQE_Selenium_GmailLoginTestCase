from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Wait for the inbox page to load after successful login
WebDriverWait(driver, 30).until(
    EC.url_contains("inbox")
)

# Click on the "Compose" button to start composing a new email
compose_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Compose']"))
)
compose_button.click()

# Wait for the "New Message" window to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
)

# Enter recipient's email address
recipient_field = driver.find_element_by_name("to")
recipient_field.send_keys("zaibiaqsa@gmail.com")

# Enter subject for the email
subject_field = driver.find_element_by_name("subjectbox")
subject_field.send_keys("Test Email")

# Enter email body/message
message_body = driver.find_element_by_xpath("//div[@role='textbox']")
message_body.send_keys("This is a test email.")

# Click on the "Send" button to send the email
send_button = driver.find_element_by_xpath("//div[contains(text()= 'Send')]")
send_button.click()

# Wait for the email to be sent successfully
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text()= 'Message sent')]"))
)

print("Email sent successfully!")

# Close the "New Message" window
close_button = driver.find_element_by_xpath("//img[@aria-label='Save & close']")
close_button.click()

# Close the browser
driver.quit()
