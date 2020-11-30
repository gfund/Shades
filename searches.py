from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time
def imsearch(query):
    driver = webdriver.Firefox()

    driver.get("https://www.google.com/search?q={0}&tbm=isch".format(query))
    
    driver.save_screenshot('search.png')
   
    
    
  
    driver.close()