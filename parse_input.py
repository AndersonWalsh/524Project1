'''
Module for processing input
    - Can be run directly for testing
From line of text at command prompt, produces int indicating prompt 1-6
    - Integers correspond to assignment questions
'''


import re

#readability
prompts = {
    "investigator": 1,
    "crime": 2,
    "perpetrator": 3,
    "perp_adj": 4,
    "concurrence": 5,
    "suspects": 6
}

#possible use for general identification of prompt
def detName(line):
    return re.findall('(([A-Z]([a-z]+|\.+))+(\s[A-Z][a-z]+)+)|([A-Z]{2,})|([a-z][A-Z])[a-z]*[A-Z][a-z]*', line)

def detInvest(line):
    return re.findall('|invest|detect|protag|main', line)

def detCrime(line):
    return re.findall('crime|thef|murder|steal|kill', line)

def detPerp(line):
    return re.findall('crim|perp|murderer|thie|bad|evil', line)

def detAdj(line):
    return re.findall('adjac|around|near|close|next|', line)

def detConc(line):
    return re.findall('meet|concur|clash|fight|talk|speak|capture|detain|arrest|apprehend', line)

def detSus(line):
    return re.findall('possible|inter|susp|potent', line)

det_funcs = [detInvest, detCrime, detPerp, detAdj, detConc, detSus] #no detName yet

def extractPrompt(line, funcs=det_funcs):
    promptList = []

    #assumes default order of det_funcs
    for i, func in enumerate(funcs):
        novelTxt = [x for x in func(line) if(x != '')]
        #novelTxt only populated if re caught something
        if(novelTxt != []):
            promptList.append(i+1)
    
    #reprompt if nothing detected
    if(promptList == []):
        print("I'm sorry, can you rephrase your question?")
        extractPrompt(input())
        return
    
    #if base case isn't true, one of these has to be
    #goes in order of most specific to least specific prompt
    #base cases last, implicit decision tree
    if(prompts["crime"] in promptList):
        return prompts["crime"]
    if(prompts["concurrence"] in promptList):
        return prompts["concurrence"]
    if(prompts["perp_adj"] in promptList):
        return prompts["perp_adj"]
    if(prompts["suspects"] in promptList):
        return prompts["suspects"]
    if(prompts["investigator"] in promptList):
        return prompts["investigator"]
    if(prompts["perpetrator"] in promptList):
        return prompts["perpetrator"]

if __name__ == "__main__":
    print("Running for direct prompt detection testing. To quit, type \"exit\"")
    print(f"\nNumber correspondence to prompts: {prompts}")
    while(1):
        line = input()
        if(line == "exit"):
            break
        print(extractPrompt(line))