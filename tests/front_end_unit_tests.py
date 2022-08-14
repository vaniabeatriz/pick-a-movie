import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BrowserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        self.driver.get("http://127.0.0.1:5000")

    def test_title(self):
        self.assertIn("Pick A Movie", self.driver.title)

    def test_home_button(self):
        self.driver.find_element(By.LINK_TEXT, "Home")

    def test_click_get_a_film(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        self.assertIn("Your movie", self.driver.title)

    def test_get_a_film_title(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        element = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn('Title:', element)

    def test_get_film_link(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        element = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertIn('TMDB link:', element)

    def test_film_image_display(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        element = self.driver.find_element(By.TAG_NAME, "img")
        image_present = element.is_displayed()
        self.assertTrue(image_present, "No image present")

    def test_get_another_movie(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        self.driver.find_element(By.LINK_TEXT, 'Get another movie').click()
        self.assertIn("Your movie", self.driver.title)
        element = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn('Title:', element)

    def test_get_movie_link(self):
        self.driver.find_element(By.LINK_TEXT, 'Click to get a film!').click()
        movie_url = self.driver.find_element(
            By.LINK_TEXT, 'Click for more info').get_attribute('href')
        movie_title = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.driver.get(movie_url)
        tmdb_movie_title = self.driver.find_element(By.TAG_NAME, "a").text
        self.driver.implicitly_wait(3)
        self.assertIn(tmdb_movie_title, movie_title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
