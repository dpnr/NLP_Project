import nltk
from nltk.tag import StanfordNERTagger
from nltk.internals import find_jars_within_path

st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
stanford_dir = st._stanford_jar.rpartition('/')[0]
stanford_jars = find_jars_within_path(stanford_dir)
st._stanford_jar = ':'.join(stanford_jars)

print(st.tag('Rami Eid is studying at Stony Brook University in NY'.split()))
