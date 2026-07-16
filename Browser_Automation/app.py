import requests

from pages.quote_page import QuotesPage

from selenium import webdriver

chrome=webdriver.Chrome()

chrome.get("https://quotes.toscrape.com")

page=QuotesPage(chrome)


for quote in page.quotes:
    print(quote)