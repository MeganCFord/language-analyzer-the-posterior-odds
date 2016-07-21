from  Spokenizer import *
from domainer import *
from emotionizer import *

class Posterior:

    def __init__(self, string):
        
        self.initial = str(string)
        # print("your sentence is " + self.initial)

        self.spokenizer = Spokenizer(self.initial)

        self.master_domain = self.spokenizer.domainer.highest_domain
        self.master_emotion = self.spokenizer.emotionizer.highest_emotion
        self.master_sentiment = self.spokenizer.emotionizer.highest_sentiment

        self.predicted_behavior = Behaviorizer(self.master_sentiment, self.master_emotion, self.master_domain)

class Behaviorizer:

    def __init__(self, sentiment, emotion, domain):

        self.behavior_dict = self.import_json()
        self.peram_list = [sentiment, emotion, domain]
        self.prediction = self.find_prediction(str(self.peram_list))

        # prints the final result.
        print("this sentence is {0}, {1}, and {2}, so the speaker probably is: {3}".format(self.peram_list[0], self.peram_list[1], self.peram_list[2], self.prediction))

    def import_json(self):
        '''
        this function imports and parses our lexicon of pre-written behavior predictions.

        arguments: none

        '''
        import json
        from pprint import pprint
        # loads json of potential behaviors (I think).
        with open('Behavior_List.json') as data_file:
            behaviors = json.load(data_file)
            return behaviors['Behaviors']
            # pprint(behaviors)

    def find_prediction(self, master):
        '''
        this function receives a stringified tuple with three items in it,
        finds a match within a dictionary of pre-defined behavior predictions,
        and returns the string value for the matching key.

        arguments: one tuple with three items in it.
        Each item is the string name of the highest-rated value for each of the three Posterior analyzation categories:
        In order: domain, emotion, sentiment.
        example: ('financial', 'sad', 'negative')

        '''
        for key, value in self.behavior_dict.items():
            if master == key:
                return value


        # ALTERNATE OPTION although it returns a list.
        # return [value for key, value  in self.behavior_dict.items() if master == key]
