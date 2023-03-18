from objects import *
from settings import *
import os
import random


def clear():
    os.system('cls')


def askQuestion(message, options):
    options = options
    print(message)
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i] + "\n")
    numOptions = []
    viableAns = False
    while True:
        answer = input("What do you do? (Enter The Number)")
        for i in range(len(options)):
            numOptions.append(i + 1)
            if answer == str(numOptions[i]):
                viableAns = True

        if viableAns == False:
            print("That was not a viable answer")
            input()
            continue
        else:
            break
    return answer

def askNumberQuestion(message,allowNegative = False):

    while True:
        negative = False
        answer = input(message)
        for i in answer:
            if i == '-':
                negative = True
                answer = answer.strip('-')
        if(answer.isnumeric()):
            break
        else:
            continue
    answer = int(answer)
    if(negative):
        if(allowNegative):
            answer *= -1

    return int(answer)



class App():
    def __init__(self):
        self.running = True

        self.characterList = []
        self.diceTower = []
        for i in diceOptions:
            self.diceTower.append(Dice(i))


        self.start_menu()

    def start_menu(self):
        clear()
        answer = askQuestion("DND Encounter Builder",["Create Encounter","Roll Dice","Quit"])
        if answer == "1":
            self.start_encounter()
        elif answer == "2":
            self.roll_dice()
        else:
            quit()
    def start_encounter(self):
        clear()
        charRange = askNumberQuestion("How many characters are included (including players and NPCs)")
        self.characterList = []
        for i in range(charRange):
            name = input(("Name for Character", i+1))
            health = askNumberQuestion(("Health for Character", i+1))
            order = askNumberQuestion(("Initiative Order for Character", i+1))
            self.characterList.append(Character(name,health,order))
        self.bubble_sort()
        self.main()

    def bubble_sort(self):
        n = len(self.characterList)

        for i in range(n):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(n - i - 1):
                if  self.characterList[j].order < self.characterList[j + 1].order:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    self.characterList[j],  self.characterList[j + 1] =  self.characterList[j + 1],  self.characterList[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                break

    def main(self):
        clear()
        print()
        print("Order | Name | Health")
        for char in self.characterList:
            print(char.order,"|",char.name,"|",char.health)
        print()
        print()
        answer = askQuestion("Select what you would like to do",["Change Character Health","Roll Dice","Quit"])
        if answer == "1":
            self.adjust_health()
        elif answer == "2":
            self.roll_dice()
        else:
            quit()
        self.main()

    def adjust_health(self):
        clear()
        characterNames = []
        for char in self.characterList:
            characterNames.append(char.name)
        answer = askQuestion("Which Health would you like to change?",characterNames)
        answer = int(answer)
        modify = askNumberQuestion(("How much health would you like to add/subtract from",str(characterNames[answer-1])+"? (Use negatives to subtract, positives to add)"),True)
        self.characterList[answer-1].health += int(modify)
    def roll_dice(self):
        clear()
        diceRange = askNumberQuestion("How much dice would you like to roll?",True)
        print("Dice Options \n _____________")
        diceNames = []
        for dice in self.diceTower:
            print(dice.name)
            diceNames.append(dice.name)
        total = 0
        values = []
        for i in range(diceRange):
            clear()
            answer = askQuestion(("Which dice would you like to use for Dice "+str(i+1)+"?"),diceNames)
            answer = int(answer)
            value = self.diceTower[answer-1].roll()
            total += value
            values.append(value)

        print("Results:")
        for i in values:
            print(i)
        print("Total:",total)
        input()
a = App()

