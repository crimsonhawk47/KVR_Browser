from bSoupBrowserClass import BSoupBrowser
from bs4 import BeautifulSoup
import pytest


@pytest.fixture
def browser():
    return BSoupBrowser()


def test_selectbycss_with_no_file_or_response(browser):
    with pytest.raises(RuntimeError):
        cssPath = ".topics .topictitle"
        assert browser.SelectByCss(cssPath)


def test_selectbycss_with_file(browser):
    listOfElements = None
    with open('./tests/soup_browser/pythonWikipedia.html', encoding="utf-8") as file:
        listOfElements = browser.SelectByCss('#firstHeading', file=file)
    assert isinstance(browser.soup, BeautifulSoup)
    title = listOfElements[0].text
    assert 'Python' in title
    assert listOfElements == browser.lastSearchedEles
