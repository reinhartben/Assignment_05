#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# BReinhart, 2021-Feb-13, Modified existing code to use a list of dictionaries
# BReinhart, 2021-Feb-14, Added functionality for loading existing data and deleting an entry
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dictRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
loadedData = False # tracks if we loded data from an existing file. 
                   # Used to determine if we should overwrite current text or add to file

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        loadedData = True
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID\t| CD Title\t| Artist')
        for row in lstTbl:
            print(*row.values(), sep = '\t| ')
        print()
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        deleteID = int(input('What ID would you like to delete? ').strip())
        idIn = False
        for row in lstTbl:
            if row['id'] == deleteID:
                lstTbl.remove(row)
                idIn = True
                break
        if not idIn:
            print('This ID is not in your inventory!')
        print()
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        if loadedData:
            objFile = open(strFileName, 'w') # overwrite data if we loaded existing data
        else:
            objFile = open(strFileName, 'a') # add to file if we did not load existing data
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

