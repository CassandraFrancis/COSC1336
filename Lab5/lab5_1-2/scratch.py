def getInput(us,metric):
    return float(input("Please enter the " + us + " that you would like converted to " + metric + ": "))

def printError(us,metric):
    print("You have entered an invalid number of " + us + ", please pay attention next time")
    global validEntries
    validEntries = "False"

def errorSwitch(us, metric, entry):
    if(us == "Farenheit"):
        errorCheckF(us, metric, entry)
    else:
        errorCheck(us, metric, entry)

def errorCheckF(us,metric,entry):
    counter = 0
    validEntry = "False"
    while counter < 3 and validEntry == "False":
        if(entry < 1000):
            validEntry = "True"
        else:
            entry = getInput(us,metric)
            counter += 1
    if(counter > 2 and validEntry == "False"):
        printError(us,metric)
    elif(counter <= 3 and validEntry == "True"):
        fahToCel(us,metric,entry)

def errorCheck(us,metric,entry):
    counter = 0
    validEntry = "False"
    while counter < 3 and validEntry == "False":
        if(entry > 0):
            validEntry = "True"
        else:
            entry = getInput(us,metric)
            counter += 1
    if(counter > 2 and validEntry == "False"):
        printError(us,metric)
    elif(counter <= 3 and validEntry == "True"):
        calcSwitch(us,metric,entry)

def printValid(us,metric,entry,result):
    print(entry , " " , us , " is equal to " , result , " " , metric)

def fahToCel(us,metric,entry):
    printValid(us,metric,entry,format(((entry-32)/1.8), ".2f"))

def galToLit(us,metric,entry):
    printValid(us,metric,entry,format(entry*3.78541178, ".2f"))

def milesToKm(us,metric,entry):
    printValid(us,metric,entry,format(entry*1.609344, ".2f"))

def poundsToKilo(us,metric,entry):
    printValid(us,metric,entry,format(entry/2.20462262, ".2f"))

def inchesToCm(us,metric,entry):
    printValid(us,metric,entry,entry*2.54)

def calcSwitch(us,metric,entry):
    if(us == "Gallons"):
        galToLit(us,metric,entry)
    elif(us == "Miles"):
        milesToKm(us,metric,entry)
    elif(us == "Pounds"):
        poundsToKilo(us, metric, entry)
    else:
        inchesToCm(us, metric, entry)

def main():
    global validEntries
    validEntries = "True"
    errorSwitch("Miles", "Kilometers",getInput("Miles", "Kilometers"))
    if validEntries == "True":
        errorSwitch("Farenheit", "Celcius",getInput("Farenheit", "Celcius"))
    if validEntries == "True":
        errorSwitch("Gallons","Liters", getInput("Gallons","Liters"))
    if validEntries == "True":
        errorSwitch("Pounds", "Kilograms",getInput("Pounds", "Kilograms"))
    if validEntries == "True":
        errorSwitch("Inches", "Centimeters",getInput("Inches", "Centimeters"))

main()

