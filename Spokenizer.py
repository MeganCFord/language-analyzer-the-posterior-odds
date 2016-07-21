from Posterior import *
import nltk
from nltk.stem.porter import *

class Spokenizer:

    def __init__(self, sentence):
        '''
        This function initializes the Spokenizer object,
        receiving a string of words, assigning it as a variable,
        and sending it to the parse_sentence function.
        The resulting list of words is saved here as parsed_sentence,
        and passed to the Domainer, Sentimentizer, and Emotionizer.

        Arguments: a string of words.
        Example: "I am not a cheesy example sentence."

        '''
        self.raw_sentence = sentence
        parsed_sentence = self.parse_sentence()

        self.domainer = Domainer(parsed_sentence)
        self.emotionizer = Emotionizer(parsed_sentence)
        self.sentimentizer = Sentimentizer(parsed_sentence)

    def parse_sentence(self):
        '''
        This function receives the sentence variable, tokenizes it
        into a list of words, changes any uppercase letters to
        lowercase, and then removes suffixes from the words.

        '''
        stemmer = PorterStemmer()

        list = nltk.word_tokenize(self.raw_sentence.lower())

        self.stemmed_list = [stemmer.stem(l) for l in list]
        print(self.stemmed_list)
        return self.stemmed_list



