#Alex S

from bs4 import BeautifulSoup
import requests, re
import os
#import matplotlib.pyplot as plt, matplotlib.ticker
import csv 
from collections import Counter
import identities

def CheckFileExists (filename):
    return (os.path.exists(filename))


BookList = []
WebsiteList = []
wordCountDictionary_List = []
wordCountUniqueDictionary_List = []

with open("./sitesToScrap.csv", newline='') as csvfile:
    linkReader = csv.reader(csvfile)
    for line in linkReader:
        website = line[0]
        bookName = line[1]
        BookList.append(bookName)
        WebsiteList.append(website)


#retreive words from all books
allbooks = len(WebsiteList)
RegenerateOption = False
for i in range (allbooks):
    cleanedBook = str(BookList[i]) + "CLEANED.txt"
    if (CheckFileExists(cleanedBook) == False or (RegenerateOption == True)):
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

    else:
        print ("file exists: ", cleanedBook," ->  (warning)API call was not made. Check the directory for the cleaned text. Change RegenerateOption parameter's value to True if you want to make the call\n")
        continue



#NOTES:
#Murder of the links uses numeric chapter numbers without chapter keyword. Need to be separated.
# Other two books have the same format for the chaptes

with open ("TheSignOfTheFourCLEANED.txt", 'r') as file:
    FullText__TheSignOfTheFour = file.read()

with open ("TheMurderOnTheLinksCLEANED.txt", 'r') as file:
    FullText__TheMurderOnTheLinks = file.read()

with open ("TheMysteriousAffairAtStylesCLEANED.txt", 'r') as file:
    FullText__TheMysteriousAffairAtStyles = file.read()

# sentenceNumber =0
# for element in FullText__TheSignOfTheFour :
#     if element == "." or element == "?" or element == '!':
#         sentenceNumber+=1
# print (sentenceNumber)


chapterKeywords = ['chapter i', 'chapter ii', 'chapter iii', 'chapter iv','chapter v','chapter vi','chapter vii', 'chapter viii', 
                   'chapter ix', 'chapter x', 'chapter xi', 'chapter xii', 'chapter xiii']
chaptersPattern = '|'.join(map(re.escape, chapterKeywords))


chapters__TheSignOfTheFour = re.split(chaptersPattern, FullText__TheSignOfTheFour)
ChapterText__TheSignOfTheFour = []
for i in range (13,len(chapters__TheSignOfTheFour)): # I know how many chapters there are
    ChapterText__TheSignOfTheFour.append(chapters__TheSignOfTheFour[i])

chapters__MysteriousAffair = re.split(chaptersPattern, FullText__TheMysteriousAffairAtStyles)
ChapterText__MysteriousAffair = []
for i in range (13,len(chapters__MysteriousAffair)): # I know how many chapters there are
    ChapterText__MysteriousAffair.append(chapters__MysteriousAffair[i])


separators = ['.', '?', '!']
pattern = '|'.join(map(re.escape, separators))

sentencesText__TheSignOfTheFour = []
for chapterNumber in range (0,len(ChapterText__TheSignOfTheFour)):
    sentencesText__TheSignOfTheFour.append (re.split(pattern, ChapterText__TheSignOfTheFour[chapterNumber]))

sentencesText__MysteriousAffair = []
for chapterNumber in range (0,len(ChapterText__MysteriousAffair)):
    sentencesText__MysteriousAffair.append (re.split(pattern, ChapterText__MysteriousAffair[chapterNumber]))





def Identities__FindOccurencesInText (identitiesList, sentences): # pass an idendtities list
    RelevantSentencesData = []
    for identity in identitiesList:
        for chapterIndex in range (0,len(sentences)):
            for sentenceIndex in range (0, len(sentences[chapterIndex])):
                if (identity in sentences[chapterIndex][sentenceIndex]):
                    RelevantSentencesData.append ((identity, chapterIndex+1, sentenceIndex+1 ))
                    #print ("character ", identity, " occured in chapter ", chapterIndex+1, " in sentence number " , sentenceIndex+1)
    return RelevantSentencesData

InvestigatorSentencesData__TheSignOfTheFour = Identities__FindOccurencesInText(identities.Investigators__SignOfTheFour, sentencesText__TheSignOfTheFour)
InvestigatorSentencesData__MysteriousAffair = Identities__FindOccurencesInText(identities.Investigators__MysteriousAffair, sentencesText__MysteriousAffair)
print (InvestigatorSentencesData__TheSignOfTheFour)
print()
print (InvestigatorSentencesData__MysteriousAffair)



'''
Chapters from The Murder on the Links
1	A Fellow Traveller
2	An Appeal for Help
3	At the Villa Geneviève
4	The Letter Signed “Bella”
5	Mrs. Renauld’s Story
6	The Scene of the Crime
7	The Mysterious Madame Daubreuil
8	An Unexpected Meeting
9	M. Giraud Finds Some Clues
10	Gabriel Stonor
11	Jack Renauld
12	Poirot Elucidates Certain Points
13	The Girl with the Anxious Eyes
14	The Second Body
15	A Photograph
16	The Beroldy Case
17	We Make Further Investigations
18	Giraud Acts
19	I Use My Grey Cells
20	An Amazing Statement
21	Hercule Poirot on the Case!
22	I Find Love
23	Difficulties Ahead
24	“Save Him!”
25	An Unexpected Dénouement
26	I Receive a Letter
27	Jack Renauld’s Story
28	Journey’s End
'''
chapterBreakdown = []

