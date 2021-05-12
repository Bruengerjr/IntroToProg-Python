# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Bruenger,5/7/2021,Added code to complete assignment 5
# Bruenger,5/10/2021,Added code to Option 1, 2, and 4
# Bruenger,5/11/2021,Added code to Option 3 and 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# File to List
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row)    # Returns a list!
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        dicRow = str(dicRow).replace("{", "(")
        dicRow = str(dicRow).replace("}", ")")
        dicRow = str(dicRow).replace("'", "")
        print()
        print("\t The record " + dicRow + " was added!")
        # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for row in lstTable:
            print(row)    # Returns a list!
        strRemove = input("Choose a Task to Delete: ")
        for dicRow in lstTable:
            if strRemove.lower() == dicRow["Task"].lower():
                lstTable.remove(dicRow)
                dicRow = str(dicRow).replace("{","(")
                dicRow = str(dicRow).replace("}",")")
                dicRow = str(dicRow).replace("'", "")
                print()
                print("\t The record " + dicRow + " was deleted!")
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        objFile.close()
        print("\tData saved to file!")
       #continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thanks for using ToDo!")
        break  # and Exit the program
