from common_utils import accept_cookies, login, driver

accept_cookies()

login()

expected_result = r"Moje konto"

assert expected_result in driver.page_source, "FAILD: Oczekiwany wzorzec nie został znaleziony w źródle strony."

print("PASSED: Test login")

driver.quit()