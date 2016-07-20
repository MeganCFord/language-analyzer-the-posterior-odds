
import unittest
from Posterior import *


class Test_posterior(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sentence_one = Posterior("This is a test sentence")

    def test_that_initial_sentence_is_string(self):
        self.assertIsInstance(self.sentence_one.initial, str)
        self.assertEqual("This is a test sentence", self.sentence_one.initial)

    def test_stringification_of_initial_sentence_edge_cases(self):
        self.number_sentence = Posterior(23)
        self.list_sentence = Posterior(["hey", "nope"])
        self.assertIsInstance(self.number_sentence.initial, str)
        self.assertIsInstance(self.list_sentence.initial, str)
        self.assertEqual(self.number_sentence.initial, "23")
        self.assertEqual(self.list_sentence.initial, "['hey', 'nope']")


    # this test will fail until combined with teammate work.
    def test_that_spokenizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.spokenizer, Spokenizer())

    def test_that_behaviorizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.predicted_behavior, Behaviorizer())


class Test_behaviorizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.behaviorizer_test = Behaviorizer("positive", "happy", "scientific")

    def test_json_load(self):
        self.assertIsInstance(self.behaviorizer_test.behavior_list, object)
        self.assertIn({"(positive, happy, scientific)": "discovering benevolent aliens."}, self.behaviorizer_test.behavior_list)
        self.assertEqual("", self.behaviorizer_test.behavior_list[(negative, fear, behavioral)])
    # TODO: test that the tuple has three strings in it.
    # TODO: test that we're passing in a tuple.
    # TODO: test that the tuples will match up.
        pass

if __name__ == '__main__':
    unittest.main()
