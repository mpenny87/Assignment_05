#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MPenny, 2021-Aug-07, Updated file for dictionary usage
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

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
        print('Exiting Program...')
        break
    if strChoice == 'l':
        objOne = open(strFileName, "r")
        for line in objOne:
            line = line.strip().split(',')
            dicRow = {'ID' : line[0], 'artist' : line[1], 'album' : line[2]}
            lstTbl.append(dicRow)
            dicRow = {}
        objOne.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        dicRow['ID'] = int(input('Enter an ID: '))
        dicRow['artist'] = input('Enter the Artist\'s Name: ')
        dicRow['album'] = input('Enter the CD\'s Title: ')
        lstTbl.append(dicRow)
        dicRow = {}
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID,Artist Name,Album')
        print('-------')
        for row in lstTbl:
            strID = row['ID']
            strArt = row['artist']
            strAlbum = row['album']
            strDisp = str(strID) + ',' + strArt + ',' + strAlbum
            print(strDisp)
        print('\n')
    elif strChoice == 'd':
        print("enter the number ID of the entry you wish to delete: ")
        delChoice = int(input('Enter ID: '))
        for row in lstTbl:
            if row['ID'] == delChoice:
                del row['ID']
                del row['artist']
                del row['album']
        while {} in lstTbl:
            lstTbl.remove({})
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strID = row['ID']
            strArt = row['artist']
            strAlbum = row['album']
            strFinal = str(strID) + ',' + strArt + ',' + strAlbum + '\n'
            objFile.write(strFinal)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

