
roomArray = []
for i in range(999):
    roomArray.append(False)

roomArray[102] = "You are standing in the corner of the dark prison cell. \nTo the east is a bed. To the south is a toilet."
roomArray[103] = "You are now infront of your bed. The matress is made out of cardboard, and the pillow is a stuffed aligator. \nTo the west is another part of your cell. To the south is the cell door."
roomArray[202] = "Here is your toilet, or rather your bucket. You have fond memories of using this against the gaurd. \nTo the north is the cell corner. To the east is the cell door."
roomArray[203] = "The cell door is open, so it must be break time. You can continue east down the hallway towards the mess. \nTo the north is your bed, and to the west is the toilet."

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
    if userInput == "n" and doesRoomExist(location) == True:
        location = location -1
    elif userInput == "s" and doesRoomExist(location) == True:
        location = location + 1
    elif userInput == "e" and doesRoomExist(location) == True:
        location = location + 100
    elif userInput == "w" and doesRoomExist(location) == True:
        location = location - 100
    else:
        location = location
    return location

