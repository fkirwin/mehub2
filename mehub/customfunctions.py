import nltk
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
import requests
from json import *
from nltk.collocations import *
import random


def getSentiment(payload):
    tokens = word_tokenize(payload)
    payload="+".join(str(each) for each in tokens)
    urlEndPoint = "https://sentity-v1.p.mashape.com/v1/sentiment?text={}".format(payload)
    headers={'X-Mashape-Key': '3NLjyTcMhDmshfDM3AxE3MRPBjBip1XwEg8jsnK3HHH2xMyqZa', 'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.get(urlEndPoint, headers=headers)
    verdict = loads(r.content.decode("utf-8"))
    return (verdict)

def verdictEvaluate(pos,neg):
    if pos>neg:
        return "Positive"
    elif pos<neg:
        return "Negative"
    else:
        return "Neutral"
        

def sentenceStructure(payload):
    tokens = word_tokenize(payload)
    phrase={}
    ##find varaibles about sentence
    for word in tokens:
        lenOfWord = (len(word))
        countOfWord = tokens.count(word)
        phrase.update({word:{"wordname":word, "count": countOfWord, "length": lenOfWord}})
    return phrase

def mrRogers(payload):
    tokens = word_tokenize(payload)
    bgm    =  nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)
    neighbors = finder.score_ngrams( bgm.likelihood_ratio  )
    return neighbors

def breakdown(textname):
    for k, v in textname.items():
        if isinstance(v, dict):
            return (v)
            
def yodaizePost(payload):
    tokens = word_tokenize(payload)
    payload="+".join(str(each) for each in tokens)
    urlEndPoint = "https://yoda.p.mashape.com/yoda?sentence=={}".format(payload)
    headers={'X-Mashape-Key': 'Hj697SmIK5msh4dQpLS9atAXku5sp1WaCemjsnqpkHVWDV9KsV', 'Content-type': 'text/plain', 'Accept': 'text/plain'}
    r = requests.get(urlEndPoint, headers=headers)
    yodasays = r.content.decode("utf-8")
    return yodasays

def randomizePost(payload):
    newPayload = sentenizer(payload)
    resultSet=[]
    for payload in newPayload:
        tokens = word_tokenize(payload)
        reList = []
        reVisit=tokens
        while len(reVisit)>0:
            selection=random.randint(0, len(reVisit)-1)
            reList.append(reVisit[selection])
            del reVisit[selection]
        resultSet.append(" ".join(str(each) for each in reList))
    return (".  ".join(str(each) for each in resultSet))

def sentenizer(sentence):
    strippers = ['.', ';']
    sentenceBase=[]
    for punc in strippers:
        for each in sentence.split(punc):
            sentenceBase.append(''.join(str(each)))
        return sentenceBase
        
    
sentence = """At eight o'clock on on Thursday morning
... Arthur didn't feel very good."""
"""
##each word
tokens = word_tokenize(sentence)

##lenght of each word##
for each in tokens:
    print (len(each))

##length of sentence
print(len(tokens))

##tree
###tree=Tree.fromstring(sentence)
###print(tree.pos())

print (tokens)

for each in tokens:
    print (each)
    
print (str(tokens))

print("+".join(str(each) for each in tokens))
"""