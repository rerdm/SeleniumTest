import os
import sys
import time
from datetime import datetime

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

from Classes.SaveLogingClass import SaveLogging


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
        self.max_display_resolution_height = None
        self.max_display_resolution_width = None
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
        self.size = ""

        # if save_log:
        # Configuration of the logger
        # logging.basicConfig(
        #     #filename="program2.log",  # -->  create logging file
        #     level=logging.INFO,  # --> set the log level
        #     style="{",
        #     format="{asctime} [{levelname:8}] {message}",
        #     # datefmt="%d.%m.%Y %H:%M:%S"
        # )

        log = SaveLogging(logfilename="LoggingTest")
        log.write_initial_line(line="line1")
        log.append_lines(line="line2")


    def open_website(self, url):
        """
        This method will open the website
        :param url: --> website you want to open
        """
        self.driver.get(url)
        logging_text = "Open website : " + url
        #SaveLogging.append_lines(line=logging_text)

    def maximize_window(self):
        self.driver.maximize_window()
        logging.info("Maximize window to 100%")
        self.driver.maximize_window()

    def set_max_size_of_monitor(self):

        self.avail_screen_height = self.driver.execute_script("return window.screen.availHeight")
        self.avail_screen_width = self.driver.execute_script("return window.screen.availWidth")

        logging.info(
            "Maximal Display resolution check - MaxWidth: " + str(self.avail_screen_width) + " MayHeight :" + str(
                self.avail_screen_height))

    def get_window_size(self):

        """
        This method can be used to get the window size of teh actual running selenium window.
        Mainly intended fot testing preparation purposes
        """

        self.size = self.driver.get_window_size()
        logging.info("GET - Window size - width: " + str(self.size["width"]) + " height : " + str(self.size["height"]))

        # self.max_display_resolution_width = int(self.size["width"])
        # self.max_display_resolution_height = int(self.size["height"])

    def set_window_size(self, width, height):
        """
        This method can be used to define a specific width and height for the current window.
        To see the available.
        Hint to see the available display resolution first check get_max_size_of_monitor()
        :param width: width in pixel (int)
        :param height: height in pixel (int)
        :return:
        """
        self.driver.set_window_size(width=width, height=height)
        logging.info("SET - Window size - width: " + str(height) + " height : " + str(height))

    def set_window_size_to_x_percentage(self, percentage=20):

        y_pixel = float((self.avail_screen_width / 100)) * percentage
        x_pixel = float((self.avail_screen_height / 100)) * percentage

        logging.info(
            "SET- Window size to : " + str(percentage) + "% - Width in Px :" + str(y_pixel) + " Height in Px :" + str(
                x_pixel))

        self.driver.set_window_size(width=y_pixel, height=x_pixel)

    def set_cookies(self, token_value):

        if token_value:
            cookie = {'name': 'token', 'value': token_value}
            self.driver.add_cookie(cookie)

    def get_cookies(self):
        print(self.driver.get_cookies())

    def sleeep_XSecs(self, seconds):

        logging.info("Set sleeping time - " + str(seconds) + " Seconds")
        time.sleep(seconds)
        """
        This method is used to set a user defined waiting 
        and print this infomration in the logging stream 
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
        example(bahn website)
        "return document.querySelector('body > div:nth-child(1)').shadowRoot.querySelector('#consent-layer > div.consent-layer__btn-container > button.btn.btn--secondary.js-accept-all-cookies')"
        """
        path_to_shadow_element = iquery_path_to_element
        # "return document.querySelector('body > div:nth-child(1)').shadowRoot.querySelector('#consent-layer > div.consent-layer__btn-container > button.btn.btn--secondary.js-accept-all-cookies')"

        coockie = self.driver.execute_script(path_to_shadow_element)
        coockie.click()

    def submit_element_by_rel_xpath_normalize_space(self, tag, search_string, objective):

        # // a[normalize - space() = 'Reise']
        rel_xpath = "//" + tag + "[normalize-space()='" + search_string + "'])"
        btn = self.driver.find_element(By.XPATH, rel_xpath)
        logging.info(objective + ": Web-Element selected by xpath and normalize-space function: " + rel_xpath)
        logging.info(objective + ": Web-Element clicked")
        btn.click()

    def submit_element_by_rel_xpath_contains(self, tag, search_string, objective):

        # TODO create function
        # "//h3[contains(text(),'CHECK24 im App Store')]"
        rel_xpath = "//" + tag + "[contains(text(),'" + search_string + "')]"
        logging.info(objective + ": Web-Element selected by xpath and contains function: " + rel_xpath)
        logging.info(objective + ": Web-Element clicked")
        self.driver.find_element(By.XPATH, rel_xpath).click()

    def submit_element(self, objective, select_by_xpath=0, select_by_class=0, select_by_id=0, select_by_link_text=0,
                       select_by_css_selector=0, value=0, get_text=False):

        if bool(select_by_xpath) and not bool(get_text):

            cookie_button = self.driver.find_element(By.XPATH, value=select_by_xpath)  # Xpath selector
            logging.info(objective + ": Web-Element selected by xpath: " + select_by_xpath)

            if bool(value):
                logging.info(objective + ": Set input value: " + value)
                cookie_button.send_keys(value)

            if not bool(value):
                logging.info(objective + ": Web-Element clicked")
                cookie_button.click()

        if bool(select_by_link_text) and not bool(get_text):

            cookie_button = self.driver.find_element(By.LINK_TEXT, value=select_by_link_text)
            logging.info(objective + ": Web-Element selected by link_text: " + select_by_link_text)

            if bool(value):
                cookie_button.send_keys(value)
                logging.info(objective + ": Set input value: " + value)
            if not bool(value):
                logging.info(objective + ": Web-Element clicked")
                cookie_button.click()

        if bool(select_by_class) and not bool(get_text):

            cookie_button = self.driver.find_element(By.CLASS_NAME, value=select_by_class)  # Xpath selector
            logging.info(objective + ": Web-Element selected by class: " + select_by_class)

            if bool(value):
                cookie_button.send_keys(value)
                logging.info(objective + ": Set input value: " + value)
            if not bool(value):
                logging.info(objective + ": Web-Element clicked")
                cookie_button.click()

        if bool(select_by_css_selector) and not bool(get_text):

            cookie_button = self.driver.find_element(By.CSS_SELECTOR, value=select_by_css_selector)  # Xpath selector
            logging.info(objective + ": Web-Element selected by css selector: " + select_by_css_selector)

            if bool(value):
                cookie_button.send_keys(value)
                logging.info(objective + ": Set input value: " + value)
            if not bool(value):
                logging.info(objective + ": Web-Element clicked")
                cookie_button.click()

        if bool(select_by_id) and not bool(get_text):
            cookie_button = self.driver.find_element(By.ID, value=select_by_id)  # Xpath selector
            logging.info(objective + ": Web-Element selected by id: " + select_by_id)

            if bool(value):
                logging.info(objective + ": Set input value: " + value)
                cookie_button.send_keys(value)

            if not bool(value):
                logging.info(objective + ": Web-Element clicked")
                cookie_button.click()

        if bool(get_text):
            element_text = ""

            return element_text

    def submit_window(self, select_by_class, objective):
        """
        This method is used to send the return key on a specific web element (simulates key press)
        :param select_by_class: --> class from the web element
        :param objective: This param is for debugging purpose the  step the
        :return:
        """
        submit_window = self.driver.find_element(By.CLASS_NAME, value=select_by_class)
        logging.info(objective + ": Submit element by using with class: " + select_by_class)
        submit_window.send_keys(Keys.ENTER)

    def find_string_in_google_search_results(self, select_by_relative_xpath):
        """
        This method will scroll the actual page to the specific web element
        :param select_by_relative_xpath: --> relative xpath of web element
        :return:
        """
        web_element = self.driver.find_element(By.XPATH, value=select_by_relative_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def scroll_page_to_specific_rel_xpath(self, scroll_to_relative_xpath):
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
        TBD
        :param id_of_element: --> id of the web element (mandatory)
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
                        logging.info("Select element - value : " + value + ": Text of element :" + select_element_text)

                if self.available_select_element.get_attribute("value") == select_element_by_value:
                    value_found = True
                    value = self.available_select_element.get_attribute("value")
                    if value:
                        logging.info(
                            "Select element - value : " + value + " Text of element : " + self.available_select_element.text)

            if element_found or value_found and value:

                select_item = Select(self.driver.find_element(By.ID, id_of_element))
                select_item.select_by_value(value)

            else:

                error = "Selected option not available"
                logging.error(error + "- see available options:")
                for self.available_select_element in self.select_options:
                    available_value = self.available_select_element.get_attribute("value")
                    if available_value:
                        logging.error("Value of element:" + available_value + ": Text of element :" +
                                      self.available_select_element.text)

                # Close the driver when web element is not available
                self.driver_close(error_string=error)

        else:
            error = "Function only accepts - select_element_text or select_element_by_value not both (XOR)"
            self.driver_close(error_string=error)

    def submit_element_from_selection(self, select_by_xpath, element_text):

        elements = self.driver.find_elements(By.XPATH, select_by_xpath)
        element_list = []
        for element in elements:

            if element_text in element.text:
                logging.info("Element found : " + element_text)
                element.click()

        return len(elements), element_list

    def get_value_of_element_via_iquery(self, select_by_class=""):

        combined_class = select_by_class.replace(" ", ".")
        assembled_class = "." + combined_class
        get_text_content_via_jquery = "return window.document.querySelector('" + assembled_class + "').textContent"

        compare_text = self.driver.execute_script(get_text_content_via_jquery)
        logging.info("GET - the value from html to compare with expected result - VALUE :" + compare_text)

        return compare_text

    def stop_test(self):
        self.driver.close()
        logging.info("Program stop")
        # sys.exit()

    def driver_close(self, error_string="0"):
        self.driver.close()

        if error_string and error_string != "0":

            logging.error(error_string + " Program will close")
            sys.exit()
        else:
            logging.info("Program stopped - Error Code:" + error_string)
            sys.exit()
