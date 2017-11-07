# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
# import spacy
# nlp = spacy.load('en')
def extracting(filename,text_clf):
    dict = {}
    dict[1] = "ARSON"
    dict[2] = "ATTACK"
    dict[3] = "BOMBING"
    dict[4] = "KIDNAPPING"
    dict[5] = "ROBBERY"

    text = []
    # fileArguments["incident"] = e_incident.extracting(path + filename)  ## replace this with some function call to get the right result
    with open(filename) as file:
        text.append(file.read())
    pred=text_clf.predict(text)
    prediction = dict[pred[0]]

    return prediction
    # print("INCIDENT: " + prediction)

        # data=data.lower()
    # doc = nlp(data.decode('utf8'))
    # data.decode()
    # doc=nlp.tokenizer(data)
    # nlp.tagger(doc)
    # nlp.parser(doc)
    # nlp.entity(doc)
    # for word in doc:
    #     print(word,word.ent_type_)
    # print (doc)

    # tokens= sent_tokenize(data)
    # tokens = nltk.word_tokenize(data)
    # for c,j in enumerate(tokens):
    #     if j=="TEXT":
    #         tokens=tokens[c+2:]
    #         break
    # pos_tag=nltk.pos_tag(tokens)
    # print pos_tag
    # print sent
    # print tokens
    # sentences = [nltk.word_tokenize(sent) for sent in data]
    # ...
    # sentences = [nltk.pos_tag(sent) for sent in sentences]
    # return id.strip()