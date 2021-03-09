import random
import time

import selenium
import selenium.webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

# List of things to search, when no search results left
search_list = ['college', 'san%20diego', 'hiking', 'stocks']

# Base url and extension for scrollingß
BASE_URL = 'https://twitter.com'
EXTENSION_URL = '/search?q={search}&src=typed'


# Setup headless browser using Firefox
driver_options = Options()
driver_options.headless = True

# It's important we set height and width arguments otherwise page content won't
# render correctly and we can't do things like scroll the full page height!
#
# Actually, this doesn't do anything for Firefox... see below
driver_options.add_argument('--height 900')
driver_options.add_argument('--width 1600')

driver = selenium.webdriver.Firefox(options=driver_options)

# We can set the height here
driver.set_window_size(height=900, width=1600)

# Set an implicit wait for all elements not immediately found
driver.implicitly_wait(10)

driver.get(BASE_URL + EXTENSION_URL.format(search = 'ucsd'))

# Gets last height of browser to compare with future height
last_height = driver.execute_script("return document.body.scrollHeight")

print(f'At {driver.current_url}')

# Driver keeps scrolling on webpage
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randint(4,25))
    
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Checks if scroller has reached end of browser
    if last_height == new_height:
        driver.get(BASE_URL + EXTENSION_URL.format(search = random.choice(search_list)))
        new_height = driver.execute_script("return document.body.scrollHeight")
        last_height = new_height
    else:
        last_height = new_height

html_source = driver.page_source
data = html_source.encode('utf-8')
