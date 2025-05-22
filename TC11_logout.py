from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from common_utils import webDriver, accept_cookies, login, driver


accept_cookies()

login()

logout_button = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Wyloguj']")))
logout_button.click()

try:
    webDriver.until_not(
        EC.visibility_of_element_located((By.XPATH, "//*[@title='Wyloguj']"))
    )
    print("PASSED: The Logout button is no visible.")
except:
    print("FAILED: The Logout button is visible.")

driver.quit()
