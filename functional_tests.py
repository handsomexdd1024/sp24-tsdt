from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        
    def tearDown(self) -> None:
        self.browser.quit
        
    def test_open_homepage(self):
        
        # Jean heard about this cool To-Do list site
        # She opens this site
        self.browser.get('http://localhost:8000')
        
        # The title contains 'To-Do'
        assert 'To-Do' in self.browser.page_source, "Browser title was:" + self.browser.title
        
        # There's an input box at the centre of homepage
        # Which is used to input to-do items
        
        # She entered 'Buy flowers' in the input box
        
        # She closes the page, open it again, and saw her to-do item still exist
        
        # Jean is now satisfied and left the page.
        
if __name__ == '__main__':
    unittest.main()