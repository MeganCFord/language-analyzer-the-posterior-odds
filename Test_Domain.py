import unittest
from Posterior import *

class Test_domainer(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        self.original_list = ['apple']

    def test_what_it_receives_is_a_list(self):
        sample_list = Domainer(self.original_list)
        self.assertIsInstance(sample_list.sample_list, list)

    def test_financial_counter(self):
        money_list = Domainer(["this","is","a","money","test"])
        self.assertEqual(money_list.financial_counter(), 1)
        money_list2 = Domainer(['money','money'])
        self.assertEqual(money_list2.financial_counter(), 2)

    def test_behavioral_counter(self):
        behavioral_list = Domainer(["this", "is", "a", "behavior", "test"])
        self.assertEqual(behavioral_list.behavioral_counter(), 1)
        behavioral_list2 = Domainer(['acting', 'crazy'])
        self.assertEqual(behavioral_list2.behavioral_counter(), 2)

    def test_scientific_counter(self):
        scientific_list = Domainer(["this", "is", "a", "scientific", "test"])
        self.assertEqual(scientific_list.scientific_counter(), 1)
        scientific_list2 = Domainer(['aliens', 'aliens', 'aliens'])
        self.assertEqual(scientific_list2.scientific_counter(), 3)

    def test_educational_counter(self):
        educational_list = Domainer(["this", "is", "a", "smart", "test"])
        self.assertEqual(educational_list.educational_counter(), 1)
        educational_list2 = Domainer(['smart', 'learning'])
        self.assertEqual(educational_list2.educational_counter(), 2)

    def test_politics_counter(self):
        political_list = Domainer(["this", "is", "a", "political", "test"])
        self.assertEqual(political_list.political_counter(), 1)
        political_list2 = Domainer(['leader', 'rules', 'law'])
        self.assertEqual(political_list2.political_counter(), 3)

    def test_relationships_counter(self):
        relationships_list = Domainer(["this", "is", "a", "relational", "test"])
        self.assertEqual(relationships_list.relationships_counter(), 1)
        relationships_list2 = Domainer(['people', 'relative', 'mother'])
        self.assertEqual(relationships_list2.relationships_counter(), 3)

    def test_list_returns_domain(self):
        this_list1 = Domainer(['money', 'money', 'money', 'aliens'])
        self.assertEqual(this_list1.domain_decimal_math(), "financial")
        this_list2 = Domainer(['money', 'aliens', 'aliens', 'aliens'])
        self.assertEqual(this_list2.domain_decimal_math(), "scientific" )
        this_list3 = Domainer(['eat', 'eat', 'eat' ,'aliens'])
        self.assertEqual(this_list3.domain_decimal_math(), "behavioral" )
        this_list4 = Domainer(['school', 'school', 'school', 'aliens'])
        self.assertEqual(this_list4.domain_decimal_math(), "educational" )
        this_list5 = Domainer(['leader', 'congress', 'leader', 'aliens'])
        self.assertEqual(this_list5.domain_decimal_math(), "politics" )
        this_list6 = Domainer(['people', 'people', 'people', 'aliens'])
        self.assertEqual(this_list6.domain_decimal_math(), "relationships" )






if __name__ == '__main__':
    unittest.main()



