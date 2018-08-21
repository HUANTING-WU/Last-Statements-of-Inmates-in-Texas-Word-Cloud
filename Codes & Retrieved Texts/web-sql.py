'''
This program retrieve racial category and last statement of death row inmates.
Create a SQL databse named RLS with two tables.
The Race table has one column, which is the racial category.
The Ls table has one column, which is the last statement.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# connect database and create cursor
connect = sqlite3.connect('RLS.sqlite')
cursor = connect.cursor()
cursor.executescript('''
    DROP TABLE IF EXISTS Race;
    DROP TABLE IF EXISTS Ls;''')

cursor.executescript('''
    CREATE TABLE Race (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    race TEXT);
    CREATE TABLE Ls (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    ls TEXT)
    ''')

# input link, open link, parse html
url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all td tags
td_tags = soup.find_all('td')

# create race set
race_set = ['White', 'Hispanic', 'Black']

# loog through all td tags and retrieve the race td tag
race_list = list()
for tag in td_tags:
    # find the td tag contains race information
    # retrieve content of race
    if tag.get_text() in race_set:
        race_temp = tag.get_text()
        race_list.append((race_temp,))

# open all urls of last statements txt file
text = open('ls-url.txt','r')

# create ls list
ls_list = list()

# loop through each ls url
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
            # la_content to store ls in case it has more than one p tags.
            ls_content = ''
            # loop through all p tags of ls content
            for tag in ls_tags:
                ls_text = tag.get_text()
                ls_content = ls_content + ls_text
            ls_list.append((ls_content,))

# For some reason(s) unknown to me, which could be a bug in my code,
# or the imperfection of the website's html and/or beautifulsoup,
# this program and only split out 300 out of all 545 last statements.
n = 1
for race in race_list:
    if n <= 330:
        cursor.executemany('INSERT INTO Race (race) VALUES (?)',(race,))
        n = n + 1
    else:
        break

for ls in ls_list:
    cursor.executemany('INSERT INTO Ls (ls) VALUES (?)',(ls,))

connect.commit()
connect.close()
