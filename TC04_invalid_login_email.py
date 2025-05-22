from common_utils import driver, accept_cookies, login, get_error_message

wrong_username = 'testproject2025@gmail'

accept_cookies()

login(username=wrong_username)

error_text = get_error_message()

expected_error_substring = f"brak {wrong_username} wśród zarejestrowanych w witrynie użytkowników"

assert expected_error_substring in error_text, (f"Expected fragment '{expected_error_substring}' was not found in the error message.")

print("PASSED: Expected fragment was found in the error message.")

driver.quit()
