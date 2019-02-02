import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from bs4 import BeautifulSoup
import re
print("----------- Importing data -------------------")
cols = ['sentiment','id','date','query_string','user','text']
df = pd.read_csv("training.1600000.processed.noemoticon.csv",header=None, names=cols)
df.drop(['id','date','query_string','user'],axis=1,inplace=True)  
df['pre_clean_len'] = [len(t) for t in df.text]
data_dict = {
    'sentiment':{
        'type':df.sentiment.dtype,
        'description':'sentiment class - 0:negative, 1:positive'
    },
    'text':{
        'type':df.text.dtype,
        'description':'tweet text'
    },
    'pre_clean_len':{
        'type':df.pre_clean_len.dtype,
        'description':'Length of the tweet before cleaning'
    },
    'dataset_shape':df.shape
}
print("----------- start data -------------------")
print("-------------------------------------------")
print(df.text[0])
print("-------------------------------------------")
t = re.sub(r'@[A-Za-z0-9]+','',df.text[0])
t =re.sub('https?://[A-Za-z0-9./]+','',t)
t = re.sub("[^a-zA-Z]", " ", t)
print(t)
print("-------------------------------------------")
print("-------------------------------------------")

print("-------------------------------------------")
print(df.text[226])
print("-------------------------------------------")

testing = df.text[226].decode("utf-8").replace(u"\ufffd", "?")
print(testing)
print("-------------------------------------------")

#print('---')
#print(df.sentiment.value_counts())
#print('---')
#Keeping only the tweet and its polarity 
#Printing first 10 negative polarities 
#print("First 10 negative polarities ---------------------------")
#print(df[df.sentiment == 0].head(10))
#print('---')
#Printing first 10 positive polarities
#print("First 10 positive polarities ---------------------------")
#print(df[df.sentiment == 4].head(10))
#print('---')
#print(df[df.sentiment == 2].head(10))
#print('----')
#looking at the tweets lenght
#print("looking at the tweets lenght ---------------------------")
#print(df.head(10))
#print("Data dictionary for the dataset ---------------------------")
#pprint(data_dict)
#print("plot pre_clean_len with box plot ----------------------------")
#fig, ax = plt.subplots(figsize=(5, 5))
#plt.boxplot(df.pre_clean_len)
#plt.show()
#print(df.text[279])
#Data Cleaning 
#exp = BeautifulSoup(df.text[279], 'lxml')
#print(exp.getText())
#print("----------------------------")
#  Data Preparation 2: ‘@’mention
'''print(df.text[343])
print("------------- Aplying regex ---------------")
exp = re.sub(r'@[A-Za-z0-9]+','',df.text[343])
print(exp)
print("-------------- Adding BS4------------------")
exp_regexed = BeautifulSoup(exp, 'lxml')
print(exp_regexed.getText())
'''

