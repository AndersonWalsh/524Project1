response_templates = {
    "investigator_pair_first_occurrence": [
        "The investigator {name} (or pair) first appears in Chapter {chapter} and Sentence {sentence}.",
        "In Chapter {chapter}, Sentence {sentence}, the investigator {name} (or pair) makes their first appearance.",
        "We first find the investigator {name} (or paie) in Chapter {chapter}, Sentence {sentence}."
    ],

    "first_mention_of_crime": [
        "The crime, which is of type {type_of_crime}, is first mentioned in Chapter {chapter}, Sentence {sentence}. The victim was {victim}.",
        "In Chapter {chapter}, Sentence {sentence}, the crime is first mentioned. It's a {type_of_crime}. The victim in this case was {victim}.",
        "The crime where {victim} was {type_of_crime} was first discussed in Chapter {chapter}, Sentence {sentence}."
    ],

    "first_mention_of_perpetrator": [
        "The perpetrator, whose name is {name}, is first mentioned in Chapter {chapter}, Sentence {sentence}.",
        "{name}, the perpetrator, makes their debut in Chapter {chapter}, Sentence {sentence}.",
        "Chapter {chapter}, Sentence {sentence} -> The first mention of the perpetrator, whose name is {name}."
    ],

    "three_words_around_perpetrator": [
        "In Chapter {chapter}, Sentence {sentence}, the three words preceding perpetrator are: {three_preceding_words} and the three words following perpetrator are: {three_following_words}.",
        "Around the perpetrator's mention in Chapter {chapter}, Sentence {sentence}, we have these words: Before - {three_preceding_words}. After - {three_following_words}.",
        "When looking at the perpetrator's mention in Chapter {chapter}, Sentence {sentence}, the words immediately around are: {three_preceding_words} (before) and {three_following_words} (after)."
    ],

    "detective_perpetrator_cooccurrence": [
        "The detective and perpetrator appear together in Chapter {chapter}, Sentence {sentence}. The verbs that are used to describe are {how}.",
        "Chapter {chapter}, Sentence {sentence} sees the detective and perpetrator in the same scene. Here's how it is described: {how}.",
        "In Chapter {chapter}, Sentence {sentence}, both the detective and perpetrator appear. Here's more information about it: {how}."
    ],

    "other_suspects_first_introduction": [
        "Other suspects are first introduced in Chapter {chapter}, Sentence {sentence}. Here are some details about them: {suspects}.",
        "Chapter {chapter}, Sentence {sentence} is where we first hear about other suspects. They are: {suspects}.",
        "The other suspects are first bought up in Chapter {chapter}, Sentence {sentence}. They are: {suspects}."
    ]
}
