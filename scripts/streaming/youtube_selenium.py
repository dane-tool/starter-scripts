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
time.sleep(5)

# Wait for videos to be available, then click on a random one to start watching
videos = wait.until(
   Condition.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#thumbnail'))
)
rand_vid = videos[random.randrange(len(videos))]
driver.get(rand_vid.get_attribute('href'))
time.sleep(5)

# To prevent YouTube from stopping our autoplay, we periodically scroll a bit.
#
# Also get a sense of what page we're at.
while True:
   
   # If the video hasn't started playing we can hit the play button!
   player_status = driver.execute_script(
      "return document.getElementById('movie_player').getPlayerState()"
   )
   # A status of -1 means it hasn't started yet
   if player_status == -1:
      player = driver.find_element_by_id('movie_player')
      player.click()

   print(f'At {driver.current_url}')
   time.sleep(200)
   driver.execute_script("window.scrollBy(0, 50);")
