from selenium import webdriver

# Initialize the WebDriver with the specified path
driver = webdriver.Chrome()

# Open Linkedin login page
driver.get("https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo")

# Get the actual title of the webpage
actual_title = driver.title

# Define the expected title
expected_title = "LinkedIn:  or Sign Up"

# Check if the actual title matches the expected title
if actual_title == expected_title:
    print("Title match: Test passed!")
else:
    print(f"Title mismatch: Expected '{expected_title}', but got '{actual_title}'")

# Close the browser
driver.quit()
