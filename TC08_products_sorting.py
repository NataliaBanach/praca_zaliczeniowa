from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

from common_utils import accept_cookies, login, webDriver, driver

accept_cookies()
login()

element_outlet = webDriver.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Outlet')]"))
)
element_outlet.click()

sorting_select = webDriver.until(
    EC.visibility_of_element_located((By.XPATH, "//select[@name='orderby']"))
)

select = Select(sorting_select)
select.select_by_value("price") 


page = 1  # Initialization of the variable page
total_pages = 0  # Initialization of the variable total_pages

while True:
    try:
        price_elements = driver.find_elements(By.XPATH, "//ins/span/bdi")
        price = []

        for el in price_elements:
            try:
                match = re.search(r'[\d\s,.]+', el.text)
                print(el.text)
                if match:
                    tekst = match.group().replace("zł", "").replace(",", ".").replace(" ", "").strip()
                    price.append(float(tekst))
            except Exception:
                continue

        if not price:
            print("FAILED: No prices found on the page")
            break
           
        posortowane = price == sorted(price)
        total_pages += 1

    except WebDriverException as e:
        print("FAILED: Error while processing prices:", e)
        break

# next page
    try:
        driver.find_element(By.CSS_SELECTOR, "a.next.page-numbers").click()

    except:
        break

print(f"PASSED: Checked {total_pages} pages. Sorting is {'correct' if posortowane else 'incorrect'}.")


driver.quit()



