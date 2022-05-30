import pandas as pd
import utils

config = {
            'lowercase': True, \
            'remove_accentuation': True, \
            'remove_punctuation': True, \
            'remove_others': True, \
            'remove_numbers': True, \
            'remove_stopwords': True, \
            'stemming': False, \
            'remove_emojis': True,\
            'remove_space': True,\
}

def preprocess(text):
    comments = utils.preprocessing(text, config)
    return comments



