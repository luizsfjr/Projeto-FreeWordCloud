import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

#Tokenizer
def tokenize(text):
    return text.split()

nltk_stop = set(stopwords.words('portuguese'))

#Remove stopwords
def remove_stop_words(text, stopWords):
    for sw in stopWords:
        text = re.sub(r'\b%s\b' % sw, "", text)
    return text

# Lower Case Transformation
def lowercase(text):
    text = text.lower()
    return text

# Emoji Removal
def remove_emojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')

# Space removal
def remove_space(text):
    word_list = text.split()
    result = []
    for w in word_list:
        result.append(w.strip())
    result = " ".join(result)
    return result

# Main Preprocessing Function

def preprocessing(tex, config):
    texts = []
    
    if(config['lowercase'] == True):
        text = lowercase(tex)
    
    if(config["remove_stopwords"] == True):
        text = remove_stop_words(text, stopWords=nltk_stop)
        
    if(config["remove_emojis"] == True):
        text = remove_emojis(text)
        
    if(config["remove_space"] == True):
        text = remove_space(text)
        
    texts.append(text)
        
    return texts