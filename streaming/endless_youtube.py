import selenium
import selenium.webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

import time
import random
import os

# Setup headless browser using Firefox
driver_options = Options()
driver_options.headless = True

# It's important we set height and width arguments otherwise page content won't
# render correctly and we can't do things like scroll the full page height!
#
# Actually, this doesn't do anything for Firefox... see below
driver_options.add_argument('--height 900')
driver_options.add_argument('--width 1600')

# Gets current path
current_path = os.getcwd()

driver = selenium.webdriver.Firefox(options=driver_options)

# Installs youtube nonstop firefox extension to succesfully autoplay videos
driver.install_addon(current_path + '/../extensions/youtube_nonstop-0.8.2-fx.xpi', temporary=True)

# We can set the height here
driver.set_window_size(height=900, width=1600)

# Set an implicit wait for all elements not immediately found
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 60)


def current():
    print(f'At {driver.current_url}')

def is_ad():
    ad_status = driver.execute_script(
        "return document.getElementById('movie_player').getAdState()"
    )
    return ad_status != -1

def ensure_playing():

    # Wait for the video player to be accessible, then make sure it's playing
    player = wait.until(
        Condition.presence_of_element_located((By.ID, 'movie_player'))
    )
    # If the video hasn't started playing we can hit the play button!
    player_status = driver.execute_script(
        "return document.getElementById('movie_player').getPlayerState()"
    )
    # A status of -1 means it hasn't started yet, 2 means it's paused. 0 means it
    # has ended.
    if player_status in [-1, 2] and not is_ad():
        player.click()
    elif player_status == 0:
        driver.execute_scripts(
            "document.getElementById('movie_player').nextVideo()"
        )

baseurl = 'https://www.youtube.com/watch?v=DqbOgx_FCbw&list=PL6aq1PBlrtR5D4xslD4VBos7zk0GSTuBb'
driver.get(baseurl)

time.sleep(5)

ensure_playing()

time.sleep(5)

while True:

    current()
    time.sleep(1)
    ensure_playing() # play
    time.sleep(random.randrange(5,18)*60)