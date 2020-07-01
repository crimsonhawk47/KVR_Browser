from src.bSoupBrowserClass import BSoupBrowser
import pytest
browser = BSoupBrowser()
file = open('./tests/soup_browser/pythonWikipedia.html', encoding="utf-8")

@pytest.mark.static
def test_wikipedia_static_title():
    browser.MakeSoup(file = file)
    titleElement = browser.SelectByCss('#firstHeading')[0]
    title = titleElement.text
    assert "Python" in title

def test_using_makesoup_before_getting_response():
    browser = BSoupBrowser()
    with pytest.raises(RuntimeError):
        assert browser.MakeSoup()