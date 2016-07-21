from lexicon import *
class Emotionizer:


    def __init__(self, list_from_original_string):

        self.list_from_sentence = list_from_original_string
        self.emotions = lexicon[0]['emotion']
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
            emotional_decimal_values = {'happy': self.happy_counter_total / self.all_points_from_emotions, 'sad': self.sad_counter_total / self.all_points_from_emotions, 'anger': self.angry_counter_total / self.all_points_from_emotions, 'disgust': self.disgust_counter_total / self.all_points_from_emotions, 'fear': self.fear_counter_total / self.all_points_from_emotions}

            # sentimental_decimal_values = {'positive': self.positive_counter_total / self.all_points_from_sentiments, 'negative': self.negative_counter_total / self.all_points_from_sentiments}

            print('Emotional & Sentimental Percentages: \n %{0}: happy \n %{1}: sad \n %{2}: anger \n %{3}: disgust \n %{4}: fear'.format(emotional_decimal_values['happy'], emotional_decimal_values['sad'], emotional_decimal_values['anger'], emotional_decimal_values['disgust'], emotional_decimal_values['fear']))

        def define_percentages_for_sentiments(self):
            sentimental_decimal_values = {'positive': self.positive_counter_total / self.all_points_from_sentiments, 'negative': self.negative_counter_total / self.all_points_from_sentiments}

            print('Sentimental Percentages: \n %{0}: Positive \n %{1}: Negative'.format(sentimental_decimal_values['positive'], sentimental_decimal_values['negative']))

        self.all_points_from_emotions = calculate_all_emotional_points(self, self.happy_counter_total, self.sad_counter_total, self.angry_counter_total, self.disgust_counter_total, self.fear_counter_total)

        self.all_points_from_sentiments = calculate_all_sentiment_points(self, self.positive_counter_total, self.negative_counter_total)

        define_percentages_for_emotions(self)

        define_percentages_for_sentiments(self)


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

        print('happy_counter', counter)
        return counter


    def sad_counter(self, list_to_analyze):

        counter = 0

        for item in list_to_analyze:

            if self.emotions['sad']['positive_words'].__contains__(item) or self.emotions['sad']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['sad']['negative_words']:

            #     counter -= 1

        print('sad_counter', counter)
        return counter


    def angry_counter(self, list_to_analyze):

        counter = 0

        for item in list_to_analyze:

            if self.emotions['anger']['positive_words'].__contains__(item) or self.emotions['anger']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['anger']['negative_words']:

            #     counter -= 1

        print('angry_counter', counter)
        return counter


    def disgust_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['disgust']['positive_words'].__contains__(item) or self.emotions['disgust']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['disgust']['negative_words']:

            #     counter -= 1

        print('disgust_counter', counter)
        return counter


    def fear_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['fear']['positive_words'].__contains__(item) or self.emotions['fear']['negative_words'].__contains__(item):

                counter += 1

            # elif item in self.emotions['fear']['negative_words']:

            #     fear_counter -= 1

        print('fear_counter', counter)
        return counter


    def positive_counter(self, list_to_analyze):


        counter = 0

        for item in list_to_analyze:

            if self.emotions['happy']['positive_words'].__contains__(item) or self.emotions['sad']['positive_words'].__contains__(item) or self.emotions['anger']['positive_words'].__contains__(item) or self.emotions['disgust']['positive_words'].__contains__(item) or self.emotions['fear']['positive_words'].__contains__(item):

                counter += 1


        print('pos_counter', counter)
        return counter



    def negative_counter(self, list_to_analyze):

        counter = 0


        for item in list_to_analyze:

            if self.emotions['happy']['negative_words'].__contains__(item) or self.emotions['sad']['negative_words'].__contains__(item) or self.emotions['anger']['negative_words'].__contains__(item) or self.emotions['disgust']['negative_words'].__contains__(item) or self.emotions['fear']['negative_words'].__contains__(item):

                counter += 1

        print('neg_counter', counter)
        return counter


    def find_master(self):
        pass



