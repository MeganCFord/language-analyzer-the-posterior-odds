from lexicon import *

class Domainer:
    def __init__(self, list_from_str):
        self.sample_list = list_from_str
        self.financial_count = 0
        self.behavioral_count = 0
        self.scientific_count = 0
        self.educational_count = 0
        self.political_count = 0
        self.relationships_count = 0

    def financial_counter(self):
        self.financial_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["financial"]])
        # for i in self.sample_list:
        #   if i in lexicon["domain"]["financial"]:
        #       self.financial_count +=1
        return self.financial_count

    def behavioral_counter(self):
        self.behavioral_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["behavioral"]])

        return self.behavioral_count

    def scientific_counter(self):
        self.scientific_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["scientific"]])

        return self.scientific_count

    def educational_counter(self):
        self.educational_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["educational"]])

        return self.educational_count

    def political_counter(self):
        self.political_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["politics"]])
        return self.political_count

    def relationships_counter(self):
        self.relationships_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["relationships"]])
        return self.relationships_count



