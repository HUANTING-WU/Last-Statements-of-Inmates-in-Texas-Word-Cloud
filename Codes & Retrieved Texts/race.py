'''
This program retrieve all racial information of each death row inmate,
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

# input link, open link, parse html
url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# td tags are content tags all information,
# including last statement and race of an inmate

# create txt file to store each race information
race_txt = open('race.txt', 'w+')

# retrieve all td tags
td_tags = soup.find_all('td')

# create race set
race_set = ['White', 'Hispanic', 'Black']

# loog through all td tags and retrieve the race td tag
for tag in td_tags:
    # find the td tag contains race information
    # retrieve content of race
    if tag.contents[0] in race_set:
        # write to text file
        race_txt.write(tag.contents[0] + '\n')

race_txt.close()
