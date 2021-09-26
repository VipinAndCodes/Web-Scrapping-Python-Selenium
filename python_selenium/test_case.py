import unittest
from selenium import webdriver
import page

#acces to some methods

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_example(self):
        #start with word test to work method
        assert True

    def tearDown(self):
        # run after test case..like cleaning the mess
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
