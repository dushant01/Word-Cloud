# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:38:38 2020

@author: jethi
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from os import path

times_data= pd.read_csv('timesData.csv')
X2011=times_data.country[times_data.year==2011]
plt.subplots(figsize=(8,8))
wordcloud= WordCloud(
    background_color='white',
    width=1200,
    height=800
     ).generate(" ".join(X2011))

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png')
plt.show()
