from response_templates import response_templates

class OutputProcessor:
    
    """ To produce responses in simple English for the analysis related to crime novels."""

    def __init__(self):
        
        self.templates = response_templates
    
    def process_investigator_pair_first_occurrence(self, data) -> str:

        """ first occurrence of the investigator or pair """

        return self.templates["investigator_pair_first_occurrence"].format(**data)

    def process_first_mention_of_crime(self, data) -> str:

        """ for the first mention of the crime """

        return self.templates["first_mention_of_crime"].format(**data)

    def process_first_mention_of_perpetrator(self, data) -> str:
        
        """ for the first mention of the perpetrator """
        
        return self.templates["first_mention_of_perpetrator"].format(**data)

    def process_three_words_around_perpetrator(self, data) -> str:
        
        """ preceding and succeeding words around the perpetrator's mention """
        
        return self.templates["three_words_around_perpetrator"].format(**data)

    def process_detective_perpetrator_cooccurrence(self, data) -> str:

        """ for the co-occurrence of detective and perpetrator """
        
        data["how"] = ", ".join(data["how"])
        return self.templates["detective_perpetrator_cooccurrence"].format(**data)

    def process_other_suspects_first_introduction(self, data) -> str:
        
        """ for the first introduction of other suspects """
        
        return self.templates["other_suspects_first_introduction"].format(**data)

