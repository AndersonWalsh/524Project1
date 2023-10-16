""" I just created this file, if this is where we're going have main.py as a driver script where everything will be interlinked."""

import parse_input as p_in
import readBooksText as rbt
import output_processor as p_out
#insert necessary output imports here

if __name__ == "__main__":
    novelProc = rbt.NovelProcessing()
    outProc = p_out.OutputProcessor()
    print("Hi, I'm the Detective Novel re based chatbot for \"Murder on the Links\", \"Sign of the Four\", and \"Mysterious Affair\". You can ask me questions about the criminals, detectives and crime. When you're done, just say \"exit\". If you'd like to change which novel we're discussing at any time, just say so! What story would you like to start with?")
    query = input()
    novelProc.cur_novel_id = p_in.extractNovel(query)
    while(1):
        print("What would you like to know?")
        query = input()
        if(novelProc.detPattern(p_in.switchRe, query)):
            print("Ok, we'll switch to that one.")
            novelProc.cur_novel_id = p_in.extractNovel(query)
            continue
        '''if(p_in.doubleQuery):
            print(p_in.extractPrompt(query))''' #not currently handling this case of intersection
        if(query == "exit"):
            break

        promptNum = p_in.extractPrompt(query)

        if promptNum == 1:
            print(outProc.process_investigator_pair_first_occurrence(novelProc.extractAnswerToQuestion(promptNum)))
        elif promptNum == 2:
            print(outProc.process_first_mention_of_crime(novelProc.extractAnswerToQuestion(promptNum)))
        elif promptNum == 3:
            print(outProc.process_first_mention_of_perpetrator(novelProc.extractAnswerToQuestion(promptNum)))
        elif promptNum == 4:
            results = novelProc.extractAnswerToQuestion(promptNum)
            formatted_results = [
                {
                    "three_preceding_words": res[0],
                    "perpetrator": res[1],
                    "three_following_words": res[2],
                    "chapter": res[3],
                    "sentence": res[4]
                } for res in results
            ]
            print(outProc.process_three_words_around_perpetrator(formatted_results))
        elif promptNum == 5:
            print(outProc.process_detective_perpetrator_cooccurrence(novelProc.extractAnswerToQuestion(promptNum)))
        elif promptNum == 6:
            print(outProc.process_other_suspects_first_introduction(novelProc.extractAnswerToQuestion(promptNum)))