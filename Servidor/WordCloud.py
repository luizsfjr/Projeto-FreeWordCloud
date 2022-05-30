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

    
