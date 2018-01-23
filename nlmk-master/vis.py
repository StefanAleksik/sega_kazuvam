#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'test.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "black.png")))

stopwords = set(STOPWORDS)
stopwords.add('на')

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)

# generate word cloud
wc.generate(text.decode('utf-8'))

# store to file
wc.to_file(path.join(d, "all_topics.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()