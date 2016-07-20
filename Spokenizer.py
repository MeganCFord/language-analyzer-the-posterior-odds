from Posterior import *
import nltk
from nltk.stem.porter import *

class Spokenizer:

    def __init__(self, sentence):

        self.raw_sentence = sentence
        self.parsed_sentence = self.parse_sentence()

    def parse_sentence(self):

        stemmer = PorterStemmer()
        sentence = self.raw_sentence.lower()

        list = nltk.word_tokenize(sentence)

        self.stemmed_list = [stemmer.stem(l) for l in list]
        return self.stemmed_list

        # self.domainer = Domainer(stemmed_list)
        # self.emotionizer = Emotionizer(stemmed_list)
        # self.sentimentizer = Sentimentizer(stemmed_list)

