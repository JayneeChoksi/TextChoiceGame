import time
import sys
import pickle

import matplotlib.pyplot as plt

maindict = {"name": [], "try": [], "win": [],"stateHistory":[]}
start_time = time.time()
userDict = {'user': 'null', 'win': 0, 'try': 0, 'item': 0, 'time': 0}
listOfStates = []
historyOfStates = {}

def dead():
    listOfStates.append(7)
    a = userDict.get('try')
    a = a + 1
    userDict.update({'try': a})
    print("Game Over")
    length = len(historyOfStates)
    old_list = list(listOfStates)
    historyOfStates.update({length+1 : old_list})
    playagain()


def fight():
    listOfStates.append(2)
    print("Oh so you think that you are a superhero and want to battle. Try your luck.")
    print("Go ahead and choose how you want to fight??")
    print("1. Hand on Hand combat with the police")
    print("2. Use the screw driver you have")
    print("3. Get on the car next to you")
    print("4. Chicken out like you always do")
    while True:
        try:
            fight_pick = int(input("Select your choice: "))
            if fight_pick >= 5:
                print ("Enter Valid Input")
            else:
                print("Got Your Ass Kicked")
                dead()
        except Exception:
            print("Invalid Input")



def door1():
    listOfStates.append(3)
    print("Entered the room. \nThe house is a maze. It is the room where it all started. \n Being a thief what are you going to do?")
    print("1. Talk to the grandpa")
    print("2. Look through the closet that you did not notice earlier")
    print("3. See the painting")
    print("4. Escape through the window")
    while True:
        try:
            door2_pick = int(input("Think carefully and select: "))
            if door2_pick == 1:
                print("Yeah talk to the grandpa good idea")
                print("Wasted 10 seconds")
            elif door2_pick == 2:
                print("Looking through the closet")
                closet()
            elif door2_pick == 3:
                print("It is awesome painting")
                print("Wasted 10 seconds")
            elif door2_pick >= 5:
                print("Enter valid input")
            else:
                print("You took a heavy blow")
                dead()
        except Exception:
            print("Invalid Input")


def closet():
    listOfStates.append(6)
    print("So you want to steal something. Looking through the closet......")
    print("You find multiple things in the closet, what are you going to take?")
    print("1. Key")
    print("2. A bag")  # bag contains gems just a suspense
    print("3. Stick")
    print("4. Box")
    base = 0
    while True:
        try:
            closet_pick = int(input("Choose wisely :"))
            if closet_pick == 2:
                it1 = userDict.get('item')
                it1 = it1 + 1000
                userDict.update({'item': it1})
                print("You hear a loud sound of breaking the door")
                print("Run to the hallway")
                hallway_1(base)
            elif closet_pick == 4:
                it1 = userDict.get('item')
                it1 = it1 + 500
                userDict.update({'item': it1})
                print("You hear a loud sound of breaking the door")
                print("Run to the hallway")
                hallway_1(base)
            elif closet_pick >= 5:
                print("Enter Valid Input")
            else:
                print("You hear a loud sound of breaking the door")
                print("Run to the hallway")
                hallway_1(base)
        except Exception:
            print("Invalid Input")



def hallway_1(base):
    listOfStates.append(1)
    print("You got what you wanted now choose your next step.\nsAct fast:")
    print("1: Fight with the police")
    print("2: Head to the Kitchen")
    if base == 0:
        print("3: Run to the basement door")
    while True:
         try:
            pick1 = int(input("Act fast: "))  # goes on a loop if the user does not give the correct input
            if pick1 == 1:
                fight()  # opens the fight function
            elif pick1 == 2:
                print("Went to the kitchen")
                kitchen1()  # opens the staircase function
            elif pick1 == 3:
                print("The basement is dark cannot go in")
                base += 1
         except Exception:
             print("Invalid input")


def kitchen1():
    listOfStates.append(4)
    print("Hurry up the officers are on you")
    print("You see:")
    print("1. Upper drawer")
    print("2. Lower drawer")
    print("3. Dishwasher")
    print("4. Door")
    while True:
        try:
            kit_pick = int(input("Choose ASAP: "))
            if kit_pick == 1 or kit_pick == 2:
                print("Found nothing")
            elif kit_pick == 4:
                print("Cannot open the door")
            else:
                print("Open the dishwasher and got a torch")
                print("You found a another way to the basement")
                base()
        except Exception:
            print("Invalid Input")


def kitchen():
    listOfStates.append(4)
    print("1. You see a back door")
    print("2. Could go back to hallway")
    print("3. Can just surrender if you want")
    print("4. Eat some leftovers")
    while True:
        try:
            kit = int(input("Select fast:"))
            if kit == 1:
                print("Cannot open it")
            elif kit == 2:
                base = 0
                hallway(base)
            elif kit == 3:
                dead()
            elif kit == 4:
                dead()
            else:
                print("Enter valid input")
        except Exception:
            print("Invalid Input")


