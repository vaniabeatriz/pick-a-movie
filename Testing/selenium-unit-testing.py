import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class browser_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get("http://127.0.0.1:5000")

    def test_title(self):
        self.assertIn("Decision Making App", self.driver.title)

    def test_home_button(self):
        self.driver.find_element(By.LINK_TEXT, "Home")

    def test_click_get_a_film(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        self.assertIn("Your movie", self.driver.title)

    def test_get_a_film_title(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        element = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertIn('Title:', element)

    def test_get_a_film_image_for_200_response(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        element = self.driver.find_element(By.TAG_NAME, "img")
        src = element.get_attribute("src")
        r = requests.get(src)
        self.assertEqual(r.status_code, 200)

    def test_get_another_movie(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        self.driver.find_element(By.LINK_TEXT, 'Get another movie').click()
        self.assertIn("Your movie", self.driver.title)
        element = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertIn('Title:', element)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
