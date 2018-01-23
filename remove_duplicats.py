import pandas as pd
df = pd.read_csv('merge.csv', sep=";", encoding='utf-8-sig', error_bad_lines=False)
#dff = df
df.drop_duplicates(subset='text', keep='first', inplace=True)
df.to_csv('clean.csv', sep=";", encoding='utf-8-sig')

#dff.drop_duplicates()

#dff['retweets'] = pd.to_numeric(dff['retweets'], errors='coerce')
#dff['favorites'] = pd.to_numeric(dff['favorites'], errors='coerce')

#sorted_tweets = dff.sort_values(by=['retweets', 'favorites'], ascending=False)
#sorted_tweets.to_csv('clean_sorted.csv', sep=";", encoding='utf-8-sig')