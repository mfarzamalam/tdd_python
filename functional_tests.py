from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        # when his work is complete he close the browser
        self.browser.quit()
        
    def test_can_start_list_and_retrieve_it_later(self):
        # alex has heard about the new cool to-do app
        # he decided to visits its homepage by clicking on the url
        self.browser.get('http://localhost:8000')


        # he notice the website title has a word To-Do 
        self.assertIn ('To-Do', self.browser.title)
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()