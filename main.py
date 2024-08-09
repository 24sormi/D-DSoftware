import init
import random

def conditions():
    if init.blindness == 'true':
        init.perc = 0
        init.passivePerc = 0
    elif init.blindness == 'false':
        if init.percProf == 'true':
            init.perc = init.wisMod+init.profBonus
            init.passivePerc = 10+init.wisMod+init.profBonus
        elif init.percProf=='false':
            init.perc=init.wisMod
            init.passivePerc=10+init.wisMod
    if init.charmed == 'true':
        init.pers=init.pers+init.profBonus
    elif init.charmed == 'false':
        if init.persProf == 'true':
            init.pers=init.chaMod+init.profBonus
        elif init.persProf == 'false':
            init.pers=init.chaMod

def rollFunc():
    if init.diceType == 'd4':
        init.roll=random.randint(1,4)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd6':
        init.roll=random.randint(1,6)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd8':
        init.roll=random.randint(1,8)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd10':
        init.roll=random.randint(1,10)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd12':
        init.roll=random.randint(1,12)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd20':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd50':
        init.roll=random.randint(1,50)
        init.roll=init.roll+init.rollMod
        print(init.roll)
    elif init.diceType == 'd100':
        init.roll=random.randint(1,100)
        init.roll=init.roll+init.rollMod
        print(init.roll)

def strRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.strMod
    print(init.roll)

def intRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.intMod
    print(init.roll)

def wisRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.wisMod
    print(init.roll)

def chaRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.chaMod
    print(init.roll)

def dexRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.dexMod
    print(init.roll)

def conRoll():
    init.roll=random.randint(1,20)
    init.roll=init.roll+init.conMod
    print(init.roll)

def acroRoll():
    if init.acroProf == 'true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod+init.profBonus
        print(init.roll)
    elif init.acroProf == 'false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod
        print(init.roll)

def animRoll():
    if init.animProf == 'true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod+init.profBonus
        print(init.roll)
    elif init.animProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        print(init.roll)

def arcaRoll():
    if init.arcaProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod+init.profBonus
        print(init.roll)
    elif init.arcaProf='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod
        print(init.roll)

def athlRoll():
    if init.athlProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.strMod+init.profBonus
        print(init.roll)
    elif init.athlProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.strMod+init.profBonus
        print(init.roll)

def deceRoll():
    if init.deceProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod+init.profBonus
        print(init.roll)
    elif init.deceProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod
        print(init.roll)

def histRoll():
    if init.histProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod+init.profBonus
        print(init.roll)
    elif init.histProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod
        print(init.roll)

def insiRoll():
    if init.insiProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod+init.profBonus
        print(init.roll)
    elif init.insiProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        print(init.roll)

def intiRoll():
    if init.intiProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod+init.profBonus
        print(init.roll)
    elif init.intiProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod
        print(init.roll)

def inveRoll():
    if init.inveProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod+init.profBonus
        print(init.roll)
    elif init.inveProf--'false':
        init.roll-random.randint(1,20)
        init.roll=init.roll+init.intMod
        print(init.roll)

def mediRoll():
    if init.mediProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod+init.profBonus
        print(init.roll)
    elif init.mediProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        print(init.roll)

def natuRoll():
    if init.natuProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod+init.profBonus
        print(init.roll)
    elif init.natuProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod
        print(init.roll)

def percRoll():
    if init.percProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod+init.profBonus
        print(init.roll)
    elif init.percProf =='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        print(init.roll)

def perfRoll():
    if init.perfProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod+init.profBonus
        print(init.roll)
    elif init.perfProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod
        print(init.roll)

def persRoll():
    if init.persProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod+init.profBonus
        print(init.roll)
    elif init.persProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.chaMod
        print(init.roll)

def reliRoll():
    if init.reliProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod+init.profBonus
        print(init.roll)
    elif init.reliProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.intMod
        print(init.roll)

def sleiRoll():
    if init.sleiProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod+init.profBonus
        print(init.roll)
    elif init.sleiProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod
        print(init.roll)

def steaRoll():
    if init.steaProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod+init.profBonus
        print(init.roll)
    elif init.steaProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.dexMod
        print(init.roll)

def survRoll():
    if init.survProf=='true':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod+init.profBonus
        print(init.roll)
    elif init.survProf=='false':
        init.roll=random.randint(1,20)
        init.roll=init.roll+init.wisMod
        print(init.roll)
