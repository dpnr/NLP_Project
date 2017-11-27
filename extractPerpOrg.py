import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path
import operator
import custom_wordnet


def extracting(filename):
    #we need to do the bio tagging and extract only the  organizations
    organizations = {}
    

    with open(filename) as file:
        input_text = file.read()

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
    
    weight = 5

    try:
        for i in tokenized[:]:

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(st.tag(words))
            for in_tuple in st.tag(words):
                if(in_tuple[1]=='ORGANIZATION'):
                    organizations = giveScore(in_tuple[0],organizations,english_vocab,weight)
                    weight -= 1
                    
    except Exception as e:
        pass

    if(len(organizations) == 0):
        return "-"
    else:
        return max(organizations.iteritems(), key=operator.itemgetter(1))[0]

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
