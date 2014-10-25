#Web scraping libraries
#import urllib.request
#I used urllib2 because I have Python 2.7 instead of Python 3 You can change it back if you want
import urllib2
from bs4 import BeautifulSoup

#Reddit library
import praw

#Other libraries
import time
import sys

#User agent
user_agent = 'R/EconomicHistory NBER Working Paper Bot v1.0'
r = praw.Reddit(user_agent=user_agent)

#Login to Reddit
uname = 'EH_NBER_Bot'
pw = ''
r.login(uname, pw)

#Variables
queue=[]

#All current links are considered as posted already
#Iterate through NBER Econ History N0-N7 pages to grab all paper links
for j in range(8):
    print 'N%d'%j
    url = urllib2.urlopen('http://www.nber.org/jel/N%d.html' % j)
    content = url.read()
    #Grab all links
    soup = BeautifulSoup(content)
    existing_links = soup.select('#mainContentTd tr a')
    #Put all old links into the posted_links list
    posted_links = [a['href'] for a in existing_links if 'nber.org/papers' in str(a)]

#Initialize loop
while True:
    #Iterate through NBER Econ History N0-N7 pages to grab all paper links
    for j in range(8):
        print 'N%d'%j
        url = urllib2.urlopen('http://www.nber.org/jel/N%d.html' % j)
        content = url.read()
        #Grab all links
        soup = BeautifulSoup(content)
        #Select all html table rows
        links_new = soup.select('#mainContentTd tr')
        #Add all the rows to the queue
        queue = [tr for tr in links_new if 'nber.org/papers' in str(a)]
    #Iterate through the paper links
    for paper in queue:
        #If a given paper link in the queue is new
        if row.a['href'] not in posted_links:
            #Get new post
            current_post = dict()
            current_post['html'] = str(b)
            #Format title
            paper_authors_tag = row.nobr
            current_post['authors'] = paper_authors_tag.text.replace('  ',', ')
            paper_title_tag = row.findAll('td')[2]
            current_post['title'] = paper_title_tag.text
            #Set title of post as title of paper plus author names
            current_post['post_title'] = u'NBER: {title} -- by {authors}'.format(**current_post)
            current_post['link'] = row.a['href']
            #out_writer.writerow(current_post)
            #Submit link to /r/EconomicHistory with the set title
            print('Posting', )
            print current_post['post_title']
            r.submit('economichistory', current_post['post_title'], url = current_post['link'])
            print('Done posting.')
            posted_links.append(row.a['href'])
            #Only posts one paper per cycle
            break
    #Run every 4 hours
    time.sleep(4*60*60)