def hallway(base):
    listOfStates.append(1)
    print("You are now in the hallway.")
    print(
        "The police will arrive at any point of time and you need to get out safely. Your mind is ticking at faster pace and finding ways to escape.")
    print("Choose the option you want to do:")
    print("1: Wait and fight with the police  ")
    print("2: Escape through the door you find next to you ")
    print("3: Head to the Kitchen")
    if base == 0:
        print("4: Run to the basement door")
    # while pick != "1" and pick != "2" and pick != "3" and pick != "4":
    #     pick = raw_input("Act fast: ")  # goes on a loop if the user does not give the correct input
    #     pick = str(pick)
    while True:
        try:
            pick = int(input("Act fast: "))
            if pick == 1:
                fight()  # opens the fight function
            elif pick == 2:
                door1()  # opens the staircase function
            elif pick == 3:
                kitchen()  # opens the kitchen function
            elif pick == 4:
                print("This might be your unlucky day. The basement door is locked")
                base += 1
            else:
                print("Enter valid input")
        except Exception:
            print("Invalid input")


def base():
    listOfStates.append(5)
    print("The door opened")
    print("You use the torch and move down to the basement")
    print("You see")
    print("1. Small window where you can escape")
    print("2. Go back up the stairs")
    print("3. Hide in the basement")
    while True:
        try:
            pick2 = int(input("Select: ") ) # goes on a loop if the user does not give the correct input

            if pick2 == 4:
                print("Enter valid input")
            elif pick2 == 1:
                win()
            elif pick2 == 3:
                print ("Keep hiding you got caught")
                dead()
            elif pick2 == 2:
                dead()
            else:
                print("Enter valid input")
        except Exception:
            print("Invalid input")


def win():
    listOfStates.append(8)
    w = userDict.get('win')
    w = w + 1
    userDict.update({'win': w})
    t = userDict.get('try')
    t = t + 1
    userDict.update({'try': t})
    length = len(historyOfStates)
    old_list = list(listOfStates)
    historyOfStates.update({length + 1: old_list})
    print("You survived the game")
    print("Congrats For Winning the game")
    playagain()


def intro():
    print('You are stuck with your life as a thief and you decide to rob a house and you break in to the house through the window')
    print("You see an old man snorting and having a good night sleep. \nYou examine the room and see a locker at the other end of the room. You slowly pass through him and move forward to the locker.")
    print("You carefully open the locker...")
    print(".")
    print(".")
    print(".")
    print("Locker is empty !!!!!!!!!")
    print("You triggered the alarm!!!!!!")
    print ("You go running through the first door you see and enter into the hallway")
    base = 0
    hallway(base)

# Function to ask user if he wants to play again
def playagain():
    # print(userDict)
    print('State: ')
    print( listOfStates)
    print('History of states: ')
    print(historyOfStates)
    while True:
        try:
            new_user = int(input("Are you a new user? \n 1. Yes \n 2. No\nChoose: "))
            if new_user == 1:
                pkl_file = open('GameHistory.pkl', 'rb')
                maindict = pickle.load(pkl_file)
                maindict['name'].append(userDict['user'])
                maindict['try'].append(userDict['try'])
                maindict['win'].append(userDict['win'])
                maindict['stateHistory'].append(historyOfStates)
                output = open('GameHistory.pkl', 'wb')
                pickle.dump(maindict, output)
                output.close()
                pkl_file.close()

                nameArray = maindict['name']
                tryArray = maindict['try']
                winArray = maindict['win']
                plt.plot(nameArray, tryArray, color='blue')
                plt.plot(nameArray, winArray, color='orange')
                plt.xlabel('Users')
                plt.ylabel('')
                plt.title('Try and Win of the user')
                plt.show()

                userDict['try'] = 0
                userDict['win'] = 0
                del listOfStates[:]


                print(maindict)
                historyOfStates.clear()
                newuser()
            else:
                print("Do you want to play again? \n 1. Yes \n 2. No")
                while True:
                    try:
                        play = int(input("Choose: "))
                        if play == 1:
                            intro()
                        else:
                            end_time = time.time()
                            tie = end_time - start_time
                            userDict.update({'time': tie})
                            print(userDict)
                            sys.exit()
                    except Exception:
                        print("Invalid Input")
        except Exception:
            print("Invalid Input")

# Function to get user name
def newuser():
    userDict['user'] = input("Enter Your name: ")
    intro()  # Introduction to the game

newuser()

