from bSoupBrowserClass import BSoupBrowser
browser = BSoupBrowser()
site = "https://en.wikipedia.org/wiki/Python_(programming_language)"
browser.GetResponse(site)
browser.MakeSoup()

def test_wikipedia_static_title():
    file = open('./tests/soup_browser/pythonWikipedia.html')
    browser.MakeSoup(file)
    titleElement = browser.SelectByCss('#firstHeading')[0]
    title = titleElement.text
    assert "Python" in title