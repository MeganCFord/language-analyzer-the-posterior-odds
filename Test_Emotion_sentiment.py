import unittest
from Posterior import *

class Test_Emotionizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):


        self.list_from_original_string = []


    def test_what_it_receives_is_a_list(self):


        emotionizer = Emotionizer(self.list_from_original_string)
        self.assertIsInstance(emotionizer.list_from_sentence, list)


    # counter start tests
    def test_happy_counter(self):


        non_happy_sentence = Emotionizer(['pissed'])
        self.assertEqual(non_happy_sentence.happy_counter_total, 0)

        happy_sentence = Emotionizer(['biscuit'])
        self.assertEqual(happy_sentence.happy_counter_total, 1)


    def test_sad_counter(self):


        non_sad_sentence = Emotionizer(['happy'])
        self.assertEqual(non_sad_sentence.sad_counter_total, 0)

        sad_sentence = Emotionizer(['mourning'])
        self.assertEqual(sad_sentence.sad_counter_total, 1)


    def test_angry_counter(self):


        non_angry_sentence = Emotionizer(['happy', 'happy', 'happy'])
        self.assertEqual(non_angry_sentence.angry_counter_total, 0)

        angry_sentence = Emotionizer(['anger'])
        self.assertEqual(angry_sentence.angry_counter_total, 1)


    def test_disgust_counter(self):


        non_disgust_sentence = Emotionizer(['happy'])
        self.assertEqual(non_disgust_sentence.disgust_counter_total, 0)

        disgust_sentence = Emotionizer(['sick'])
        self.assertEqual(disgust_sentence.disgust_counter_total, 1)


    def test_fear_counter(self):


        non_fear_sentence = Emotionizer(['happy'])
        self.assertEqual(non_fear_sentence.fear_counter_total, 0)

        fear_sentence = Emotionizer(['tyrant'])
        self.assertEqual(fear_sentence.fear_counter_total, 1)


    def test_positive_counter(self):


        non_positive_sentence = Emotionizer(['hate'])
        self.assertEqual(non_positive_sentence.positive_counter_total, 0)

        positive_sentence = Emotionizer(['happy'])
        self.assertEqual(positive_sentence.positive_counter_total, 1)


    def test_negative_counter(self):


        non_negative_sentence = Emotionizer(['happy'])
        self.assertEqual(non_negative_sentence.negative_counter_total, 0)

        negative_sentence = Emotionizer(['hate'])
        self.assertEqual(negative_sentence.negative_counter_total, 1)


    def test_output_is_emotion_with_highest_value(self):


        happy_sentence = Emotionizer(['love', 'is', 'love'])
        self.assertEqual(happy_sentence.find_highest_emotion(), 'happy')

        sad_sentence = Emotionizer(['sadly', 'is', 'sadly'])
        self.assertEqual(sad_sentence.find_highest_emotion(), 'sad')

        angry_sentence = Emotionizer(['hostile', 'is', 'hostile'])
        self.assertEqual(angry_sentence.find_highest_emotion(), 'anger')

        disgust_sentence = Emotionizer(['vomit', 'is', 'vomit'])
        self.assertEqual(disgust_sentence.find_highest_emotion(), 'disgust')

        fear_sentence = Emotionizer(['tyrant', 'is', 'tyrant'])
        self.assertEqual(fear_sentence.find_highest_emotion(), 'fear')

        positive_sentence = Emotionizer(['biscuit', 'is', 'biscuit'])
        self.assertEqual(positive_sentence.find_highest_sentiment(), 'positive')

        negative_sentence = Emotionizer(['hostile', 'is', 'hostile'])
        self.assertEqual(negative_sentence.find_highest_sentiment(), 'negative')



    # TODO: loop test with counter end tests (test that match adds one, that no match does not add one)
    # TODO: math test to divide each non-zero counter against total num of accrued points.
    # TODO: print the decimal value of each non-zero counter.
    # TODO: find the highest non-zero value(s)
    # TODO: assigns highest value(s) to an object to send to the behaviorizer
    # TODO: test that we can send more than one value

    # TODO: loop through the emotion counters and test that match adds one, that no match does not add one)
    # TODO: math test to subtract neg from pos and divide result by total num of accrued points.
    # TODO: print the decimal value
    # TODO: assigns highest value(s) to an object to send to the behaviorizer


if __name__ == '__main__':
    unittest.main()

