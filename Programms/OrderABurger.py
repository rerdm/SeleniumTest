from Classes.SeleniumClass import SeleniumClass

if __name__ == '__main__':
    waiting_time = 2
    waiting_time_extended = 500

    test_url_google = "https://www.google.com/"
    web_test_google = SeleniumClass(driver="firefox")
    web_test_google.open_website(test_url_google)

    web_test_google.set_max_size_of_monitor()
    web_test_google.set_window_size_to_x_percentage(percentage=100)

    web_test_google.sleeep_XSecs(waiting_time)

    #  Accept cookies from google
    web_test_google.submit_element(select_by_id="L2AGLb", objective="Coockies btn")
    web_test_google.sleeep_XSecs(waiting_time)

    #  Enter input in google
    input_class = "gLFyf"  # id from input field
    input_value = "Heidi und paul"  #

    web_test_google.submit_element(select_by_class=input_class, value=input_value, objective="Input filed")
    web_test_google.sleeep_XSecs(waiting_time)

    # Function will send return key one this element tu submit the page
    web_test_google.submit_window(input_class, objective="Submit element with Return Key")
    web_test_google.sleeep_XSecs(waiting_time)

    # This function will scroll the page till it will find the xpath by relative path
    xpath_element = "//h3[normalize-space()='Heidi und Paul Lieferservice']"
    # web_test_google.scroll_page_to_specific_xpath(scroll_to_relative_xpath=xpath_element)
    # web_test_google.sleeep(waiting_time)

    # Submit web element
    web_test_google.submit_element(select_by_xpath=xpath_element, objective="Google")
    web_test_google.sleeep_XSecs(waiting_time)

    # Accept the cookies
    xpath_to_coockie = "CybotCookiebotDialogBodyButtonAccept"
    web_test_google.submit_element(select_by_id=xpath_to_coockie, objective="Select Cookies")
    web_test_google.sleeep_XSecs(waiting_time)

    # Click in select filed to see all options
    selector = "store-id"
    web_test_google.submit_element(select_by_id=selector, objective="See available select options")
    web_test_google.sleeep_XSecs(waiting_time)

    # Select a value from possible options - in case the option is not available the program will stop and
    # list the available options
    selection_web_element_id = "store-id"
    web_test_google.set_select_option(id_of_element="store-id", select_element_text="Eschborn")
    # web_test_google.set_select_option(id_of_element=selection_web_element_id, select_element_by_value="3")

    web_test_google.sleeep_XSecs(waiting_time)

    # iquery_path = "return document.querySelector('.layout-header__desktop-nav.d-none.d-none.d-lg-flex > a')"
    # web_test_google.submit_shadow_element(iquery_path_to_element=iquery_path)

    # Select delivery: Delivery
    # selector = "//div[@ng-show='ctrl.store.is_delivery_active']"
    # web_test_google.submit_element(select_by_xpath=selector)
    # web_test_google.sleeep(waiting_time_extended)

    # Select delivery: take-away
    selector = "//div[@ng-show='ctrl.store.is_take_away_active']"
    web_test_google.submit_element(select_by_xpath="//div[@ng-show='ctrl.store.is_take_away_active']",
                                   objective="Select take away")
    web_test_google.sleeep_XSecs(waiting_time)

    # Go to Menu
    web_test_google.submit_element(select_by_xpath="//button[normalize-space()='Zur Menü-Auswahl']",
                                   objective="submit menu")

    # Note: Class elements will be concationated with a dot (.) eg. class = "btn btn-primary btn-block" --> btn.btn-primary.btn-block
    # web_test_google.submit_element(select_by_css_selector=".btn.btn-primary.btn-block", value="61476")
    web_test_google.sleeep_XSecs(waiting_time)

    # Select  Burger 1
    # Available_burgers
    # "Der Pure",
    # "Der Klassiker",
    # "Der Käsige",
    # "Der Manchego",
    # "Der Scharfe",
    # "Die Grünhilde",
    # "Der Waldmeister",
    # "Der Farmer",

    web_test_google.submit_element_from_selection(select_by_xpath="//*[@id='category-3']/div/div", element_text="Der Farmer")
    web_test_google.sleeep_XSecs(waiting_time)

    web_test_google.submit_element_by_rel_xpath_contains(tag="span", search_string="Weizenbrötchen", objective="Choose bred")
    web_test_google.sleeep_XSecs(waiting_time)

    web_test_google.submit_element_by_rel_xpath_contains(tag="span", search_string="Bacon", objective="Choose extra")
    web_test_google.submit_element_by_rel_xpath_contains(tag="span", search_string='Knusprige Süßkartoffelpommes', objective="Our Fingerfood")
    web_test_google.sleeep_XSecs(waiting_time)

    # Add to Burger to card
    web_test_google.submit_element(select_by_xpath="// button[@class ='btn btn-primary btn-block ng-binding']", objective="Add burger to card")
    web_test_google.sleeep_XSecs(waiting_time)

    # Select  Burger 1
    # Available_burgers
    # "Der Pure",
    # "Der Klassiker",
    # "Der Käsige",
    # "Der Manchego",
    # "Der Scharfe",
    # "Die Grünhilde",
    # "Der Waldmeister",
    # "Der Farmer",

    web_test_google.submit_element_from_selection(select_by_xpath="//*[@id='category-3']/div/div", element_text="Der Waldmeister")
    web_test_google.sleeep_XSecs(waiting_time)

    web_test_google.submit_element_by_rel_xpath_contains(tag="span", search_string="Weizenbrötchen", objective="Choose bred")
    web_test_google.sleeep_XSecs(waiting_time)

    web_test_google.submit_element_by_rel_xpath_contains(tag="span", search_string='Knusprige Süßkartoffelpommes', objective="Our Fingerfood")
    web_test_google.sleeep_XSecs(waiting_time)

    # Add to Burger to card
    web_test_google.submit_element(select_by_xpath="// button[@class ='btn btn-primary btn-block ng-binding']", objective="Add burger to card")
    web_test_google.sleeep_XSecs(waiting_time)


    # Get the result to compare the price ##############################################################################

    compare_value = web_test_google.get_value_of_element_via_iquery(select_by_class="price ng-binding")

    web_test_google.driver_close()




