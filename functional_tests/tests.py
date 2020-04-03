""" 
Functional and unit tests for the project, using Selenium.

Coded by Ovid Mazuru, following Obey the Testing Goat
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    """
    Test that follows the story of a new user, whom adds a to do item and checks if it persists
    """
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        Name is self explanatory -- test to see if user can start a list and retrieve
        it later from generated URL
        """
        # Edith has heard about a cool new To-Do App, she goes to checkout the homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'Buy peacock feathers' in the text box  (She seems to have strange hobbies)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and now the page lists
        # '1.  Buy Peacock Feathers' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_table("1: Buy peacock feathers")

        # There is still a text-box inviting her to add another item.  She
        # enters "Use Peacock Feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_table("1: Buy peacock feathers")
        self.check_for_row_in_table("2: Use peacock feathers to make a fly")

        # Edith wonders whether the site will remember her list.  The she sees that
        # the site has generated a unique URL for her -- there is some explanatory text
        # to that effect
        self.fail("Finish the test!")

        # She visits the URL.  Her to do list is still there.

        # satisfied, she goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
