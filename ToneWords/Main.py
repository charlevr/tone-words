'''
Created on Jun 19, 2017

@author: chadd
'''
import re
from collections import defaultdict

def openText(file: open) -> list:
    try:
        text = open(file)
    except:
        print("File is not readable")
    pattern  = '[^a-zA-Z]'
    words = []
    for line in text.readlines():
        for word in line.split():
            newWord = re.sub(pattern, '', word)
            words.append(newWord.lower())
    return words

def openToneWords():
    toneWords = defaultdict(list)
    def getToneWords(file: open, tone: str) -> dict:
        words = open(file)
        for line in words.readlines():
            toneWords[tone] = toneWords[tone] + [w.lower() for w in line.split()]
    getToneWords('PositiveTone.txt', 'Positive')
    getToneWords('NegativeTone.txt', 'Negative')
    getToneWords('HumorIronySarcasm.txt', 'HumorIronySarcasm')
    getToneWords('SorrowFearWorry.txt', 'SorrowFearWorry')
    getToneWords('Neutral.txt', 'Neutral')
    return toneWords
    
def countWords(wordList: list, toneDict: dict) -> dict:
    toneCount = defaultdict(int)
    words = defaultdict(list)
    for word in wordList:
        for tone in toneDict.keys():
            if word in toneDict[tone]:
                toneCount[tone] += 1
                words[tone].append(word)
    return (toneCount, words)

def countToneWords(wordDict: dict):
    count = 0
    for word in wordDict.keys():
        count += wordDict[word]
    return count

text = countWords(openText('TheEgg.txt'), openToneWords())

print(len(openText('TheEgg.txt')))
print(countToneWords(text[0]))
print(text[0])
print(text[1])

        

