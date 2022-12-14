import os
import sys
import time
import unittest

import xmlrunner as xmlrunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from unittest import TestCase


class TestUrl(TestCase):

    # function will be opened one time before all test

    def setUp(self):

        self.test_url = "https://seleniumkurs.codingsolo.de/"
        self.website_url = "https://seleniumkurs.codingsolo.de/login?came_from=https%3A//seleniumkurs.codingsolo.de/"

        # options: "chrom" , "edge" ,"firefox"
        self.web_driver = "chrom"

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
        username = self.driver.find_element(By.ID, "__ac_name")
        # Enter values in the input field
        username.send_keys("User01")

        # Select the input field by the ID selector
        password = self.driver.find_element(By.NAME, "__ac_password")
        # Enter values in the input field
        password.send_keys("WrongPassword")

        # Act

        # Select the button by the CSS selector
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[value=Anmelden")
        # Click the button to submit
        login_button.click()

        time.sleep(10)

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

