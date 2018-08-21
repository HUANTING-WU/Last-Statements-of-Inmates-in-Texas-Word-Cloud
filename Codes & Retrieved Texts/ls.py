'''
This program retrieve all the actual contents of each last statement,
and export them into a txt file
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# print a message at the beginning coz the program kinda takes long
print('The program is running...')

# open all urls of last statements txt file
text = open('ls-url.txt','r')

# create txt file for ls content
ls = open('ls.txt', 'w+')

# loop through each ls url and analyze each one
for line in text:
    # split ls url list and retrieve each url
    line = line.split()
    url = line[0]

    # open url, parse html
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # retrieve all p tags
    p_tags = soup.find_all('p')

    for tag in p_tags:
        # all p tags of ls content is next to title 'Last Statement'
        if tag.contents[0] == 'Last Statement:':
            # ls_tag is all p tags of ls content
            # retrieve all p tags of ls content
            ls_tags = tag.find_all_next('p')
            # loop through all p tags of ls content
            for tag in ls_tags:
                # retrieve content of each Last Statement
                ls_text = tag.get_text()
                # write to text file
                ls.write(ls_text)
            ls.write('\n' + '----' + '\n')

ls.close()
