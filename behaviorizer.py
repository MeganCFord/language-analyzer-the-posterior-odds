class Posterior:

    def __init__(self, string):
        
        self.initial = str(string)
        # TODO: handle if it's not a string. maybe str()?

        self.spokenizer = Spokenizer(Posterior.initial)

        # TODO: rename these three finders to what teammates name their find-highest-variable functions.
        self.master_domain = Domainizer.find_master()
        self.master_emotion = Emotionizer.find_master()
        self.master_sentiment = Sentimentizer.find_master()

        self.predicted_behavior = Behaviorizer(Posterior.master_domain, Posterior.master_emotion, Posterior.master_sentiment)


class Behaviorizer:

    def __init__(self, domain, emotion, sentiment):

        self.behavior_list = self.import_json()
        self.peram_tuple = (domain, emotion, sentiment)
        self.prediction = self.find_prediction(self.peram_tuple)

    def import_json(self):
        # TODO: write docstring here.
        import json
        from pprint import pprint
        # loads json of potential behaviors (I think).
        with open('Behavior_List.json') as data_file:
            behaviors = json.load(data_file)
            return behaviors['Behaviors']
            # pprint(behaviors)

    def find_prediction(self, masters):
        # TODO: write docstring here.
        # loop through behavior list somehow.
        # return a string from the behaviors lexicon.
        # print the returned value.
        pass
