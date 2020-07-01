from src.bSoupBrowserClass import BSoupBrowser
import pytest
browser = BSoupBrowser()
site = "https://en.wikipedia.org/wiki/Python_(programming_language)"
browser.GetResponse(site)
browser.MakeSoup()

@pytest.mark.static
def test_wikipedia_static_title():
    file = open('./tests/soup_browser/pythonWikipedia.html', encoding="utf-8")
    browser.MakeSoup(file)
    titleElement = browser.SelectByCss('#firstHeading')[0]
    title = titleElement.text
    assert "Python" in title