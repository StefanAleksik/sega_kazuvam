#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pandas as pd
df = pd.read_csv('clean.csv', sep=";", encoding='utf-8-sig', error_bad_lines=False)

#print df['text']

txtfile = open('all_topics.txt', 'w')
znaci = ['!', '.', ',', '"', "'", '?', ':', ';', '/', 'www', 'html', 'the', 'https','twitter','com', 'pic']
#zborovi = [' им ',' им ',' им ',' ама ',' му ',' тоа ',' додека ','tanitregoj', ' ги ','биде',' сум ',' нешто ', 'pic', ' ти ', ' ја ', ' многу ', 'mk', 'twitter', ' колку ', ' има ', ' само ', ' сте ', ' па ', 'https', ' од ', ' не ', ' по ', ' да ', 'pic.twitter.com', ' си ', ' што ', ' ако ', ' кои ', ' ми ', ' се ', 'сегакажувам', ' треба ', ' ни ', ' го ', ' кога ', ' затоа ', ' без ', ' во ', ' в ', ' врз ',' до ', ' за ', ' зад ', ' заради ', ' кај ', ' каде ', ' како ', ' кон ', ' крај ', ' меѓу ', ' над ', ' ќе ', ' на ', ' пред ',' зад ',' дека ', ' и ',' со ',' кого ']

for row in df.iterrows():
	txt = row[1]['text'].lower().encode('utf-8-sig')
	for zn in znaci:
		txt = txt.replace(zn, ' ')
	# for z in zborovi:
	# 	txt = txt.replace(z, ' ')
		
	txtfile.write(txt + ' ')
	 
txtfile.close()