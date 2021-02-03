import selenium
import selenium.webdriver
import time
from selenium.webdriver.firefox.options import Options

# Setup headless browser using Firefox
driver_options = Options()
driver_options.headless = True
driver = webdriver.Firefox(options=driver_options)

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
