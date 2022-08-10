from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.keys import Keys

# set up the path for the chromedriver
PATH = "C:\Program Files\chromedriver.exe"
# selecting Chrome to use as browser for selenium to run
driver = webdriver.Chrome(PATH)
driver.maximize_window()

# open up the website
driver.get("http://127.0.0.1:5000")


# test for missing element, if the button doesn't exist then our page is broken

try:
    link = driver.find_element(By.LINK_TEXT, 'Click to get a film!')
    link.click()

    for x in range(20):
        driver.implicitly_wait(2)
        driver.find_element(By.LINK_TEXT, 'Get another movie').click()

except NoSuchElementException:
    print("web not loading, unable to choose another movie")

finally:
    driver.close()

