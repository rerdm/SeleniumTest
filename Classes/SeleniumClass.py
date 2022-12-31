import os
import sys
import time

import xmlrunner as xmlrunner
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import logging

from unittest import TestCase

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def sleep_x_secs():
    time.sleep(300)


class SeleniumClass:
    """
    The class contains all methods for testing a website via selenium
    Available options , parameters and return values can ve checked with help(SeleniumClass)
    """

    def __init__(self, driver):
        """
        The constructor method is used to initialize the driver
        :param driver: --> available options  chrom , firefox , edge
        """
        self.web_driver = driver

        if self.web_driver == "firefox":
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.driver = webdriver.Firefox(options=options)

        if self.web_driver == "chrom":
            self.driver = webdriver.Chrome()

        if self.web_driver == "edge":
            self.driver = webdriver.Edge()

        self.wait = WebDriverWait(self.driver, 5)

        # Configuration of the logger
        logging.basicConfig(
            filename="program2.log",
            level=logging.INFO,
            style="{",
            format="{asctime} [{levelname:8}] {message}",

        )

    def open_website(self, url):

        self.driver.get(url)
        self.driver.maximize_window()

    def set_cookies(self, token_value):

        if token_value:
            cookie = {'name': 'token', 'value': token_value}
            self.driver.add_cookie(cookie)

    def get_cookies(self):
        print(self.driver.get_cookies())

    def sleeep_5Secs(self):
        """
        This method is used to set a small waiting time from 5 seconds
        """
        time.sleep(5)

    def sleeep_500Secs(self):
        time.sleep(500)
        """
        This method is used to set a big waiting time from 500 seconds.
        Can be used to analyze the web page while the program is running 
        """

    def submit_shadow_element(self, iquery_path_to_element):
        """
        This method can be used to find html elements in teh shadow dom. Without such functionality the shwdow
        dom elements can not be fond
        How to :
        1. You have to find the Root Host element
           The first element parent element which don´t show the error:"This element is inside shadow dome..."
           That element will be you host element.
        2. With JavasCript (Inside the Console) you can search this elements inside the shadow dome and generate the code.
        3. This code can be inserted the selenium method "execute_stript" of you driver
        4. Then you can use teh available methods (click..)

        :param iquery_path_to_element --> Generated iquery string
        example( bahn website)
        "return document.querySelector('body > div:nth-child(1)').shadowRoot.querySelector('#consent-layer > div.consent-layer__btn-container > button.btn.btn--secondary.js-accept-all-cookies')"
        """
        path_to_shadow_element = iquery_path_to_element
        # "return document.querySelector('body > div:nth-child(1)').shadowRoot.querySelector('#consent-layer > div.consent-layer__btn-container > button.btn.btn--secondary.js-accept-all-cookies')"

        coockie = self.driver.execute_script(path_to_shadow_element)
        coockie.click()

    def purpose_of_event(self, event_name):
        print("Action")

    def submit_element(self, select_by_xpath=0, select_by_class=0, select_by_id=0, select_by_link_text=0, select_by_css_selector=0, value=0):

        if bool(select_by_xpath):

            cookie_button = self.driver.find_element(By.XPATH, value=select_by_xpath)  # Xpath selector
            logging.info("Element selected")

            if bool(value):
                cookie_button.send_keys(value)
            if not bool(value):
                cookie_button.click()

        if bool(select_by_link_text):

            cookie_button = self.driver.find_element(By.LINK_TEXT, value=select_by_link_text)
            logging.info("Element selected")

            if bool(value):
                cookie_button.send_keys(value)
            if not bool(value):
                cookie_button.click()

        if bool(select_by_class):

            cookie_button = self.driver.find_element(By.CLASS_NAME, value=select_by_class)  # Xpath selector
            logging.info("Element selected")

            if bool(value):
                cookie_button.send_keys(value)
            if not bool(value):
                cookie_button.click()

        if bool(select_by_css_selector):

            cookie_button = self.driver.find_element(By.CSS_SELECTOR, value=select_by_css_selector)  # Xpath selector
            logging.info("Element selected")

            if bool(value):
                cookie_button.send_keys(value)
            if not bool(value):
                cookie_button.click()

        if bool(select_by_id):
            cookie_button = self.driver.find_element(By.ID, value=select_by_id)  # Xpath selector
            logging.info("Element selected")

            if bool(value):
                cookie_button.send_keys(value)
            if not bool(value):
                cookie_button.click()

    def submit_window(self, select_by_class):
        """
        This method is used to send the return key on a specific web element (simulates key press)
        :param select_by_class: --> class from the web element

        """
        submit_window = self.driver.find_element(By.CLASS_NAME, value=select_by_class)
        submit_window.send_keys(Keys.ENTER)

    def find_string_in_google_search_results(self, select_by_relative_xpath):
        """
        This method will scroll the actual page to the specific web element
        :param select_by_relative_xpath: --> relative xpath of web element
        :return:
        """
        web_element = self.driver.find_element(By.XPATH, value=select_by_relative_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def scroll_page_to_specific_xpath(self, scroll_to_relative_xpath):
        """
        This method will scroll to a specific web element on the webpage
        input parameter = xpath to specific web element ( recommended to use relative xpath )
                          example = "//h3[normalize-space()='Heidi und Paul Lieferservice']"
        :param scroll_to_relative_xpath:
        """
        scroll_to_element = self.driver.find_element(By.XPATH, value=scroll_to_relative_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_element)

    def scroll_page_to_top(self):
        """
        This method can be used to scroll the actual page to the top. This method uses the
        execute_script functionality:
        Script:  window.scrollBy(0,0),""  --> window.scrollBy(x,y),""
        """
        self.driver.execute_script("window.scrollBy(0,1000)", "")

    def set_select_option(self, id_of_element, select_element_text="", select_element_by_value=""):
        """
        This function
        :param id_of_element: --> if of the web element (mandatory)
        :param select_element_text: --> this will select the item via the text
        :param select_element_by_value: --> this will select the item via the value
        :return:
        """

        if bool(select_element_text) != bool(select_element_by_value):

            self.select_options = self.driver.find_elements(By.TAG_NAME, 'option')

            element_found = False
            value_found = False
            value = ""

            for self.available_select_element in self.select_options:

                if self.available_select_element.text == select_element_text:
                    element_found = True
                    value = self.available_select_element.get_attribute("value")
                    if value:
                        print("Value of element:", value, ": Text of element", select_element_text)

                if self.available_select_element.get_attribute("value") == select_element_by_value:
                    value_found = True
                    value = self.available_select_element.get_attribute("value")
                    if value:
                        print("Value of element:", value, " ", self.available_select_element.text)

            if element_found or value_found and value:

                select_item = Select(self.driver.find_element(By.ID, id_of_element))
                select_item.select_by_value(value)

            else:

                error = "selected option not available"
                print(error + "- see available options:")
                for self.available_select_element in self.select_options:
                    available_value = self.available_select_element.get_attribute("value")
                    if available_value:
                        print("Value of element:", available_value, ": Text of element :",
                              self.available_select_element.text)

                # Close the driver when web element is not available
                self.driver_close(error_string=error)

        else:
            error = "Function only accepts - select_element_text or select_element_by_value not both (XOR)"
            self.driver_close(error_string=error)

    def get_elements(self, select_by_xpath, element_text):

        elements = self.driver.find_elements(By.XPATH, select_by_xpath)

        for element in elements:

            if element_text in element.text:

                print(element.text)
                element.click()
                print("\n")

        print(len(elements))

    def stop_test(self):
        self.driver.close()
        sys.exit("Program stop - DEBUGGING ")

    def driver_close(self, error_string="0"):
        self.driver.close()
        if error_string and error_string != "0":
            print("\n")
            sys.exit("\t Error : "+error_string)
        else:
            pass


if __name__ == '__main__':

    #  TODO main program
    waiting_time = 2
    waiting_time_extended = 500

    test = int(input("""
    Available tests: \n
     1 - Order a Burger via google  
     2 - Google website test
     3 - Help \n
     Enter test number:  """))

    # Google test
    if test == 1:
        test_url_google = "https://www.google.com/"
        web_test_google = SeleniumClass(driver="firefox")
        web_test_google.open_website(test_url_google)
        web_test_google.sleeep(waiting_time)

        #  Accept cookies from google
        web_test_google.submit_element(select_by_id="L2AGLb")
        web_test_google.sleeep(waiting_time)

        #  Enter input in google
        input_class = "gLFyf"  # id from input field
        input_value = "Heidi und paul"  #

        web_test_google.submit_element(select_by_class=input_class, value=input_value)
        web_test_google.sleeep(waiting_time)

        # Function will send return key one this element tu submit the page
        web_test_google.submit_window(input_class)
        web_test_google.sleeep(waiting_time)

        # This function will scroll the page till it will find the xpath by relative path
        xpath_element = "//h3[normalize-space()='Heidi und Paul Lieferservice']"
        # web_test_google.scroll_page_to_specific_xpath(scroll_to_relative_xpath=xpath_element)
        # web_test_google.sleeep(waiting_time)

        # Submit the web element
        web_test_google.submit_element(select_by_xpath=xpath_element)
        web_test_google.sleeep(waiting_time)

        # Accept the cookies
        xpath_to_coockie = "CybotCookiebotDialogBodyButtonAccept"
        web_test_google.submit_element(select_by_id=xpath_to_coockie)
        web_test_google.sleeep(waiting_time)

        # Click in select filed to see all options
        #selector = "store-id"
        #web_test_google.submit_element(select_by_id=selector)
        #web_test_google.sleeep(waiting_time)

        # Select a value from possible options - in case the option is not available the program will stop and
        # list the available options
        # web_test_google.set_select_option(select_element_by_value="3")

        #web_test_google.set_select_option(id_of_element="store-id", select_element_text="Eschborn")
        web_test_google.submit_element(select_by_link_text="Kontakt")

        web_test_google.sleeep(waiting_time_extended)


        # Select delivery: Delivery
        # selector = "//div[@ng-show='ctrl.store.is_delivery_active']"
        # web_test_google.submit_element(select_by_xpath=selector)
        # web_test_google.sleeep(waiting_time_extended)

        # Select delivery: take-away
        selector = "//div[@ng-show='ctrl.store.is_take_away_active']"
        web_test_google.submit_element(select_by_xpath="//div[@ng-show='ctrl.store.is_take_away_active']")
        web_test_google.sleeep(waiting_time)

        # Go to Menu
        web_test_google.submit_element(select_by_xpath="//button[normalize-space()='Zur Menü-Auswahl']")
        # Note: Class elements will be concationated with a dot (.) eg. class = "btn btn-primary btn-block" --> btn.btn-primary.btn-block
        #web_test_google.submit_element(select_by_css_selector=".btn.btn-primary.btn-block", value="61476")
        web_test_google.sleeep(waiting_time)

        # Select a Burger
        Available_burgers = {1: "Der Pure",
                             2: "Der Klassiker",
                             3: "Der Käsige",
                             4: "Der Manchego",
                             5: "Der Scharfe",
                             6: "Die Grünhilde",
                             7: "Der Waldmeister",
                             8: "Der Framer",
                             }

        web_test_google.get_elements(select_by_xpath="//*[@id='category-3']/div/div", element_text=Available_burgers[7])
        web_test_google.sleeep(waiting_time)


        web_test_google.submit_element(select_by_xpath="// span[normalize - space() = 'Weizenbrötchen']")
        web_test_google.sleeep(waiting_time_extended)

        web_test_google.driver_close()

    # Bahn test
    if test == 2:
        test_url_bahn = "https://www.bahn.de/"

        web_test_bahn = SeleniumClass(driver="firefox")
        web_test_bahn.open_website(test_url_bahn)
        web_test_bahn.sleeep(5)

        # Error : This element is inside Shadow DOM and for such elements XPat
        # //This Element is inside "single" shadow DOM - if you have more shadows you can see find the selectors in
        # selectorsHub
        # shadow-root (open)
        # How to get the shadow path see function

        web_test_bahn.submit_shadow_element()
        # test.get_cookies()
        web_test_bahn.sleeep(5)

        web_test_bahn.driver_close()

    if test == 7:
        # Order A Burger
        test_url_order_a_burger = "https://www.heidiundpaul.de/"
        web_test_bahn.open_website(test_url_order_a_burger)
        cookie_path_01_id = "CybotCookiebotDialogBodyButtonAccept"

        web_test_bahn.submit_element(select_by_id=cookie_path_01_id)


        # test.select_cookies(selected_by_id="consent-layer")

        # You can also run all test ( test_XX ) in the current folder: Folder -> Run Python Test Selenium
        # unittest.main will start the complete Testcase
        # unittest.main()
        # Terminal ( for CI tool ore test-machine)
        # python -m unittest  (run all test form the suite)
        # python -m unittest tests.test_url.TestUrl.test_open_Url_with_chrom ( will start 1 method of a testcase)
        #
        # ( will start 2 methods of the testcase)
        # python -m unittest tests.test_url.TestUrl.test_open_Url_with_chrom tests.test_url.TestUrl.test_open_Url_with_chrom

        # python coverage
        # after running the test enter : coverage report -m
        # python -m unittest main.TestUrl.test_open_Url_with_edge

    if test == 3:
        print(SeleniumClass.__doc__)
        print(help(SeleniumClass))
