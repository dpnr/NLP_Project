# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import spacy

#
# def extracting(filename):
#     # we need to do the bio tagging and extract only the  organizations
#     organizations = []
#
#     with open(filename) as file:
#         input_text = file.read().lower()
#
#
#     custom_sent_tokenizer = PunktSentenceTokenizer(input_text)
#
#     tokenized = custom_sent_tokenizer.tokenize(input_text)
#
#     ####stanford stuff
#     st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
#     stanford_dir = st._stanford_jar[0].rpartition('/')[0]
#     stanford_jars = find_jars_within_path(stanford_dir)
#     st._stanford_jar = ':'.join(stanford_jars)
#     #### end of stanford stuff
#
#     ##How common is the word ???
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#
#     try:
#         for i in tokenized[0:]:
#
#             words = nltk.word_tokenize(i)
#             # words=words.lower()
#             tagged = nltk.pos_tag(words)
#             # print(st.tag(words))
#             for in_tuple in st.tag(words):
#                 if (in_tuple[1] == 'ORGANIZATION'):
#                     print(in_tuple)
#                     print(in_tuple[0].lower() in english_vocab)
#
#
#     except Exception as e:
#         print(str(e))
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



#
# # Change the path according to your system
def extracting(filename):
    nlp = spacy.load('en')
    with open(filename) as file:
        input_text = file.read()
        parsed_text = nlp(input_text.lower())
    stanford_classifier = 'F:\Stanford_data\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
    stanford_ner_path = 'F:\Stanford_data\stanford-ner-2015-12-09\stanford-ner.jar'
#
#     # Creating Tagger Object
    st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
#
#     text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
#
    tokenized_text = word_tokenize(input_text)
    classified_text = st.tag(tokenized_text)
#
    print (classified_text)

    nlp = spacy.load('en')

    for text in parsed_text:
        # subject would be
        if text.dep_ == "nsubj":
            subject = text.orth_
            print("subject"+ subject)
        # iobj for indirect object
        if text.dep_ == "iobj":
            indirect_object = text.orth_
            print("iobj"+indirect_object)

        # dobj for direct object
        if text.dep_ == "dobj":
            direct_object = text.orth_
            print("dobj"+direct_object)


    #
    #