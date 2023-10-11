""" I just created this file, if this is where we're going have main.py as a driver script where everything will be interlinked."""

import parse_input as p_in
import readBooksText as rbt
#insert necessary output imports here

if __name__ == "__main__":
    novelProc = rbt.NovelProcessing()
    print("Hi, I'm the Detective Novel re based chatbot for \"Murder on the Links\", \"Sign of the Four\", and \"Mysterious Affair\". You can ask me questions about the criminals, detectives and crime. When you're done, just say \"exit\". If you'd like to change which novel we're discussing at any time, just say so! What story would you like to start with?")
    query = input()
    novelProc.cur_novel_id = p_in.extractNovel(query)
    while(1):
        print("What would you like to know?")
        query = input()
        if(novelProc.detPattern(p_in.switchRe, query)):
            print("Ok, we'll switch to that one.")
            novelProc.cur_novel_id = p_in.extractNovel(query)
            print(novelProc.cur_novel_id)
            continue
        '''if(p_in.doubleQuery):
            print(p_in.extractPrompt(query))''' #not currently handling this case of intersection
        if(query == "exit"):
            break
        print(novelProc.extractAnswerToQuestion(p_in.extractPrompt(query)))