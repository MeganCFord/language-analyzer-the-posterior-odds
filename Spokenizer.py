import nltk
from nltk.stem.porter import *
from domainer import *

class Spokenizer:

    def __init__(self, sentence):

        self.raw_sentence = sentence
        parsed_sentence = self.parse_sentence()

        self.domainer = Domainer(parsed_sentence)
        # self.emotionizer = Emotionizer(parsed_sentence)
        # self.sentimentizer = Sentimentizer(parsed_sentence)

    def parse_sentence(self):
        '''
        This function receives the sentence variable, a string of
        words.

        Example sentence: "I am not a cheesy example sentence."

        The sentence is tokenized into a list of words,
        changes any uppercase letters to lowercase, and then removes
        suffixes from the words. The resulting list of words is
        printed, and saved above as parsed_sentence. Then it is
        passed to the Domainer, Sentimentizer, and Emotionizer.

        '''
        stemmer = PorterStemmer()

        self.the_list = nltk.word_tokenize(self.raw_sentence.lower())

        # self.stemmed_list = [stemmer.stem(l) for l in list]
        # print(self.stemmed_list)
        return self.the_list



