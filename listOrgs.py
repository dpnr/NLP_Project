
organizations = []
with open('test.test') as file:
    for line in file:
        words = line.split()
        
        if("INDIV:" in words):
        
            organizations.append(" ".join(words[words.index("INDIV:")+1:]))

for org in list(set(organizations)):
    print org


