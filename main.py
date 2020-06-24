import RegisterChrome
import webbrowser
import os
from bSoupBrowserClass import BSoupBrowser

# custom section
site = 'https://www.kvraudio.com/forum/'

homeCategoriesCss, topicsPart1Css, topicsPart2Css = ['.list-inner > a',
                                                     'li.row.bg1 > dl > dt >.list-inner > .topictitle',
                                                     'li.row.bg2 > dl > dt >.list-inner > .topictitle']
searchlist = {'waves': ['brauer', 'scheps', 'motion'], 'dmg': ['track', 'limitless'], 'oeksound': None,
              'soothe': None, 'soundtheory': ['foss'], 'gullfoss': None, 'u-he': ['presswerk', 'satin'], 'psp': 'mixpack2', 'sly-fi': 'deflector'}
pagestosearch = 5

####
print('Creating BSoupBrowser object')
KVR_Browser = BSoupBrowser()
print("Getting html of KVR's Homepage")
homeCategoryForums = KVR_Browser.GetEles(site, homeCategoriesCss)
print("Searching homepages elements for a Sell & Buy topic")
# Getting the link for the first page of sell+buy=
sellRelativePath = next(firstPageElement.get('href') for firstPageElement in homeCategoryForums if 'Sell & Buy' in firstPageElement.text)
sellUrl = site+sellRelativePath[2:]

# sellTopicsLink = site+firstPageElement if 'Sell & Buy' in firstPageElement.text for firstPageElement in firstPageEles

print("Creating a list of all sell topics")
linksToSellerTopics = [KVR_Browser.GetEles(sellUrl+f'&start={str(30*page)}', topicsPart1Css, topicsPart2Css) for page in range(0, pagestosearch)]


def searchPagesTopics(currentPagesTopics):
    for topicElement in currentPagesTopics:  # for each topic on the page...
        topicTitle = topicElement.text.lower()
        topicLink = site + topicElement.get('href')[2:]
        for term in searchlist:  # and for each dictionary key compared to that topic...
            if term in topicTitle:  # if the key is in the topic title
                # and if that key's value is none, which would happen if the topic title is all you care about...
                if searchlist[term] == None:
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
    searchPagesTopics(linksToSellerTopics[time])

# BHandle.close()
