import unittest
import nltk
from Posterior import *
from Spokenizer import *

class Test_Spokenizer(unittest.TestCase):

    def test_sentence_converts_to_lower(self):
        test_sentence = Spokenizer("This is A sentence.")
        self.assertEqual(test_sentence.sentence, "this is a sentence.")

    def test_nltk_tokenized_sentence_outputs_a_list(self):
        pass

    def test_that_domainer_was_created(self):
        pass

    def test_that_emotionizer_was_created(self):
        pass

    def test_that_sentimentizer_was_created(self):
        pass


if __name__ == '__main__':
    unittest.main()

