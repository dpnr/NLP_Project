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
    nlp = spacy.load('en')
    doc = nlp(corpus)
    custom_sent_tokenizer = PunktSentenceTokenizer(corpus)

    tokenized = custom_sent_tokenizer.tokenize(corpus)

    # chunkGram = r"""Chunk: {<CD>*<RB.?>*<VB.?>*<JJ>+<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""
    # stanford_classifier = 'F:\Stanford_data\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
    # stanford_ner_path = 'F:\Stanford_data\stanford-ner-2015-12-09\stanford-ner.jar'
    # st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
    ps = PorterStemmer()
    # w1_1 = wordnet.synset('attack.n.01')
    # w1_2 = wordnet.synset('damage.n.01')
    # w1_3 = wordnet.synset('kill.n.01')


    data_List = []
    try:
        # data_List = []
        for i in tokenized:

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<NNP|NNS|NNPS|VBD.?|VBN.?>+<IN>?(<DT>*<JJ|RB.?>*<NNP|NN|NNS|NNPS>+)+(<,>*<JJ|RB.?>*<NNP|NN|NNS|NNPS>*)*(<CC>?<JJ|RB.?>*<NNP|NN|NNS|NNPS>*)?}
                         Chunk2: {(<JJ|RB.? >*< NNP|NNS|NNPS|NN>+)+(<,>*<JJ|RB.?>*<NNP|NN|NNS|NNPS>*)*(<CC>?<JJ|RB.?>*<NNP|NN|NNS|NNPS>*)?<VBD.?>+<VBN.?>+}

                        """
            # chunkGram = r"""Chunk: {<RB.?>*<CD|JJ|RB.?|VBN.?|NNS>+<RB.?|JJ|VBN.?>*<NN>*<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""
            # Chunk2: {( < JJ | RB.? > * < NNP | NNS | NNPS | NN  > +)+( <, > * < JJ | RB.? > * < NNP | NN | NNS | NNPS > * )*( < CC >? < JJ | RB.? > * < NNP | NN | NNS | NNPS > * )?}}

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # print(chunked)



            for subtree in chunked.subtrees():
                if (subtree.label() == 'Chunk2'):
                    chunk = []

                    # try:
                    #     w2 = wordnet.synset(".".join([ps.stem(subtree[-1][0]), "n.01"]))
                    #     # print(str(w2)+ ":" + str(w1_1.wup_similarity(w2)))
                    #     # print(w2+":"+ str( w1_2.wup_similarity(w2)))
                    #     if ((w1_2.wup_similarity(w2)) >0.5) :
                    #         pass
                    #     else:
                    #         break
                    #
                    # except:
                    #     break

                    if (nlp(subtree[-1][0]).similarity(nlp(u"destroy")) > 0.65) or (nlp(subtree[-1][0]).similarity(nlp(u"damage")) > 0.65):
                        pass
                    else:
                        break

                    for i in range(1, len(subtree)):
                        chunk.append(subtree[i])

                    chunkGram_1 = r"""Chunk1: {<JJ|RB.?>*<NNP|NN|NNS|NNPS>+}"""
                    chunkParser_1 = nltk.RegexpParser(chunkGram_1)
                    chunked_1 = chunkParser_1.parse(chunk)

                    for subtree_1 in chunked_1.subtrees():
                        if (subtree_1.label() == 'Chunk1'):
                            tokens = []
                            for i in range(0, len(subtree_1)):
                                tokens.append(subtree_1[i][0])

                            data = " ".join(tokens)
                            data = data.upper()
                            data_List.append(data)


                if (subtree.label() == 'Chunk'):
                    chunk = []
                    # try:
                    #     w2 = wordnet.synset(".".join([ps.stem(subtree[0][0]), "n.01"]))
                    #     # print(str(w2)+ ":" + str(w1_1.wup_similarity(w2)))
                    #     # print(w2+":"+ str( w1_2.wup_similarity(w2)))
                    #     if (((w1_1.wup_similarity(w2)) >0.5 or (w1_2.wup_similarity(w2))>0.5) and (w1_3.wup_similarity(w2))<0.85) :
                    #         pass
                    #     else:
                    #         break
                    #
                    # except:
                    #     break
                    if (((nlp(subtree[0][0]).similarity(nlp(u"attack")) > 0.65) or (nlp(subtree[0][0]).similarity(nlp(u"damage")) > 0.65)) and (nlp(subtree[0][0]).similarity(nlp(u"kill")) < 0.80)):
                        pass
                    else:
                        break

                    data=[]
                    flag_in=0
                    for i in range(1, len(subtree)):

                        if (subtree[i][1] == "IN" and (subtree[1][0]== "as" or subtree[1][0]== "between" or subtree[1][0]== "by" or subtree[1][0]== "of" or subtree[1][0]== "from" or subtree[1][0]== "against")) :
                            chunk=[]
                            break
                        # if (flag_in == 1):
                        chunk.append(subtree[i])
                        # if (subtree[i][1] == "IN"):
                        #     flag_in = 1

                    # if (subtree[1][0]== "as"):
                    #     break

                    chunkGram_1= r"""Chunk1: {<JJ|RB.?>*<NNP|NN|NNS|NNPS>+}"""
                    chunkParser_1 = nltk.RegexpParser(chunkGram_1)
                    chunked_1 = chunkParser_1.parse(chunk)

                    for subtree_1 in chunked_1.subtrees():
                        if (subtree_1.label() == 'Chunk1'):
                            tokens = []
                            for i in range(0, len(subtree_1)):
                                tokens.append(subtree_1[i][0])

                            data = " ".join(tokens)
                            data=data.upper()
                            data_List.append(data)



                    # for i in range(0, len(subtree)):
                    #     chunk.append(subtree[i])
                    #     tokens.append(subtree[i][0])
                    #      # if subtree[i][0]!= "IN":
                    #      #     continue
                        #

    except Exception as e:
        print(e)
    if not data_List:
        data_List.append("-")
    return data_List