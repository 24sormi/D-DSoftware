import init

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