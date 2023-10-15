from response_templates import response_templates
import random

class OutputProcessor:
    
    """ To produce responses in simple English for the analysis related to crime novels."""

    def __init__(self):
        
        self.templates = response_templates
    
    def process_investigator_pair_first_occurrence(self, data) -> str:

        """ first occurrence of the investigator or pair """

        data["name"] = data["name"].title()  # For names
        response = random.choice(self.templates["investigator_pair_first_occurrence"])

        return response.format(**data)
    
    def change_tense(self, verb: str) -> str:

        """ We can add more verbs as required. """

        crime_type_tense = {
            "poisoned": "poisoning",
            "stabbed": "stabbing",
            "shot": "shooting"  
        }
        
        return crime_type_tense.get(verb, verb)

    def process_first_mention_of_crime(self, data) -> str:

        """ for the first mention of the crime """

        data["type_of_crime"] = self.change_tense(data["type_of_crime"])
        data["victim"] = data["victim"].title()  # For victims
        response = random.choice(self.templates["first_mention_of_crime"])
        
        return response.format(**data)

    def process_first_mention_of_perpetrator(self, data) -> str:
        
        """ for the first mention of the perpetrator """
        
        data["name"] = data["name"].title()  # For names
        response = random.choice(self.templates["first_mention_of_perpetrator"])
        return response.format(**data)


    def process_three_words_around_perpetrator(self, data_list) -> str:
        """ preceding and succeeding words around the perpetrator's mention """
        responses = []
        for data in data_list:
            response = random.choice(self.templates["three_words_around_perpetrator"])
            formatted_response = response.format(**data)
            responses.append(formatted_response)

        return "\n".join(responses)

    def process_detective_perpetrator_cooccurrence(self, data) -> str:

        """ for the co-occurrence of detective and perpetrator """
        
        data["how"] = ", ".join(data["how"])
        response = random.choice(self.templates["detective_perpetrator_cooccurrence"])
        return response.format(**data)

    def process_other_suspects_first_introduction(self, data) -> str:
        
        """ for the first introduction of other suspects """
        
         # Ensure that data is in the expected format
        if isinstance(data, dict):
            data = [data]
        elif not data or not isinstance(data, list):
            return "I couldn't find any information on other suspects."

        suspect_intro = []
        for suspect_data in data:

            # Capitalize the suspect's name
            if "type" in suspect_data:
                suspect_data["type"] = suspect_data["type"].title()
            formatted_suspect = f"{suspect_data['type']} in Chapter {suspect_data['chapter']}, Sentence {suspect_data['sentence']}"
            suspect_intro.append(formatted_suspect)

        intro_text = ", ".join(suspect_intro[:-1])
        if len(suspect_intro) > 1:
            intro_text += f", and {suspect_intro[-1]}"
        else:
            intro_text = suspect_intro[0]

        return f"The other suspects were first introduced as follows: {intro_text}."

