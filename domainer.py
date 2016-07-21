from lexicon import *

class Domainer:
    def __init__(self, list_from_str):
        self.sample_list = list_from_str
        self.financial_total = self.financial_counter()
        self.behavioral_total = self.behavioral_counter()
        self.scientific_total = self.scientific_counter()
        self.educational_total = self.educational_counter()
        self.political_total = self.political_counter()
        self.relationships_total = self.relationships_counter()
        self.total_domain_points =self.total_all_domain_points()
        self.highest_domain = None
        self.domain_decimals = self.domain_decimal_math()

    def total_all_domain_points(self):
        self.total = self.financial_total + self.behavioral_total + self.scientific_total + self.educational_total + self.political_total + self.relationships_total

        return self.total


    def financial_counter(self):
        self.financial_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["financial"]])

        return self.financial_count

    def behavioral_counter(self):
        self.behavioral_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["behavioral"]])

        return self.behavioral_count

    def scientific_counter(self):
        self.scientific_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["scientific"]])

        return self.scientific_count

    def educational_counter(self):
        self.educational_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["educational"]])

        return self.educational_count

    def political_counter(self):
        self.political_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["politics"]])
        return self.political_count

    def relationships_counter(self):
        self.relationships_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["relationships"]])
        return self.relationships_count


    def domain_decimal_math(self):
        if self.total_domain_points == 0:
            self.final_domain_values = dict.fromkeys(lexicon.keys(), 0)
        else:

            self.final_domain_values = {
                "financial": self.financial_total / self.total_domain_points,
                "behavioral": self.behavioral_total/self.total_domain_points,
                "scientific": self.scientific_total/self.total_domain_points,
                "educational": self.educational_total/self.total_domain_points,
                "politics": self.political_total/self.total_domain_points,
                "relationships": self.relationships_total/self.total_domain_points
                }


        self.highest_domain = max(self.final_domain_values.keys(), key=(lambda key: self.final_domain_values[key]))
        return self.highest_domain
        print(self.highest_domain)

    def give_me_highest_domain(self):

        return self.highest_domain


    def __str__(self):
           return "this sentence has an domain count of: {0} financial, {1} behavioral, {2} scientific, {3} educational,  {4} politics, and {5} relationships".format(self.final_domain_values["financial"], self.final_domain_values["behavioral"], self.final_domain_values["scientific"], self.final_domain_values["educational"], self.final_domain_values["politics"], self.final_domain_values["relationships"])
