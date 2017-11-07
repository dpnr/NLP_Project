from os import walk

def readFromFolder(path):
    inputFilenames = []
    
    for (dirpath, dirnames, filenames) in walk(path):
        inputFilenames.extend(filenames)
    
    return inputFilenames

def createOutputFile(path):
    files = readFromFolder(path)
    testfiles = []
    for filename in files:
        if(filename[0:3]=="TST"):
            testfiles.append(filename)

    testfiles.sort()
        
    for filename in testfiles:
        with open(path+filename) as file:
            print(file.read())


