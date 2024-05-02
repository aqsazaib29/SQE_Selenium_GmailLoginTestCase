from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.youtube.com/")

# Wait for the element to be visible
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "rendering-content"))
    )
    print("Element is present on the webpage!")
except:
    print("Element is not present on the webpage!")

# Close the browser
driver.quit()
