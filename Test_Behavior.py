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

    def test_that_behaviorizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.predicted_behavior, Behaviorizer())

    # this test will fail until combined with teammate work.
    def test_that_spokenizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.spokenizer, Spokenizer())


class Test_behaviorizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.behaviorizer_test = Behaviorizer("positive", "happy", "scientific")
        self.another_behaviorizer_test = Behaviorizer("negative", "anger", "politics")

    def test_tuple_contents(self):
        self.assertIsInstance(self.behaviorizer_test.peram_tuple, tuple)
        # TODO: test to make sure the arguments are strings
        self.assertIsInstance(self.behaviorizer_test.peram_tuple[0], str)
        self.assertIsInstance(self.behaviorizer_test.peram_tuple[1], str)
        self.assertIsInstance(self.behaviorizer_test.peram_tuple[2], str)
        # test to make sure the arguments are one of the words I expect.
        self.assertIn(self.behaviorizer_test.peram_tuple[0], ["positive", "negative"])
        self.assertIn(self.behaviorizer_test.peram_tuple[1], ["disgust", "fear", "anger", "happy", "sad"])
        self.assertIn(self.behaviorizer_test.peram_tuple[2], ["financial", "behavioral", "scientific", "educational", "politics", "relationships"])

    def test_json_load(self):
        self.assertIsInstance(self.behaviorizer_test.behavior_dict, dict)
        self.assertIn("('positive', 'happy', 'scientific')", self.behaviorizer_test.behavior_dict)
        self.assertEqual("pregnant.", self.behaviorizer_test.behavior_dict["('negative', 'fear', 'behavioral')"])

    def test_find_prediction(self):
        self.assertEqual(self.behaviorizer_test.predicted_behavior, "discovering benevolent aliens.")
        self.assertEqual(self.another_behaviorizer_test.predicted_behavior, "rioting.")


if __name__ == '__main__':
    unittest.main()
