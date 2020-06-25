from bSoupBrowserClass import BSoupBrowser
browser = BSoupBrowser()
site = "https://en.wikipedia.org/wiki/Python_(programming_language)"
browser.GetResponse(site)

def test_wikipedia_title():
    titleElement = browser.GetEles("#firstHeading")[0]
    title = titleElement.text
    assert "Python" in title

def test_python_website_is_listed():
    infoboxElement = browser.GetEles('.infobox a')
    pythonWebsite = next(url.text for url in infoboxElement if "python.org" in url.text)
    assert pythonWebsite == "www.python.org"