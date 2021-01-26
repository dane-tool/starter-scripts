import selenium
import selenium.webdriver
import time

# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup automated driver. Currently headful.
driver = selenium.webdriver.Firefox()

# Base url and extension for scrolling
BASE_URL = 'https://twitter.com'
EXTENSION_URL = '/search?q=ucsd&src=typed'


driver.get(BASE_URL + EXTENSION_URL)

# Driver keeps scrolling on webpage
for i in range(1,100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
html_source = driver.page_source
data = html_source.encode('utf-8')