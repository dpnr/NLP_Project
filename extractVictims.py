# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path


def extracting(filename):
    with open(filename) as file:
        input_text = file.read()

    # chunkGram = r"""Chunk: {<CD>*<RB.?>*<VB.?>*<JJ>+<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""
    stanford_classifier = 'F:\Stanford_data\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
    stanford_ner_path = 'F:\Stanford_data\stanford-ner-2015-12-09\stanford-ner.jar'
    #
    #     # Creating Tagger Object
    st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
    # st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    # stanford_dir = st._stanford_jar[0].rpartition('/')[0]
    stanford_dir = st._stanford_jar[0].rpartition("\\")[0]
    stanford_jars = find_jars_within_path(stanford_dir)
    # st._stanford_jar = ':'.join(stanford_jars)

    tokenized_text = nltk.word_tokenize(input_text)
    classified_text = st.tag(tokenized_text)
    c1=0
    nameList=[]
    for c,j in enumerate(classified_text):
        if(c<c1):
            continue

        name=[]
        if j[1]=="PERSON":
            c1=c
            while(c1<len(classified_text) and (classified_text[c1][1]=="PERSON")):
                name.append((classified_text[c1][0]))
                c1 = c1+ 1
            if(" ".join(name) not in nameList and len(name)>1):
                # print(" ".join(name))
                nameList.append(" ".join(name))
    if not nameList:
        nameList.append("-")
    return nameList
