class Posterior:

    def __init__(self, string):
        
        self.initial = string
        self.spokenizer = Spokenizer(Posterior.initial)

        self.master_domain = Domainizer.find_master()
        self.master_emotion = Emotionizer.find_master()
        self.master_sentiment = Sentimentizer.find_master()

        self.predicted_behavior = Behaviorizer(Posterior.master_domain, Posterior.master_emotion, Posterior.master_sentiment)

class Behaviorizer:
    import json
    from pprint import pprint


    def __init__(self, domain, emotion, sentiment):

        self.peram_set = tuple(domain, emotion, sentiment)
        self.prediction = find_prediction(peram_set)

        # loads json of potential behaviors (I think).
        with open('Behavior_List.json') as data_file:
            behaviors = json.load(data_file)
            pprint(behaviors)

    def find_prediction(domain, emotion, sentiment):
        # loop through behavior list somehow.
        # return a thing from the lexicon.
        pass

