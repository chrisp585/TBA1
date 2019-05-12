import roomParser
from roomParser import parseNewRoomData

class gameState:
    """This class maintains current state of the game"""

    def __init__(self):
        self.player = ""
        self.currentRoom = "Prison Cell"
        self.playerInventory = []
        self.roomList = []
        self.objectList = []
        self.roomStatus = []
        self.passageList = []
        #print ("GameState Instance Created")#for testing

    def modifyState(self, verb, noun):
        if (verb == 'take'):
            for item in self.objectList:
                if (item['Name'] == noun and item['Movable'] == 'y'):
                    self.addInventory(noun)
                    return
        elif (verb == 'open'):
            for item in self.passageList:
                if (item['Name'] == noun):
                    self.currentRoom = item['Connection']
                    self.printRoomDescription()
                    return
        elif (verb == 'drop'):
            for item in self.objectList:
                if (item['Name'] == noun and item['Location'] == 'Inventory'):
                    self.removeInventory(noun)
                    return

        #print ("State modified")

    def setRoomStatus(self, roomName):
        for item in self.roomList:
            if (item['Name'] == roomName):
                if (item['Status'] == 'not visited'):
                    item['Status'] = 'visited'
                    #print ("Room status changed to", item['Status'])#for testing

    # Not sure this function is needed
    def getRoomStatus(self):
        for item in self.roomList:
            if (item['Name'] == self.currentRoom):
                return (item['Status'])

    def addObject(self, objectDict):
        self.objectList.append(objectDict)
        #print ("Object added to the list")#for testing

    def addPassage(self, passageDict):
        self.passageList.append(passageDict)
        #print("Passage added to list")#for testing

    def addInventory(self, itemName):
        self.playerInventory.append(itemName)
        for item in self.objectList:
            if (item['Name'] == itemName):
                item['Location'] = 'Inventory'
                #print ("Item added to inventory")#for testing

    def removeInventory(self, itemName):
        for item in self.playerInventory:
            if (item == itemName):
                self.playerInventory.remove(item)
                for item in self.objectList:
                    if (item['Name'] == itemName):
                        item['Location'] = self.currentRoom
                        #print ("Item added to inventory")#for testing

    def printRoomDescription(self):
        for item in self.roomList:
            rmName = str(item['Name'])
            if (item['Name'] == self.currentRoom):
                if (item['Status'] == 'visited'):
                    print ("Location: ", item['Name'])
                    print (item['ShortDesc'], '\n')
                else:
                    print ("Location: ", item['Name'])
                    print (item['LongDesc'], '\n')
                    self.setRoomStatus(self.currentRoom)
                break

    def loadSavedGame(self):
        print ("Load game function: code needed")#replace with code

    def saveGame(self):
        print ("Code needed")#replace with code

    def createRoom(self, roomDict):
        self.roomList.append(roomDict)
        #print ("Room added to the list")#for testing

    def printDescription(self, objectName):
        for item in self.objectList:
            if (item['Name'] == objectNameName):
                if (item['Location'] == self.currentRoom):
                    print ("Room status changed to", item['Status'])#for testing

    def gameOver(self):
        for item in self.objectList:
            if (item['Name'] == 'Key'):
                if (item['Location'] == 'Cell Block' and self.currentRoom == 'Cell Block'):
                    print("Demo Over")
                    return 1
        return 0