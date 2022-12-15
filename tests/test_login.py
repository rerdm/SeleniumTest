import os
import sys
import time
import unittest

import xmlrunner as xmlrunner
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from unittest import TestCase


class TestUrl(TestCase):

    # function will be opened one time before all test

    def setUp(self):

        self.test_url = "https://www.google.de/"


        # options: "chrom" , "edge" ,"firefox"
        self.web_driver = "firefox"

        if self.web_driver == "firefox":
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.driver = webdriver.Firefox(options=options)
            print("Test started with " + self.driver.title)

        if self.web_driver == "chrom":
            self.driver = webdriver.Chrome()
            print("Test started with " + self.driver.title)

        if self.web_driver == "edge":
            self.driver = webdriver.Edge()
            print("Test started with " + self.driver.title)

    def tearDown(self):
        print("Tear down called after all tests")

    def test_login(self):

        # Open the website
        self.driver.get(self.test_url)

        # Select the input field by the ID selector
        cockie_button = self.driver.find_element(By.XPATH, value="//*[@id='L2AGLb']")  # Xpath selector
        # Enter values in the input field
        cockie_button.click()

        # Select the search filed
        select_search = self.driver.find_element(By.CSS_SELECTOR, value=".gLFyf") # class selector
        # Add the data in the input field
        select_search.send_keys("Mangia Mania Kronberg")

        # Select the search filed
        submit_search = self.driver.find_element(By.CSS_SELECTOR, value=".gLFyf")  # class selector
        # submit the search by click the enter hot key
        submit_search.send_keys(Keys.ENTER)

        time.sleep(500)

        # Assert


if __name__ == '__main__':
    # You can also run all test ( test_XX ) in the current folder: Folder -> Run Python Test Selenium
    # unittest.main will start the complete Testcase
    unittest.main()
    # Terminal ( for CI tool ore test-machine)
    # python -m unittest  (run all test form the suite)
    # python -m unittest tests.test_url.TestUrl.test_open_Url_with_chrom ( will start 1 method of a testcase)
    #
    # ( will start 2 methods of the testcase)
    # python -m unittest tests.test_url.TestUrl.test_open_Url_with_chrom tests.test_url.TestUrl.test_open_Url_with_chrom

    # python coverage
    # after running the test enter : coverage report -m
    # python -m unittest main.TestUrl.test_open_Url_with_edge

