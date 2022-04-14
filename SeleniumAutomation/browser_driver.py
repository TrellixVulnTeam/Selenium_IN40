import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#open chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# go to the url
driver.get("http://demostore.supersqa.com/")
time.sleep(6)
