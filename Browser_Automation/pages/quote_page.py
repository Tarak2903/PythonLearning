from bs4 import BeautifulSoup

from Browser_Automation.locators.quote_page_locators import QuotesPageLocators
from Browser_Automation.parsers.quotes import QuoteParser




class QuotesPage:
    def __init__(self, browser):
        self.browser=browser

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.browser.find_elements_by_css_selector(QuotesPageLocators.QUOTE)]