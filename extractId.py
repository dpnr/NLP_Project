def extracting(filename):
    id = 0
    with open(filename) as file:
        for line in file:
            id = line
            break
    
    return id.strip()
    