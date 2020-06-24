import RegisterChrome
import webbrowser
import os
from bSoupBrowserClass import BSoupBrowser

site = 'https://www.kvraudio.com/forum/'

homeCategoriesCss, topicsPart1Css, topicsPart2Css = ['.list-inner > a',
                                                     'li.row.bg1 > dl > dt >.list-inner > .topictitle',
                                                     'li.row.bg2 > dl > dt >.list-inner > .topictitle']

KVR_Browser = BSoupBrowser()


# custom section
searchlist = {'waves': ['brauer', 'scheps', 'motion'], 'dmg': ['track', 'limitless'], 'oeksound': None,
              'soothe': None, 'soundtheory': ['foss'], 'gullfoss': None, 'u-he': ['presswerk', 'satin'], 'psp': 'mixpack2', 'sly-fi': 'deflector'}
pagestosearch = 5

print("Getting html of KVR's Homepage")
firstPageEles = KVR_Browser.GetEles(site, homeCategoriesCss)
pagesOfSellTopics = []

print("Searching homepage for Sell & Buy topic")
# Getting the link for the first page of sell+buy=
for firstPageElement in firstPageEles:
    if 'Sell & Buy' in firstPageElement.text:
        selltopicslink = site+firstPageElement.get('href')[2:]
        break

print("Creating a list of all sell topics")
for i in range(0, pagestosearch):
    sellTopics = KVR_Browser.GetEles(
        selltopicslink+f'&start={str(30*i)}', topicsPart1Css, topicsPart2Css)
    # Getting a list of all HTML topic elements on that seller page, as some are of different elements
    pagesOfSellTopics.append(sellTopics)

print("Now searching topic titles for your search terms")


def searchPagesTopics(currentPagesTopics):
    for topicElement in currentPagesTopics:  # for each topic on the page...
        topicTitle = topicElement.text.lower()
        topicLink = site + topicElement.get('href')[2:]
        for term in searchlist:  # and for each dictionary key compared to that topic...
            if term in topicTitle:  # if the key is in the topic title
                # and if that key's value is none, which would happen if the topic title is all you care about...
                if searchlist[term] == None:
                    # open the post...
                    # webbrowser.open(site + topic.get('href')[2:])
                    print(f'opening {topicLink}')
                    break  # and move onto the next topic on the page.
                else:  # otherwise, if you're curious what is inside that topic, and not just what's in the title...
                    # Get the link to that topic's page...
                    contentElements = KVR_Browser.GetEles(topicLink, '.content')  # Get the posts HTML
                    postBody = contentElements[0].text.lower()
                    # Check if any of the specific products are in the post body
                    if any(product in postBody for product in searchlist[term]):
                        print(f'opening {topicLink}')
                        break


for time in range(pagestosearch):
    searchPagesTopics(pagesOfSellTopics[time])

# BHandle.close()
