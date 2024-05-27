from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(executable_path=r"C:\Users\rudol\Downloads\delete\chromedriver.exe", options=chrome_options)

# Navigate to the website
driver.get('https://www.online.fnb.co.za/banking/main.jsp')

# Wait for the "Accounts" button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shortCutLinks"]//span[@class="shortCutLink  " and text()="Accounts"]')))

# Click the "Accounts" button
button.click()

# Close the web driver
driver.quit()
