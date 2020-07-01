import KVR_Browser.src.RegisterChrome
import os
import json
import webbrowser
from bSoupBrowserClass import BSoupBrowser

# Getting constants
with open('./config/constants.json') as jsonFile:
    config = json.load(jsonFile)
searchList = config['searchList']
pagesToSearch = config["pagesToSearch"]
kvr_url = "https://www.kvraudio.com/forum/"

KVR_Browser = BSoupBrowser()

def getSellerPages(forumElements, KVR_Browser):
    
    sellRelativePath = next(element.get('href')
                            for element in forumElements if 'Sell & Buy' in element.text)
    # Turning relative path into an actual url
    marketplaceUrl = kvr_url+sellRelativePath[2:]

    print(f"Downloading {pagesToSearch} pages worth of HTML from seller topics")
    pageUrls = [marketplaceUrl +
                f'&start={str(30*page)}' for page in range(pagesToSearch)]
    return [KVR_Browser.SelectByCss(
        ".topics .topictitle", site=x) for x in pageUrls]

def main():
    print("Getting html of KVR's Homepage")
    forumElements = KVR_Browser.SelectByCss(".list-inner > a", site=kvr_url)
    print("Searching homepages elements for a Sell & Buy topic")
    # Getting the link for the first page of sell+buy=
    
    pagesOfSellTopics = getSellerPages(forumElements, KVR_Browser)

    print("Now searching topic titles for your search terms")
    for pageIndex in range(pagesToSearch):
        searchPagesTopics(pagesOfSellTopics[pageIndex])

def searchPagesTopics(currentPagesTopics):
    for topicElement in currentPagesTopics:  # for each topic on the page...
        topicTitle = topicElement.text.lower()
        topicLink = kvr_url + topicElement.get('href')[2:]
        for term in searchList:  # and for each dictionary key compared to that topic...
            if term in topicTitle:  # if the key is in the topic title
                # and if that key's value is false, which would happen if the topic title is all you care about...
                if searchList[term] == False:
                    # open the post...
                    # webbrowser.open(topicLink)
                    print(f'opening {topicLink}')
                    break  # and move onto the next topic on the page.
                else:  # otherwise, if you're curious what is inside that topic, and not just what's in the title...
                    # Get the link to that topic's page...
                    contentElements = KVR_Browser.SelectByCss(
                        '.content', site=topicLink)  # Get the posts HTML
                    postBody = contentElements[0].text.lower()
                    # Check if any of the specific products are in the post body
                    if any(product in postBody for product in searchList[term]):
                        # webbrowser.open(topicLink)
                        print(f'opening {topicLink}')
                        break

if __name__ == "__main__":
    main()


