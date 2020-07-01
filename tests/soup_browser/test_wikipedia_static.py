from src.bSoupBrowserClass import BSoupBrowser
from bs4 import BeautifulSoup
import pytest

@pytest.fixture
def browser():
    with open('./tests/soup_browser/pythonWikipedia.html', encoding="utf-8") as file:
            browser = BSoupBrowser()
            browser.MakeSoup(file=file)
    return browser


@pytest.mark.static
def test_wikipedia_static_title(browser):
        assert isinstance(browser.soup, BeautifulSoup)
        titleElement = browser.SelectByCss('#firstHeading')[0]
        title = titleElement.text
        assert "Python" in title
