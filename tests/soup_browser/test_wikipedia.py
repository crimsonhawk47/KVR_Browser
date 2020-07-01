from src.bSoupBrowserClass import BSoupBrowser
import pytest


@pytest.fixture(scope='module')
def browser():
    browser = BSoupBrowser()
    site = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    browser.GetResponse(site)
    browser.MakeSoup()
    print('--------------setup----------------')
    return browser


@pytest.mark.rest
def test_wikipedia_title(browser):
    titleElement = browser.SelectByCss("#firstHeading")[0]
    title = titleElement.text
    assert "Python" in title


@pytest.mark.rest
def test_python_website_is_listed(browser):
    infoboxElement = browser.SelectByCss('.infobox a')
    pythonWebsite = next(
        url.text for url in infoboxElement if "python.org" in url.text)
    assert pythonWebsite == "www.python.org"
