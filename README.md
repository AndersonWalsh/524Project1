# 524Project1

## Limitations
- RegEx, Python 3.10 libraries only
- Tokenization, Preprocessing, Pipeline
    * Don't do things every time to everything
- Can use pickle files

## Generalized input processing
* assignment specification reflects format of
    - "Describe when the ..." and direct questions "When the ..." or more personal 
    - "Tell me when the ...".

## From input, derive one of
1. Chapter + sentence # of investigator
2. First mention of crime, type and details, chapter + sentence #
3. Chapter + sentence # of perpetrator intro
4. Words, 3 preceding 3 following, of each perpetrator mention
5. Chapter + sentence # of perpetrator + investigator concurrence, how they encounter
6. Chapter + sentence # other suspects introduced

## Project roles:
- “Data finding, preparation and normalization”
- “Data analysis, modeling”
- “Domain specific/background research, literature survey, guide other components”
- “Creativity, novelty, cleverness”

# Project components:
- Data preprocessing
- Input processing
- Extract pertinent information based on input
	
## Data preprocessing
### Applies to both novel and user input
- Normalization
- Equivalence of terms
- Case folding
- Stemming
- Lemmatization
- Purging, cleaning, merging, organization

## Input Processing
- Derive meaning of query, one of
    * Perpetrator
        * Conditionally, words adjacent to perpetrator, no #s
    * Investigator
        * Conditionally investigator perpetrator concurrence + circumstance
    * Crime, type and details
    * Other suspects
- All except conditional perpetrator case requires chapter + sentence #

## Extract Information
- Lexical + relational semantics

# Data Representation
...

# Algorithms, High Level Problem Analysis

## Chapter + Sentence #
- Punctuations indicate sentence #, simple increment
- Assign sentence # ranges to chapter #s
    * upon detection of chapter specification
        * relate floor to last chapter upper sentence # + 1
            * base case of 0 for chapter 1
        * relate ceiling to sentence number prior

### Other detections may be derivable via detection of crime

## Generalizations given context of inquiries
- Crime
    * Detection of class of nouns/verbs indicative of criminal behavior
- All else relates to, what are likely, proper nouns
    * Named entity recognition

## Crime
- Circumstance detection
    * Find instance of crime, likely in verb form with tense
    * Assume circumstance description based on
        * Density of surrounding past/present tense verbs
        * Higher, greater likelihood of circumstance description
        * Possible detection of concurrent nouns/verbs indicative of criminal behavior


## Perpetrator
- Proper noun proximity
    * present/past tense of crime verb

## Investigator
- Proper noun proximity
    * noun form of crime

### Concurrence of above
- Greatest proximity of proper nouns for investigator + perpetrator

# Big idea: analyze novels author-specific, create list of keywords pertaining to above novel aspects
- In spirit of assignment to limit keyword usage somewhat
    * Otherwise, could ostensibly make a hashmap of each novel's characters and their roles
- Keep generalizable to detective novels on the whole to the greatest extent

# Roles:
- Anderson: Input Processing
- Ani: Output Processing
- Data Representation: Alex and Bryson
- Data Extraction: Alex and Bryson

# Availability:
- Anderson: class during Tuesday/Thursday 10AM-2PM