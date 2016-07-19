class Posterior:

    def __init__(self, string):
        
        self.initial = string
        self.spokenizer = Spokenizer(Posterior.initial)

        self.master_domain = Domainizer.find_master()
        self.master_emotion = Emotionizer.find_master()
        self.master_sentiment = Sentimentizer.find_master()

        self.predicted_behavior = Behaviorizer.find_prediction(Posterior.master_domain, Posterior.master_emotion, Posterior.master_sentiment)

class Behaviorizer:

    def find_prediction(domain, emotion, sentiment):
        # do something here.
        # return a thing from the lexicon.
        pass
