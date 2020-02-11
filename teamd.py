from time import *

roomArray = []
itemArray = []
inventoryArray = []

global bossDead
bossDead = False
global passComplete
passComplete = False


for i in range(999):
    roomArray.append(False)
for i in range(999):
    itemArray.append(False)


roomArray[102] = "You are standing in the corner of the dark prison cell. \nTo the east is a bed. To the south is a toilet."
roomArray[103] = "You are now infront of your bed. The matress is made out of cardboard, and the pillow is a stuffed aligator. \nTo the west is another part of your cell. To the south is the cell door."
roomArray[202] = "Here is your toilet, or rather your bucket. You have fond memories of using this against the gaurd. \nTo the north is the cell corner. To the east is the cell door."
roomArray[203] = "The cell door is open, so it must be break time. You can continue east down the hallway towards the mess. \nTo the north is your bed, and to the west is the toilet."
roomArray[303] = "You now find yourself in a damp hall with a flickering overhead light.\nHeading east will have you in the mess hall. Going west leads back to the cell."
roomArray[505] = "You are in the guard office, you definetly should not be in here. To the south is a messy desk and computer, and to the east is calendar and posters of old movies. "
roomArray[506] = "A calendar on the wall has some of the days crossed off, there is a poster for Top Gun. To the south is a mini fridge, to the west is the door to the mess hall."
roomArray[605] = "There is a desk in front of you, it is covered in papers and some empty chip bags. The compter on the desk is displying the camera feed from out side. To the north is the door to the mess hall, to the east is a mini fridge."
roomArray[606] = "In front of you is a mini fridge that is puring loudly. To the north is a calendar and old movie posters, to the west is a messy desk and computer."
roomArray[402] = "To the north and west, there are walls. To the east, you see a tall figure lurking in the shadows. To the south, there is a table."
roomArray[403] = "You are in the mess hall. You stand before a table. To the west is the entrance to the hall. There is another table to the east."
roomArray[404] = "There are walls to the south and west. To the north, there is a table. To the east, you see a red light blinking in the darkness."
roomArray[504] = "You are in the mess hall. To the south there is an entrance to the guard's office, and to the east, a wall. A security camera with a blinking red light is nestled in the corner. To the north is a table."
roomArray[502] = "The guard snores where he stands. South of you is a table. To the north is the exit. To the east is a wall."
roomArray[503] = "You stand before a table. To the south, there is a red, blinking light in the darkness. To the west, there is another table. To the north, there is a tall figure lurking in the shadows. To the east, there is a wall."
roomArray[501] = "You have made it to the exit. The mess hall is to the south."
roomArray[603] = "Down the hall you see sun light and workout equipment. To the east is the yard, to the west is the mess hall."
roomArray[804] = "You enter the vent, it smells like feet and has mounts of dust in it. To the south the vent continues, to the north is the yard."
roomArray[805] = "As you get further in the vent the smell and dust build up only get worse. To the south the vent continues, to the north is sun light and more vent."
roomArray[806] = "You reach the end of the vent covered in the thickest layer of dust posible. To the nourth is dim light and more vent."
roomArray[701] = "To the north and west, there are fences You look up, and wonder if you can climb it."
roomArray[801] = "To the north and east, there are fences. There's a hole at the bottom, only just big enough for a cat to fit through."
roomArray[802] = "You kick the dirt of the yard. From the other side, there's an inmate glaring at you."
roomArray[702] = "To the west, there is a fence. Beneath your feet, some grass grows."
itemArray[202] = "aligator tooth"
itemArray[103] = "wire cutters"
itemArray[403] = "candy bar"
itemArray[503] = "tray"
itemArray[506] = "key"
itemArray[606] = "soda"

def randomHealth():
    health = randint(30,50)
    return health

def randomTrueFalse():
    chooser = randint(1,2)
    if chooser == 1:
        return True
    else:
        return False

def diceRoll():
    roll = randint(1,6)
    return roll

