
import messages
import unittest


class Test_analyzer_creation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        sentence_one = Analyzer("This is a test sentence")
        sentence_bad = Analyzer(2)

    def test_that_tokenizer_is_instantiated(self):  # isInstanceOf tokenizer
        pass

    def test_that_initial_sentence_is_string(self):

        self.assertIsInstance(str, self.sentence_one.initial)
        self.assertEqual("This is a test sentence", self.sentence_one.initial)

    def test_printer_of_string_sentence(self):
        pass

    def test_that_behaviorizer_was_also_created(self):


class Test_behaviorizer(unittest.TestCase):

    def test_what_it_receives(self):  # going to be receiving a bunch of little tuples or something.
        pass
    # TODO: loop test through behavior object to find matches
    # TODO: print matches


if __name__ == '__main__':
    unittest.main()

