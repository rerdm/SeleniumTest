import os
import time
import unittest

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
        driver.get(self.test_url)
        print(driver.title)
        self.assertEqual(driver.current_url, "https://www.google.de/")
        driver.close()

    @classmethod
    def tearDown(self):
        print("Tear down called after all tests")

    # python coverage
    # after running the test enter : coverage report -m
    # python -m unittest main.TestUrl.test_open_Url_with_edge
