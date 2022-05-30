import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import Preprocessing

#path_file = 'Attraction_Alter.csv'

import warnings
warnings.filterwarnings('ignore')

def make_wordcloud(text):
    comments = Preprocessing.preprocess(text)
    #print(comments)
    words = ''.join(review for review in comments)
    wordcloud = WordCloud(background_color="black", stopwords=STOPWORDS).generate(words)

    return wordcloud

    
