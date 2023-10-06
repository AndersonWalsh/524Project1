#Alex S

from bs4 import BeautifulSoup
import requests, re
import os
#import matplotlib.pyplot as plt, matplotlib.ticker
import csv 
from collections import Counter
import identities


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


class NovelProcessing:
    def __init__(self):

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
    def getFullText(self, novelId):
        
        if(novelId == 0):
            if(self.FullText__MysteriousAffair == ''):

                if(not CheckFileExists('TheMysteriousAffairAtStylesCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheMysteriousAffairAtStylesCLEANED.txt", 'r') as file:
                    self.FullText__MysteriousAffair = file.read()
            
            return self.FullText__MysteriousAffair
        
        elif(novelId == 1):
            if(self.FullText__TheSignOfTheFour == ''):

                if(not CheckFileExists('TheSignOfTheFourCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheSignOfTheFourCLEANED.txt", 'r') as file:
                    self.FullText__TheSignOfTheFour = file.read()
            
            return self.FullText__TheSignOfTheFour
        
        elif(novelId == 2):
            if(self.FullText__TheMurderOnTheLinks == ''):

                if(not CheckFileExists('TheMurderOnTheLinksCLEANED.txt')):
                    self.redownloadRegenerateCleanedTextFiles()

                with open ("TheMurderOnTheLinksCLEANED.txt", 'r') as file:
                    self.FullText__TheMurderOnTheLinks = file.read()
            
            return self.FullText__TheMurderOnTheLinks
        
        return None


    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), return ALL of its chapters as a list of strings (each string is the text for a full chapter)
    def getChaptersText(self, novelId):

        if(novelId == 0 and self.ChapterText__MysteriousAffair):
            return self.ChapterText__MysteriousAffair
        elif(novelId == 1 and self.ChapterText__TheSignOfTheFour):
            return self.ChapterText__TheSignOfTheFour
        elif(novelId == 2 and self.ChapterText__TheMurderOnTheLinks):
            return self.ChapterText__TheMurderOnTheLinks

        if(novelId == 0 or novelId == 1):
            chaptersPattern = '|'.join(CHAPTER_KEYWORDS)
        elif(novelId == 2):
            chaptersPattern = '|'.join(CHAPTER_KEYWORDS_THE_MURDER_ON_THE_LINKS)

        chapters = re.split(chaptersPattern, self.getFullText(novelId))

        if(novelId == 0):
            for i in range (14,len(chapters)): # I know how many chapters there are
                self.ChapterText__MysteriousAffair.append(chapters[i])
            return self.ChapterText__MysteriousAffair
        elif(novelId == 1):
            for i in range (13,len(chapters)): # I know how many chapters there are
                self.ChapterText__TheSignOfTheFour.append(chapters[i])
            return self.ChapterText__TheSignOfTheFour
        elif(novelId == 2):
            for i in range (1,len(chapters)): # I know how many chapters there are
                self.ChapterText__TheMurderOnTheLinks.append(chapters[i])
            return self.ChapterText__TheMurderOnTheLinks

        return None
    

    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), return ALL of its sentences as a list of lists of strings (Outside list is keyed on chapter, inside lists are keyed on sentence number relative to the start of the chapter, each value of inside lists is a single sentence)
    def getSentencesText(self, novelId):

        separators = ['.', '?', '!']
        pattern = '|'.join(map(re.escape, separators))
        novelChapters = self.getChaptersText(novelId)

        if(novelId == 0):

            if(not self.SentencesText__MysteriousAffair):
                for chapterNumber in range (0,len(novelChapters)):
                    self.SentencesText__MysteriousAffair.append (re.split(pattern, novelChapters[chapterNumber]))

            return self.SentencesText__MysteriousAffair
        
        elif(novelId == 1):

            if(not self.SentencesText__TheSignOfTheFour):
                for chapterNumber in range (0,len(novelChapters)):
                    self.SentencesText__TheSignOfTheFour.append (re.split(pattern, novelChapters[chapterNumber]))

            return self.SentencesText__TheSignOfTheFour
        
        elif(novelId == 2):

            if(not self.SentencesText__TheMurderOnTheLinks):
                for chapterNumber in range (0,len(novelChapters)):
                    self.SentencesText__TheMurderOnTheLinks.append (re.split(pattern, novelChapters[chapterNumber]))

            return self.SentencesText__TheMurderOnTheLinks
        
        return None

    
    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), answer the question: When does the investigator (or a pair) occur for the first time -  chapter #, the sentence(s) # in a chapter
    def answer1(self, novelId):

        sentences = self.getSentencesText(novelId)

        if(novelId == 0):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__MysteriousAffair, sentences)
        elif(novelId == 1):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__SignOfTheFour, sentences)
        elif(novelId == 2):
            InvestigatorSentencesData = Identities__FindOccurencesInText(identities.Investigators__murderOnTheLinks, sentences)

        return None


    # For a given novel (0=MysteriousAffair, 1=SignOfFour, 2=MurderOnLinks), extract and return an answer to the given question (number corresponds to Canvas assignment)
    def extractAnswerToQuestion(self, novelId, questionId):
        
        if(questionId == 1):
            return self.answer1(novelId)

        return None

if __name__ == "__main__":
    proc = NovelProcessing()
    print(proc.extractAnswerToQuestion(0, 1))