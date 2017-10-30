from os import walk

def readFromFolder(path):
    inputFilenames = []
    
    for (dirpath, dirnames, filenames) in walk(path):
        inputFilenames.extend(filenames)
    
    return inputFilenames