
import unittest
from Posterior import *


class Test_posterior(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sentence_one = Posterior("This is a test sentence")

    def test_that_initial_sentence_is_string(self):
        self.assertIsInstance(self.sentence_one.initial, str)
        self.assertEqual("This is a test sentence", self.sentence_one.initial)

        with self.assertRaises(TypeError):
            sentence_bad = Posterior(2)
            sentence_also_bad = Posterior(set())

    # these tests will fail until combined with teammate work.
    def test_that_spokenizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.spokenizer, Spokenizer())


class Test_behaviorizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        sentence_two = Posterior("This is a test sentence")

    def test_that_master_variables_start_as_none(self):
        self.assertEqual(self.master_domain, None)
        self.assertEqual(self.master_emotion, None)
        self.assertEqual(self.master_sentiment, None)

        # NOTE: the other classes should be sending final values to these variables after they're done with their calculations?

    def test_some_kind_of_non_none_checker(self):
        pass


    # TODO: loop test through behavior object to find matches




if __name__ == '__main__':
    unittest.main()