def hitBoss(weapon):
    damage = 0
    weapon = weapon.lower()
    if "shiv" in inventoryArray or "weight" in inventoryArray or "aligator Tooth" in inventoryArray or "dirty sock" in inventoryArray:
        if "shiv" in weapon or "weight" in weapon or "aligator tooth" in weapon or "dirty sock" in weapon:
            damage = damage + 5 + diceRoll()
        elif "fist" in weapon:
            damage = damage + diceRoll()
    else:
        if "fist" in weapon:
            damage = damage + diceRoll()
    print(damage)
    return damage

def hitPlayer(playerHealth):
    myList = ["Punchy Punch", "Tazer", "Roundhouse Kick", "Drop Kick", "Haymaker", "Baton Beat", "Shooty Shooty"]
    attack = choice(myList)
    print("Gaurd uses" + attack)
    damage = 0
    damage = damage + diceRoll()
    if playerHealth > 25:
        damage = damage + diceRoll()
    print(damage)
    return damage

def whoWins(playerHealth, bossHealth):
    if bossHealth <= 0:
        print("Player Wins")
        bossDead = True
    else:
        print("Boss Wins")

def mainBoss():
  playerHealth = 50
  bossHealth = randomHealth()
  while playerHealth > 0 and bossHealth > 0:
    print("Gaurd " + str(bossHealth) + " health")
    sleep(1)
    print("What do you want to use?")
    if "shiv" in inventoryArray:
        print("Shiv")
    if "weight" in inventoryArray:
        print("Weight")
    if "aligator tooth" in inventoryArray:
        print("Aligator Tooth")
    if "aligator tooth" in inventoryArray:
        print("Dirty Sock")
    print("Fist")
    weapon = input()
    sleep(1)
    damage = hitBoss(weapon)
    bossHealth = bossHealth - damage
    if bossHealth > 0:
      damage = hitPlayer(playerHealth)
      sleep(1)
      playerHealth = playerHealth - damage
      print("You have " + str(playerHealth) + " remaining")
      sleep(1)
  whoWins(playerHealth, bossHealth)

def lockedRoom(location):
    if location == 504:
        if roomArray[505] == False and "key" in inventoryArray:
            print("Do you want to use key? If so type use key")
            userInput = input()
            userInput = userInput.lower()
            if userInput == "use key":
                print("The nearby room unlocks")
                roomArray[505] = "You are in the guard office, you definetly should not be in here. To the south is a messy desk and computer, and to the east is calendar and posters of old movies. "

            else:
                print("The nearby room remains locked")

def doesRoomExist(roomNumber):
    try:
        lockedRoom(roomNumber)
        if roomArray[roomNumber] == False:
            print("You can't go there. You hit a wall, -1 intelligence")
            return False
        else:
            return True
    except:
        print("You can't go there. You hit a wall, -1 intelligence")
        return False

def move(userInput, location):
    userInput = userInput.lower()
    if userInput == "n":
        location = location -1
        if doesRoomExist(location) == True:
            return location
        else:
            return location + 1
    elif userInput == "s":
        location = location + 1
        if doesRoomExist(location) == True:
            return location 
        else:
            return location - 1
    elif userInput == "e":
        location = location + 100
        if doesRoomExist(location) == True:
            return location
        else:
            return location - 100
    elif userInput == "w":
        location = location - 100
        if doesRoomExist(location) == True:
            return location
        else:
            return location + 100
    else:
        print("not valid")
        return location

def guessthepassword():
    passComplete = False
    while True:
        print("You sit in front of the guard's computer. \nThere is a sticky note stuck to the top of the monitor. It reads: \nMain character in the bible \nIgneous _____ \n \nPLEASE ENTER A PASSWORD")
        userinput = str.lower(input())
        if userinput == "jesusrocks":
            print("The computer blinks a loading symbol. You wait, sweat upon your brow. \nLoading... \nLoading... \nYou're in!")
            print("The open page blares Never Gonna Give You Up by Rick Astley. A cat is playing piano on-screen. \nYou resist the urge to gag. What is this, 2008?")
            passComplete = True
            break
        else:
            print("The computer blinks a loading symbol. You wait, sweat upon your brow. \nLoading... \nLoading... \nWrong password. Try again.")

 def randomSecretWord ():
    firstDigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    secondDigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    thirdDigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    combinedList = firstDigit + secondDigit + thirdDigit
    randFirst = choice(combinedList)
    randSecond = choice(combinedList)
    randThird = choice(combinedList)
    randCombo = randFirst + randSecond + randThird
    return randCombo

