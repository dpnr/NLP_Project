
organizations = []
with open('testset1-anskeys.txt') as file:
    for line in file:
        words = line.split()
        
        if("ORG:" in words):
        
            organizations.append(" ".join(words[words.index("ORG:")+1:]))

for org in list(set(organizations)):
    print org


