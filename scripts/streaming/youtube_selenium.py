from . import driver, By, WebDriverWait, Condition, Keys

import random
import time

# Head to the site
baseurl = 'https://youtube.com'
driver.get(baseurl)

print(f'At {driver.current_url}')

# Wait for the search bar to load, then submit a query
wait = WebDriverWait(driver, 30)
search_field = wait.until(
   Condition.presence_of_element_located((By.CSS_SELECTOR, 'input[id ="search"]')))

search_field.send_keys("dragon ball super")
search_field.send_keys(Keys.RETURN)

# Wait for videos to be available, then click on a random one to start watching
videos = wait.until(
   Condition.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#thumbnail'))
)
rand_vid = videos[random.randrange(len(videos))]
rand_vid.click()
time.sleep(5)

# To prevent YouTube from stopping our autoplay, we periodically scroll a bit.
#
# Also get a sense of what page we're at.
while True:
    print(f'At {driver.current_url}')
    time.sleep(1800)
    driver.execute_script("window.scrollBy(0, 50);")
