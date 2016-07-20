
import unittest
from Posterior import *


class Test_posterior(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sentence_one = Posterior("This is a test sentence")

    def test_that_initial_sentence_is_string(self):
        self.assertIsInstance(self.sentence_one.initial, str)
        self.assertEqual("This is a test sentence", self.sentence_one.initial)

        # what if I just stringified everything in the argument, to make sure?
        with self.assertRaises(TypeError):
            sentence_bad = Posterior(2)
            sentence_also_bad = Posterior(set())


    # this test will fail until combined with teammate work.
    def test_that_spokenizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.spokenizer, Spokenizer())

    def test_that_behaviorizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.predicted_behavior, Behaviorizer())


class Test_behaviorizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sentence_json = Behaviorizer("positive", "happy", "scientific")

    def test_json_load(self):
    # TODO: test the loading of the json.
    # TODO: test that the json is traversable.
    # TODO: test that we're passing in a tuple.
    # TODO: test that the tuples will match up.
        pass

if __name__ == '__main__':
    unittest.main()
