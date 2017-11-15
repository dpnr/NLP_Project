# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import spacy
def extracting(filename):
    with open(filename) as file:
        corpus = file.read().lower()

    custom_sent_tokenizer = PunktSentenceTokenizer(corpus)

    tokenized = custom_sent_tokenizer.tokenize(corpus)

    # chunkGram = r"""Chunk: {<CD>*<RB.?>*<VB.?>*<JJ>+<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""
    stanford_classifier = 'F:\Stanford_data\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
    stanford_ner_path = 'F:\Stanford_data\stanford-ner-2015-12-09\stanford-ner.jar'
    st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        chunkGram = r"""Chunk: {<NNP+|NN+|NNS+|NNPS+|VBD+|VBN+><IN*><JJ*|RB*><NNP+|NN+|NNS+|NNPS+><CC?><NNP?|NN?|NNS?|NNPS?>}"""
        # chunkGram = r"""Chunk: {<RB.?>*<CD|JJ|RB.?|VBN.?|NNS>+<RB.?|JJ|VBN.?>*<NN>*<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""

        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        # print(chunked)
        for subtree in chunked.subtrees():
            if (subtree.label() == 'Chunk'):
                chunk = []
                tokens = []

                for i in range(0, len(subtree)):
                    chunk.append(subtree[i])
                    tokens.append(subtree[i][0])