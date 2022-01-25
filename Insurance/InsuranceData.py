#Xander Fermier
#1/24/22
#Learning how to manipulate and prepare a .csv file with python
#Prepare it by changing male/female and smoker/non-smoker to numeric values
#import csv to read file and use lists

import csv, os

os.system("cls")

file = open("Insurance\insurance_data - insurance.csv")

insuranceFile = csv.reader(file)
header = next(insuranceFile)

insuranceData = []

for row in insuranceFile:
    insuranceData.append(row)
    
    if(row[1] == "female"):
        row[1] = int(0)
        # print(row)
    elif (row[1] == "male"):
        row[1] = int(1)
    else:
        row[1] = int(1)

    if(row[4] == "no"):
        row[4] = int(0)
        # print(row)
    elif (row[4] == "yes"):
        row[4] = int(1)
    else:
        row[4] = int(1)

    # print(row)

#adds insurance cost as final column
for row in insuranceData:
    cost = 250*float(row[0]) - 128*float(row[1]) + 370*float(row[2]) + 425*float(row[3]) + 24000*float(row[4]) - 12500
    cost = int(cost*100)/100
    row.append(cost)
    # print(row)

#create new list with 4 regions insurance cost average

NE = 0.0
SE = 0.0
SW = 0.0
NW = 0.0

NECounter = 0
SECounter = 0
SWCounter = 0
NWCounter = 0

regionAverage = []
for row in insuranceData:
    

    if(row[5] == "northeast"):
        NE += row[len(row) - 1]
        NECounter += 1
        # print(NECounter)
    elif(row[5] == "southeast"):
        SE += row[len(row) - 1]
        SECounter += 1
        # print(SECounter)
    elif(row[5] == "southwest"):
        SW += row[len(row) - 1]
        SWCounter += 1
        # print(SWCounter)
    elif(row[5] =="northwest"):
        NW += row[len(row) - 1] 
        NWCounter += 1
        # print(NWCounter)
    
NE /= NECounter
SE /= SECounter
SW /= SWCounter
NW /= NWCounter
regionAverage.append(NE)
regionAverage.append(SE)
regionAverage.append(SW)
regionAverage.append(NW)
print(regionAverage)

#create a list with only females and another list with only males
#create a list with only smokers, and another with non-smokers

insuranceDataFemale = []
insuranceDataMale = []
insuranceDataSmoker = []
insuranceDataNonSmoker = []

for i in insuranceData:
    if(i[1] == 0):
        insuranceDataFemale.append(i)
    elif(i[1] == 1):
        insuranceDataMale.append(i)
    
    if(i[4] == 0):
        insuranceDataNonSmoker.append(i)
    elif(i[4] == 1):
        insuranceDataSmoker.append(i)