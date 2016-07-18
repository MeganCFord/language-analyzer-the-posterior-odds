
import analyzer
import unittest


class Test_analyzer_creation(unittest.TestCase):

    def test_that_analyzer_argument_is_string(self):

    def test_that_list_version_was_created(self):

    def test_that_argument_and_initial_sentence_property_are_equal(self):


class Test_list_version(unittest.TestCase):

    def test_that_sentimentizer_was_created(self):

    def test_that_domainer_was_created(self):

    def test_that_behaviorizer_was_created(self):

    def test_what_it_receives_is_the_initial_sentence_property(self):

    def test_what_it_outputs_is_a_list(self):


class Test_sentimentizer(unittest.TestCase):

    def test_what_it_receives_is_a_list(self):

    def test_that_it_can_connect_to_lexicon(self):

    def test_that_lexicon_is_a_list(self):
        
    def test_that_positive_counter_starts_at_zero(self):

    def test_that_negative_counter_starts_at_zero(self):


class Test_behaviorizer(unittest.TestCase):

    def test_what_it_receives_is_a_list(self):

    def test_that_it_can_connect_to_lexicon(self):

    def test_that_lexicon_is_a_list(self):

    def test_that_happy_counter_starts_at_zero(self):

    def test_that_sad_counter_starts_at_zero(self):

    def test_that_angry_counter_starts_at_zero(self):

    def test_that_disgust_counter_starts_at_zero(self):
        
    def test_that_fear_counter_starts_at_zero(self):


class Test_domainer(unittest.TestCase):

    def test_what_it_receives_is_a_list(self):

    def test_that_it_can_connect_to_lexicon(self):

    def test_that_lexicon_is_a_list(self):

    def test_that_financial_counter_starts_at_zero(self):

    def test_that_behavioral_counter_starts_at_zero(self):

    def test_that_scientific_counter_starts_at_zero(self):

    def test_that_educational_counter_starts_at_zero(self):

    def test_that_politics_counter_starts_at_zero(self):

    def test_that_relationships_counter_starts_at_zero(self):


if __name__ == '__main__':
    unittest.main()
>>>>>>> Stashed changes
