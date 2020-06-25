import requests
import bs4


class BSoupBrowser:
    def __init__(self):
        self.lastSearchedEles = []
        self.response = None
        self.soup = None
        # self.__getElesRunCount = 0

    def GetResponse(self, site):
        response = requests.get(site, headers={  # Fakes a user
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        response.raise_for_status()
        self.response = response
        return self.response

    def GetEles(self,  initialCssSelector, *extraCssSelectors, site=False):
        # print(f'Get Eles has run {self.__getElesRunCount} times')
        # self.__getElesRunCount+= 1
        if site:
            res = self.GetResponse(site)
            self.MakeSoup(res.text)
        elif self.soup == None:
            raise RuntimeError(
                "Tried to use GetEles before any response was gotten")
        listOfElements = self.soup.select(initialCssSelector)
        for selector in extraCssSelectors:
            listOfElements += self.soup.select(selector)
        self.lastSearchedEles = listOfElements
        return listOfElements

    def MakeSoup(self, *text):
        # print(text)
        if text:
            soupObject = bs4.BeautifulSoup(text[0], features='lxml')
            self.soup = soupObject
        else:
            soupObject = bs4.BeautifulSoup(self.response.text, features='lxml')
            self.soup = soupObject
        return self.soup
