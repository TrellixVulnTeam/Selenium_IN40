from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def start_browser() -> WebDriver:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("http://demostore.supersqa.com/")
    time.sleep(4)
    return browser


def stop_browser() -> None:
    time.sleep(4)
    driver.close()


# Finding elements by ID
driver = start_browser()
site_header_cart: WebElement = driver.find_element(By.ID, "site-header-cart")
print(site_header_cart.text)
site_header_cart.click()
stop_browser()

# Finding elements by CSS Selector
driver = start_browser()
site_header_cart: WebElement = driver.find_element(By.CSS_SELECTOR, "ul[id='site-header-cart']")
print(site_header_cart.text)
site_header_cart.click()
stop_browser()

# Finding elements by class name
driver = start_browser()
product: WebElement = driver.find_element(By.CLASS_NAME, "product")
products: List = driver.find_elements(By.CLASS_NAME, "product")
print(product)
print(products)
stop_browser()

# Finding elements by link text
driver = start_browser()
link_element: WebElement
link_element = driver.find_element(By.LINK_TEXT, "Cart")
print(link_element.text, type(link_element))
link_element = driver.find_element(By.LINK_TEXT, "My account")
print(link_element.text, type(link_element))
stop_browser()