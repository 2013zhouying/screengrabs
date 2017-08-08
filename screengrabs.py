from selenium import webdriver
from PIL import Image
import os
from time import strftime, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# pip install Pillow
# pip install selenium
# Manually install PhantomJS


masterdirectory = "e:\screengrabs"
PhantomJSlocation = 'C:\helpers\phantomjs.exe'


# So you can have as many sites as you want. Each goes in a parenthesis: (URL, abbreviation)
mysites = [
    ("http://www.palmbeachpost.com", "pb"),
    ("http://www.mypalmbeachpost.com", "my"),
    ("http://www.palmbeachdailynews.com", "dn")
    ]


#delay = 50      # Time to wait to finish loading AJAX-y things after main page loads.   
delay = 50      # Time to wait to finish loading AJAX-y things after main page loads.       

datepath = strftime("/%Y/%m/%d/")
filesuffix = strftime("_%Y-%m-%d_%H%M")

if not os.path.exists(masterdirectory + datepath):
    os.makedirs(masterdirectory + datepath)


browser = webdriver.PhantomJS(executable_path = PhantomJSlocation)
#webdriver.manage().window().setSize( new Dimension( 1500, 6000 ) );
browser.set_window_size(1300, 1920);
        
for site in mysites:
    URL, abbreviation = site
    browser.get(URL)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")       # activate scroll-over stuff like photo gallery
    browser.execute_script("window.scrollTo(0, 0);")     # Then return up top for header.
    sleep(delay)
    browser.save_screenshot(masterdirectory + "/screenie.png")
    im = Image.open(masterdirectory + '/screenie.png')
    im = im.convert("RGB")
    im.save(masterdirectory + datepath + abbreviation + filesuffix + ".jpg")

browser.quit()
