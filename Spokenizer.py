from Posterior import *
import nltk

class Spokenizer:

    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.list = nltk.word_tokenize(sentence)

        # self.Domainizer = Domainizer()


# import code
# code.interact(local=locals())
