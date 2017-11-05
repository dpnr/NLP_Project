import readWriteFiles as rw_files

def generate(argument):
    answers = {}
    
    files = rw_files.readFromFolder('answers/')
    for filename in files:
        weapons = []
        lines = []
        with open('answers/'+filename) as file:
            lines = file.readlines()
            ids = lines[0].split()
            weapons.append(lines[2].split()[1])
            index = 3
            
            while(lines[index][:4] != "PERP" and index < len(lines) ):
                
                weapons.append(lines[index].strip())
                index += 1

            answers[ids[1]] = ",".join(weapons)
    
    return answers


def printAccuracy(predicted,actual):
    debug = open("debug.log","w")
    ## go over the actual keys and check the values for the corresponding key
    prediction = {"correct": 0,"wrong": 0}
    for key in predicted:
        if(predicted[key] == actual[key]):
            prediction["correct"] += 1
        else:
            prediction["wrong"] += 1
            print >>debug, "\n##### for ID  " + key + "\n"+ "ACTUAL: " + actual[key] + "\n" + "PREDICTED: " + predicted[key] + "\n"
    
    print "accuracy is " + str(prediction["correct"]*100.0/ (len(predicted)) )

            

    

