from lexicon import *
class Emotionizer:


    def __init__(self, list_from_original_string):

        self.list_from_sentence = list_from_original_string
        self.emotions = lexicon['emotion']
        # counters for emotion lexicon matches.
        self.happy_counter_total = self.happy_counter(self.list_from_sentence)
        self.sad_counter_total = self.sad_counter(self.list_from_sentence)
        self.angry_counter_total = self.angry_counter(self.list_from_sentence)
        self.disgust_counter_total = self.disgust_counter(self.list_from_sentence)
        self.fear_counter_total = self.fear_counter(self.list_from_sentence)
        #counter for pos/negative emotion lexicon matches.
        self.positive_counter_total = self.positive_counter(self.list_from_sentence)
        self.negative_counter_total = self.negative_counter(self.list_from_sentence)
        # total num of points.
        self.emotion_points = self.calculate_all_emotional_points()
        self.sentiment_points = self.calculate_all_sentiment_points()
        # percentages.
        self.emotional_percentage_dict = self.define_percentages_for_emotions()
        self.sentiment_percentage_dict = self.define_percentages_for_sentiments()
        # string value/highest emotions.
        self.highest_emotion = self.find_highest_emotion()
        self.highest_sentiment = self.find_highest_sentiment()


        print('Emotional Percentages: \n %{0}: happy \n %{1}: sad \n %{2}: anger \n %{3}: disgust \n %{4}: fear'.format(self.emotional_percentage_dict['happy'], self.emotional_percentage_dict['sad'], self.emotional_percentage_dict['anger'], self.emotional_percentage_dict['disgust'], self.emotional_percentage_dict['fear']))

        print('Sentimental Percentages: \n %{0}: Positive \n %{1}: Negative'.format(self.sentiment_percentage_dict['positive'], self.sentiment_percentage_dict['negative']))

    def calculate_all_emotional_points(self):
        emotion_total = self.happy_counter_total + self.sad_counter_total + self.angry_counter_total + self.disgust_counter_total + self.fear_counter_total
        return emotion_total

    def calculate_all_sentiment_points(self):

        sentiment_total =self.positive_counter_total + self.negative_counter_total
        return sentiment_total

    def define_percentages_for_emotions(self):
        if self.emotion_points == 0:
            self.emotional_decimal_values = {
                "happy": 0,
                "sad": 0,
                "anger": 0,
                "disgust": 0,
                "fear": 0
            }

        else:
            self.emotional_decimal_values = {
                'happy': self.happy_counter_total / self.emotion_points,
                'sad': self.sad_counter_total / self.emotion_points,
                'anger': self.angry_counter_total / self.emotion_points,
                'disgust': self.disgust_counter_total / self.emotion_points,
                'fear': self.fear_counter_total / self.emotion_points
            }

        return self.emotional_decimal_values

    def define_percentages_for_sentiments(self):
        if self.sentiment_points == 0:
            self.sentimental_decimal_values = {
                "positive": 0,
                "negative": 0
            }

        else:
            self.sentimental_decimal_values = {
                'positive': self.positive_counter_total / self.sentiment_points,
                'negative': self.negative_counter_total / self.sentiment_points
            }

        return self.sentimental_decimal_values


    def happy_counter(self, list_to_analyze):

        # counter = sum([1 for word in self.list_from_sentence
        #     if word in lexicon['emotions']['happy']['positive']])

        # SAME AS BELOW

        counter = 0

        for item in list_to_analyze:

            if self.emotions['happy']['positive_words'].__contains__(item) or self.emotions['happy']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['happy']['negative_words']:

            #     counter -= 1

        print('happy_counter', '%' + str(counter))
        return counter


    def sad_counter(self, list_to_analyze):

        counter = 0

        for item in list_to_analyze:

            if self.emotions['sad']['positive_words'].__contains__(item) or self.emotions['sad']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['sad']['negative_words']:

            #     counter -= 1

        print('sad_counter', '%' + str(counter))
        return counter


    def angry_counter(self, list_to_analyze):

        counter = 0

        for item in list_to_analyze:

            if self.emotions['anger']['positive_words'].__contains__(item) or self.emotions['anger']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['anger']['negative_words']:

            #     counter -= 1

        print('angry_counter', '%' + str(counter))
        return counter


    def disgust_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['disgust']['positive_words'].__contains__(item) or self.emotions['disgust']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['disgust']['negative_words']:

            #     counter -= 1

        print('disgust_counter', '%' + str(counter))
        return counter


    def fear_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['fear']['positive_words'].__contains__(item) or self.emotions['fear']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['fear']['negative_words']:

            #     fear_counter -= 1

        print('fear_counter', '%' + str(counter))
        return counter


    def positive_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['happy']['positive_words'].__contains__(item) or self.emotions['sad']['positive_words'].__contains__(item) or self.emotions['anger']['positive_words'].__contains__(item) or self.emotions['disgust']['positive_words'].__contains__(item) or self.emotions['fear']['positive_words'].__contains__(item):

                counter += 1


        print('pos_counter', '%' + str(counter))
        return counter



    def negative_counter(self, list_to_analyze):

        counter = 0


        for item in list_to_analyze:

            if self.emotions['happy']['negative_words'].__contains__(item) or self.emotions['sad']['negative_words'].__contains__(item) or self.emotions['anger']['negative_words'].__contains__(item) or self.emotions['disgust']['negative_words'].__contains__(item) or self.emotions['fear']['negative_words'].__contains__(item):

                counter += 1

        print('neg_counter', '%' + str(counter))
        return counter


    def find_highest_emotion(self):

        self.highest_emotion = max(self.emotional_percentage_dict.keys(), key=(lambda key: self.emotional_percentage_dict[key]))
        return self.highest_emotion


    def find_highest_sentiment(self):

        self.highest_sentiment = max(self.sentiment_percentage_dict.keys(), key=(lambda key: self.sentiment_percentage_dict[key]))
        return self.highest_sentiment


