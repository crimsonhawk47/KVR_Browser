from bSoupBrowserClass import BSoupBrowser
browser = BSoupBrowser()
site = "https://en.wikipedia.org/wiki/Python_(programming_language)"
browser.GetResponse(site)
browser.MakeSoup()


def test_wikipedia_title():
    titleElement = browser.SelectByCss("#firstHeading")[0]
    title = titleElement.text
    assert "Python" in title

def test_python_website_is_listed():
    infoboxElement = browser.SelectByCss('.infobox a')
    pythonWebsite = next(url.text for url in infoboxElement if "python.org" in url.text)
    assert pythonWebsite == "www.python.org"

