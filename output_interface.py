class OutputInterface:

    """ This file has interfaces for the analysis that we're doing on the crime novels. This will be used to create the output. """

    def investigator_pair_first_occurrence(name: str=None, chapter: int=None, sentence: int=None) -> dict:

        """ This has details about the first occurrence of the investigator (or pair). """
        return {
            "name": name,
            "chapter": chapter,
            "sentence": sentence,
        }

    def first_mention_of_crime(chapter: int=None, sentence: int=None, type_of_crime: str=None, details: str = None) -> dict:

        """ This has details about the first mention of the crime. """

        return {
            "chapter": chapter,
            "sentence": sentence,
            "type_of_crime": type_of_crime,
            "details": details    
        }

    def first_mention_of_perpetrator(name: str = None, chapter: int = None, sentence: int = None) -> dict:

        """ This has details about the first mention of the perpetrator. """
        
        return {
            "name": name,
            "chapter": chapter,
            "sentence": sentence,
        }
    
    def three_words_around_perpetrator(chapter: int = None, sentence: int = None, perpetrator: str = None, three_preceding_words: list = None, three_following_words: list = None) -> dict:
        
        """ This has details about the three words that re present before and after the perpetrator. """

        return {
            "chapter": chapter,
            "sentence": sentence,
            "perpetrator": perpetrator,
            "three_preceding_words": three_preceding_words or [],
            "three_following_words": three_following_words or []
        }

    def detective_perpetrator_cooccurrence(chapter: int = None, sentence: int = None, how: list = None) -> dict:

        """  This has details about the instance where the detective and perpetrator appear together. """

        return {
            "chapter": chapter,
            "sentence": sentence,
            "how": how or []

        }
    
    def other_suspects_first_introduction(chapter: int = None, sentence: int = None, suspects: list = None) -> dict:

        """ This has details about the first appearance introduction of other suspects. """

        return {
            "chapter": chapter,
            "sentence": sentence,
            "suspects": suspects or []
        }