from wordcloud import WordCloud, STOPWORDS
import Preprocessing

import warnings
warnings.filterwarnings('ignore')

def make_wordcloud(text, color):
    comments = Preprocessing.preprocess(text)
    words = ''.join(review for review in comments)
    wordcloud = WordCloud(background_color=color, stopwords=STOPWORDS).generate(words)

    return wordcloud

    