def highLowMain():
    secretNumber = randomSecretWord()
    secretNumber = str(secretNumber)
    print("I'm thinking of a secret three number combination. Take a guess and I'll tell you if the secret number is before your number or after your number.")
    while True:
        print("Guess a word")
        userInput = input()
        userInput = str(userInput)
        if userInput < secretNumber:
            print("The secret word is after " + userInput)
        if userInput > secretNumber:
            print("The secret word is before " + userInput)
        if userInput == secretNumber:
            print("You got it!!!!!")
            quizComplete = True
            break           
            
def main():
    location = 102
    print("   ▄████████  ▄█        ▄██████▄     ▄████████  ▄█  ████████▄     ▄████████        ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄                             ")
sleep(0.2)
print("  ███    ███ ███       ███    ███   ███    ███ ███  ███   ▀███   ███    ███      ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄                           ")
sleep(0.2)
print("  ███    █▀  ███       ███    ███   ███    ███ ███▌ ███    ███   ███    ███      ███   ███   ███   ███    ███ ███   ███                           ")
sleep(0.2)
print(" ▄███▄▄▄     ███       ███    ███  ▄███▄▄▄▄██▀ ███▌ ███    ███   ███    ███      ███   ███   ███   ███    ███ ███   ███                           ")
sleep(0.2)
print("▀▀███▀▀▀     ███       ███    ███ ▀▀███▀▀▀▀▀   ███▌ ███    ███ ▀███████████      ███   ███   ███ ▀███████████ ███   ███                           ")
sleep(0.2)
print("  ███        ███       ███    ███ ▀███████████ ███  ███    ███   ███    ███      ███   ███   ███   ███    ███ ███   ███                           ")
sleep(0.2)
print("  ███        ███▌    ▄ ███    ███   ███    ███ ███  ███   ▄███   ███    ███      ███   ███   ███   ███    ███ ███   ███                           ")
sleep(0.2)
print("  ███        █████▄▄██  ▀██████▀    ███    ███ █▀   ████████▀    ███    █▀        ▀█   ███   █▀    ███    █▀   ▀█   █▀                            ")
sleep(0.2)
print("             ▀                      ███    ███                                                                                                    ")
sleep(0.2)
print("   ▄███████▄    ▄████████  ▄█     ▄████████  ▄██████▄  ███▄▄▄▄           ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████ ")
sleep(0.2)
print("  ███    ███   ███    ███ ███    ███    ███ ███    ███ ███▀▀▀██▄        ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ ")
sleep(0.2)
print("  ███    ███   ███    ███ ███▌   ███    █▀  ███    ███ ███   ███        ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀  ")
sleep(0.2)
print("  ███    ███  ▄███▄▄▄▄██▀ ███▌   ███        ███    ███ ███   ███       ▄███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄     ")
sleep(0.2)
print("▀█████████▀  ▀▀███▀▀▀▀▀   ███▌ ▀███████████ ███    ███ ███   ███      ▀▀███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀     ")
sleep(0.2)
print("  ███        ▀███████████ ███           ███ ███    ███ ███   ███        ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄  ")
sleep(0.2)
print("  ███          ███    ███ ███     ▄█    ███ ███    ███ ███   ███        ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███ ")
sleep(0.2)
print(" ▄████▀        ███    ███ █▀    ▄████████▀   ▀██████▀   ▀█   █▀         ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████ ")
sleep(0.2)
print("               ███    ███                                                                                                                         ")
    print("By Dom, Ethan, and Irene")
    sleep(1)
    while True:
        print(roomArray[location])
        if itemArray[location] == False:
            print("Please type: n, s, e, w, or quit")
            userInput = input()
            userInput = userInput.lower()
            if userInput == "quit":
                break
            else:
                location = move(userInput, location)
        else:
            print("There is an " + itemArray[location] + " here.")
            print("Please type: n, s, e, w, pickup or quit")
            userInput = input()
            userInput = userInput.lower()
            if userInput == "quit":
                break
            elif userInput == "pickup":
                inventoryArray.append(itemArray[location])
                itemArray[location] = False
            else:
                location = move(userInput, location)

