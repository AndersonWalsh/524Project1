from response_templates import response_templates
import random

class OutputProcessor:
    
    """ To produce responses in simple English for the analysis related to crime novels."""

    def __init__(self):
        
        self.templates = response_templates
    
    def process_investigator_pair_first_occurrence(self, data) -> str:

        """ first occurrence of the investigator or pair """

        response = random.choice(self.templates["investigator_pair_first_occurrence"])
        return response.format(**data)

    def process_first_mention_of_crime(self, data) -> str:

        """ for the first mention of the crime """

        response = random.choice(self.templates["first_mention_of_crime"])
        return response.format(**data)

    def process_first_mention_of_perpetrator(self, data) -> str:
        
        """ for the first mention of the perpetrator """
        
        response = random.choice(self.templates["first_mention_of_perpetrator"])
        return response.format(**data)

    def process_three_words_around_perpetrator(self, data) -> str:
        
        """ preceding and succeeding words around the perpetrator's mention """
        
        response = random.choice(self.templates["three_words_around_perpetrator"])
        return response.format(**data)

    def process_detective_perpetrator_cooccurrence(self, data) -> str:

        """ for the co-occurrence of detective and perpetrator """
        
        data["how"] = ", ".join(data["how"])
        response = random.choice(self.templates["detective_perpetrator_cooccurrence"])
        return response.format(**data)

    def process_other_suspects_first_introduction(self, data) -> str:
        
        """ for the first introduction of other suspects """
        
        response = random.choice(self.templates["other_suspects_first_introduction"])
        return response.format(**data)

