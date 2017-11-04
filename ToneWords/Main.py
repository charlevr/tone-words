'''
Created on Jun 19, 2017

@author: chadd
'''
import re
from collections import defaultdict

def openText(file: open) -> list:
    '''
    Opens a file and reads the words. Takes out punctuation points and other non-word items
    using regular expressions and returns all of the words in a list
    '''
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
    '''
    takes each text file of tone words and adds them to a particular list and returns a dictionary with each list
    '''
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
    '''
    Go through each word in each text and determine the tone of each word, if it has one. 
    '''
    toneCount = defaultdict(int)
    words = defaultdict(list)
    for word in wordList:
        for tone in toneDict.keys():
            if word in toneDict[tone]:
                toneCount[tone] += 1
                words[tone].append(word)
    return (toneCount, words)

def countToneWords(wordDict: dict):
    '''
    Returns the number of tone words in the dictionary
    '''
    count = 0
    for word in wordDict.keys():
        count += wordDict[word]
    return count

#no specific function implemented here, but if I decide to add more to this project then a function will be used
text = countWords(openText('TheEgg.txt'), openToneWords())

print(len(openText('TheEgg.txt')))
print(countToneWords(text[0]))
print(text[0])
print(text[1])

        

