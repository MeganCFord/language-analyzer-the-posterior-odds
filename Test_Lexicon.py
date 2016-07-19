
import messages
import unittest


class Test_analyzer_creation(unittest.TestCase):

    @classmethod:
        def setUpClass(self):
            sentence_one = Analyzer("This is a test sentence")
            sentence_bad = Analyzer(2)
            

    def test_that_tokenizer_is_instantiated(self):  # isInstanceOf tokenizer

    def test_that_initial sentence_is_string(self):

        self.assertIsInstance(str, self.sentence_one.initial)
        self.assertEqual("This is a test sentence", self.sentence_one.initial)

    def test_printer_of_string_sentence(self):


class Test_tokenizer(unittest.TestCase):

    def test_what_it_receives_is_the_initial_sentence_property(self):

    def test_that_domainer_was_created(self):

    def test_that_emotionizer_was_created(self):

    def test_what_it_outputs_is_a_list(self):

    # we also need tests in here that output the word count, character count, word placement



class Test_emotionizer(unittest.TestCase):

    def test_that_sentimentizer_was_created(self):

    def test_what_it_receives_is_a_list(self):

    def test_that_it_can_connect_to_lexicon(self):

    def test_that_lexicon_is_the_thing(self):

    def test_that_each_emotion_includes_sentiments(self):


    # counter start tests
    def test_that_happy_counter_starts_at_zero(self):

    def test_that_sad_counter_starts_at_zero(self):

    def test_that_angry_counter_starts_at_zero(self):

    def test_that_disgust_counter_starts_at_zero(self):

    def test_that_fear_counter_starts_at_zero(self):

    # TODO: loop test with counter end tests (test that match adds one, that no match does not add one)
    # TODO: math test to divide each non-zero counter against total num of accrued points.
    # TODO: print the decimal value of each non-zero counter.
    # TODO: find the highest non-zero value(s)
    # TODO: assigns highest value(s) to an object to send to the behaviorizer
    # TODO: test that we can send more than one value

class Test_sentimentizer(unittest.TestCase):

    # counter start tests
    def test_that_positive_counter_starts_at_zero(self):

    def test_that_negative_counter_starts_at_zero(self):
    # TODO: loop through the emotion counters and test that match adds one, that no match does not add one)
    # TODO: math test to subtract neg from pos and divide result by total num of accrued points.
    # TODO: print the decimal value
    # TODO: assigns highest value(s) to an object to send to the behaviorizer

class Test_domainer(unittest.TestCase):

    def test_what_it_receives_is_a_list(self):

    def test_that_it_can_connect_to_lexicon(self):

    def test_that_lexicon_is_a_list(self):

    # counter start tests
    def test_that_financial_counter_starts_at_zero(self):

    def test_that_behavioral_counter_starts_at_zero(self):

    def test_that_scientific_counter_starts_at_zero(self):

    def test_that_educational_counter_starts_at_zero(self):

    def test_that_politics_counter_starts_at_zero(self):

    def test_that_relationships_counter_starts_at_zero(self):

    # TODO: loop test with counter end tests (match adds a point, no match does not add a point)
    # TODO: math test to divide each non-zero counter against total num of accrued points.
    # TODO: print the decimal value of each non-zero counter.
    # TODO: assigns highest value(s) to an object to send to the behaviorizer

class Test_behaviorizer(unittest.TestCase):

    def test_what_it_receives(self):  # going to be receiving a bunch of little tuples or something.

    # TODO: loop test through behavior object to find matches
    #  TODO: print matches


if __name__ == '__main__':
    unittest.main()

