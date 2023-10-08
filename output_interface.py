class OutputInterface:

    def investigator_pair_first_occurrence(chapter: int=None, sentence: int=None) -> dict:

        return
        {
            "type": "investigator_pair_first_occurrence",
            "chapter": None,
            "sentence": None,
        }

    def first_mention_of_crime(chapter: int=None, sentence: int=None, type_of_crime: str=None, details: str = None) -> dict:

        return
        {
            "type": "first_mention_of_crime",
            "chapter": chapter,
            "sentence": sentence,
            "type_of_crime": type_crime,
            "details": details    
        }

    def first_mention_of_perpetrator(chapter: int = None, sentence: int = None) -> dict:
        
        return 
        {
            "type": "first_mention_of_perpetrator",
            "chapter": chapter,
            "sentence": sentence,
        }
    
    def three_words_around_perpetrator(chapter: int = None, sentence: int = None, three_preceding_words: list = None, three_following_words: list = None) -> dict:
        
        return 
        {
            "type": "three_words_around_perpetrator",
            "chapter": chapter,
            "sentence": sentence,
            "three_preceding_words": preceding_words or [],
            "three_following_words": following_words or []
        }

    def detective_perpetrator_cooccurrence(chapter: int = None, sentence: int = None) -> dict:

        return 
        {
            "type": "detective_perpetrator_cooccurrence",
            "chapter": chapter,
            "sentence": sentence,
        }
    
    def other_suspects_first_introduction(chapter: int = None, sentence: int = None, suspects: list = None) -> dict:
        return 
        {
            "type": "other_suspects_first_introduction",
            "chapter": chapter,
            "sentence": sentence,
            "suspects": suspects or []
        }