def extracting(filename):
    id = 0
    with open(filename) as file:
        for line in file:
            id = line.split()[0]
            break
    
    return id.strip()
    