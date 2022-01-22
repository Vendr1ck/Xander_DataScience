#Xander Fermier
#1/20/22
#practice with lists, tuples, sets, and dictionaries

import math
import os

os.system("cls")

# fruits = ["apples", "oranges", 1, 7, "banana"]
# print(len(fruits))

# for elem in fruits:
#     print(type(elem))

# myList = list((3, 5, 6)) #typecasts a tuple into a list
# print(myList)

# fruits.append("orange")
# fruits.insert(3, "kiwi")#shoves the elements in the slot to the right
# print(fruits)

#finds the first instance of 20 and replaces it with 200
list1 = [15, 100, 154, 20, 253, 530, 203]
print(list1)
list1[list1.index(20)] = 200
print(list1)

print("\n==========================================================\n") #formatting break

#removes all instances of 20
list2 = [5, 20, 15, 20, 25, 50, 20]
print(list2)
elmntCheck = True
while(elmntCheck):
    try:
        list2.remove(20)
    except:
        elmntCheck = False
print(list2)

print("\n==========================================================\n") #formatting break

#removes all intances of "" from the list
def emptyRemove(str):
    if(str == ""):
        return False
    else:
        return True

list3 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list3)
list4 = filter(emptyRemove, list3)
for x in list4:
    print(x, end=" ")

print("\n==========================================================\n") #formatting break

#appends a value at a specified location
list5 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list5)
# print(list5[2])
# print(list5[2][1])
# # print(list5.index(300))
# print(isinstance(list5[2], list))

for i in list5:
    # print(i)
    if(isinstance(list5[list5.index(i)], list)):
        for j in list5[list5.index(i)]:
            if(isinstance(list5[list5.index(i)][list5[list5.index(i)].index(j)], list)):
                list6 = list5[list5.index(i)][list5[list5.index(i)].index(j)]
                list6.append(7000)
                # list5[i][j][list5[i][j].index(6000)+1] = 7000

print(list5)

print("\n==========================================================\n") #formatting break

#same as previous but with strings
list7 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]

print(list7)

for i in list7:
    # print(i)
    if(isinstance(list7[list7.index(i)], list)):
        for j in list7[list7.index(i)]:
            if(isinstance(list7[list7.index(i)][list7[list7.index(i)].index(j)], list)):
                for y in list7[list7.index(i)][list7[list7.index(i)].index(j)]:
                    if(isinstance(list7[list7.index(i)][list7[list7.index(i)].index(j)][list7[list7.index(i)][list7[list7.index(i)].index(j)].index(y)], list)):
                        list8 = list7[list7.index(i)][list7[list7.index(i)].index(j)][list7[list7.index(i)][list7[list7.index(i)].index(j)].index(y)]
                        list8.extend(sublist)

print(list7)

print("\n==========================================================\n") #formatting break

#prints one list in standard order and the other in reverse order (assumed both list are the same length?)
list9 = [10, 20, 30, 40]
list10 = [100, 200, 300, 400]

for i in list9:
    # print(list9.index(i))
    # print(len(list10))
    print(str(list9[list9.index(i)]) + " " + str(list10[len(list10) - 1 - list9.index(i)]))

print("\n==========================================================\n") #formatting break
#combines two lists by the items at different indexes
list11 = ["M", "na", "i", "Ke"]
list12 = ["y", "me", "s", "lly"]
list13 = []

print(list11)
print(list12)

for i in list11:
    list13.append(list11[list11.index(i)] + list12[list11.index(i)])

print(list13)

print("\n==========================================================\n") #formatting break
#returns every element in the list as its square
list14 = [1, 2, 3, 4, 5, 6, 7]
list15 = []

print(list14)

for i in list14:
    list15.append(int(math.pow(list14[list14.index(i)], 2)))

print(list15)

print("\n==========================================================\n") #formatting break
#separates the string into elements by words
phrase = " The best class in Greenhill is Data Science"
phrase2 = phrase + " "
spaces = []
words = []
print(phrase)

for i in range(len(phrase2)):
    if(phrase2[i] == " "):
        spaces.append(phrase2.index(" "))
        phrase2 = phrase2.replace(" ", "!", 1)
# print(phrase2)
# print(len(spaces))
for i in range(1, len(spaces)):
    # print(spaces[i])
    # print(str(spaces[i-1]) + " " + str(spaces[i])) 
    words.append(phrase[spaces[i-1]+1 : spaces[i]])

print(words)