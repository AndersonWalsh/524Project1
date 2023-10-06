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

novels = {
    "mys_affair": 0,
    "sign_of": 1,
    "murder_ol": 2
}

'''
The Murder on the Links:
Crime: murder (victim Paul Renauld)
    - stabbing
    - knife
Investigator: Giraud and Hercule Poirot (possibly Hastings)
Criminal: Marthe Daubreuil
Suspects: Jack, Bella Duveen

The Sign of the Four:
Crime: theft, murder (bit unclear, it's a Holmes novel)
    - Multiple victims arguably, Bartholomew of murder, Sholto death by shock
    - One indirect "murder", another more active murder
    - A lot of nuance 
Investigator: Holmes, Watson
Criminal: Tonga (murder), Small (prison escape, conspiracy?), Sholto (theft)
Suspects: Arthur Morstan, Jonathan Small, Thaddeus

The Mysterious Affair at Styles
Crime: Murder (victim Emily Inglethorp)
    - Poisoning (strychnine)
Investigator: Arthur Hastings, Hercule Poirot
Criminal: Alfred Inglethorp (accomplice Evelyn Howard)
Suspects: Alfred Inglethorp, Evelyn Howard, Cynthia Murdoch, Mary Cavendish, Lawrence Cavendish, John Cavendish
'''

#possible use for general identification of prompt
def detName(line):
    return re.findall('(([A-Z]([a-z]+|\.+))+(\s[A-Z][a-z]+)+)|([A-Z]{2,})|([a-z][A-Z])[a-z]*[A-Z][a-z]*', line)

def detInvest(line):
    return re.findall('invest|detect|protag|main|hercule|poirot|arthur|hastings|giraud|sherlock|holmes|john|watson|inform|sleuth|officer|agent|inspect|police', line)

def detCrime(line):
    return re.findall('crime|thef|murder|steal|stole|kill|stab|thiev|kni|theft|murder|prison|escape|conspir|shock|poison|stryc|felony|scandal|wrong|lawless|misdeed|assass|homici|shoot|slay|burgli|burgle', line)

def detPerp(line):
    return re.findall('commit|crimin|perp|murderer|killer|thief|bad|evil|marthe|daubreuil|tonga|small|sholto|alf|inglethorp|felon|crook|robber|burglar', line)

def detAdj(line):
    return re.findall('adjac|around|near|close|next|border|neigh', line)

def detConc(line):
    return re.findall('meet|concur|clash|fight|talk|speak|capture|detain|arrest|apprehend|convers|contact|face|see|altercat|conflict|brawl|exchang|skirmi|scuffl|chat|exchang|imprison|jail|incarcer|interrogat', line)

def detSus(line):
    return re.findall('poss|inter|susp|potent|jack|bella|duveen|morstan|small|jonathan|john|thaddeus|evelyn|howard|cynthia|murdoch|mary|cavendish|lawrence|conceiv|feas|plaus|proba|viabl|likel', line)

det_funcs = [detInvest, detCrime, detPerp, detAdj, detConc, detSus] #no detName yet

#funcMatch currently unused feature to get name of functions that found matches
def getPromptsList(promptList, line, funcs):
    funcMatch = []
    for i, func in enumerate(funcs):
        novelTxt = [x for x in func(line) if(x != '')]
        #novelTxt only populated if re caught something
        if(novelTxt != []):
            promptList.append(i+1)
            funcMatch.append(func)
    return promptList

#currently zombie code, sticking around for potential further use in further generalization
'''
#catch overlap in cases to give most specific reply
#this isn't perfect, two query strings of max length breaks it
def checkSuperset(queryFlags, funcs):
    if(len(funcs) <= 1):
        return funcs[0] #find the func that gives the most specific thing
    biggestMatch = 0
    #find longest match
    #test against matching functions
    #keep going until only 1 matches
    #for word in queryFlags:

    #biggestMatch = [x for x in queryFlags if(len(x) > biggestMatch)][0]
    queryFlags, funcs = getPromptsList(queryFlags, biggestMatch, funcs)

    return queryFlags.index(biggestMatch)
'''

doubleQuery = False

def extractPrompt(line, funcs=det_funcs):
    #catch possible intersecting queries
    global doubleQuery
    if(doubleQuery):
        print("debugging message: double query case triggered, previous input ignored to handle for potential dual crime + criminal prompt")
        secQuery = doubleQuery
        doubleQuery = False
        return secQuery

    promptList = []
    line = line.lower()
    #assumes default order of det_funcs
    promptList = getPromptsList(promptList, line, funcs)
    
    #reprompt if nothing detected
    if(promptList == []):
        print("I'm sorry, can you rephrase your question?")
        return extractPrompt(input())
    
    #if above case isn't true, one of these has to be
    #goes in order of most specific to least specific prompt
    #base cases last, implicit decision tree

    #first, handle some more complex sequences
    if(prompts["crime"] in promptList and prompts["perpetrator"] in promptList and prompts["investigator"] in promptList):
        return prompts["concurrence"] #mention of all 3 implies inquiry about meeting
    if(prompts["crime"] in promptList and prompts["perpetrator"] in promptList):
        doubleQuery = prompts["crime"] #both being true could imply either case, keeps API intact by signaling to data pipeline to show results for both queries
        print("double prompt detection case, carriage return through the next input call")
        return prompts["perpetrator"]
    '''
    possible we want a more advanced decision tree, for cases such as referring to the criminal not by name but by the crime they committed
    if they mentioned the crime
        did they also mention the perpetrator
            if yes, they want to know the crime details
    currently handling this by making the intersection signal the data pipeline with both possible prompts
    '''
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
    

def det_MysAff(line):
    return re.findall('mysterious|affair', line)

def det_Sof(line):
    return re.findall('sign|four', line)

def det_Mol(line):
    return re.findall('links', line)

det_funcs_novel = [det_MysAff, det_Sof, det_Mol]

def extractNovel(line, funcs=det_funcs_novel):
    novel = getPromptsList([], line, funcs)

    #reprompt if nothing detected
    if(len(novel) <= 0):
        print("Sorry, I don't know that one. Are you interested in one of the listed novels?")
        return extractNovel(input())

    # -1 due to 0 indexing on novels 
    novel = novel[0] - 1
    #if something was detected, it has to be one of the novels
    if(novels["murder_ol"] == novel):
        return novels["murder_ol"]
    if(novels["mys_affair"] == novel):
        return novels["mys_affair"]
    if(novels["sign_of"] == novel):
        return novels["sign_of"]

if __name__ == "__main__":
    print("Running for direct prompt detection testing. To quit, type \"exit\"")
    print(f"\nNumber correspondence to novel prompts: {novels}")
    print(f"\nNumber correspondence to content prompts: {prompts}")
    print("\nWhat novel are you interested in?")
    print(extractNovel(input()))
    while(1):
        print("What subject are you interested in?")   
        if(doubleQuery):
            print(extractPrompt(line))
        line = input()
        if(line == "exit"):
            break
        print(extractPrompt(line))