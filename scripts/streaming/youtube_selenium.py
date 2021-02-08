from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
import random
import time

# Setup headless browser using Firefox
driver_options = Options()
driver_options.headless = True
driver = webdriver.Firefox(options=driver_options)
 
# Head to the site
baseurl = 'https://youtube.com'
driver.get(baseurl)

wait = WebDriverWait(driver, 5)
# Wait for the search bar to load, then submit a query
search_field = wait.until(
   EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id ="search"]')))



search_field.send_keys("dragon ball super")
search_field.send_keys(Keys.RETURN)



videos = driver.find_elements_by_css_selector('a#thumbnail')
rand_vid = videos[random.randrange(len(videos))]
rand_vid.click()
time.sleep(5)
while True:
    time.sleep(1800)
    driver.execute_script("window.scrollBy(0, 50);")
