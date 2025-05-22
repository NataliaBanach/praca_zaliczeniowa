from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from common_utils import accept_cookies, login, webDriver, driver, clear_cart, add_racer_dab_item_to_cart


accept_cookies()
login()

add_racer_dab_item_to_cart()


try:
    cart_product_name = webDriver.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.product-name"))
    ).text.lower()

    assert "blat drewniany racer dąb naturalny albero 100x50x2,6 cm" in cart_product_name, "FAILED: The expected product was not found in the cart"
    quantity_value = webDriver.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.qty"))
    ).get_attribute("value")

    assert quantity_value == "2", f"FAILED: The quantity in the cart is{quantity_value}, not 2"

    clear_cart()

except:
    print("FAILED: An error occurred while adding the product to the cart.")

print("PASSED: The product has been added to the cart and the quantity is correct.")

driver.quit()