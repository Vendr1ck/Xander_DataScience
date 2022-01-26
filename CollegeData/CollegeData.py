#Xander Fermier
#1/26/21
#analyzes some data of college diversity

import csv, os

os.system("cls")

file = open("CollegeData\diversity_school.csv", encoding="utf-8")

collegeFile = csv.reader(file)
header = next(collegeFile)

#uses these in the for loops
categoryIndex = header.index("category")
stateIndex = header.index("state")
nameIndex = header.index("name")
total_enrollmentIndex = header.index("total_enrollment")

stateMinorityList = []
stateMinorityInfo = [[]] * 50 #list of groups, with total students

for row in collegeFile:
    #filters out categories that do not contribute to the total
    if(row[categoryIndex] == "Women"):
        continue
    elif(row[categoryIndex] == "Unknown"):
        continue
    else:
        stateMinorityList.append(row)
        # print(row)

for row in stateMinorityList:
    #makes a list based on states
    row.pop(categoryIndex)
    row.pop(nameIndex)
    row.pop(total_enrollmentIndex)
    newStateIndex = row.index("state")
    newCategoryIndex = row.index("category")
    for i in range(len(stateMinorityInfo)):
        if(stateMinorityInfo[i][newStateIndex] != row[newStateIndex]):
            stateMinorityInfo[i].append(row)
        else:
            for j in stateMinorityInfo:
                if(j[i][newCategoryIndex] == stateMinorityList[i][newCategoryIndex]):
                    stateMinorityInfo[i] += stateMinorityList[i]
            for j in range(len(stateMinorityList[i])):
                stateMinorityInfo[i] += stateMinorityList[i]
        print(stateMinorityInfo[i])

# print(stateMinorityInfo)