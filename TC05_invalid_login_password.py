from dotenv import load_dotenv
import os

from common_utils import driver, accept_cookies, login, get_error_message


load_dotenv()

username = os.getenv('USERNAME')

accept_cookies()

login(password='wrong_password')

error_text = get_error_message()

expected_error_substring = f"dla adresu e-mail {username} podano nieprawidłowe hasło. Nie pamiętasz hasła?"

assert expected_error_substring in error_text, (f"FAILED: Expected fragment  '{expected_error_substring}' was not found in the error message.")

print(f"PASSED:'{expected_error_substring}' was found in the error message.")

# Close the browser
driver.quit()
