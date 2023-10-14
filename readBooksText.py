#Alex S

from bs4 import BeautifulSoup
import requests, re
import os
#import matplotlib.pyplot as plt, matplotlib.ticker
import csv 
from collections import Counter
import identities
from output_interface import OutputInterface


# Murder of the links uses numeric chapter numbers with chapter names
# Other two books have the same format for the chapters (Roman numerals)
CHAPTER_KEYWORDS = ('chapter i\W', 'chapter ii\W', 'chapter iii\W', 'chapter iv\W','chapter v\W','chapter vi\W','chapter vii\W', 'chapter viii\W', 
                   'chapter ix\W', 'chapter x\W', 'chapter xi\W', 'chapter xii\W', 'chapter xiii\W')

CHAPTER_KEYWORDS_THE_MURDER_ON_THE_LINKS = (
'1\W*.\W*.ellow\W*.raveller',
'2\W*.n\W*.ppeal\W*.or\W*.elp',
'3\W*.t\W*.he\W*.illa\W*.enevi..ve',
'4\W*.he\W*.etter\W*.igned\W*..ella.',
'5\W*.rs.\W*.enauld.s\W*.tory',
'6\W*.he\W*.cene\W*.f\W*.he\W*.rime',
'7\W*.he\W*.ysterious\W*.adame\W*.aubreuil',
'8\W*.n\W*.nexpected\W*.eeting',
'9\W*..\W*.iraud\W*.inds\W*.ome\W*.lues',
'10\W*.abriel\W*.tonor',
'11\W*.ack\W*.enauld',
'12\W*.oirot\W*.lucidates\W*.ertain\W*.oints',
'13\W*.he\W*.irl\W*.ith\W*.he\W*.nxious\W*.yes',
'14\W*.he\W*.econd\W*.ody',
'15\W*.\W*.hotograph',
'16\W*.he\W*.eroldy\W*.ase',
'17\W*.e\W*.ake\W*.urther\W*.nvestigations',
'18\W*.iraud\W*.cts',
'19\W*.\W*.se\W*.y\W*.rey\W*.ells',
'20\W*.n\W*.mazing\W*.tatement',
'21\W*.ercule\W*.oirot\W*.n\W*.he\W*.ase!',
'22\W*.\W*.ind\W*.ove',
'23\W*.ifficulties\W*.head',
'24\W*.ave\W*.im!.',
'25\W*.n\W*.nexpected\W*...nouement',
'26\W*.\W*.eceive\W*.\W*.etter',
'27\W*.ack\W*.enauld.s\W*.tory',
'28\W*.ourney.s\W*.nd')


def CheckFileExists (filename):
    return (os.path.exists(filename))

def Identities__FindOccurencesInText (identitiesList, sentences): # pass an idendtities list
        RelevantSentencesData = []
        for identity in identitiesList:
            for chapterIndex in range (0,len(sentences)):
                for sentenceIndex in range (0, len(sentences[chapterIndex])):
                    if (identity in sentences[chapterIndex][sentenceIndex]):
                        RelevantSentencesData.append ((identity, chapterIndex+1, sentenceIndex+1 ))
                        #print ("character ", identity, " occured in chapter ", chapterIndex+1, " in sentence number " , sentenceIndex+1)
        return RelevantSentencesData

def FindThreeWordsAround (identitiesList, sentences):
    PrecedingFollowingThreeWords = []
    for identity in identitiesList:
        for chapterIndex in range (0,len(sentences)):
            for sentenceIndex in range (0, len(sentences[chapterIndex])):
                if (identity in sentences[chapterIndex][sentenceIndex]):
                    sentence = sentences[chapterIndex][sentenceIndex]
                    splitSentence = sentence.split(identity)
                    precedingWords = splitSentence[0].split()
                    preceding3Words = precedingWords[-3:]
                    preceding3WordsJoined = ' '.join(preceding3Words)
                    #print (preceding3WordsJoined)

                    followingWords = splitSentence[1].split()
                    following3Words = followingWords[:3]
                    following3WordsJoined = ' '.join(following3Words)

                    PrecedingFollowingThreeWords.append ((preceding3WordsJoined, identity, following3WordsJoined,chapterIndex+1, sentenceIndex+1 ))
                    PrecedingFollowingThreeWords.sort(key=lambda x: x[1])
                    #print ("character ", identity, " occured in chapter ", chapterIndex+1, " in sentence number " , sentenceIndex+1)
    return PrecedingFollowingThreeWords



