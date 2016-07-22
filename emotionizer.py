from lexicon import *
class Emotionizer:


    def __init__(self, list_from_original_string):

        self.list_from_sentence = list_from_original_string
        self.emotions = lexicon['emotion']
        self.happy_counter_total = self.happy_counter(self.list_from_sentence)
        self.sad_counter_total = self.sad_counter(self.list_from_sentence)
        self.angry_counter_total = self.angry_counter(self.list_from_sentence)
        self.disgust_counter_total = self.disgust_counter(self.list_from_sentence)
        self.fear_counter_total = self.fear_counter(self.list_from_sentence)
        self.positive_counter_total = self.positive_counter(self.list_from_sentence)
        self.negative_counter_total = self.negative_counter(self.list_from_sentence)





        def calculate_all_emotional_points(self, happy, sad, angry, disgust, fear):
            emotion_total = happy + sad + angry + disgust + fear
            return emotion_total

        def calculate_all_sentiment_points(self, positive, negative):

            sentiment_total = positive + negative
            return sentiment_total


        def define_percentages_for_emotions(self):
            if self.all_points_from_emotions == 0:
                self.emotional_decimal_values = {
                    "happy": 0,
                    "sad": 0,
                    "anger": 0,
                    "disgust": 0,
                    "fear": 0
                }

                print('Emotional Percentages: \n %{0}: happy \n %{1}: sad \n %{2}: anger \n %{3}: disgust \n %{4}: fear'.format(self.emotional_decimal_values['happy'], self.emotional_decimal_values['sad'], self.emotional_decimal_values['anger'], self.emotional_decimal_values['disgust'], self.emotional_decimal_values['fear']))
            else:
                self.emotional_decimal_values = {
                    'happy': self.happy_counter_total / self.all_points_from_emotions,
                    'sad': self.sad_counter_total / self.all_points_from_emotions,
                    'anger': self.angry_counter_total / self.all_points_from_emotions,
                    'disgust': self.disgust_counter_total / self.all_points_from_emotions,
                    'fear': self.fear_counter_total / self.all_points_from_emotions
                }

                print('Emotional Percentages: \n %{0}: happy \n %{1}: sad \n %{2}: anger \n %{3}: disgust \n %{4}: fear'.format(self.emotional_decimal_values['happy'], self.emotional_decimal_values['sad'], self.emotional_decimal_values['anger'], self.emotional_decimal_values['disgust'], self.emotional_decimal_values['fear']))

            return self.emotional_decimal_values

        def define_percentages_for_sentiments(self):
            if self.all_points_from_sentiments == 0:
                self.sentimental_decimal_values = {
                    "positive": 0,
                    "negative": 0
                }

                print('Sentimental Percentages: \n %{0}: Positive \n %{1}: Negative'.format(self.sentimental_decimal_values['positive'], self.sentimental_decimal_values['negative']))
            else:
                self.sentimental_decimal_values = {
                    'positive': self.positive_counter_total / self.all_points_from_sentiments,
                    'negative': self.negative_counter_total / self.all_points_from_sentiments
                }

                print('Sentimental Percentages: \n %{0}: Positive \n %{1}: Negative'.format(self.sentimental_decimal_values['positive'], self.sentimental_decimal_values['negative']))

            return self.sentimental_decimal_values

        self.all_points_from_emotions = calculate_all_emotional_points(self, self.happy_counter_total, self.sad_counter_total, self.angry_counter_total, self.disgust_counter_total, self.fear_counter_total)

        self.all_points_from_sentiments = calculate_all_sentiment_points(self, self.positive_counter_total, self.negative_counter_total)

        # define_percentages_for_emotions(self)

        # define_percentages_for_sentiments(self)

        self.final_emotional_decimal_values = define_percentages_for_emotions(self)
        self.final_sentimental_decimal_values = define_percentages_for_sentiments(self)
        self.highest_emotion = self.find_highest_emotion()
        self.highest_sentiment = self.find_highest_sentiment()



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

        self.highest_emotion = max(self.final_emotional_decimal_values.keys(), key=(lambda key: self.final_emotional_decimal_values[key]))
        return self.highest_emotion


    def find_highest_sentiment(self):

        self.highest_sentiment = max(self.final_sentimental_decimal_values.keys(), key=(lambda key: self.final_sentimental_decimal_values[key]))
        return self.highest_sentiment

    # def find_highest_domain(self):

    #     self.highest_domain = max(self.final_domain_values.keys(), key=(lambda key: self.final_domain_values[key]))
    #     return self.highest_domain



