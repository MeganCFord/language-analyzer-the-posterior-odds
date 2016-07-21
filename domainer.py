from lexicon import *

class Domainer:
    def __init__(self, list_from_str):
        self.sample_list = list_from_str
        # counters for how many points each domain gets in a sentence)
        self.financial_total = self.financial_counter()
        self.behavioral_total = self.behavioral_counter()
        self.scientific_total = self.scientific_counter()
        self.educational_total = self.educational_counter()
        self.political_total = self.political_counter()
        self.relationships_total = self.relationships_counter()
        # total of all the points from the above counters.
        self.total_domain_points = self.total_all_domain_points()
        # dictionary of the counter values vs the total number of points assigned.
        self.domain_decimals = self.domain_decimal_math()
        # a string of the highest domain value, to be used in the behaviorizer.
        self.highest_domain = self.find_highest_domain()

        #prints as part of init.
        print("this sentence has an domain count of: {0} financial, {1} behavioral, {2} scientific, {3} educational,  {4} politics, and {5} relationships".format(self.domain_decimals["financial"], self.domain_decimals["behavioral"], self.domain_decimals["scientific"], self.domain_decimals["educational"], self.domain_decimals["politics"], self.domain_decimals["relationships"]))

    def total_all_domain_points(self):
        self.total = self.financial_total + self.behavioral_total + self.scientific_total + self.educational_total + self.political_total + self.relationships_total

        return self.total


    def financial_counter(self):
        """
        The financial_counter adds a 1 for each word in the list passed in that matches the financial lexicon and then adds them together, stores and returns the total of 1s added to financial_count
        """
        self.financial_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["financial"]])

        return self.financial_count

    def behavioral_counter(self):
        """
        The behavioral_counter adds a 1 for each word in the list passed in that matches the behavioral lexicon and then adds them together, stores and returns the total of 1s added to behavioral_count
        """
        self.behavioral_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["behavioral"]])

        return self.behavioral_count

    def scientific_counter(self):
        """
        The scientific_counter adds a 1 for each word in the list passed in that matches the scientific lexicon and then adds them together, stores and returns the total of 1s added to scientific_count
        """
        self.scientific_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["scientific"]])

        return self.scientific_count

    def educational_counter(self):
        """
        The educational_counter adds a 1 for each word in the list passed in that matches the educational lexicon and then adds them together, stores and returns the total of 1s added to educational_count
        """
        self.educational_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["educational"]])

        return self.educational_count

    def political_counter(self):
        """
        The political_counter adds a 1 for each word in the list passed in that matches the political lexicon and then adds them together, stores and returns the total of 1s added to political_count
        """
        self.political_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["politics"]])
        return self.political_count

    def relationships_counter(self):
        """
        The relationships_counter adds a 1 for each word in the list passed in that matches the relationship lexicon and then adds them together, stores and returns the total of 1s added to relationships_count
        """
        self.relationships_count = sum([1 for word in self.sample_list
            if word in lexicon["domain"]["relationships"]])
        return self.relationships_count

    def domain_decimal_math(self):
        """
        This function first checks to see if the total domain points is at zero, if so, it creates a dictionary where the keys are the different domains and the values are set to zero. Else, it takes the total from from each counter and divides that number by the total of ALL of the counters and returns the final domain values as a decimal
        """
        if self.total_domain_points == 0:
            self.final_domain_values = {
                "financial": 0,
                "behavioral": 0,
                "scientific": 0,
                "educational": 0,
                "politics": 0,
                "relationships": 0
            }
        else:
            self.final_domain_values = {
                "financial": self.financial_total / self.total_domain_points,
                "behavioral": self.behavioral_total/self.total_domain_points,
                "scientific": self.scientific_total/self.total_domain_points,
                "educational": self.educational_total/self.total_domain_points,
                "politics": self.political_total/self.total_domain_points,
                "relationships": self.relationships_total/self.total_domain_points
                }

        return self.final_domain_values

    def find_highest_domain(self):


        """
        This function is getting the domain with the highest count and storing and returning the answer to self.final_domain_values.
        """
        self.highest_domain = max(self.final_domain_values.keys(), key=(lambda key: self.final_domain_values[key]))
        return self.highest_domain


    def __str__(self):
        """
        This is the a string of all of the information that we need from this class Domainer and can be printed in the terminal when importing Domainer
        """
        return "this sentence has an domain count of: {0} financial, {1} behavioral, {2} scientific, {3} educational,  {4} politics, and {5} relationships".format(self.domain_decimals["financial"], self.domain_decimals["behavioral"], self.domain_decimals["scientific"], self.domain_decimals["educational"], self.domain_decimals["politics"], self.domain_decimals["relationships"])
