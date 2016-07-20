import unittest
import nltk
from Posterior import *
from Spokenizer import *

# whatever these will be called, they need importing
# from Domainer import *
# from Emotionizer import *
# from Sentimentizer import *

class Test_Spokenizer(unittest.TestCase):
    # Can't test individually for lowercase-ing and list-ifying.
    # Can only test the final output, being sent to the other modules.

    def test_stemmed_list_returns_stemmed_lowercase_word_list(self):
        phrase = Spokenizer("Baked A cake, and Eating it tomorrow")
        self.assertEqual(phrase.parse_sentence(), ['bake', 'a', 'cake', ',', 'and', 'eat', 'it', 'tomorrow'])

    def test_that_domainer_property_was_initialized(self):
        # test_spokenizer = Spokenizer("Duh, a sentence")
        # self.assertIsInstance(test_spokenizer.domainer, Domainer)
        pass

    def test_that_emotionizer_property_was_initialized(self):
        # test_spokenizer = Spokenizer("Here's another!!")
        # self.assertIsInstance(test_spokenizer.emotionizer, Emotionizer)
        pass

    def test_that_sentimentizer_property_was_initialized(self):
        # test_spokenizer = Spokenizer("What up, language?")
        # self.assertIsInstance(test_spokenizer.sentimentizer, Spokenizer)
        pass

if __name__ == '__main__':
    unittest.main()

