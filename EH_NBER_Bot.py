#Web scraping libraries
import urllib.request
from bs4 import BeautifulSoup

#Reddit library
import praw

#Other libraries
import time
import sys

#User agent
##user_agent =
#r = praw.Reddit(user_agent=user_agent)
#
#Login to Reddit
#uname = "EH_NBER_Bot"
#pw = "ehiscool"
#r.login(uname, pw)



#Variables
queue=[]
n0_links=[]

#Initialize loop
while True:
    #Open the NBER Econ History N0 (General) page
    url = urllib.request.urlopen('http://www.nber.org/jel/N0.html')
    content = url.read()
    #Grab all links
    soup = BeautifulSoup(content)
    links_new=soup.find_all('a')
    
    #Iterate through the links
    for a in links_new:
        #If a given link links to a paper
        if 'nber.org/papers' in str(a):
            #Put it in a queue
            queue.append(a)
    #Iterate through the paper links
    for b in queue:
        #And iterate through the links already posted
        for c in n0_links[]
            #If a given paper link in the queue is new
            if b != c:
                try:
                    #Get new post
                    curr_post = n0.links.pop()
                    print('Posting ', curr_post[str(b)])
                    link = curr_post[b]
                    #Set title of post as title of paper
                    title = "[NBER]" + str(b)
                    #Submit link to /r/EconomicHistory with the set title
                    r.submit('economichistory', title, url = link)
                    print('Done posting.')
                except Exception as e:
                    print e
                    print('No new posts.')
                #Add it to the list of new paper links already posted 
                n0_links.append(b)
    #Run every 4 hours
    time.sleep(4*60*60)    
