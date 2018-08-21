'''
This program retrieve all the urls of all last Statement,
and export them into a txt file
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input link, open link, parse html
url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all a tags
a_tags = soup.find_all('a')

# ls = Last Statement
ls_url = list()

# loop through all a tags and filter ls tags from all a tags
for tag in a_tags:
    # all ls tags have a content of 'Last Statement'
    if tag.contents[0] == 'Last Statement':
        # retrieve the link from ls tags
        ls_link = tag.get('href')
        # real world is not perfect. have to tinker with each returned href
        # #Government html #Texas
        # add each last statement into a list
        if not ls_link.startswith('/death_row/'):
            ls_link = 'http://www.tdcj.state.tx.us/death_row/' + ls_link
            ls_url.append(ls_link)
        else:
            ls_link = 'http://www.tdcj.state.tx.us' + ls_link
            ls_url.append(ls_link)

# create txt file for ls url
ls_url_txt = open('ls-url.txt', 'w+')
# loop and write each ls url into txt file
for url in ls_url:
    ls_url_txt.write(url + '\n')
# close txt file
ls_url_txt.close()

'''










'''
