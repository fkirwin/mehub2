from nltk import *
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
import requests
from json import *

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
sentence = """At eight o'clock on Thursday morning
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