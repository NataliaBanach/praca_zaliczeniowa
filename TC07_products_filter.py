from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from common_utils import accept_cookies, login, webDriver, driver

accept_cookies()
login()


tile_category_select = webDriver.until(
    EC.visibility_of_element_located((By.ID, "mega-menu-item-227217"))
)

actions = ActionChains(driver)
actions.move_to_element(tile_category_select).perform()

wood_option = webDriver.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='mega-menu-item-227232']/a"))
)
wood_option.click()

availability_select = webDriver.until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Dostępność')]/following::button"))
)

availability_select.click()

available_option = webDriver.until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Dostępność')]/following::input[@value='dostepny']"))
)

available_option.click()

filter_button = webDriver.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='product_filer']/div/button"))
)

filter_button.click()

def check_products_on_current_page():
    all_valid = True
    products = webDriver.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product.type-product"))
    )
    print(f"Found {len(products)} products")

    for i, product in enumerate(products, start=1):
        try:
            cls = product.get_attribute("class").lower()
            text = product.find_element(By.CLASS_NAME, "availability-info").text.lower()

            if "dostępny" in text and ("drewnopodobne" in cls or "imitujace-drewno" in cls):
                print(f"Product #{i} PASSED")
            else:
                print(f"Product #{i} FAILED: dostępność = '{text}', klasy = '{cls}'")
                all_valid = False
        except Exception as e:
            print(f"Error with product #{i}: {e}")
            all_valid = False

    return all_valid

def go_to_next_page():
    try:
        driver.find_element(By.CSS_SELECTOR, "a.next.page-numbers").click()
        webDriver.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product.type-product"))
        )
        return True
    except:
        return False

def check_all_products():
    page, all_ok = 1, True
    while True:
        print(f"\n Page {page}")
        if not check_products_on_current_page():
            all_ok = False
        if not go_to_next_page(): break
        page += 1

   
    print("PASSED Everything" if all_ok else "Some products failed")

check_all_products()


driver.quit()