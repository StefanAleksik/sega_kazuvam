# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 01:44:50 2018

@author: Stefan Aleksik
"""
from nlmk import tokenizer, stopwords #, corpus
#from nlmk import ngramgen as ngramgenmod
stopwords = stopwords()
f = open('all_topics.txt', 'r')
linii = (line.decode('utf-8') for line in f)
tokens = tokenizer.iter_tokenize(linii)
zborovi = list(token.lower() for token in tokens if token[0].isalpha())

for zbor in zborovi:
    if zbor not in stopwords and len(zbor) > 2:
        print zbor.encode('utf-8')