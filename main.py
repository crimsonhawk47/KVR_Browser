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
              'soothe': None, 'soundtheory': ['foss'], 'gullfoss': None, 'u-he': ['presswerk', 'satin'], 'psp': None}
pagestosearch = 5


firstPageEles = KVR_Browser.GetEles(site, homeCategoriesCss)
pagesOfSellTopics = []


# Getting the link for the first page of sell+buy
for firstPageElement in firstPageEles:
    if 'Sell & Buy' in firstPageElement.text:
        selltopicslink = site+firstPageElement.get('href')[2:]
        break

for i in range(0, pagestosearch):
    sellTopics = KVR_Browser.GetEles(
        selltopicslink+f'&start={str(30*i)}', topicsPart1Css, topicsPart2Css)
    # Getting a list of all HTML topic elements on that seller page, as some are of different elements
    pagesOfSellTopics.append(sellTopics)


def searchPagesTopics(currentPagesTopics):
    for topic in currentPagesTopics:  # for each topic on the page...
        for term in searchlist:  # and for each dictionary key compared to that topic...
            termFoundInBody = False
            if term in topic.text.lower():  # if the key is in the topic title
                # and if that key's value is none, which would happen if the topic title is all you care about...
                if searchlist[term] == None:
                    # open the post...
                    webbrowser.open(site + topic.get('href')[2:])
                    break  # and move onto the next topic on the page.
                else:  # otherwise, if you're curious what is inside that topic, and not just what's in the title...
                    # Get the link to that topic's page...
                    sellerpage = site + topic.get('href')[2:]
                    postbody = KVR_Browser.GetEles(
                        sellerpage, '.content')  # Get the posts HTML
                    # For every value in the key that got you interested (that's in the topic title)...
                    for product in searchlist[term]:
                        # if one of those values is in the body of the post
                        if product in postbody[0].text.lower():
                            webbrowser.open(sellerpage)  # Open that page..
                            termFoundInBody = True
                            # and move onto the next topic on the original page.
                            break
                    if termFoundInBody == True:
                        break


for time in range(pagestosearch):
    searchPagesTopics(pagesOfSellTopics[time])

# BHandle.close()

