# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:38:04 2020

@author: jethi
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from os import path

""" data Set """

data= pd.read_csv("HRDataset_v13.csv")

RC= data.RecruitmentSource[data.Sex =='F']

wordcloud= WordCloud(
    
    background_color="white",
    width=1200,
    height= 800
    ).generate(" ".join(RC))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
