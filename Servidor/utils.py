import unicodedata
import re
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')

#Tokenizer
def tokenize(text):
    return text.split()

# Stopwords
#with open('stopPort.txt') as f:
#    stopwords_pt = f.read().split('\n')
nltk_stop = set(stopwords.words('portuguese'))

def remove_stop_words(text, stopWords):
    for sw in stopWords:
        text = re.sub(r'\b%s\b' % sw, "", text)
    return text

#Special Characters
def remove_others(text):
    new_text = text.replace('"', '')
    new_text = new_text.replace('(','')
    new_text = new_text.replace(')','')
    new_text = new_text.replace("'","")
    new_text = new_text.replace('%','')
    new_text = re.sub(r"u+h","", new_text)
    new_text = re.sub(r"o+h","", new_text)
    new_text = re.sub(r"a+h","", new_text)
    new_text = re.sub(r"ah+","", new_text)
    return new_text

# Lower Case Transformation
def lowercase(text):
    text = text.lower()
    return text

# Punctuation Removal
def remove_punctuation(text):
    # re.sub(replace_expression, replace_string, target)
    new_text = re.sub(r"\.|,|;|:|-|!|\?|´|`|^|'", " ", text)
    new_text = re.sub(r"[A-Z0-9]+|\.|\!|\,",' ', new_text)
    new_text = re.sub(r"\$|\@|\(|\)|\&|\¨|\_|\=",' ', new_text)
    new_text = re.sub(r"\\|\||\/|\>|\<|\[|\]|\{|\}",' ', new_text)
    new_text = re.sub(r"\n|\t|\r",'', new_text)
    new_text = re.sub(r"\`|\´|\^|\%|\;|\:|\§|\ª|\º|\₢|\°",' ', new_text)
    return new_text

# Accent Removal
def remove_accentuation(text):
    nfkd_form = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Numeric Character Removal
def remove_numbers(text):
    text = str(text)
    new_text = re.sub(r"[0-9]+", "", text)
    return new_text

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
    
    if(config['remove_accentuation'] == True):
        text = remove_accentuation(text)
    
    if(config["remove_punctuation"] == True):
        text = remove_punctuation(text)

    if(config["remove_others"] == True):
        text = remove_others(text)

    if(config["remove_numbers"] == True):
        text = remove_numbers(text)

    if(config["remove_stopwords"] == True):
        text = remove_stop_words(text, stopWords=nltk_stop)
        
    if(config["remove_emojis"] == True):
        text = remove_emojis(text)
        
    if(config["remove_space"] == True):
        text = remove_space(text)
        
    texts.append(text)
        
    return texts