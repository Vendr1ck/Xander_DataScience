import json
from black import diff
from datetime import date
import pip._vendor.requests as requests
import random
import os

url = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")

data = json.loads(url.text)

wordList = list(data.keys())

triesMax = 10

score = 0

highScore = 0

difficulty = ""

file = open("WordGame\\WordGameScores.txt", "a")
# word = wordList[random.randint(0, len(wordList)-1)]

# print(word[0])

# import os, random
os.system("cls")
word=""
guess=""
record = {"name":"", "score":0, "date":"XXXX-XX-XX", "word":""}
# print(date.today())
def selectWord():
    global word
    # fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    # "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]

    # size= len(fruits)
    # randy= random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)+
    # word=random.choice(fruits)
    global difficulty
    difficulty = input("Number of letters? [5, 7, 9] ")

    word = wordList[random.randint(0, len(wordList)-1)]
    while(len(word) != int(difficulty)):
        word = wordList[random.randint(0, len(wordList)-1)]

def guessFunction():
    global guess
    check=True
    while check:
        try:
            print("\nenter a letter to guess the word ")
            guess=input().lower()
            if guess.isalpha() and len(guess)==1 and not(guess in letterGuessed):
                check=False
            elif(guess in letterGuessed):
                print("Please guess a new letter")
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")
           
def GameReset():
    selectWord()
    global score
    score = 0
    global tries
    tries = 0
    global letterGuessed
    letterGuessed = ""

def LogScore():
    global record
    record["name"] = username
    record["date"] = str(date.today())
    record["score"] = score
    record["word"] = word

    global highScore

    if score > highScore:
        highScore = score

    file.write(json.dumps(record) + "\n")

def Restart():
    replay = input("Would you like to play again? [y/n]").lower()
    if(replay == "y"):
        LogScore()
        GameReset()
    else:
        LogScore()
        global gameOn
        gameOn = False
           
gameOn=True
tries=0
letterGuessed=""
username = input("What is your name? ")

selectWord()
while gameOn:
   
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        # print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    print()
    print("Letters Guessed: " + letterGuessed)
    print("Tries remaining: " + str(triesMax - tries), end="")
    if tries >= triesMax:
        print("\n Sorry run out chances ")
        print("The word was \"" + word + "\".")
        score = 0
        Restart()
        #playGame() ask if they want to play again
    if countLetter == len(word):
        print ("\nYou guessed \"" + word + "\" in " + str(tries) + " tries!")
        score = len(word) * (triesMax - tries) * int(difficulty)
        Restart()
        #Calculate score
        #playGame()
file.close()
print("Thank you for playing, " + username + "! Your high score this session was " + str(highScore) + ".")