from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from appium import webdriver
import time
import os

def get_wikipedia_app_caps():
    apk_full_path = f'{BuiltIn().get_variable_value("${EXECDIR}")}{os.sep}apk_files{os.sep}org.wikipedia_2.7.50324-r-2020-06-29-50324_minAPI21(nodpi)_apkmirror.com.apk'
    capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            appPackage='org.wikipedia',
            appActivity='org.wikipedia.main.MainActivity',
            newCommandTimeout=500,
            dontStopAppOnReset=True,
            uiautomator2ServerInstallTimeout=50000,
            app=apk_full_path,
    )
    capabilities['deviceName'] = BuiltIn().get_variable_value("${DEVICE_NAME}")
    capabilities['platformVersion'] = BuiltIn().get_variable_value("${PLATFORM_VERSION}")
    return capabilities

class WikipediaAppiumLibrary:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.appium_server = BuiltIn().get_variable_value("${APPIUM_SERVER}")
        self.capabilities = get_wikipedia_app_caps()
        self.wait_period = int(BuiltIn().get_variable_value("${IMPLICIT_WAIT_PERIOD}"))
        self.locators = BuiltIn().get_variable_value("${LOCATORS}")

    def launch_mobile_app(self):
        logger.info(f'Wikipedia Android app Appium needed capabilities: {self.capabilities}')
        self.driver = webdriver.Remote(self.appium_server, self.capabilities)
        self.driver.implicitly_wait(self.wait_period)
        self.driver.launch_app()

    def go_to_home_page(self):
        try:
            self.driver.find_element_by_xpath(self.locators['cancelButton']).click()
        except Exception:
            pass

        try:
            self.driver.find_element_by_id(self.locators['skipButton']).click()
        except Exception:
            pass

    def login(self, username, password):
        """This keyword assumes that we are at Wikipedia's main page.
           Once logged in, the app goes back to home page
        """
        self.driver.find_element_by_xpath(self.locators['moreOption']).click()
        self.driver.find_element_by_xpath(self.locators['loginMenuOption']).click()
        self.driver.find_element_by_id(self.locators['createAnAccountLoginOption']).click()
        time.sleep(self.wait_period)
        # set username
        username_field = self.driver.find_element_by_xpath(self.locators['usernameField'])
        username_field.set_text(username)
        # set password
        password_field = self.driver.find_element_by_xpath(self.locators['passwordField'])
        password_field.set_text(password)
        self.driver.find_element_by_id(self.locators['loginButton']).click()

    def logout(self):
        """This keyword assumes that we are at Wikipedia's main page.
           Once logged out, the app goes back to home page
        """
        self.driver.find_element_by_xpath(self.locators['moreOption']).click()
        self.driver.find_element_by_xpath(self.locators['logoutOption']).click()
        self.driver.find_element_by_xpath(self.locators['logoutOption']).click()

    def search(self, search_term):
        """This keyword assumes that we are at Wikipedia's main page.
           This keyword selects the first search term that pop-ups with the given search_term
        """
        try:
            self.driver.find_element_by_xpath(self.locators['searchElementNonEditable']).click()
        except Exception:
            pass

        # type in search_term
        search_element = self.driver.find_element_by_id(self.locators['searchElementEditable'])
        search_element.set_text(search_term)
        time.sleep(self.wait_period)
        # look for the first search result containing the search_term
        search_result_item_locator = self.locators['genericSearchResultItem'] % search_term
        logger.info(f'search_result_item_locator: {search_result_item_locator}')
        self.driver.find_element_by_xpath(search_result_item_locator).click()

    def clear_search(self):
        self.driver.find_element_by_id(self.locators['searchElementEditable']).set_text('')

    def _get_rid_of_got_it(self):
        try:
            self.driver.find_element_by_xpath(self.locators['gotItButton']).click()
        except Exception:
            pass

    def bookmark_article(self, list_name):
        "This keyword assumes that an article's page is open"
        self.driver.find_element_by_id(self.locators['bookmarkArticleOption']).click()
        self._get_rid_of_got_it()
        self.driver.find_element_by_xpath(self.locators['createNewBookmark']).click()
        self.driver.find_element_by_id(self.locators['nameOfBookmarkList']).set_text(list_name)
        self.driver.find_element_by_xpath(self.locators['okButton']).click()

    def press_back_button(self):
        try:
            self.driver.find_element_by_xpath(self.locators["backButtonOne"]).click()
        except Exception:
            pass

        try:
            self.driver.find_element_by_xpath(self.locators["backButtonTwo"]).click()
        except Exception:
            pass

    def select_my_lists_tab(self):
        """ This keyword assumes that we are at Wikipedia's main page. """
        self.driver.find_element_by_xpath(self.locators["myListsTab"]).click()

    def remove_list(self, partial_list_name):
        """ This keyword assumes that we are at Wikipedia's My lists page. """
        listLocator = self.locators['genericListItem'] % partial_list_name
        self.driver.find_element_by_xpath(listLocator).click()
        self.driver.find_element_by_id(self.locators["listMenu"]).click()
        self.driver.find_element_by_xpath(self.locators["deleteListOption"]).click()
        self.driver.find_element_by_xpath(self.locators['okButton']).click()

    def select_explore_tab(self):
        """ Assumes the tab menu is shown """
        self.driver.find_element_by_xpath(self.locators['exploreTab']).click()
