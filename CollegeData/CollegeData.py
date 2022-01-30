#Xander Fermier
#1/26/21
#analyzes some data of college diversity

from ast import Not
from asyncio.windows_events import NULL
import csv, os

os.system("cls")

file = open("CollegeData\diversity_school.csv", encoding="utf-8")
finalFile = open("CollegeData\FinalCollegeData.txt", "w")

collegeFile = csv.reader(file)
header = next(collegeFile)

#uses these in the for loops
categoryIndex = header.index("category")
stateIndex = header.index("state")
nameIndex = header.index("name")
total_enrollmentIndex = header.index("total_enrollment")
enrollmentIndex = header.index("enrollment")

stateMinorityList = []
# stateMinorityInfo = [] #list of groups, with total students
checkedStates = []
statesInfo = []

stateSchools = {}
stateEthnic = {}
stateEthnicCheck = []
stateTotal = {}
# print(stateMinorityInfo[0][stateIndex])
# checkedStates.append(stateMinorityInfo[0][stateIndex])

for row in collegeFile:
    #filters out categories that do not contribute to the total
    if(row[categoryIndex] == "Women"):
        continue
    elif(row[categoryIndex] == "Unknown"):
        continue
    else:
        stateMinorityList.append(row)
        # print(row)

counter = 0

for i in range(0, len(stateMinorityList)-9): #each state and the 8 minorities plus total category
    # for j in range(9):
    if not (stateMinorityList[i][stateIndex] in checkedStates):
        for j in range(9):
            stateInstance = []
            stateInstance.append(stateMinorityList[i+j][stateIndex])
            stateInstance.append(stateMinorityList[i+j][categoryIndex])
            stateInstance.append(int(stateMinorityList[i+j][enrollmentIndex]))
            statesInfo.append(stateInstance)
            checkedStates.append(stateMinorityList[i+j][stateIndex])
        stateSchools[stateMinorityList[i][stateIndex]] = 1
        stateEthnic[stateMinorityList[i][stateIndex]] = ""
        stateTotal[stateMinorityList[i][stateIndex]] = stateMinorityList[i+8][enrollmentIndex]
    else:
        if not(stateMinorityList[i][categoryIndex] == "Total Minority"):
            infoIndex = 0
            for item in statesInfo:
                if(stateMinorityList[i][stateIndex] in item):
                    infoIndex = statesInfo.index(item)
                    break
            for j in range(9):
                statesInfo[infoIndex + j][2] += int(stateMinorityList[i + j][enrollmentIndex])
        stateSchools[stateMinorityList[i][stateIndex]] += 1

currentLargest = 0
for i in range(len(statesInfo)-9):
    if not(statesInfo[i][0] in stateEthnicCheck):
        for j in range(8):
            if(statesInfo[i+j][2] > currentLargest):
                currentLargest = statesInfo[i+j][2]
                stateEthnic[statesInfo[i+j][0]] = statesInfo[i+j][1]
        stateEthnicCheck.append(statesInfo[i][0])
        currentLargest = 0

for i in range(len(statesInfo)):
    print(statesInfo[i])

print("====================================================")
print(stateSchools)

print("====================================================")
print(stateEthnic)

print("====================================================")
header.append("percentage")
finalFile.write(str(header) + "\n")
for i in range(len(stateMinorityList)):
    instance = []
    instance.extend(stateMinorityList[i])
    instanceString = str((int(stateMinorityList[i][enrollmentIndex])/int(stateTotal[stateMinorityList[i][stateIndex]]))*100) + "%"
    instance.append(instanceString)
    finalFile.write(str(instance) + "\n")
finalFile.close()

# for row in stateMinorityList:
#     if(stateMinorityList[stateIndex])

# for row in stateMinorityList:
# #makes a list based on states
# # for item in stateMinorityInfo:
#     if(statesInfo[stateIndex] == row[stateIndex]):
#         if (statesInfo[counter][0] in checkedStates):
#             statesInfo[statesInfo.index(row[categoryIndex])][2] += item[enrollmentIndex]
#             # print(statesInfo)
#         else:
#             stateInstance = []
#             stateInstance.append(item[stateIndex])
#             stateInstance.append(item[categoryIndex])
#             stateInstance.append(item[enrollmentIndex])
#             statesInfo.append(stateInstance)
#             checkedStates.append(item[stateIndex])
#         # print(checkedStates)
#         # print("name match")
#         # item[enrollmentIndex] += row[enrollmentIndex]
#         # print(item)
#     else:
#         # pass
#         if not(row[stateIndex] in checkedStates):
#             stateMinorityInfo.append(row)
#             checkedStates.append(row[stateIndex])
#             # print(item[stateIndex])
#             # print(row)
#         elif(len(checkedStates) == 1 and item[stateIndex] == "state"):
#             stateMinorityInfo.append(row)
#     counter += 1

# print(statesInfo)  
# for row in stateMinorityList:
#     pass
    
    # row.pop(0)
    # row.pop(1)
    # print(row)
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