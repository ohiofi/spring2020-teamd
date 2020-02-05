from time import *

roomArray = []
itemArray = []
inventoryArray = []
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
itemArray[202] = "aligator tooth"
itemArray[103] = "wire cutters"
itemArray[403] = "candy bar"
itemArray[503] = "tray"
itemArray[506] = "key"
itemArray[606] = "soda"

def doesRoomExist(roomNumber):
    try: 
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


def main():
    location = 102
    print("Florida Man Prison Escape")
    print("By Dom, Ethan, and Irene")
    sleep(1)
    while True:
        print(roomArray[location])
        if itemArray[location] == False:
            print("Please type: n, s, e, w, or quit")
            userInput = input()
            location = move(userInput, location)
        else:
            print("There is an " + itemArray[location] + " here.")
            print("Please type: n, s, e, w, pickup or quit")
            userInput = input()
            if userInput == "pickup":
                inventoryArray.append(itemArray[location])
                itemArray[location] = False
            else:
                location = move(userInput, location)

