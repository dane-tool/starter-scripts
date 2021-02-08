from . import driver, By, WebDriverWait, Condition, Keys

import time

# Base url and extension for scrolling
BASE_URL = 'https://twitter.com'
EXTENSION_URL = '/search?q=ucsd&src=typed'


driver.get(BASE_URL + EXTENSION_URL)

print(f'At {driver.current_url}')

# Driver keeps scrolling on webpage
for i in range(1,100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
html_source = driver.page_source
data = html_source.encode('utf-8')
