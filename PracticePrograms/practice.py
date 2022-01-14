#strings and lists practice
#Xander Fermier
#1/13/22

import os, sys, random

os.system("cls")

stringVar1 = "Hello World"
stringVar2 = 'Hello Universe'
num1 = 8
num2 = 4.5
char = 't'
flag=False

#concatenate the two strings
# print(stringVar1 + " " + stringVar2)
# print(stringVar1 + " " + str(2) + stringVar2 + " " + str(2))

# print(type(num2)) #will return float

# print(stringVar1[0]) #gets first char of a string

# print(stringVar1[3:7]) #returns characters 4-7 (exclusive end, inclusive front)

# print("Hello \t Peter \t \n I am here\\or not\"Goodbye\"")

# for letter in stringVar1:
#     print(letter, end="*")
# print()

# for i in range(8):
#     print(i, end=" ")
# print()

# for i in range(10, 20+1):
#     print(i, end=" ")
# print("\n")

#maxLength = 8
rows = 4
playing = True
while playing:
    rows = int(input("Number of rows? (1-25) (-1 to exit): "))
    if rows == -1:
        break
    if (rows < 1 and rows != -1) or rows > 25:
        print("Invalid number provided. Please pick a number between 1 and 25")
    else:
        spaceCounter = 0
        for i in range(rows):
            for j in range(int(rows)+1 - i):
                print(" ", end = "")
                spaceCounter += 1
            for t in range(int(rows)+2 - spaceCounter):
                print("*", end = "")

            spaceCounter = 0

            print("  ", end = "")

            for x in range(int((rows)+1 -rows)+ i):
                print("*", end = "")
                spaceCounter += 1
            spaceCounter = 0
            print("")
    print()