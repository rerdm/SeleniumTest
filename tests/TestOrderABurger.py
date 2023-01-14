import unittest

from Classes.SeleniumClass import SeleniumClass


class TestOrderABruger(unittest.TestCase):

    def setUp(self):
        print("SETUP - class is called")
        self.driver = SeleniumClass(driver="firefox")

    def tearDown(self):
        pass

    def test_order_a_burger(self):
        ## Arrange
        self.driver.open_website("https://www.google.com/")
        self.driver.maximize_window()

        #  Accept cookies from Google
        self.driver.submit_element(select_by_id="L2AGLb", objective="Coockies btn")

        #  Enter input in google
        input_class = "gLFyf"  # id from input field
        input_value = "Heidi und paul"  #

        self.driver.submit_element(select_by_class=input_class, value=input_value, objective="Input filed")

        # Function will send return key one this element tu submit the page
        self.driver.submit_window(input_class, objective="Submit element with Return Key")

        text = self.driver.get_value_of_element_via_iquery(select_by_class="LC20lb MBeuO DKV0Md")
        print(text)



if __name__ == '__main__':
    unittest.main()
