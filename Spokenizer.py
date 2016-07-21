from Posterior import *
import nltk
from nltk.stem.porter import *

class Spokenizer:

    def __init__(self, sentence):

        self.raw_sentence = sentence
        parsed_sentence = self.parse_sentence()

        self.domainer = Domainer(parsed_sentence)
        self.emotionizer = Emotionizer(parsed_sentence)
        self.sentimentizer = Sentimentizer(parsed_sentence)

    def parse_sentence(self):

        stemmer = PorterStemmer()

        list = nltk.word_tokenize(self.raw_sentence.lower())

        self.stemmed_list = [stemmer.stem(l) for l in list]
        print(self.stemmed_list)
        return self.stemmed_list



