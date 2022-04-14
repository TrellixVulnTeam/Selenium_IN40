import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ..rough import Browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# go to the url
driver.get("http://demostore.supersqa.com/")
time.sleep(10)
driver.close()


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# go to the url
driver.get("http://demostore.supersqa.com/")
time.sleep(10)
driver.close()