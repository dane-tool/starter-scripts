# Driver
# ======
#
# This is the base module that all scripts will import from. Basically, we just
# set up the web driver in here, along with an desired options (e.g. Firefox or,
# Chrome, headless, height and width, etc)
#

import selenium
import selenium.webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
# See: https://selenium-python.readthedocs.io/waits.html#explicit-waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

# Setup headless browser using Firefox
driver_options = Options()
# driver_options.headless = True

# It's important we set height and width arguments otherwise page content won't
# render correctly and we can't do things like scroll the full page height!
#
# Actually, this doesn't do anything for Firefox... see below
driver_options.add_argument('--height 900')
driver_options.add_argument('--width 1600')

# We can make sure autoplay is enabled and set other preferences by using a
# Firefox Profile
profile = selenium.webdriver.FirefoxProfile()
# https://support.mozilla.org/en-US/questions/1238033
profile.set_preference('media.autoplay.default', 0)

driver = selenium.webdriver.Firefox(options=driver_options, firefox_profile=profile)

# We can set the height here
driver.set_window_size(height=900, width=1600)

# Set an implicit wait for all elements not immediately found
driver.implicitly_wait(10)
