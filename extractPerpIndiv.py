import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
from nltk.stem import PorterStemmer



stopwords = list(set(stopwords.words('english')))


def extracting(filename):

    ps = PorterStemmer()
    persons = []
    persons_nn = []
    weapon = ""
    with open(filename) as file:
        corpus = file.read().replace('\n',' ').lower()
        
    custom_sent_tokenizer = PunktSentenceTokenizer(corpus)

    tokenized = custom_sent_tokenizer.tokenize(corpus)
    

    ####stanford stuff
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    stanford_dir = st._stanford_jar.rpartition('/')[0]
    stanford_jars = find_jars_within_path(stanford_dir)
    st._stanford_jar = ':'.join(stanford_jars)
    #### end of stanford stuff

    ps = PorterStemmer()
    w1_1 = wordnet.synset('person.n.01')
    w1_2 = wordnet.synset('member.n.01')
    w1_3 = wordnet.synset('men.n.01')
    w1_4 = wordnet.synset('suspect.n.01')

    try:
        for i in tokenized[:]:

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r"""Chunk: {<CD>*<RB.?>*<VB.?>*<JJ>+<NNP>*<NNP|NN|NNS|NNPS>+<VBZ>*}"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            for subtree in chunked.subtrees():
                if(subtree.label() == 'Chunk'):
                    chunk = []
                    tokens = []
                    
                    for i in range(0,len(subtree)): 
                        chunk.append(subtree[i])
                        tokens.append(subtree[i][0])
                        
                        if(subtree[i][0] in ['text','u.s.','officials','official','authorities','military','states','is','troops','police']):

                            chunk = []
                            break
                        
                        if(i == len(subtree)-1):
                            #it has to be related to person or group
                            
                            try:
                                w2 = wordnet.synset( ".".join([ps.stem(subtree[i][0]),"n.01"]) )
                            except:
                                chunk = []
                                break
                            # print("for "+subtree[i][0])
                            # print(w1_1.wup_similarity(w2))
                            # print(w1_2.wup_similarity(w2))
                            # print(w1_3.wup_similarity(w2))
                            if(w1_1.wup_similarity(w2) < 0.80 and w1_2.wup_similarity(w2) < 0.80 and w1_3.wup_similarity(w2) < 0.80 and w1_4.wup_similarity(w2) < 0.80 ):
                                chunk = []
                                break

                    
                    if(len(chunk)>1 and len(chunk) <=4):
                        
                        data = " ".join(tokens)
                        return data.upper()
                        # print(chunk)
                        # print('\n')
                                              
    except Exception as e:
        print(e)
    
    return "-"