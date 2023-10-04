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
    bookText = file.read()

sentenceNumber =0
for element in bookText :
    if element == "." or element == "?" or element == '!':
        sentenceNumber+=1
print (sentenceNumber)


separators = ['.', '?', '!']
pattern = '|'.join(map(re.escape, separators))
sentences = re.split(pattern, bookText)
print(len(sentences))
# for i in range (0,40):
#     print (result[i])

investigatorSentences = []
for investigator in identities.Investigators__SignOfTheFour:
    for i in range (0, len(sentences)):
        if (investigator in sentences[i]):
            investigatorSentences.append(sentences[i])
            #print (sentences[i])

print(len(investigatorSentences))