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

    def SelectByCss(self,  initialCssSelector, *extraCssSelectors, site=False, file=False):
        # print(f'Get Eles has run {self.__getElesRunCount} times')
        # self.__getElesRunCount+= 1
        if site:
            self.GetResponse(site)
            self.MakeSoup()
        elif file:
            self.MakeSoup(file)
        elif self.soup == None:
            raise RuntimeError(
                "Tried to use GetEles before soup was created")
        else:
            listOfElements = self.soup.select(initialCssSelector)
            for selector in extraCssSelectors:
                listOfElements += self.soup.select(selector)
            self.lastSearchedEles = listOfElements
            return listOfElements

    def MakeSoup(self, file=None):
        # print(text)
        if file:
            soupObject = bs4.BeautifulSoup(file, features='lxml')
        else:
            if not self.response:
                raise RuntimeError(
                    'There is no response to make soup of. Please use functions like GetResponse or SelectByCss first')
            else:
                soupObject = bs4.BeautifulSoup(
                    self.response.text, features='lxml')
        self.soup = soupObject
        return self.soup
