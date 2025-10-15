import time

from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import pytest
import pyautogui

# Connect to the existing Chrome session running in debugging mode

chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"  # same port as above

driver = webdriver.Chrome(options=chrome_options)

# Navigate to ChatGPT (must already be logged in)

driver.get("https://chatgpt.com/")
wait = WebDriverWait(driver, 10)


# Click on the "+" button to open attachment options

time.sleep(2)
click_on_attach= wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='composer-plus-btn']/parent::span"))
)

click_on_attach.click()

# Select "Add photos & files" from the popup menu

addphotosandfile= wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add photos & files')]/ancestor::div[contains(@class,'__menu-item')]"))
)

addphotosandfile.click()
# Wait a bit before triggering the file upload dialog

time.sleep(1)
# Use pyautogui to type the file path and press Enter (this interacts with the OS-level file picker)

pyautogui.write(r"C:\Users\sanket\OneDrive\Desktop\Monthly_report (1).xlsx")
pyautogui.press('enter')

# Wait for the message input field to become clickable

senthetext= wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[@data-placeholder='Ask anything']"))
)

time.sleep(2)
senthetext.send_keys("explain this")
# Submit the input and file by clicking the send button

time.sleep(3)
clickonupload= wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='composer-submit-button']"))
)
clickonupload.click()


verify_uploaded_file = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Monthly_report (1).xlsx')]"))
)

if verify_uploaded_file:
    print("File uploaded successfully.")
else:
    print(" File upload failed.")

print("✅ ChatGPT responded. Upload and message successful.")
