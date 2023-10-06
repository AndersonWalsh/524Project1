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

# Metadata for Novels

## The Murder on the Links:
* Crime: murder (victim Paul Renauld)
    - stabbing
    - knife
* Investigator: Giraud and Hercule Poirot (possibly Hastings)
* Criminal: Marthe Daubreuil
* Suspects: Jack, Bella Duveen

## The Sign of the Four:
* Crime: theft, murder (bit unclear, it's a Holmes novel)
    - Multiple victims arguably, Bartholomew of murder, Sholto death by shock
    - One indirect "murder", another more active murder
    - A lot of nuance 
* Investigator: Holmes, Watson
* Criminal: Tonga (murder), Small (prison escape, conspiracy?), Sholto (theft)
* Suspects: Arthur Morstan, Jonathan Small, Thaddeus

## The Mysterious Affair at Styles
* Crime: Murder (victim Emily Inglethorp)
    - Poisoning (strychnine)
* Investigator: Arthur Hastings, Hercule Poirot
* Criminal: Alfred Inglethorp (accomplice Evelyn Howard)
* Suspects: Alfred Inglethorp, Evelyn Howard, Cynthia Murdoch, Mary Cavendish, Lawrence Cavendish, John Cavendish

# Roles:
- Anderson: Input Processing
- Ani: Output Processing
- Data Representation: Alex and Bryson
- Data Extraction: Alex and Bryson

# Availability:
- Anderson: class during Tuesday/Thursday 10AM-2PM
- Alex:
    * Available after 11:30 Monday, Friday
    * Available after 2:30 Tuesday
    * Available between 11:30 - 1:30 Wednesday
    * Available between 2:30-5 Thursday
- Bryson: Available after 10 on MW, after 11:30 on F, and before 3 on TR.

- Anirudh:
	It's easier for me to give  my available timings, and here they are.

	* Monday (10/2): 9am-10:30am & 3:00pm-5:30pm
	* Tuesday (10/3): 2:30pm-7:30pm
	* Wednesday (10/4): 9am-10:30am & 4pm - 7:30pm
	* Thursday (10/5): 2:30pm-7:30pm
	* Friday (10/6): 10am - 7:30pm

# 10/6/23 Meeting 2 Notes

## Agenda
- Standup for individual progress so far
- Work moving forward for each project component
- Timeline
### Discussion
- Have preprocessing done, data structure of lists, per book, indexed by book chapter, each index has text of book
    * sentence list has indexes that are also chapters, but each index is a nested list containing each sentence as a separate string
- 6 functions to answer questions
- preprocess text on boot
- answer questions per prompt
- high level structure being implemented by Bryson, OOP
- Input processing implemented at baseline
- Answer extraction
    * Chapter and sentence # derived from data structures by linear search: questions 1, 3, 6
### Next Steps
- Input processing just needs QA testing
- For data preprocessing, implement paragraph separation (stretch goal)
- Answer extraction WIP
    * Andy: question 5 concurrence case
        * How many words within anchor does perpetrator occur, look within certain num words, or paragraph representation
        * Capture shared sentences as a baseline, action verbs
    * Bryson: Prompt 2, code structuring, and main() code
        * Crime type, method, victim, possibly setting (person, place, thing)
    * Alex: Finish prompts 1, 3, and 6; prompt 4
- Ani is going to define an interface he anticipates for output, based on that interface create output
    * Data team will use that model once completed
- Next meeting: Wednesday, 1PM
    * Code done, fully functional Friday
    * Presentation done over the weekend
        * 10 minute script
        * Presentation slides
        * 2 page report
- Last meeting: Sunday, time TBD