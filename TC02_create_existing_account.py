from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os   

from common_utils import get_error_message, driver, webDriver, accept_cookies, click_login_icon


load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

accept_cookies()

click_login_icon()

reg_email_input = webDriver.until(EC.visibility_of_element_located((By.ID, "reg_email")))
reg_email_input.send_keys(username)

reg_password_input = webDriver.until(EC.visibility_of_element_located((By.ID, "reg_password")))
reg_password_input.send_keys(password)


register_button = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='register']")))

register_button.click()


error_message = get_error_message()

expected_message = "Konto jest już zarejestrowane"

assert expected_message in error_message, f"FAILED: Expected error message not found. Actual: {error_message}"

print("PASSED: Expected error message found.")

driver.quit()