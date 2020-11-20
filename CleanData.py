# Machine Learning - AssessChallenge - F2021
# Removes extra data/cleans data from CSV labour data file
# Author: Ahmed Mohamed

import csv                          #CSV manipulation

#Change As Needed ##
dataFileName = "data.csv"       #Original Data
outputFileName = "newData.csv"  #Clean Data (Updated)
rowStartRemoval = 4288709       #First row to start removing (inclusive)
rowEndRemoval = 4837159         #Last row to end removing (exclusive)
##

data = open(dataFileName,"r")       #Data File

print("Converting Data To List...")
fullList = list( csv.reader(data) )   #Convert data to a list
print("Conversion Complete.",end="\n\n")

condensedList = []                    #New List
condensedList.append(fullList[0])     #Append headers
#print(fullList)

print("Copying Desired Values...")
for x in range(rowStartRemoval,rowEndRemoval):        #(inclusive, exclusive)
    condensedList.append(fullList[x])   #Append values
#print(condensedList)
print("Copy Complete.",end="\n\n")

##I/O
newFile = open('newData.csv', 'w+')    #Create Output File (csv)

print("Writing Output File..")
#WRITE DESIRED VALUES TO OUTPUT FILE (using condensed list)
for word in condensedList:
    newFile.write('"' + word[0] + '","' + word[1] + 
    '","' + word[3] + '","' + word[4] + '","' + word[5] + '","' + word[6] + 
    '","' + word[7] + '","' + word[10] + '","' + word[14] + '"' + '\n')
print("Writing to Output File Complete.",end="\n\n")

newFile.close()         #Close Output File

print("Fully Complete. Script Terminating.")