from . import driver, By, WebDriverWait, Condition, Keys

import random
import time

time.sleep(3)

# List of things to search, when no search results left
search_list = ['college', 'san%20diego', 'hiking', 'stocks']

# Base url and extension for scrollingß
BASE_URL = 'https://twitter.com'
EXTENSION_URL = '/search?q={search}&src=typed'

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
