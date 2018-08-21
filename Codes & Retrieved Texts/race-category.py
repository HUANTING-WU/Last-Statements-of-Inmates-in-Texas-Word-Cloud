'''
This program reads RLS database,
retrieve all last statement from three racial categories,
and draw a word cloud for each race.
'''
import sqlite3
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

connect = sqlite3.connect('RLS.sqlite')
cursor = connect.cursor()

# White
white = open('white.txt','w+')

white_text = cursor.execute('SELECT * FROM White')

for i in white_text:
    white.write(i[0])

white.close()
white = open('white.txt').read()

wordcloud = WordCloud(background_color = 'Snow', width = 1000, height = 500,
    prefer_horizontal = 1).generate(white)

wordcloud.to_file('draw-white.png')

plt.imshow(wordcloud, interpolation='bilinear')
plt.title('White Last Words')
plt.axis('off')
plt.show()

# Black
black = open('black.txt','w+')

black_text = cursor.execute('SELECT * FROM Black')

for i in black_text:
    black.write(i[0])

black.close()
black = open('black.txt').read()

wordcloud = WordCloud(background_color = 'Snow', width = 1000, height = 500,
    prefer_horizontal = 1).generate(black)

wordcloud.to_file('draw-black.png')

plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Black Last Words')
plt.axis('off')
plt.show()

# Hispanic
hispanic = open('hispanic.txt','w+')

hispanic_text = cursor.execute('SELECT * FROM Hispanic')

for i in hispanic_text:
    hispanic.write(i[0])

hispanic.close()
hispanic = open('hispanic.txt').read()

wordcloud = WordCloud(background_color = 'Snow', width = 1000, height = 500,
    prefer_horizontal = 1).generate(hispanic)

wordcloud.to_file('draw-hispanic.png')

plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Hispanic Last Words')
plt.axis('off')
plt.show()
