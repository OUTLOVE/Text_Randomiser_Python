import re
import random
text = '{ Добрый вечер| Добрый день} я\n     [ xочу| могу|  буду]  {делать | писать} [ это| то ] или нет?'
quad = re.findall(r'\[[(a-zа-яА-ЯA-Z\(\)\'\"=\+"\\\*\/\?\.\,\s\n:\!\;\-)*|(\|)+]*\]?', text)
def Randomise(text):
    figs = re.findall(r'\{[(a-zа-яА-ЯA-Z\'\"=\+"\\"\*\/\?\.\,\s :\!\;\-)*|(\|)+]*\}?', text)
    plusind = 1
    textoutfigsplited = re.split(r'\{[(a-zа-яА-ЯA-Z\'\"=\+"\\"\*\/\?\.\, :\;\-)*|(\|)+]*\}?', text)
    for i, fig in enumerate(figs):
        matchesfig = re.findall(r'[a-zа-яА-ЯA-Z\'\"\-=\+\\ "\*/\?\.\, :\;]+', fig)
        matchfig = random.choice(matchesfig)
        indtoins = i + plusind
        textoutfigsplited.insert(indtoins, matchfig)
        plusind += 1
    text = ''.join(textoutfigsplited)
    quad = re.findall(r'\[[(a-zа-яА-ЯA-Z\'\"=\+"\\"\*\/\?\.\,\s :\!\;\-)*|(\|)+]*\]?', text)
    matcheses = []
    for i in quad:
        matches = re.findall(r'[a-zа-яА-ЯA-Z\'\"\-=\+\\ "\*/\?\.\, :\;]+', i)
        random.shuffle(matches)
        match = ''.join(matches)
        matcheses.append(match)

        textoutsplited = re.split(r'\[[(a-zа-яА-ЯA-Z\'\"=\+"\\"\*\/\?\.\, :\;\-)*|(\|)+]*\]?',text)
    plusind = 1
    for i in range(len(matcheses)):
        indtoins = i + plusind
        textoutsplited.insert(indtoins,matcheses[i])
        plusind += 1
    textout = ''.join(textoutsplited)
    return textout
readytext = Randomise(text)
print(readytext)
