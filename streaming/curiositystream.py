import dotenv
import os
import random
import time
import urllib.parse as up

import selenium
import selenium.webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

BASEURL = 'https://curiositystream.com'

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
# To figure out that the url was /login I just looked at the url after clicking
# the link manually.
driver.get(up.urljoin(BASEURL, 'login'))

# Now we need to enter our credentials.
#
# There are only two <input> elements on the page (again, all of the initial
# page exploration is done manually!) so we can just use those tags as the email
# and password fields.
#
# Note that these fields might not be loaded in by the time our script want to
# execute. We need to realy on Waits.
# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits

# Wait a maximum of 30 seconds for a condition to be met. We can reuse this wait
# object.
wait = WebDriverWait(driver, 30)

# Here's our condition
email_field, pass_field = wait.until(
    # This uses the concept of a 'locator' -- instead of directly asking the
    # driver to get us some elements, we're just passing the location of the
    # elements as a tuple: (By.TAG_NAME, 'input')
    Condition.visibility_of_all_elements_located((By.TAG_NAME, 'input'))
)

# And now populate those fields by sending keys.
#
# The values we populate it with should be KEPT SECRET -- we can use environment
# variables from a .env file.
#
# NOTE: Make sure your .env file is ignored by git to avoid adding your secrets
# into version control!
assert dotenv.load_dotenv(), "Failed to load from .env file!"

email_field.send_keys(os.environ['CURIOSITYSTREAM_EMAIL'])
pass_field.send_keys(os.environ['CURIOSITYSTREAM_PASS'])

# Our submit button has the type="submit" (pretty common practice for fields!)
#
# To make sure that we're not going to accidentally hit a different submit
# button somewhere else on the page, it's helpful to open up the Developer Tools
# Console in the browser and try out your selector using
# `document.querySelector(...)`. Make sure that the element returned is the one
# you want!
submit_botton = driver.find_element_by_css_selector('button[type="submit"]')
submit_botton.click()

# Now click on a video!
#
# Videos are linked to with an anchor pointing to a link that starts with /video
#
# We'll need to wait for the links to load in again -- this time we just want to
# make sure the dom has them registered. I originally tried to wait for them to
# be visible -- but some of them are off the page (d'oh)!
video_links = wait.until(
    Condition.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/video"'))
)

# We'll choose a random video then go to its url.
#
# I originally tried clicking on the element, but Selenium complained that we
# shouldn't be allowed to click the element because it's behind other elements.
target_video = video_links[random.randrange(len(video_links))]
driver.get(target_video.get_attribute('href'))

# Finally, wait for the player to be visible then click it to play!
player = wait.until(
    Condition.visibility_of_element_located((By.CLASS_NAME, 'player'))
)
player.click()

# After a set (or random) period of time, we can do something else. For now I'm
# just quiting.
#
# NOTE: If you want to play with the script further, comment out these lines.
time.sleep(10)
driver.quit()
exit(0) # Success!
