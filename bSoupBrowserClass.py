import requests, bs4
class BSoupBrowser:
    def __init__(self):
        self.searchedeles = []
    def GetEles(self, sitelink, *htmlPaths):
        res = requests.get(sitelink, headers={ #Fakes a user
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        res.raise_for_status()
        oSoup = bs4.BeautifulSoup(res.text, features = 'lxml')
        listOfElements = []
        for htmlPath in htmlPaths:
            listOfElements += oSoup.select(htmlPath)
        return listOfElements

    def SearchEles(self, sitelink, htmlpath, searchterm, anchor = False):
        eles = self.GetEles(sitelink, htmlpath)
        searchedeles = []
        searchedelesD = {}
        if isinstance(searchterm, list):
            for i in eles:
                for q in searchterm:
                    if q in i.text.lower():
                        if i.get('href'):
                            link = i.get('href')
                            if link[0] == '.':
                                link = sitelink+link[2:]
                            searchedelesD[i.text] = link
                        else:
                            #print('match:',i.text)
                            searchedeles.append(i.text)
                    break
            if i.get('href'):
                return searchedelesD
            else:
                return searchedeles
        elif isinstance(searchterm, str):
            for i in eles:
                if searchterm in i.text.lower():
                    if i.get('href'):
                        link = i.get('href')
                        if link[0] == '.':
                            link = sitelink+link[2:]
                        searchedelesD[i.text] = link
                    else:
                        #print('match:',i.text)
                        searchedeles.append(i.text)
            if i.get('href'):
                return searchedelesD
            else:
                return searchedeles
        else:
            print('type of term is', type(searchterm))
            return 0
