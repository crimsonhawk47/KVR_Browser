import RegisterChrome
import os
import json
import webbrowser
from bSoupBrowserClass import BSoupBrowser

# custom section
site = 'https://www.kvraudio.com/forum/'

searchlist = json.load(open('./config/constants.json'))['searchList']

pagestosearch = 5

####
KVR_Browser = BSoupBrowser()
print("Getting html of KVR's Homepage")
forumElements = KVR_Browser.GetEles(site, ".list-inner > a")
print("Searching homepages elements for a Sell & Buy topic")
# Getting the link for the first page of sell+buy=
sellRelativePath = next(element.get('href')
                        for element in forumElements if 'Sell & Buy' in element.text)
# Turning relative path into an actual url
marketplaceUrl = site+sellRelativePath[2:]

print("Creating a list of all paginated links for the sell&buy section of the site")
pageUrls = [marketplaceUrl +
            f'&start={str(30*page)}' for page in range(pagestosearch)]
pagesOfSellTopics = [KVR_Browser.GetEles(
    x, ".topics .topictitle") for x in pageUrls]


def searchPagesTopics(currentPagesTopics):
    for topicElement in currentPagesTopics:  # for each topic on the page...
        topicTitle = topicElement.text.lower()
        topicLink = site + topicElement.get('href')[2:]
        for term in searchlist:  # and for each dictionary key compared to that topic...
            if term in topicTitle:  # if the key is in the topic title
                # and if that key's value is false, which would happen if the topic title is all you care about...
                if searchlist[term] == False:
                    # open the post...
                    # webbrowser.open(topicLink)
                    print(f'opening {topicLink}')
                    break  # and move onto the next topic on the page.
                else:  # otherwise, if you're curious what is inside that topic, and not just what's in the title...
                    # Get the link to that topic's page...
                    contentElements = KVR_Browser.GetEles(
                        topicLink, '.content')  # Get the posts HTML
                    postBody = contentElements[0].text.lower()
                    # Check if any of the specific products are in the post body
                    if any(product in postBody for product in searchlist[term]):
                        # webbrowser.open(topicLink)
                        print(f'opening {topicLink}')
                        break


print("Now searching topic titles for your search terms")
for time in range(pagestosearch):
    searchPagesTopics(pagesOfSellTopics[time])
