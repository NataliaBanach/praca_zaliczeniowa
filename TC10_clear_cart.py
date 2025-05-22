from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from common_utils import accept_cookies, login, webDriver, driver, clear_cart, add_racer_dab_item_to_cart

accept_cookies()

login()

add_racer_dab_item_to_cart()

try:
    clear_cart()

    webDriver.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "td.product-name")))

    print("PASSED: Cart is empty.")
except:
    print('FAILED')

driver.quit()