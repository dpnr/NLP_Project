
import readWriteFiles as rwFiles
import extractId as e_Id
import extractWeapon as e_weapon
import extractVictims as e_Victims
import extractIncident as e_incident
import eventextract_ML as train_model
import predict



path = 'texts/'
filenames = rwFiles.readFromFolder(path)
weapons = {}
victims = {}

''' 
    for every file we need to extract the arguments 

'''
text_clf=train_model.model()

for filename in filenames:
    fileArguments = {}
    
    ## Do stuff here to extract the arguments and #print it out!!!
    
    fileArguments["id"] = e_Id.extracting(path + filename) 

    #we could directly write a print here instead of adding to results
    print ("ID: "+ fileArguments["id"])


    fileArguments["incident"] = e_incident.extracting(path + filename,text_clf)  ## replace this with some function call to get the right result
    print("INCIDENT: " + fileArguments["incident"])
    
    fileArguments["weapon"] =  e_weapon.extracting(path + filename)
    print ("WEAPON: " + ''.join(fileArguments["weapon"]))
    
    fileArguments["perp indiv"] = "example" ## replace this with some function call to get the right result
    print ("PERP INDIV: "+ fileArguments["perp indiv"])

    fileArguments["perp org"] = "example" ## replace this with some function call to get the right result
    print ("PERP ORG: "+ fileArguments["perp org"])

    # fileArguments["target"] = e_Target.extracting(path + filename) ## replace this with some function call to get the right result
    # victims[fileArguments["id"]] = ",".join(fileArguments["weapon"])
    # print("WEAPON:\t" + "\n\t".join(fileArguments["weapon"]))

    # print ("TARGET: "+ fileArguments["target"])

    fileArguments["victim"] = e_Victims.extracting(path + filename) ## replace this with some function call to get the right result
    victims[fileArguments["id"]] = ",".join(fileArguments["victim"])
    print("VICTIM:\t" + "\n\t\t".join(fileArguments["victim"]))

    print ("") ##line space


    

weapons_ans = predict.generate('weapon')


predict.printAccuracy(weapons,weapons_ans)
