from wordcloud import WordCloud
import Preprocessing

import warnings
warnings.filterwarnings('ignore')

def make_wordcloud(text, color, tema):
    comments = Preprocessing.preprocess(text)
    words = ''.join(review for review in comments)
    wordcloud = WordCloud(background_color=color, colormap=tema).generate(words)

    return wordcloud

    
