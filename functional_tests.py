from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time


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

        # he notice the website header has a word To-Do 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He invited to fill the To-Do list
        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputBox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types 'Play the Piano' in the text-box and hit enter
        inputBox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_table_list')
        rows  = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Play the Piano') for row in rows)

        # There's still a text-box asking him to enter another item.
        # He enter another item 'Come back home with dhaniya'
        self.fail("Finish the test!")

        # The page updates again when she press the enter and show both item in his list


if __name__ == '__main__':
    unittest.main()