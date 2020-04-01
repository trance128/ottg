""" 
Functional and unit tests for the project, using Selenium.

Coded by Ovid Mazuru, following Obey the Testing Goat
"""

import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    """
    Test that follows the story of a new user, whom adds a to do item and checks if it persists
    """
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        Name is self explanatory -- test to see if user can start a list and retrieve it later from generated URL
        """
        # Edith has heard about a cool new To-Do App, she goes to checkout the homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item straight away

        # She types 'Buy peacock feathers' in the text box  (She seems to have strange hobbies)

        # When she hits enter, the page updates and now the page lists
        # '1.  Buy Peacock Feathers' as an item in the to-do list

        # There is still a text-box inviting her to add another item.  She
        # enters "Use Peacock Feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.  The she sees that
        # the site has generated a unique URL for her -- there is some explanatory text
        # to that effect

        # She visits the URL.  Her to do list is still there.

        # satisfied, she goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
