import requests, bs4
class BSoupBrowser:
    def __init__(self):
        self.lastSearchedEles = []
        self.response = None
        # self.__getElesRunCount = 0
    def GetResponse(self, site):
        response = requests.get(site, headers={ #Fakes a user
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        response.raise_for_status()
        self.response = response
        return response

    def GetEles(self,  initialCssSelector, *extraCssSelectors, site=False):
        # print(f'Get Eles has run {self.__getElesRunCount} times')
        # self.__getElesRunCount+= 1
        res = None
        if site:
            res = self.GetResponse(site)
        else:
            res = self.response
        oSoup = bs4.BeautifulSoup(res.text, features = 'lxml')
        listOfElements = oSoup.select(initialCssSelector)
        for htmlPath in extraCssSelectors:
            listOfElements += oSoup.select(htmlPath)
        self.lastSearchedEles = listOfElements
        return listOfElements
