import readWriteFiles as rwFiles
import extractId as e_Id
import extractWeapon as e_weapon
# import extractIncident as e_incident
import extractPerpOrg as e_perporg
import extractPerpIndiv as e_perpindiv
import extractVictims as e_Victims
import extractIncident as e_incident
import eventextract_ML as train_model
import predict
import sys



path = 'texts/'
filenames = rwFiles.readFromFolder(path)
weapons = {}
victims = {}

''' 
    for every file we need to extract the arguments 
'''

allFiles = rwFiles.readFromFolder(path)
testFiles = []
for filename in allFiles:
    if(filename[0:3]=='TST'):
        testFiles.append(filename)


first = False
testFiles.sort()
testFile = sys.argv[1]
testData = []
with open(testFile) as file:
    lines = file.readlines()
    # print lines
    para = []
    para.append(lines[0])
    for line in lines[1:]: 
        if("DEV-MUC3-" in line or  "TST1-MUC3-" in line or "TST2-MUC4-" in line and first):
            testData.append(" ".join(para))
            para = []
            para.append(line)
        else:
            para.append(line)
            first= True
    #for the last para we need to append it to the data
    testData.append(" ".join(para))

text_clf=train_model.model()

# print testData


for data in testData:
    fileArguments = {}
    
    ## Do stuff here to extract the arguments and print it out!!!
    with open('temfile.txt','w') as temp:
        temp.write(data)
        
    fileArguments["id"] = e_Id.extracting('temfile.txt') 
    #we could directly write a print here instead of adding to results
    print ("ID:\t"+ fileArguments["id"])
    
    fileArguments["incident"] = e_incident.extracting('temfile.txt',text_clf)#e_incident.extracting(path + filename)  ## replace this with some function call to get the right result
    #fileArguments["incident"] = "-"
    print ("INCIDENT:\t"+ fileArguments["incident"])
    
    fileArguments["weapon"] =  e_weapon.extracting('temfile.txt')
    weapons[fileArguments["id"]] = ",".join(fileArguments["weapon"])
    print ("WEAPON:\t"+ "\n\t".join(fileArguments["weapon"]))
    
    
    fileArguments["perp indiv"] = e_perpindiv.extracting('temfile.txt') ## replace this with some function call to get the right result
    print ("PERP INDIV:\t"+ fileArguments["perp indiv"])

    fileArguments["perp org"] = e_perporg.extracting('temfile.txt') ## replace this with some function call to get the right result
    print ("PERP ORG:\t"+ fileArguments["perp org"])

    fileArguments["target"] = "-" ## replace this with some function call to get the right result
    print ("TARGET:\t"+ fileArguments["target"])


    # print ("TARGET: "+ fileArguments["target"])

    fileArguments["victim"] = e_Victims.extracting('temfile.txt') ## replace this with some function call to get the right result
    victims[fileArguments["id"]] = ",".join(fileArguments["victim"])
    print("VICTIM:\t" + "\n\t".join(fileArguments["victim"]))

    print ("\n") ##line space


    

# weapons_ans = predict.generate('weapon')


# predict.printAccuracy(weapons,weapons_ans)

# e_perporg.extracting('texts/DEV-MUC3-0045')
# e_perpindiv.extracting('texts/TST2-MUC4-0076')
