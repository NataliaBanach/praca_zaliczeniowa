from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


url = "https://kaflando.pl/moje-konto/"

driver = webdriver.Chrome()
driver.get(url)
driver.set_window_size(1420, 1080)

webDriver = WebDriverWait(driver, 10)

def accept_cookies():
    accept_cookies = webDriver.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))

    accept_cookies.click()


def login(username = username, password = password):
    # Enter invalid username
    email_field = webDriver.until(EC.visibility_of_element_located((By.ID, "username")))
    email_field.send_keys(username)
    #email_field.send_keys(Keys.ENTER)


    # Enter invalid password
    password_field = webDriver.until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.send_keys(password)
    #password_field.send_keys(Keys.ENTER)

    login_button = webDriver.until(EC.visibility_of_element_located((By.NAME, "login")))
    login_button.click()


def get_error_message():
    error_message_element = webDriver.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-error-msg"))
    )

    return error_message_element.text


def click_login_icon():
    login_icon = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Logowanie / Rejestracja']")))
    login_icon.click()


def click_on_cart():
    cart_anchor = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'cart-header')]")))
    cart_anchor.click()

def clear_cart():
    remove_button = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='remove']")))
    remove_button.click()

def add_racer_dab_item_to_cart():
    # Dodanie produktu do koszyka
    blaty_navbar_item = webDriver.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='mega-menu-item-228187']/a"))
    )
    blaty_navbar_item.click()

    racer_dab_product = webDriver.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'post-214964')]/a"))
    )
    racer_dab_product.click()

    button_plus = webDriver.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'plus')]")))
    button_plus.click()

    add_to_cart_button = webDriver.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='add-to-cart']")))
    add_to_cart_button.click()
