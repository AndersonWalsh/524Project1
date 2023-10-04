#Alex S

'''
The Murder on the Links:
Crime: murder (victim Paul Renauld)
    - stabbing
    - knife
Investigator: Giraud and Hercule Poirot (possibly Arthur Hastings)
Criminal: Marthe Daubreuil
Suspects: Jack, Bella Duveen
'''
Investigators__murderOnTheLinks = ['hercule poirot', 'poirot, monsieur poirot', 'poirot',
                                   'arthur hastings', 'hastings',
                                   'monsieur giraud', 'giraud']
Criminal__murderOnTheLinks = ['marthe daubreuil', 'daubreuil']
Suspects__murderOnTheLinks = ['jack duveen', 'bella duveen', 'duveen']
Crime__murderOnTheLinks = ['murder', 'stabbing']
murderWeapon__murderOnTheLinks = ['knife']

'''
The Sign of the Four:
Crime: theft, murder (bit unclear, it's a Holmes novel)
    - Multiple victims arguably, Bartholomew of murder, Sholto death by shock
    - One indirect "murder", another more active murder
    - A lot of nuance 
Investigator: Holmes, Watson
Criminal: Tonga (murder), Small (prison escape, conspiracy?), Sholto (theft)
Suspects: Arthur Morstan, Jonathan Small, Thaddeus
'''

Investigators__SignOfTheFour = ['holmes', 'watson', 'sherlock', 'sherlock homes', 'john watson']
Criminal__SignOfTheFour = ['tonga', 'small', 'sholto']
Suspects__SignOfTheFour = ['arthur morstan', 'morstan', 'arthur'
                           'jonathan small', 'small', 'jonathan'
                           'thaddeus']
Crime__SignOfTheFour = ['theft', 'murder', 'prison escape', 'conspiracy']

murderWeapon__SignOfTheFour = []

'''
The Mysterious Affair at Styles
Crime: Murder (victim Emily Inglethorp)
    - Poisoning (strychnine)
Investigator: Arthur Hastings, Hercule Poirot
Criminal: Alfred Inglethorp (accomplice Evelyn Howard)
Suspects: Alfred Inglethorp, Evelyn Howard, Cynthia Murdoch, Mary Cavendish, Lawrence Cavendish, John Cavendish
'''
Investigators__MysteriousAffair = ['hercule poirot', 'poirot, monsieur poirot', 'poirot',
                                   'arthur hastings', 'hastings',
                                   ]
Criminal__MysteriousAffair = ['alfred inglethorp', 'inglethorp', 'alfred']
Suspects__MysteriousAffair = ['alfred inglethorp', 'inglethorp', 'alfred'
                              'evelyn howard', 'evelyn', 'howard'
                              'cynthia murdoch', 'cynthia', 'murdoch'
                              'mary cavendish', 'mary', 'cavendish',
                              'lawrence cavendish', 'lawrence'
                              'john cavendish', 'john'
                              ]
Crime__MysteriousAffair = ['murder', 'poisoning']
murderWeapon__MysteriousAffair = ['strychnine']


All_investigators = set (Investigators__murderOnTheLinks + Investigators__SignOfTheFour + Investigators__MysteriousAffair)
All_criminals = set (Criminal__murderOnTheLinks + Criminal__SignOfTheFour + Criminal__MysteriousAffair)
All_suspects = set (Suspects__murderOnTheLinks + Suspects__SignOfTheFour + Suspects__MysteriousAffair)
All_crimes = set (Crime__murderOnTheLinks + Crime__SignOfTheFour + Crime__MysteriousAffair)
print (All_suspects)