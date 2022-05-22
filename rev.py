import pandas as pd
from itertools import chain
df = pd.read_csv('review.csv')
for s in ['[', ']', "'", ' ']:
    df['token'] = df['token'].str.replace(s,'', regex=True)
df['token'] = df['token'].str.split(',')
df = df[df['token'].apply(lambda x: '' not in x)]
df = df.reset_index(drop=True)
token_dic = list(set(chain(*df['token'].tolist())))
#%%time
score = []
for t in token_dic:
    score.append(df[df['token'].apply(lambda x: t in x)]['star'].mean())
df_token = pd.DataFrame()
df_token['token'] = token_dic
df_token['value'] = score
def sentiment(number):
    if number <= 2:
        return -1
    elif number >= 4:
        return 1
    else:
        return 0

df_token['sentiment'] = df_token['value'].apply(lambda x: sentiment(x))
df_token.to_csv('token_value.csv', sep=',', index=False)
def review_sentiment(review_t):
    result = 0
    if review_t==['']:
        return result
    for t in review_t:
        v = df_token[df_token['token'] == t]['sentiment'].values[0]
        print("%s : %s" % (t, v))
        result += v
    return result / len(review_t)
token = ["맛", "냄새", "기분"]
review_sentiment(token)
