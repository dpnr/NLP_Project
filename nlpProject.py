import readWriteFiles as rwFiles
import extractId as e_Id
import extractWeapon as e_weapon
import extractIncident as e_incident

path = 'texts/'
filenames = rwFiles.readFromFolder(path)

''' 
    for every file we need to extract the arguments 

'''



for filename in filenames:
    fileArguments = {}
    
    ## Do stuff here to extract the arguments and print it out!!!
    
    fileArguments["id"] = e_Id.extracting(path + filename) 
    #we could directly write a print here instead of adding to results
    print ("ID: "+ fileArguments["id"])
    
    fileArguments["incident"] = e_incident.extracting(path + filename)  ## replace this with some function call to get the right result
    print ("INCIDENT: "+ fileArguments["incident"])
    
    fileArguments["weapon"] =  e_weapon.extracting(path + filename)
    print ("WEAPON: "+ fileArguments["weapon"])
    
    fileArguments["perp indiv"] = "example" ## replace this with some function call to get the right result
    print ("PERP INDIV: "+ fileArguments["perp indiv"])

    fileArguments["perp org"] = "example" ## replace this with some function call to get the right result
    print ("PERP ORG: "+ fileArguments["perp org"])

    fileArguments["target"] = "example" ## replace this with some function call to get the right result
    print ("TARGET: "+ fileArguments["target"])

    fileArguments["victim"] = "example" ## replace this with some function call to get the right result
    print ("VICTIM: "+ fileArguments["victim"])

    print ("") ##line space

    