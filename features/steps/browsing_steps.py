from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from config_reader import ConfigReader
from pages.login_page import LoginPage
from components.right_menu import RightMenu
from components.navigation_bar import NavigationBar
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://techskillacademy.net/brainbucket/index.php"
configs = ConfigReader("config.ini")


@given("user opens Brainbucket home page in a browser")
def launch_home_page(context):
    browser = Browser(URL, configs.get_browser('environment'), configs.get_wait_time('environment'))
    context.browser = browser
    header = Header(context.browser)
    context.header = header
    # checking the user is on Brainbucket website, the logo is visible
    header.logo.wait_until_visible()
    # checking the user is on home page, the slideshow is visible
    slideshow = Element(browser, By.ID, "slideshow0")
    slideshow.wait_until_visible()


@when('user moves to "{section}" in navigation bar')
def open_section_page(context, section):
    browser = context.browser
    navigation_bar = NavigationBar(browser)
    context.navigation_bar = navigation_bar
    if section == 'Desktops':
        navigation_bar.move_to_desktops()
    elif section == 'Phones & PDAs':
        navigation_bar.move_to_phones_and_pdas()
    elif section == 'Components':
        navigation_bar.move_to_components()


@when('user clicks on "{option}" of a dropdown menu')
def open_option_page(context, option):
    navigation_bar = context.navigation_bar
    if option == 'Macs':
        navigation_bar.select_mac_desktops()
    elif option == 'PC':
        navigation_bar.select_pcs()
    elif option == 'Phones':
        navigation_bar.select_phones()
    elif option == 'Show All Components':
        navigation_bar.select_all_components()


@then('page with all "{product}" is open')
def check_product_page_open(context, product):
    browser = context.browser
    # product page title on a product page
    product_page_title = Element(browser, By.XPATH, "//h2")
    if product == 'Mac desktops':
        assert product_page_title.get_text() == 'Mac'
    elif product == 'PC desktops':
        assert product_page_title.get_text() == 'PC'
    elif product == 'Phones':
        assert product_page_title.get_text() == 'Phones'
    elif product == 'Components':
        assert product_page_title.get_text() == 'Components'
    time.sleep(2)
    browser.shutdown()
