import RegisterChrome
import os
from bSoupBrowserClass import BSoupBrowser

site = 'https://www.kvraudio.com/forum/'

firstPageHTMLPattern, secondPageHTMLPattern, thirdPageHTMLPattern = ['.list-inner > a', 
'li.row.bg1 > dl > dt >.list-inner > .topictitle', 
'li.row.bg2 > dl > dt >.list-inner > .topictitle']

KVR_Browser = BSoupBrowser()


#custom section
searchlist =  {'waves': ['brauer', 'scheps', 'motion'], 'dmg':['track', 'limitless'], 'oeksound':None, 'soothe': None, 'soundtheory':['foss'], 'gullfoss':None, 'u-he':['presswerk', 'satin'], 'psp':None}
pagestosearch = 5


firstPageEles = KVR_Browser.GetEles(site, firstPageHTMLPattern)
BHandle = RegisterChrome.Get('gg')
selltopics = []


#Getting the link for the first page of sell+buy
for firstPageElement in firstPageEles:
    if 'Sell & Buy' in firstPageElement.text:
        selltopicslinks = site+firstPageElement.get('href')[2:]
        break

for i in range(0, pagestosearch):
    topicspart1 = KVR_Browser.GetEles(selltopicslinks+f'&start={str(30*i)}', secondPageHTMLPattern, thirdPageHTMLPattern)
    selltopics.append(topicspart1) #Getting a list of all HTML topic elements on that seller page, as some are of different elements

def searchKVR(topics):
    for topic in topics: #for each topic on the page...
        for term in searchlist: #and for each dictionary key compared to that topic...
            termFoundInBody = False
            if term in topic.text.lower(): #if the key is in the topic title
                if searchlist[term] == None:#and if that key's value is none, which would happen if the topic title is all you care about...
                    BHandle.open(site + topic.get('href')[2:])#open the post...
                    break #and move onto the next topic on the page. 
                else:                       #otherwise, if you're curious what is inside that topic, and not just what's in the title...
                    sellerpage = site + topic.get('href')[2:] #Get the link to that topic's page...
                    postbody = KVR_Browser.GetEles(sellerpage, '.content') #Get the posts HTML
                    for product in searchlist[term]: #For every value in the key that got you interested (that's in the topic title)...
                        if product in postbody[0].text.lower(): #if one of those values is in the body of the post
                            BHandle.open(sellerpage) #Open that page..
                            termFoundInBody = True
                            break #and move onto the next topic on the original page. 
                    if termFoundInBody == True:
                        break

for time in range(pagestosearch):
    searchKVR(selltopics[time])

#BHandle.close()






