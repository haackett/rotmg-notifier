import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
import requests
from models import rotmg_server
import os
from util import openconfig

class Scraper():
   
    def __init__(self):
        self.URL = 'https://realmstock.com/pages/event-notifier'
        self.chrome_options = self.__set_chrome_options()
        self.driver = self.__setup_driver()
        self.driver.implicitly_wait(5) #seconds
        self.driver.get(self.URL)
        self.__set_site_options()

    def __setup_driver(self):
        try:
            driver = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver", options=self.chrome_options)
            return driver
        except TypeError:
            raise TypeError("Env variable CHROMEDRIVER is not defined")

    def __set_site_options(self) -> None:
        """Configures options on the site's input elements according to the config.json"""
        config_dict = openconfig.open_config()
        for key in openconfig.DEFAULT_TRUE_KEYS:
            if not config_dict[key]:
                self.driver.find_element_by_id(key).click()
        for key in openconfig.DEFAULT_FALSE_KEYS:
            if config_dict[key]:
                self.driver.find_element_by_id(key).click()
    
    def __set_chrome_options(self) -> Options:
        """Sets chrome options for Selenium. Chrome options for headless browser is enabled.
           Images are disabled as they are not used in this app."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options
        
    def __get_content(self, content_div) -> rotmg_server:
        event_title = content_div.find_element_by_css_selector(
            '.event-title').text
        event_server = content_div.find_element_by_css_selector(
            '.event-server').text
        realm = content_div.find_element_by_css_selector('.event-realm').text
        realm_population = self.__parse_population(
            content_div.find_element_by_css_selector('.event-population').text)
        remaining = content_div.find_element_by_css_selector(
            '.event-events-wrapper').find_element_by_css_selector('.event-events').text
        last_updates = content_div.find_element_by_css_selector(
            '.event-time').text
        server = rotmg_server.Server(
            event_server, realm, event_title, realm_population, remaining, last_updates)
        print(server)
        return server

    def __parse_population(self, fraction: str):
        "Helper method for __get_content. Returns the numerator of a fractions i.e. 48/85 becomes 48."
        return fraction.split('/')[0]

    def get_servers(self):
        print('Scraping server data ...')
        
        parent_div = self.driver.find_element_by_id('history')
        event_divs = parent_div.find_elements_by_css_selector(
            '.realmstock-panel.event')
        servers = []
        for event_div in event_divs:
            try:
                content_div = event_div.find_element_by_css_selector(
                    '.event-content')
                servers.append(self.__get_content(content_div))
            except exceptions.StaleElementReferenceException as e:
                print(e)
                pass
        print('Returning servers ...')
        return servers

    def close(self):
        self.driver.close()
