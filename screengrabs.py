from selenium import webdriver
from PIL import Image
import os
from time import strftime, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# pip install Pillow
# pip install selenium

masterdirectory = "e:\screengrabs"

# So you can have as many sites as you want. Each goes in a parenthesis: (URL, abbreviation)
mysites = [
    ("http://www.palmbeachpost.com", "pb"),
    ("http://www.mypalmbeachpost.com", "my")
    ]


delay = 45      # Time to wait to finish loading AJAX-y things after main page loads.   
    

datepath = strftime("/%Y/%m/%d/")
filesuffix = strftime("_%Y-%m-%d_%H%M")

if not os.path.exists(masterdirectory + datepath):
    os.makedirs (masterdirectory + datepath)

browser = webdriver.Firefox()
for site in mysites:
    URL, abbreviation = site
    browser.get(URL)
    sleep(delay)
## Below didn't work, so above is a replacement.    
#    delay = 20 # Maximum page load time for extras like AJAX
#    try:
#        WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_id('IdOfMyElement')))
#        print "Page is ready!"
#    except TimeoutException:
#        print "Loading took too much time!"
    browser.save_screenshot(masterdirectory + "/screenie.png")
    im = Image.open(masterdirectory + '/screenie.png').save(masterdirectory + datepath + abbreviation + filesuffix + ".jpg")

browser.quit()
