import os
import time
import unittest

import xmlrunner as xmlrunner
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from unittest import TestCase

class TestUrl(TestCase):

    # function will be opened one time before all test
    @classmethod
    def setUpClass(self):
        self.test_url = "https://www.google.de/"


    def test_open_Url_with_firefox(self):

        print("Test fireFox")
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(options=options)
        driver.get(self.test_url)
        print(driver.title)
        self.assertEqual(driver.current_url,"https://www.google.de/")
        driver.close()

    def test_open_Url_with_chrom(self):
        print("Test Chrom")
        driver = webdriver.Chrome()
        driver.get(self.test_url)
        print(driver.title)
        self.assertEqual(driver.current_url, "https://www.google.de/")
        driver.close()

    def test_open_Url_with_edge(self):
        print("Test Edge")
        driver = webdriver.Edge()
        driver.get(self.test_url)
        print(driver.title)
        self.assertEqual(driver.current_url, "https://www.google.de/")
        driver.close()

    def test_open_Url_with_ie(self):
        print("Test Internet Explorer")
        driver = webdriver.Edge()
        driver.maximize_window() #  To fix the Zoom issue

        try:
            driver.get(self.test_url)
        except Exception as ex:
            print("Exception : " + ex)

        print(driver.title)
        self.assertEqual(driver.current_url, "https://www.google.de/")
        driver.close()

    @classmethod
    def tearDown(self):
        print("Tear down called after all tests")

if __name__ == '__main__':

    # You can also run all test ( test_XX ) in the current folder: Folder -> Run Python Test Selenium
    # unittest.main will start the complete Testcase
    unittest.main()
    # from terminal:
    # python -m unittest  (run all test form the suite)
    # python -m unittest tests.test_url.TestUrl.test_open_Url_with_chrom ( will start a specific tc from suite)

    # python coverage
    # after running the test enter : coverage report -m
    # python -m unittest main.TestUrl.test_open_Url_with_edge
