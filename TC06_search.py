from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common_utils import accept_cookies, login, webDriver, driver

accept_cookies()
login()

input_field = webDriver.until(EC.visibility_of_element_located((By.ID, "ajax-search")))
input_field.send_keys("kabina prysznicowa New Renoma chrom")
input_field.send_keys(Keys.RETURN)

# Sprawdź, czy wynik zawiera nazwę produktu
product_title = webDriver.until(EC.visibility_of_element_located((By.XPATH, "//h1")))

assert "kabina prysznicowa new renoma chrom" in product_title.text.lower(), "FAILED: The expected product was not found on the page"

print("PASSED: The searched product was found on the page.")

driver.quit()
