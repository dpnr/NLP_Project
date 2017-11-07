# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path


def extracting(filename):
    # we need to do the bio tagging and extract only the  organizations
    organizations = []

    with open(filename) as file:
        input_text = file.read().lower()


    custom_sent_tokenizer = PunktSentenceTokenizer(input_text)

    tokenized = custom_sent_tokenizer.tokenize(input_text)

    ####stanford stuff
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    stanford_dir = st._stanford_jar[0].rpartition('/')[0]
    stanford_jars = find_jars_within_path(stanford_dir)
    st._stanford_jar = ':'.join(stanford_jars)
    #### end of stanford stuff

    ##How common is the word ???
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())

    try:
        for i in tokenized[0:]:

            words = nltk.word_tokenize(i)
            # words=words.lower()
            tagged = nltk.pos_tag(words)
            # print(st.tag(words))
            for in_tuple in st.tag(words):
                if (in_tuple[1] == 'ORGANIZATION'):
                    print(in_tuple)
                    print(in_tuple[0].lower() in english_vocab)


    except Exception as e:
        print(str(e))
# import nltk
# import spacy
# nlp = spacy.load('en')
# def extracting(filename):
#
#     with open(filename) as file:
#         data = file.read()
#         data=data.lower()
#     doc=nlp(data)
#     for ent in doc.ents:
#         print(ent.label_, ent.text)


