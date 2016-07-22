import unittest
from Posterior import *


class Test_posterior(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sentence_one = Posterior("In the country of Sokovia, the Avengers – Tony Stark, Steve Rogers, Thor, Bruce Banner, Natasha Romanoff, and Clint Barton – raid a Hydra outpost led by Wolfgang von Strucker, who has been experimenting on humans using the scepter previously wielded by Loki. They encounter two of Strucker's experiments – twins Pietro, who has superhuman speed, and Wanda Maximoff, who can manipulate minds and project energy – and apprehend Strucker, while Stark retrieves Loki's scepter.")

    def test_that_initial_sentence_is_string(self):
        self.assertIsInstance(self.sentence_one.initial, str)
        self.assertEqual("In the country of Sokovia, the Avengers – Tony Stark, Steve Rogers, Thor, Bruce Banner, Natasha Romanoff, and Clint Barton – raid a Hydra outpost led by Wolfgang von Strucker, who has been experimenting on humans using the scepter previously wielded by Loki. They encounter two of Strucker's experiments – twins Pietro, who has superhuman speed, and Wanda Maximoff, who can manipulate minds and project energy – and apprehend Strucker, while Stark retrieves Loki's scepter.", self.sentence_one.initial)

    def test_stringification_of_initial_sentence_edge_cases(self):
        self.number_sentence = Posterior(23)
        self.list_sentence = Posterior(["hey", "nope"])
        self.assertIsInstance(self.number_sentence.initial, str)
        self.assertIsInstance(self.list_sentence.initial, str)
        self.assertEqual(self.number_sentence.initial, "23")
        self.assertEqual(self.list_sentence.initial, "['hey', 'nope']")

    def test_that_behaviorizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.predicted_behavior, Behaviorizer)

    def test_that_spokenizer_is_instantiated(self):
        self.assertIsInstance(self.sentence_one.spokenizer, Spokenizer)



class Test_behaviorizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.behaviorizer_test = Posterior("yes happy science")
        self.another_behaviorizer_test = Posterior("no angry politics")

    def test_tuple_contents(self):
        self.assertIsInstance(self.behaviorizer_test.predicted_behavior.peram_list, list)
        # TODO: test to make sure the arguments are strings
        self.assertIsInstance(self.behaviorizer_test.predicted_behavior.peram_list[0], str)
        self.assertIsInstance(self.behaviorizer_test.predicted_behavior.peram_list[1], str)
        self.assertIsInstance(self.behaviorizer_test.predicted_behavior.peram_list[2], str)
        # test to make sure the arguments are one of the words I expect.
        self.assertIn(self.behaviorizer_test.predicted_behavior.peram_list[0], ["positive", "negative"])
        self.assertIn(self.behaviorizer_test.predicted_behavior.peram_list[1], ["disgust", "fear", "anger", "happy", "sad"])
        self.assertIn(self.behaviorizer_test.predicted_behavior.peram_list[2], ["financial", "behavioral", "scientific", "educational", "politics", "relationships"])

    def test_json_load(self):
        self.assertIsInstance(self.behaviorizer_test.predicted_behavior.behavior_dict, dict)
        self.assertIn("['positive', 'happy', 'scientific']", self.behaviorizer_test.predicted_behavior.behavior_dict)
        self.assertEqual("pregnant.", self.behaviorizer_test.predicted_behavior.behavior_dict["['negative', 'fear', 'behavioral']"])

    def test_find_prediction(self):
        self.assertEqual(self.behaviorizer_test.predicted_behavior.prediction, "discovering benevolent aliens.")
        self.assertEqual(self.another_behaviorizer_test.predicted_behavior.prediction, "rioting.")


if __name__ == '__main__':
    unittest.main()
