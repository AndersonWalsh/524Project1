
from output_interface import OutputInterface
from response_templates import response_templates

class OutputProcessor:
    
    """ To produce responses in simple English for the analysis related to crime novels."""

    def __init__(self):
        
        self.interface = OutputInterface()
        self.templates = response_templates
    
    def process_investigator_pair_first_occurrence(self, name: str, chapter: int, sentence: int) -> str:

        """ first occurrence of the investigator or pair """

        data = self.interface.investigator_pair_first_occurrence(name, chapter, sentence)
        return self.templates["investigator_pair_first_occurrence"].format(**data)

    def process_first_mention_of_crime(self, chapter: int, sentence: int, type_of_crime: str, details: str) -> str:

        """ for the first mention of the crime """

        data = self.interface.first_mention_of_crime(chapter, sentence, type_of_crime, details)
        return self.templates["first_mention_of_crime"].format(**data)

    def process_first_mention_of_perpetrator(self, name: str, chapter: int, sentence: int) -> str:
        
        """ for the first mention of the perpetrator """
        
        data = self.interface.first_mention_of_perpetrator(name, chapter, sentence)
        return self.templates["first_mention_of_perpetrator"].format(**data)

    def process_three_words_around_perpetrator(self, chapter: int, sentence: int, three_preceding_words: list, three_following_words: list) -> str:
        
        """ preceding and succeeding words around the perpetrator's mention """
        
        data = self.interface.three_words_around_perpetrator(chapter, sentence, three_preceding_words, three_following_words)
        return self.templates["three_words_around_perpetrator"].format(**data)

    def process_detective_perpetrator_cooccurrence(self, chapter: int, sentence: int, how: list) -> str:

        """ for the co-occurrence of detective and perpetrator """
        
        data = self.interface.detective_perpetrator_cooccurrence(chapter, sentence, how)
        data["how"] = ", ".join(data["how"])
        return self.templates["detective_perpetrator_cooccurrence"].format(**data)

    def process_other_suspects_first_introduction(self, chapter: int, sentence: int, suspects: list) -> str:
        
        """ for the first introduction of other suspects """
        
        data = self.interface.other_suspects_first_introduction(chapter, sentence, suspects)
        return self.templates["other_suspects_first_introduction"].format(**data)

