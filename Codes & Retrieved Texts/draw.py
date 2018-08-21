from wordcloud import WordCloud
from PIL import Image
import numpy as np

# read the text.
text = open('ls.txt').read()

# read mask image
# map = np.array(Image.open('map.png'))

# generate a word cloud image
wordcloud = WordCloud(background_color = 'Snow', width = 1000, height = 500,
    prefer_horizontal = 1).generate(text)

# export to an image file
wordcloud.to_file('draw.png')

# display the generated image in matplotlib
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('My Word Cloud')
plt.axis('off')
plt.show()
