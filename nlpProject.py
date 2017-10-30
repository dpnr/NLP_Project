import readWriteFiles as rwFiles

filenames = rwFiles.readFromFolder('texts/')

''' 
    for every file we need to extract the arguments 

'''



for filename in filenames:
    fileArguments = {}
    
    ## Do stuff here to extract the arguments and print it out!!!
    
    fileArguments["id"] = "example" ## replace this with some function call to get the right result
    #we could directly write a print here instead of adding to results
    print "ID: "+ fileArguments["id"]
    
    fileArguments["incident"] = "example" ## replace this with some function call to get the right result
    print "INCIDENT: "+ fileArguments["incident"]
    
    fileArguments["weapon"] = "example" ## replace this with some function call to get the right result
    print "WEAPON: "+ fileArguments["weapon"]
    
    fileArguments["perp indiv"] = "example" ## replace this with some function call to get the right result
    print "PERP INDIV: "+ fileArguments["perp indiv"]

    fileArguments["perp org"] = "example" ## replace this with some function call to get the right result
    print "PERP ORG: "+ fileArguments["perp org"]

    fileArguments["target"] = "example" ## replace this with some function call to get the right result
    print "TARGET: "+ fileArguments["target"]

    fileArguments["victim"] = "example" ## replace this with some function call to get the right result
    print "VICTIM: "+ fileArguments["victim"]

    print "" ##line space

    