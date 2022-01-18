#Xander Fermier
#Data Science Program 1/18/22
#Demos multiple string

#from _curses import *
import os, string
#import _curses

os.system("cls")

baseString = "Test String!"
baseStringTabs = "Te\tst\tSt\tri\tng"
baseStringFormat = "The artifact is {years:,} years old. The cost is ${cost:.2f}. This person's BMI is {bmi:.2f}"

#Capitalize
print("Capitalize() Example\n")
print("Base String: " + baseString)
print("With Capitalize() -> " + baseString.capitalize())
print("Converts the string to all uppercase.")
print("====================================================================================")

#Center
print("Capitalize() Example\n")
print("Base String: " + baseString)
print("With Center() -> " + baseString.center(26))
print("Centers the text within the space of x characters. Here it is 26.")
print("====================================================================================")

#Encode
print("Encode() Example\n")
print("Base String: " + baseString)
baseStringEncode = baseString.encode().decode("utf-8")
print("With Encode() -> " + baseStringEncode)
print("Encodes the string. Default encoder is UTF-8")
print("====================================================================================")

#ExpandTabs
print("ExpandTabs() Example\n")
print("Base String: " + baseStringTabs)
print("With ExpandTabs() -> " + baseStringTabs.expandtabs(5))
print("Sets the tab space. Here it is set to 5.")
print("====================================================================================")

#Format
print("Format() Example\n")
print("Base String: " + baseStringFormat)
print("With Format() -> " + baseStringFormat.format(years = 1000000, cost = 100, bmi = 20))
print("Allows you to format strings. Would recommend checking W3 Schools for a list of options.")
print("====================================================================================")

#Index
print("Index() Example\n")
print("Base String: " + baseString)
print("With Format() -> ", end = "")
print(str(baseString.index("S")))
print("Returs the index of the character you search for.")
print("====================================================================================")

#IsAlpha
print("IsAlpha() Example\n")
print("Base String: " + baseString)
print("With isalpha() -> ", end = "")
print(baseString.isalpha())
print("Returs true if all characters are letters.")
print("====================================================================================")

#IsDigit
print("IsDigit() Example\n")
print("Base String: " + baseString)
print("With isdigit() -> ", end = "")
print(baseString.isalpha())
print("Returs true if all characters are numbers.")
print("====================================================================================")

#IsLower
print("IsLower() Example\n")
print("Base String: " + baseString)
print("With islower() -> ", end = "")
print(baseString.islower())
print("Returs true if all letters are lowercase.")
print("====================================================================================")

#IsPrintable
print("IsPrintable() Example\n")
print("Base String: " + baseString)
print("With isprintable() -> ", end = "")
print(baseString.isprintable())
print("Returs true if all characters are printable.")
print("====================================================================================")

#IsTitle
print("IsTitle() Example\n")
print("Base String: " + baseString)
print("With istitle() -> ", end = "")
print(baseString.istitle())
print("Returs true if string follows the formatting of a title.")
print("====================================================================================")

#join
print("Join() Example")
testTuple = ("str1", "str2", "str3")
testStringJoin = "example".join(testTuple)
print("\"str1\", \"str2\", \"str3\"")
print("With join() -> ", end = "")
print(testStringJoin)
print("Appends the contents of an iterable to the string.")
print("====================================================================================")

#lower
print("lower() Example\n")
print("Base String: " + baseString)
print("With lower() -> ", end = "")
print(baseString.lower())
print("Returs true if string follows the formatting of a title.")
print("====================================================================================")