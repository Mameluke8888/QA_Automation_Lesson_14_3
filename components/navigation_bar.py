from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By
from actions_fixed import Actions
from webelements.dropdown2 import Dropdown


class NavigationBar:
    def __init__(self, browser):
        self.actions = Actions(browser)
        self.driver = browser.get_driver()
        self._option_text = ""

        # Items
        self.desktops = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[1]")
        self.laptops = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[2]")
        self.components = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[3]")
        self.tablets = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[4]")
        self.software = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[5]")
        self.phones_and_pdas = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[6]")
        self.cameras = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[7]")
        self.mp3_players = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[8]")

        # Dropdowns
        self.dropdown_list_xpath = "//div[@class='dropdown-menu']"
        self.desktops_dropdown = Dropdown(browser, By.XPATH, self.desktops.get_locator() + self.dropdown_list_xpath)
        self.laptops_dropdown = Dropdown(browser, By.XPATH, self.laptops.get_locator() + self.dropdown_list_xpath)
        self.components_dropdown = Dropdown(browser, By.XPATH, self.components.get_locator() + self.dropdown_list_xpath)
        self.tablets_dropdown = Dropdown(browser, By.XPATH, self.tablets.get_locator() + self.dropdown_list_xpath)
        self.software_dropdown = Dropdown(browser, By.XPATH, self.software.get_locator() + self.dropdown_list_xpath)
        self.phone_dropdown = Dropdown(browser, By.XPATH, self.phones_and_pdas.get_locator() + self.dropdown_list_xpath)
        self.cameras_dropdown = Dropdown(browser, By.XPATH, self.cameras.get_locator() + self.dropdown_list_xpath)
        self.mp3_players_dropdown = Dropdown(browser, By.XPATH, self.mp3_players.get_locator() + self.dropdown_list_xpath)


    def show_all_desktops(self):
        self.actions.move_to_element(self.desktops)
        self.desktops_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_pcs(self):
        self.actions.move_to_element(self.desktops)
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(), 'PC')]")

    def show_mac_desktops(self):
        self.actions.move_to_element(self.desktops)
        self._option_text = self.driver.find_element_by_xpath("//a[contains(text(), 'Mac')]").text
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(), 'Mac')]")

    def show_all_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_mac_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[contains(text(), 'Macs')]")

    def show_windows_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[contains(text(), 'Windows')]")

    def show_all_components(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_mice(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Mice')]")

    def show_monitors(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Monitors')]")

    # added methods
    def show_printers(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Printers')]")

    def show_scanners(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Scanners')]")

    def show_webcams(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Web Cameras')]")

    def show_all_phones_and_pdas(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phone_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_pdas(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phone_dropdown.select_by_option_xpath("//a[contains(text(), 'PDAs')]")

    def show_phones(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phone_dropdown.select_by_option_xpath("//a[contains(text(), 'Phones')]")

    def move_to_desktops(self):
        self.actions.move_to_element(self.desktops)

    def move_to_laptops(self):
        self.actions.move_to_element(self.laptops)

    def move_to_phones_and_pdas(self):
        self.actions.move_to_element(self.phones_and_pdas)

    def move_to_components(self):
        self.actions.move_to_element(self.components)

    def select_mac_desktops(self):
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(), 'Mac')]")

    def select_pcs(self):
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(), 'PC')]")

    def select_phones(self):
        self.phone_dropdown.select_by_option_xpath("//a[contains(text(), 'Phones')]")

    def select_all_components(self):
        self.components_dropdown.select_by_option_xpath("//a[@class='see-all']")
