import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import custom_wordnet
from nltk.tokenize import PunktSentenceTokenizer

stopwords = list(set(stopwords.words('english')))


def extracting(filename):

    ps = PorterStemmer()
    weapons = []
    weapons_nn = []
    weapon = ""
    with open(filename) as file:
        corpus = file.read().replace('\n',' ').lower()
        
    word_tokens = word_tokenize(corpus)
    filteredCorpus = [ w for w in word_tokens if not w.lower() in stopwords ]
    
    w1 = wordnet.synset('weapon.n.01')
    for index,word in enumerate(filteredCorpus):
        if(word not in ['(','.',',',')'] ):
            if("-" in word ):
                try:
                    
                    words = word.split('-')
                    original = word
                    word = words[1]
                    w2 = wordnet.synset( ".".join([ps.stem(word),"n.01"]) )
                    if(w1.wup_similarity(w2) >= 0.75):
                        weapons.append(original)
                    
                    
                except(Exception):
                    pass
            
            elif(word in custom_wordnet.weapons()):  
                ##see if we can do some regex matchings with the word matching with the custom wordnet
                try:
                    #lets build the corpus
                    corpus = []
                    for i in range(-2,2):
                        corpus.append(filteredCorpus[index+i])

                    corpus = " ".join(corpus)
                    

                    custom_sent_tokenizer = PunktSentenceTokenizer(corpus)
                    tokenized = custom_sent_tokenizer.tokenize(corpus)
                    
                    for i in tokenized[:]:

                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        chunkGram = r"""Chunk: {<RB.?>*<JJ|'car'>+<NNP|NN|NNS|NNPS>+}"""
                        
                        chunkParser = nltk.RegexpParser(chunkGram)
                        chunked = chunkParser.parse(tagged)
                        ##collect the chunks
                        for subtree in chunked.subtrees():
                            if(subtree.label() == 'Chunk'):
                                chunk = []
                                tokens = []
                                
                                for i in range(0,len(subtree)): 
                                    chunk.append(subtree[i])
                                    tokens.append(subtree[i][0])
                                    
                                    if(i == len(subtree)-1):
                                        #it has to be in the weapons
                                        
                                        if(subtree[i][0] in custom_wordnet.weapons() or subtree[i][0] in ["devices"]):
                                            data = " ".join(tokens)
                                        else:
                                            chunk = []
                                            break
                                    elif(i == len(subtree)-2):
                                        if(subtree[i][0] in ["explosive"]):
                                           
                                            data = " ".join(tokens)
                                        else:
                                            continue
                        
                        if(len(chunk)==2 or len(chunk)==3):
                            return [data.upper()]
                        else:
                            weapons.append(word)
                            
                                        


                except:
                    weapons.append(word)
                        
            else:
                try:
                    w2 = wordnet.synset( ".".join([ps.stem(word),"n.01"]) )
                    
                    if(w1.wup_similarity(w2) >= 0.80 ):
                        weapons.append(word)
                except(Exception):
                    pass

            
    
    ## remove the stop words from the corpus
    
    tagged = nltk.pos_tag(weapons)
    
    if(len(tagged) == 0):
        weapons_nn.append('-')
    else:
        for tuplePresent in tagged:
            if(tuplePresent[1] in ['NN','NNS','JJ'] and tuplePresent[0] not in custom_wordnet.notweapons()):
                weapons_nn.append(tuplePresent[0].upper())

    if(len(weapons_nn)==0):
        weapons_nn.append('-')   

    if("EXPLOSIVES" in weapons_nn):
        return ["EXPLOSIVES"]
    elif("BOMBS" in weapons_nn):
        if("BOMB" in weapons_nn):
            weapons_nn.remove("BOMB")
        return list(set(weapons_nn))
    else:
        return list(set(weapons_nn))