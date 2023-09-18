def MenuSys(): #Menu function
    MenuInt = int(input("""Press 1 to read data,
Press 2 to Search data,
Press 3 to Enter data,
Press 4 to Exit menu.""")) #User Choice
    if MenuInt == 1:
        FileRead()
    elif MenuInt == 2:
        FileSearch()
    elif MenuInt == 3:
        FileEnter()

    
def FileRead(): #Printing the file
    f = open("SPAFile.csv", "r")#Opening file so it can be read
    print(f.read())
    MenuSys()

def FileSearch(): #Searching the file for name/make
    Request = input("Enter person/make")
    f = open("SPAFile.csv", "r")
    for x in f:
        if Request in x:#Using user input
            print(x)
    MenuSys()#Opening the menu after function is finished

def FileEnter(): #Adding new data to file
    Name = input("Enter name of customer")
    Make = input("Enter make of car")
    Model = input("Enter model of car")
    Colour = input("Enter colour of car")
    Cost = input("Enter cost of car")
    Plate = input("Enter number plate of car")#Entering new data
    f = open("SPAFile.csv", "a")
    f.write(Name)
    f.write(","+Make)
    f.write(","+Model)
    f.write(","+Colour)
    f.write(","+Cost)
    f.write(","+Plate)#Writing to file
    f.write("\n")#Allowing next write to be on next line
    f.close()
    MenuSys()

MenuSys()