class NovelProcessing:
    def __init__(self):

        self.cur_novel_id = 0
        # Init novel full text as empty strs
        self.FullText__MysteriousAffair = ''
        self.FullText__TheSignOfTheFour = ''
        self.FullText__TheMurderOnTheLinks = ''

        # Init list of novel chapters as empty lists
        self.ChapterText__MysteriousAffair = []
        self.ChapterText__TheSignOfTheFour = []
        self.ChapterText__TheMurderOnTheLinks = []

        # Init list of novel chapters, whose each value will hold a list of the sentences in the given chapter index, as empty lists
        self.SentencesText__MysteriousAffair = []
        self.SentencesText__TheSignOfTheFour = []
        self.SentencesText__TheMurderOnTheLinks = []

        # Sets all object variables above to correct values when object is created
        for i in range(3):
            self.cur_novel_id = i
            self.getSentencesText()


    # Make Project Gutenberg requests to get novel text and (re)generate novel clean text files
    def redownloadRegenerateCleanedTextFiles(self):
        BookList = []
        WebsiteList = []

        with open("./sitesToScrap.csv", newline='') as csvfile:
            linkReader = csv.reader(csvfile)
            for line in linkReader:
                website = line[0]
                bookName = line[1]
                BookList.append(bookName)
                WebsiteList.append(website)

        #retreive words from all books
        allbooks = len(WebsiteList)
        for i in range (allbooks):
            cleanedBook = str(BookList[i]) + "CLEANED.txt"
            file = open (str(cleanedBook), 'w')
            #print ("file does not exist | regeneration requested -> clean the text and create a new file")
            print ("Processing book text for "+ str(BookList[i]))

            r = requests.get(WebsiteList[i])
            soup = BeautifulSoup(r.text, 'html.parser')
            textExtracted = soup.get_text().lower()

            #start to end headers cleanup
            list_begin = textExtracted.split(str("*** START OF THE PROJECT GUTENBERG EBOOK ").lower())
            if (len(list_begin)>1):
                begin_book_text = list_begin[1].split(" ***\n")
                textExtracted = begin_book_text[1].split("*** end")
                textExtracted = textExtracted[0]

            textExtracted = textExtracted.replace("—"," ")

            wordsInBook = re.split("\s+", textExtracted)#long dash taken care of

            for j in range (len(wordsInBook)):
                wordsInBook[j] = re.sub('[][,"&|:@,<>()*$\\/;=”“‘]', "", wordsInBook[j])# REMOVED . AND ! AND ? TO SEPARATE INTO SENTENCES
                wordsInBook[j] = re.sub('^[0-9\.]*$', "", wordsInBook[j])

                file.write (str(wordsInBook[j]) + " ")
            file.close()


    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), return its full text as a single string
    def getFullText(self):
        
        if(self.cur_novel_id == 0):
            if(self.FullText__MysteriousAffair == ''):

                if(not CheckFileExists('TheMysteriousAffairAtStylesCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheMysteriousAffairAtStylesCLEANED.txt", 'r') as file:
                    self.FullText__MysteriousAffair = file.read()
            
            return self.FullText__MysteriousAffair
        
        elif(self.cur_novel_id == 1):
            if(self.FullText__TheSignOfTheFour == ''):

                if(not CheckFileExists('TheSignOfTheFourCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheSignOfTheFourCLEANED.txt", 'r') as file:
                    self.FullText__TheSignOfTheFour = file.read()
            
            return self.FullText__TheSignOfTheFour
        
        elif(self.cur_novel_id == 2):
            if(self.FullText__TheMurderOnTheLinks == ''):

                if(not CheckFileExists('TheMurderOnTheLinksCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheMurderOnTheLinksCLEANED.txt", 'r') as file:
                    self.FullText__TheMurderOnTheLinks = file.read()
            
            return self.FullText__TheMurderOnTheLinks
        
        return None


    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), return ALL of its chapters as a list of strings (each string is the text for a full chapter)
    def getChaptersText(self):

        if(self.cur_novel_id == 0 and self.ChapterText__MysteriousAffair):
            return self.ChapterText__MysteriousAffair
        elif(self.cur_novel_id == 1 and self.ChapterText__TheSignOfTheFour):
            return self.ChapterText__TheSignOfTheFour
        elif(self.cur_novel_id == 2 and self.ChapterText__TheMurderOnTheLinks):
            return self.ChapterText__TheMurderOnTheLinks

        if(self.cur_novel_id == 0 or self.cur_novel_id == 1):
            chaptersPattern = '|'.join(CHAPTER_KEYWORDS)
        elif(self.cur_novel_id == 2):
            chaptersPattern = '|'.join(CHAPTER_KEYWORDS_THE_MURDER_ON_THE_LINKS)

        chapters = re.split(chaptersPattern, self.getFullText())

        if(self.cur_novel_id == 0):
            for i in range (14,len(chapters)): # I know how many chapters there are
                self.ChapterText__MysteriousAffair.append(chapters[i])
            return self.ChapterText__MysteriousAffair
        elif(self.cur_novel_id == 1):
            for i in range (13,len(chapters)): # I know how many chapters there are
                self.ChapterText__TheSignOfTheFour.append(chapters[i])
            return self.ChapterText__TheSignOfTheFour
        elif(self.cur_novel_id == 2):
            for i in range (1,len(chapters)): # I know how many chapters there are
                self.ChapterText__TheMurderOnTheLinks.append(chapters[i])
            return self.ChapterText__TheMurderOnTheLinks

        return None
    

    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), return ALL of its sentences as a list of lists of strings (Outside list is keyed on chapter, inside lists are keyed on sentence number relative to the start of the chapter, each value of inside lists is a single sentence)
    def getSentencesText(self):
        separators = ['.', '?', '!']
        pattern = '|'.join(map(re.escape, separators))
        novelChapters = self.getChaptersText()

        if(self.cur_novel_id == 0):

            if(not self.SentencesText__MysteriousAffair):
                for chapterNumber in range (0,len(novelChapters)):
                    novelChaptersAbbrevReplaced = re.sub(r'([aApP])\.([mM])\.', r'\1<tmp_prd>\2<tmp_prd>', novelChapters[chapterNumber])
                    novelChaptersAbbrevReplaced = re.sub(r'(\W)(mr|mrs|ms|dr|st|m|prof|capt|cpt|lt|mme|mlle)\.', r'\1\2<tmp_prd>', novelChaptersAbbrevReplaced)
                    chapterSentences = re.split(pattern, novelChaptersAbbrevReplaced)
                    for i, sent in enumerate(chapterSentences):
                        chapterSentences[i] = sent.replace('<tmp_prd>', '.')
                    self.SentencesText__MysteriousAffair.append (chapterSentences)

            return self.SentencesText__MysteriousAffair
        
        elif(self.cur_novel_id == 1):

            if(not self.SentencesText__TheSignOfTheFour):
                for chapterNumber in range (0,len(novelChapters)):
                    novelChaptersAbbrevReplaced = re.sub(r'([aApP])\.([mM])\.', r'\1<tmp_prd>\2<tmp_prd>', novelChapters[chapterNumber])
                    novelChaptersAbbrevReplaced = re.sub(r'(\W)(mr|mrs|ms|dr|st|m|prof|capt|cpt|lt|mme|mlle)\.', r'\1\2<tmp_prd>', novelChaptersAbbrevReplaced)
                    chapterSentences = re.split(pattern, novelChaptersAbbrevReplaced)
                    for i, sent in enumerate(chapterSentences):
                        chapterSentences[i] = sent.replace('<tmp_prd>', '.')
                    self.SentencesText__TheSignOfTheFour.append (re.split(pattern, novelChapters[chapterNumber]))

            return self.SentencesText__TheSignOfTheFour
        
        elif(self.cur_novel_id == 2):

            if(not self.SentencesText__TheMurderOnTheLinks):
                for chapterNumber in range (0,len(novelChapters)):
                    novelChaptersAbbrevReplaced = re.sub(r'([aApP])\.([mM])\.', r'\1<tmp_prd>\2<tmp_prd>', novelChapters[chapterNumber])
                    novelChaptersAbbrevReplaced = re.sub(r'(\W)(mr|mrs|ms|dr|st|m|prof|capt|cpt|lt|mme|mlle)\.', r'\1\2<tmp_prd>', novelChaptersAbbrevReplaced)
                    chapterSentences = re.split(pattern, novelChaptersAbbrevReplaced)
                    for i, sent in enumerate(chapterSentences):
                        chapterSentences[i] = sent.replace('<tmp_prd>', '.')
                    self.SentencesText__TheMurderOnTheLinks.append (re.split(pattern, novelChapters[chapterNumber]))

            return self.SentencesText__TheMurderOnTheLinks
        
        return None

    
    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), answer the question: When does the investigator (or a pair) occur for the first time -  chapter #, the sentence(s) # in a chapter
    # Return value is TBD (likely determined by Ani's output format)
    def answer1(self):
        sentences = self.getSentencesText()
        InvestigatorSentencesData = []
        
        if(self.cur_novel_id == 0):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__MysteriousAffair, sentences)
        elif(self.cur_novel_id == 1):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__SignOfTheFour, sentences)
        elif(self.cur_novel_id == 2):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__murderOnTheLinks, sentences)
        return OutputInterface.investigator_pair_first_occurrence(InvestigatorSentencesData[0][0], InvestigatorSentencesData[0][1], InvestigatorSentencesData[0][2])
    
    def answer2(self):
        
        # The Mysterious Affair At Styles
            # Correct sentence for first mention of victim+death: Inglethorp cried out in a strangled voice, her eyes fixed on the doctor: “Alfred—Alfred——” Then she fell back motionless on the pillows
            # Correct sentence for first mention of cause of death: I believe she has been poisoned! I’m certain Dr. Bauerstein suspects it
            # Both in chapter 3

        # The Sign of the Four
            # Correct sentence for first mention of death: It means murder,” said he, stooping over the dead man [chapter 5]
            # Correct sentence for first mention of cause of death: But be careful, for it is poisoned [chapter 5]
            # Correct sentence for first mention of robbery: They have robbed him of the treasure [chapter 5]

        # Murder On the Links
            # Correct sentence for first mention of victim+death: Renauld was murdered this morning [very end of chapter 2]
            # Correct sentence for first mention of cause of death: Going to call her mistress as usual, a younger maid, Léonie, was horrified to discover her gagged and bound, and almost at the same moment news was brought that M. Renauld’s body had been discovered, stone dead, stabbed in the back [chapter 3]
        
        sentences = self.getSentencesText()

        if(self.cur_novel_id == 0):
            victim = 'mrs. inglethorp'
        elif(self.cur_novel_id == 1):
            victim = 'bartholomew'
        elif(self.cur_novel_id == 2):
            victim = 'renauld'

        pronouns = ['she', 'he', 'it']
        verbs = ['was', 'is', 'ha[sd]\W*been', 'means']
        murderWords = ['murder(ed)?', 'killed']
        causeOfDeathWords = ['poisoned', 'stabbed']

        allKillWords = murderWords + causeOfDeathWords

        subjects = pronouns
        subjects.append(victim)

        for i, subject in enumerate(subjects):
            subjects[i] = '(^|(?<=\W))' + subject + '(?=\W|$)'
        for i, verb in enumerate(verbs):
            verbs[i] = '(^|(?<=\W))' + verb + '(?=\W|$)'
        for i, killWord in enumerate(allKillWords):
            allKillWords[i] = '(^|(?<=\W))' + killWord + '(?=\W|$)'

        pattern = '(' + '|'.join(subjects) + ').*(' + '|'.join(verbs) + ').*(' + '|'.join(allKillWords) + ')'

        foundCrimeFirstSentence = False
        crimeChapterNum = 0
        crimeSentenceNum = 0
        causeOfDeath = ''
        for chapterNum, chapter in enumerate(sentences):
            for sentenceNum, sentence in enumerate(chapter):
                match = re.search(pattern, sentence)
                if(match != None):
                    for causeOfDeathWord in causeOfDeathWords:
                        if(causeOfDeathWord in sentence):
                            causeOfDeath = causeOfDeathWord
                            break
                    if(not foundCrimeFirstSentence):
                        foundCrimeFirstSentence = True
                        crimeChapterNum = 1 + chapterNum
                        crimeSentenceNum = 1 + sentenceNum

        return OutputInterface.first_mention_of_crime(crimeChapterNum, crimeSentenceNum, causeOfDeath, victim)  

    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), answer the question: 
    # When is the perpetrator first mentioned - chapter #, the sentence(s) # in a chapter
    def answer3(self):
        sentences = self.getSentencesText()
        PerpetratorSentencesData = []
        if(self.cur_novel_id == 0):
            PerpetratorSentencesData = Identities__FindOccurencesInText(identities.Criminal__MysteriousAffair, sentences)
        elif(self.cur_novel_id == 1):
            PerpetratorSentencesData = Identities__FindOccurencesInText(identities.Criminal__SignOfTheFour, sentences)
        elif(self.cur_novel_id == 2):
            PerpetratorSentencesData = Identities__FindOccurencesInText(identities.Criminal__murderOnTheLinks, sentences)
        return OutputInterface.first_mention_of_perpetrator(PerpetratorSentencesData[0][0], PerpetratorSentencesData[0][1], PerpetratorSentencesData[0][2])
    

    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), answer the question: 
    # What are the three words that occur around the perpetrator on each mention 
    # (i.e., the three words preceding and the three words following the mention of a perpetrator),
    def answer4(self):
        sentences = self.getSentencesText()
        PrecedingFollowing3SentencesData = []
        if(self.cur_novel_id == 0):
            PrecedingFollowing3SentencesData = FindThreeWordsAround(identities.Criminal__MysteriousAffair, sentences)
        elif(self.cur_novel_id == 1):
            PrecedingFollowing3SentencesData = FindThreeWordsAround(identities.Criminal__SignOfTheFour, sentences)
        elif(self.cur_novel_id == 2):
            PrecedingFollowing3SentencesData = FindThreeWordsAround(identities.Criminal__murderOnTheLinks, sentences)

        return (PrecedingFollowing3SentencesData)

    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), answer the question: 
    # When are other suspects first introduced - chapter #, the sentence(s) # in a chapter
    def answer6(self):
        sentences = self.getSentencesText()
        SuspectsSentencesData = []
        suspectList = []
        if(self.cur_novel_id == 0):
            suspectList = identities.Suspects__MysteriousAffair
            SuspectsSentencesData = Identities__FindOccurencesInText(suspectList, sentences)
        elif(self.cur_novel_id == 1):
            suspectList = identities.Suspects__SignOfTheFour
            SuspectsSentencesData = Identities__FindOccurencesInText(suspectList, sentences)
        elif(self.cur_novel_id == 2):
            suspectList = identities.Suspects__murderOnTheLinks
            SuspectsSentencesData = Identities__FindOccurencesInText(suspectList, sentences)
        finalListOfAllSuspectOccurences = []

        seen = set()
        uniqueData = []
        FirstLastNamesList = []
        for name in suspectList:
            if (' ' in name):
                FirstLastNamesList.append(name)
        for element in SuspectsSentencesData:
            if element[0] not in seen :
                seen.add(element[0])
                uniqueData.append(element)

        #check if there is a longer name available
        ExtendNamesList = []
        for element in uniqueData:
            FullName = ""
            for i in range (0, len(FirstLastNamesList)):
                if ((element[0] in FirstLastNamesList[i])):
                    FullName = FirstLastNamesList[i]
                    ExtendNamesList.append((FullName, element[1], element[2]))

        ExtendNamesList.sort()

        seen = set()
        finalListOfAllSuspectOccurences = []
        FirstLastNamesList = []
        for element in ExtendNamesList:
            if element[0] not in seen :
                seen.add(element[0])
                finalListOfAllSuspectOccurences.append(element)

        return finalListOfAllSuspectOccurences



    #take list of identity strings, return or'd regex format string
    @staticmethod
    def genIdentityRegex(identityList):
        identStr = ""
        for identity in identityList:
            identStr += identity + '|'
        return identStr[:-1] #pop last | char

    #takes a regex pattern, query, and looks for any matches in novelStr
    #returns boolean, true if anything was found, else false
    @staticmethod
    def detPattern(query, novelStr):
        queryRes = [x for x in re.findall(query, novelStr) if (x != '')]
        return queryRes != []

    #take a sentence and use two regex patterns to extract the verbs
    @staticmethod
    def getVerbs(sentence):
        keywordMatch = [x for x in re.findall('\\b(investi|discov|deduc|conclud|expos|exam|search|question|allow|inter|follow|track|pursu|verif|stud|confront|prosecut|arrest|interv|chas|identif|confront|protect|guard|trail|trac|eliminat|analyz|observ|creep|solv|detect|confess|confer|inspect|deduc|gather|uncover|interv|report|reveal|review|explor|assess|locate|find|check|tail|retriev|secur|recover|collect|proceed)(\\w+)?\\b', sentence) if (x != '')]
        #could be modifiers preceding matches that change tense, these are generalizations
        presentTense = [x for x in re.findall('\\b[a-z]+ing\\b', sentence) if (x != '')]
        #print(sentence)
        pastTense = [x for x in re.findall('\\b[a-z]+ed\\b', sentence) if (x != '')]
        #print(pastTense)
        action = [x for x in re.findall('\\b[a-z]+s\\b', sentence) if (x != '')] #very likely too general
        thirdPerson = [x for x in re.findall('\\b[a-z]+es\\b', sentence) if (x != '')]
        
        return keywordMatch, presentTense, pastTense, action, thirdPerson
        
    @staticmethod
    #pass list of RE output that produced keywords, 1D, and any number of identities lists
    #return the passed list with identities removed (don't want names popping up as verbs)
    def popIdentities(keywordList, *identities):
        identities = set([identity for identityList in identities for identity in identityList]) #flatten identities, make set
        #print(keywordList)
        keywordList = set([keyword for keywordSub in keywordList for keyword in keywordSub]) #clean up RE output, can also produce multi D list. Actually is consequence of getVerbs output, but this may be a desirable check anyway
        return list(keywordList - identities) #returns a list, but uses set ops to remove intersection with identities

    @staticmethod
    #pass list of regex output
    #returns list with any tuples of strings flattened, concatenated to 1 string
    def concatReTup(reOutList):
        for i, match in enumerate(reOutList):
            if(isinstance(match, tuple)):
                tupleConcat = ""
                for substr in match:
                    tupleConcat += substr
                reOutList[i] = tupleConcat
        return reOutList

    #for a given novel, answer when (chapter + sentence #) and how (currently, action verbs in vicinity of concurrence)
    #returns list of verbs, needs update for output interface
    #could add whether encounter happened before or after the crime by checking sentence # and chapter # against other answer call
    #currently only detects concurrence by name in sentence, novel ID 2 first "encounter" by this standard is investigator mentioning criminal
    def answer5(self):
        sentences = self.getSentencesText()
        if(self.cur_novel_id == 0):
            Investigators = identities.Investigators__MysteriousAffair
            Criminal = identities.Criminal__MysteriousAffair
        elif(self.cur_novel_id == 1):
            Investigators = identities.Investigators__SignOfTheFour
            Criminal = identities.Criminal__SignOfTheFour
        elif(self.cur_novel_id == 2):
            Investigators = identities.Investigators__murderOnTheLinks
            Criminal = identities.Criminal__murderOnTheLinks

        chapterNum = sentenceNum = concurrence = 0
        encounterSent = None
        #print(Investigators)
        #print("list should be above")
        investigatorRe = self.genIdentityRegex(Investigators)
        criminalRe = self.genIdentityRegex(Criminal)
        #print(investigatorRe)
        #print(criminalRe)
        for chapter in sentences:
            chapterNum += 1
            for sentence in chapter:
                sentenceNum += 1
                investigatorFlag = self.detPattern(investigatorRe, sentence)
                criminalFlag = self.detPattern(criminalRe, sentence)
                if(investigatorFlag and criminalFlag):
                    encounterSent = sentence
                    concurrence = True
                    break
            #only get first concurrence
            if(concurrence):
                break
        #print(chapterNum)
        #print(sentenceNum)
        if(encounterSent is None):
            print("Sorry, it looks like the investigator and perpetrator didn't ever actually meet.")
        else:
            return OutputInterface.detective_perpetrator_cooccurrence(chapterNum, sentenceNum, self.concatReTup(self.popIdentities(self.getVerbs(encounterSent), Investigators, Criminal)))            
        #sentenceNum, chapterNum = sentenceNum + 1, chapterNum + 1


    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), extract and return an answer to the given question (number corresponds to Canvas assignment)
    def extractAnswerToQuestion(self, questionId):
        
        if(questionId == 1):
            return self.answer1()

        elif(questionId == 2):
            return self.answer2()

        elif(questionId == 3):
            return self.answer3()

        elif(questionId == 4):
            return self.answer4()

        elif(questionId == 5):
            return self.answer5()
        
        elif(questionId == 6):
            return self.answer6()

        return None

if __name__ == "__main__":
    #boolean flags to turn on and off on individual runs to test different cases
    if(False):
        proc = NovelProcessing()
        print(proc.SentencesText__MysteriousAffair[0][0])

    #case 5 testing
    if(False):
        proc = NovelProcessing()
        # print (proc.answer1(0))
        # print (proc.answer3(0))
        # print (proc.answer4(0))
        print(proc.answer5())
        print (proc.answer6())

    #case 2 testing
    if(True):
        proc = NovelProcessing()
        proc.cur_novel_id = 2
        # print(proc.answer2())