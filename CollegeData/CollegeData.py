#Xander Fermier
#1/26/21
#analyzes some data of college diversity

from ast import Not
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
enrollmentIndex = header.index("enrollment")

stateMinorityList = []
stateMinorityInfo = [] #list of groups, with total students
checkedStates = []
stateMinorityInfo.append(header)
# print(stateMinorityInfo[0][stateIndex])
checkedStates.append(stateMinorityInfo[0][stateIndex])

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
    for item in stateMinorityInfo:
        if(item[stateIndex] == row[stateIndex]):
            if not(item[stateIndex] in checkedStates):
                checkedStates.append(item[stateIndex])
            # print(checkedStates)
            # print("name match")
            # item[enrollmentIndex] += row[enrollmentIndex]
            # print(item)
        else:
            # pass
            if not(row[stateIndex] in checkedStates):
                stateMinorityInfo.append(row)
                checkedStates.append(row[stateIndex])
                # print(item[stateIndex])
                # print(row)
            elif(len(checkedStates) == 1 and item[stateIndex] == "state"):
                stateMinorityInfo.append(row)
                 
for row in stateMinorityList:
    row.pop(0)
    row.pop(1)
    # print(row)
print(stateMinorityInfo)
    # row.pop(categoryIndex)
    # row.pop(nameIndex)
    # row.pop(total_enrollmentIndex)
    # newStateIndex = row.index("state")
    # newCategoryIndex = row.index("category")
    # for i in range(len(stateMinorityInfo)):
    #     if(stateMinorityInfo[i][newStateIndex] != row[newStateIndex]):
    #         stateMinorityInfo[i].append(row)
    #     else:
    #         for j in stateMinorityInfo:
    #             if(j[i][newCategoryIndex] == stateMinorityList[i][newCategoryIndex]):
    #                 stateMinorityInfo[i] += stateMinorityList[i]
    #         for j in range(len(stateMinorityList[i])):
    #             stateMinorityInfo[i] += stateMinorityList[i]
    #     print(stateMinorityInfo[i])

# print(stateMinorityInfo)