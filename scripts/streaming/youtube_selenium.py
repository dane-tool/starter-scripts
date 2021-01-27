from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
# from random import randint
import numpy as np
import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\dania\Downloads\chromedriver_win32\chromedriver.exe')
 
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
rand_vid = np.random.choice(videos)
rand_vid.click()
time.sleep(5)
while True:
    time.sleep(1800)
    driver.execute_script("window.scrollBy(0, 50);")