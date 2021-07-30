import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_present_page(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form")
    time.sleep(7)
    assert button, "No such button on the page"