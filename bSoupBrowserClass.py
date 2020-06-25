import requests, bs4
class BSoupBrowser:
    def __init__(self):
        self.lastSearchedEles = []
        self.__getElesRunCount = 0
    def __GetResponse(self, siteLink):
        response = requests.get(siteLink, headers={ #Fakes a user
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        response.raise_for_status()
        return response
        
    def GetEles(self, siteLink, initialCssSelector, *extraCssSelectors):
        print(f'Get Eles has run {self.count} times')
        self.getElesRunCount+= 1
        res = self.__GetResponse(siteLink)
        oSoup = bs4.BeautifulSoup(res.text, features = 'lxml')
        listOfElements = oSoup.select(initialCssSelector)
        for htmlPath in extraCssSelectors:
            listOfElements += oSoup.select(htmlPath)
        self.lastSearchedEles = listOfElements
        return listOfElements
