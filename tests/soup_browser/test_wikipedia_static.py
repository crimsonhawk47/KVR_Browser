from src.bSoupBrowserClass import BSoupBrowser
from bs4 import BeautifulSoup
import pytest


@pytest.mark.static
def test_wikipedia_static_title():
    with open('./tests/soup_browser/pythonWikipedia.html', encoding="utf-8") as file:
        browser = BSoupBrowser()
        browser.MakeSoup(file=file)
        assert isinstance(browser.soup, BeautifulSoup)
        titleElement = browser.SelectByCss('#firstHeading')[0]
        title = titleElement.text
        assert "Python" in title
