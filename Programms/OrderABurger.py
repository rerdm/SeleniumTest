from Classes.SeleniumClass import SeleniumClass

if __name__ == '__main__':
    waiting_time = 5
    waiting_time_extended = 500


    test_url_google = "https://www.google.com/"
    web_test_google = SeleniumClass(driver="firefox")
    web_test_google.open_website(test_url_google)
    web_test_google.stop_test()

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
    # selector = "store-id"
    # web_test_google.submit_element(select_by_id=selector)
    # web_test_google.sleeep(waiting_time)

    # Select a value from possible options - in case the option is not available the program will stop and
    # list the available options
    # web_test_google.set_select_option(select_element_by_value="3")

    # web_test_google.set_select_option(id_of_element="store-id", select_element_text="Eschborn")
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
    # web_test_google.submit_element(select_by_css_selector=".btn.btn-primary.btn-block", value="61476")
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
