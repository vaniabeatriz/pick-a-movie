from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# set up the path for the chromedriver
PATH = "C:\Program Files\chromedriver.exe"
# selecting Chrome to use as browser for selenium to run
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:5000")

# test for looking for home element

try:
    page_title = driver.title
    assert page_title == "Decision Making App"
    driver.find_element(By.LINK_TEXT, "Home")

except NoSuchElementException:
    print("cannot find home element")

finally:
    driver.close()
# test for missing element, if the button doesn't exist/work then our page is broken
#
try:

    link = driver.find_element(By.LINK_TEXT, 'Click to get a film!')
    link.click()

    for x in range(20):
        driver.implicitly_wait(2)
        driver.find_element(By.LINK_TEXT, 'Get another movie').click()

except NoSuchElementException:
    print("the web crashed after clicking on get another movie", {x},"times")

finally:
    driver.close()

