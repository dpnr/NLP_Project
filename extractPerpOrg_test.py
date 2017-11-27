import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.internals import find_jars_within_path
import operator
import custom_wordnet
from nltk.corpus import wordnet


def getTheWords(corpus):

    

    w1_1 = wordnet.synset('group.n.01')
    w1_2 = wordnet.synset('force.n.01')


    try:
        custom_sent_tokenizer = PunktSentenceTokenizer(corpus)
        ps = PorterStemmer()
        tokenized = custom_sent_tokenizer.tokenize(corpus)
        for i in tokenized[:]:

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            

            chunkGram = r"""Chunk: {<NNP|NN|NNS|NNPS>+}"""
            chunks_present = False
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # print chunked
            for subtree in chunked.subtrees():
                if(subtree.label() == 'Chunk'):
                    chunks_present = True
                    chunk = []
                    tokens = []
                    
                    for i in range(0,len(subtree)): 
                        chunk.append(subtree[i])
                        tokens.append(subtree[i][0])
                        
                        # if(subtree[i][0] in ['text','u.s.','officials','official','authorities','military','states','is','troops','police']):

                        #     chunk = []
                        #     break
                        
                        if(i == len(subtree)-1):
                            #it has to be related to person or group
                            
                            try:
                                
                                w2 = wordnet.synset( ".".join([ps.stem(subtree[i][0]),"n.01"]) )
                            except:
                                chunk = []
                                break
                                
                                    
                            # print("\n\nfor "+subtree[i][0])
                            # print(w1_1.wup_similarity(w2))
                            # print(w1_2.wup_similarity(w2))
                            # print "\n\n"
                            # print(w1_3.wup_similarity(w2))
                            # print(w1_4.wup_similarity(w2))
                            # print(w1_5.wup_similarity(w2))
                            # print(w1_7.wup_similarity(w2))
                            if(w1_1.wup_similarity(w2) < 0.80 and w1_2.wup_similarity(w2) < 0.80 ):
                                chunk = []
                                break
                            
                        if(subtree[i][0] == 'path'.upper()):
                            if(subtree[i-1][0] == 'shining'.upper()):
                                
                                chunk = []
                                tokens = [] 
                                chunk.append(subtree[i-1])
                                chunk.append(subtree[i])
                                tokens.append(subtree[i-1][0])
                                tokens.append(subtree[i][0])
                                break
                    

                    
                    if(len(chunk)>1 and len(chunk) <=4):
                        
                        data = " ".join(tokens)
                        return [data.upper()]
                    
            
                                              
    except Exception as e:
        pass



def extracting(filename):
    #we need to do the bio tagging and extract only the  organizations
    organizations = []
    linesOfInterest = []
    

    clean = open(filename).read().replace('\n', ' ')
    
    lines = clean.split(".")

    start = False
    preferedOrg = []
    for line in lines:
        #check for lines of interest
        words = line.split()

        if( "CLAIMED" in words or "REPORTED" in words or "INVOLVED" in words or "MASSACRE" in words or "COMMANDO" in words or "RESPONSIBLE" in words or "ADMIT" in words or "FORCES" in words):
            ##add to the lines of interest
            # print line
            linesOfInterest.append(line)
        
        if("[TEXT]" in words):
            #read from the text
            words = words[words.index("[TEXT]")+1:]
            start = True
            # print "\n#### NEW PARA ####\n"
        if(start):
            for word in words:
                if(word.strip() in custom_wordnet.orgs()):
                    organizations.append(word.strip())

    # print " ".join(linesOfInterest)   
     
    preferedOrg = getTheWords(" ".join(linesOfInterest))
    
    try:
        if(len(preferedOrg)!=0):
            return preferedOrg[0]
        elif(len(organizations) != 0):
            return organizations[0]
        else:
            return "-"
    except:
        if(len(organizations) != 0):
            return list(set(organizations))[0]
        return "-"
        



    # custom_sent_tokenizer = PunktSentenceTokenizer(input_text)

    # tokenized = custom_sent_tokenizer.tokenize(input_text)
    
    # ####stanford stuff
    # st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    # stanford_dir = st._stanford_jar.rpartition('/')[0]
    # stanford_jars = find_jars_within_path(stanford_dir)
    # st._stanford_jar = ':'.join(stanford_jars)
    # #### end of stanford stuff

    # ##How common is the word ???
    # english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    
    # weight = 5

    # try:
    #     for i in tokenized[:]:

    #         words = nltk.word_tokenize(i)
    #         tagged = nltk.pos_tag(words)
    #         # print(st.tag(words))
    #         for in_tuple in st.tag(words):
    #             if(in_tuple[1]=='ORGANIZATION'):
    #                 organizations = giveScore(in_tuple[0],organizations,english_vocab,weight)
    #                 weight -= 1
                    
    # except Exception as e:
    #     pass

    # if(len(organizations) == 0):
    #     return "-"
    # else:
    #     return max(organizations.iteritems(), key=operator.itemgetter(1))[0]

def giveScore(word,organizations,english_vocab,weight):
    ##only if it is not a general word and length doesn't exceed 4
    if((word.lower() not in english_vocab) and len(word)<=4 and len(word)>2 and (word not in english_vocab) and (word not in custom_wordnet.notorgs())):
        if word in organizations:
            organizations[word] += 1
        elif(word in custom_wordnet.orgs()):
            organizations[word] = 10
        else:
            organizations[word] = weight
    return organizations


extracting("testset1-input.txt")


