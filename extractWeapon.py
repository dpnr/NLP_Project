import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import custom_wordnet

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
    for word in filteredCorpus:
        if(word not in ['(','.',',',')'] ):
            if("-" in word ):
                try:
                    
                    words = word.split('-')
                    original = word
                    word = words[1]
                    w2 = wordnet.synset( ".".join([ps.stem(word),"n.01"]) )
                    if(w1.wup_similarity(w2) >= 0.80):
                        weapons.append(original)
                        
                except(Exception):
                    pass
            elif(word in custom_wordnet.weapons()):  
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
            if(tuplePresent[1] in ['NN','NNS','JJ'] and tuplePresent[0] not in ['weapon','instrument','key','trap','weapons','instrumental']):
                weapons_nn.append(tuplePresent[0].upper())

    if(len(weapons_nn)==0):
        weapons_nn.append('-')      
    return list(set(weapons_nn))