from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# set up the path for the chromedriver
PATH = "C:\Program Files\chromedriver.exe"
# selecting Chrome to use as browser for selenium to run
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:5000")

# test case for rerendering 20 times to test the user experience (how many movies the user can view before the page crashes)

try:
    link = driver.find_element(By.LINK_TEXT, 'Click to get a film!')
    link.click()

    for x in range(20):
        driver.implicitly_wait(2)
        driver.find_element(By.LINK_TEXT, 'Get another movie').click()

except NoSuchElementException:
    print("the web crashed after clicking on get another movie", {x}, "times")

finally:
    driver.close()
