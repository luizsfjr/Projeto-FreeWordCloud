import utils

config = {
            'lowercase': True, \
            'remove_stopwords': True, \
            'remove_emojis': True,\
            'remove_space': True,
    }

def preprocess(text):
    comments = utils.preprocessing(text, config)
    return comments



