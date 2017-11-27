# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.tag import StanfordNERTagger
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy
def extracting(filename):
    with open(filename) as file:
        corpus = file.read().lower()
    try:
        for i in range(corpus.__len__()):
            if (corpus[i]=="[") and (corpus[i+1] =="t") and (corpus[i+2]=="e") and (corpus[i+3]=="x") and corpus[i+4]=="t" and corpus[i+5]=="]":
                corpus =corpus[i+7:]
                break
    except:
        pass

    nlp=spacy.load('en')
    doc=nlp(corpus)

    for token1 in doc:
        if(token1.similarity(nlp(u"destroy"))>0.5):
            print(token1)
            print(token1.similarity(nlp(u"destroy")))

    return '-'