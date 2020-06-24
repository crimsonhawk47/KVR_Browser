import requests, bs4
class BSoupBrowser:
    def __init__(self):
        self.lastSearchedEles = []
        self.count = 0
    def GetEles(self, sitelink, initialHtmlPath, *extraHtmlPaths):
        print(f'Get Eles has run {self.count} times')
        self.count+= 1
        res = requests.get(sitelink, headers={ #Fakes a user
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        res.raise_for_status()
        oSoup = bs4.BeautifulSoup(res.text, features = 'lxml')
        listOfElements = oSoup.select(initialHtmlPath)
        for htmlPath in extraHtmlPaths:
            listOfElements += oSoup.select(htmlPath)
        self.lastSearchedEles = listOfElements
        return listOfElements
