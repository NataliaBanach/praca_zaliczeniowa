from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os   

from common_utils import driver, webDriver, accept_cookies, click_login_icon

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

accept_cookies()

click_login_icon()

reg_email_input = webDriver.until(EC.visibility_of_element_located((By.ID, "reg_email")))
reg_email_input.send_keys(username)

reg_password_input = webDriver.until(EC.visibility_of_element_located((By.ID, "reg_password")))
reg_password_input.send_keys(password)


register_button = webDriver.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-Button.woocommerce-button.button.woocommerce-form-register__submit")))

register_button.click()

try:
    title = webDriver.until(EC.visibility_of_element_located((By.CLASS_NAME, "my-account-title")))

    assert "Witaj" in title.text, f"FAILED: 'Witaj' not found in: {title.text}"

    print("PASSED: 'Witaj' found in title.")
except:
    print("FAILED: 'Witaj' not found in title.")

    
driver.quit()
