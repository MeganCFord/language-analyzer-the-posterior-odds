import unittest
from Posterior import *

class Test_emotionizer(unittest.TestCase):

    def test_that_sentimentizer_was_created(self):
        pass
    def test_what_it_receives_is_a_list(self):
        pass
    def test_that_it_can_connect_to_lexicon(self):
        pass
    def test_that_lexicon_is_the_thing(self):
        pass
    def test_that_each_emotion_includes_sentiments(self):
        pass

    # counter start tests
    def test_that_happy_counter_starts_at_zero(self):
        pass
    def test_that_sad_counter_starts_at_zero(self):
        pass
    def test_that_angry_counter_starts_at_zero(self):
        pass
    def test_that_disgust_counter_starts_at_zero(self):
        pass
    def test_that_fear_counter_starts_at_zero(self):
        pass
    # TODO: loop test with counter end tests (test that match adds one, that no match does not add one)
    # TODO: math test to divide each non-zero counter against total num of accrued points.
    # TODO: print the decimal value of each non-zero counter.
    # TODO: find the highest non-zero value(s)
    # TODO: assigns highest value(s) to an object to send to the behaviorizer
    # TODO: test that we can send more than one value


class Test_sentimentizer(unittest.TestCase):

    # counter start tests
    def test_that_positive_counter_starts_at_zero(self):
        pass
    def test_that_negative_counter_starts_at_zero(self):
        pass
    # TODO: loop through the emotion counters and test that match adds one, that no match does not add one)
    # TODO: math test to subtract neg from pos and divide result by total num of accrued points.
    # TODO: print the decimal value
    # TODO: assigns highest value(s) to an object to send to the behaviorizer


if __name__ == '__main__':
    unittest.main()

