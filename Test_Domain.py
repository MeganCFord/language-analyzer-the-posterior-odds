import unittest
from Posterior import *

class Test_domainer(unittest.TestCase):

    def test_what_it_receives_is_a_list(self):
        pass
    def test_that_it_can_connect_to_lexicon(self):
        pass
    def test_that_lexicon_is_a_list(self):
        pass
    # counter start tests
    def test_that_financial_counter_starts_at_zero(self):
        pass
    def test_that_behavioral_counter_starts_at_zero(self):
        pass
    def test_that_scientific_counter_starts_at_zero(self):
        pass
    def test_that_educational_counter_starts_at_zero(self):
        pass
    def test_that_politics_counter_starts_at_zero(self):
        pass
    def test_that_relationships_counter_starts_at_zero(self):
        pass
    # TODO: loop test with counter end tests (match adds a point, no match does not add a point)
    # TODO: math test to divide each non-zero counter against total num of accrued points.
    # TODO: print the decimal value of each non-zero counter.
    # TODO: assigns highest value(s) to an object to send to the behaviorizer


if __name__ == '__main__':
    unittest.main()

