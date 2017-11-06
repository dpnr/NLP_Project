import readWriteFiles as rwFiles
import extractId as e_Id
import extractWeapon as e_weapon
# import extractIncident as e_incident
import extractPerpOrg as e_perporg
import extractPerpIndiv as e_perpindiv
import predict



path = 'texts/'
filenames = rwFiles.readFromFolder(path)
weapons = {}

''' 
    for every file we need to extract the arguments 

'''



for filename in ['TST2-MUC4-0076']:
    fileArguments = {}
    
    ## Do stuff here to extract the arguments and print it out!!!
    
    fileArguments["id"] = e_Id.extracting(path + filename) 

    #we could directly write a print here instead of adding to results
    print ("ID: "+ fileArguments["id"])
    
    fileArguments["incident"] = "example"#e_incident.extracting(path + filename)  ## replace this with some function call to get the right result
    print ("INCIDENT: "+ fileArguments["incident"])
    
    fileArguments["weapon"] =  e_weapon.extracting(path + filename)
    weapons[fileArguments["id"]] = ",".join(fileArguments["weapon"])
    print ("WEAPON: "+ ",".join(fileArguments["weapon"]))
    
    fileArguments["perp indiv"] = e_perpindiv.extracting(path + filename) ## replace this with some function call to get the right result
    print ("PERP INDIV: "+ fileArguments["perp indiv"])

    fileArguments["perp org"] = e_perporg.extracting(path+filename) ## replace this with some function call to get the right result
    print ("PERP ORG: "+ fileArguments["perp org"])

    fileArguments["target"] = "example" ## replace this with some function call to get the right result
    print ("TARGET: "+ fileArguments["target"])

    fileArguments["victim"] = "example" ## replace this with some function call to get the right result
    print ("VICTIM: "+ fileArguments["victim"])

    print ("") ##line space


    

# weapons_ans = predict.generate('weapon')


# predict.printAccuracy(weapons,weapons_ans)

# e_perporg.extracting('texts/DEV-MUC3-0045')
# e_perpindiv.extracting('texts/TST2-MUC4-0076')