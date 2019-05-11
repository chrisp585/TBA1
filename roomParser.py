import sys
import os
import gameState
import gameEngine

def parseNewRoomData(newGame):

    # Room dictionaries need to have 4 keys: Name, LongDesc, ShortDesc, and Status
    roomDict = {'Name': 'Prison Cell', \
        'LongDesc': 'You\'ve arrived at your Prison Cell! It is dimly lit \n\
with thick brick walls and you can\'t help but notice a \n\
foul-smelling odor. Distinct features of this room include a \n\
bed, poster, toilet, sink, Bible, and air vent.', \
        'ShortDesc': 'You\'re back at the Prison Cell. Features: Bed, \n\
poster, toilet, sink, Bible, air vent.', \
        'Status': 'not visited'}

    newGame.createRoom(roomDict)

    roomDict = {'Name': 'Cell Block', \
        'LongDesc': 'Now you are in the cell block, there are a lot of people \n\
roaming about.  You should explore.  But this is just a sample so you can\'t \n\
actually do anything but go back to your prison cell', \
        'ShortDesc': 'Again this is the short description telling you, go back', \
        'Status': 'not visited'}

    newGame.createRoom(roomDict)

    # Object will be anything that but can be inspected that's not a passage
    objectDict = {'Name': 'Key', 'Description': 'Key opens cell door', 'Location': 'Prison Cell', 'Movable': 'y'}

    newGame.addObject(objectDict)

    # Passages will be passage way, door, hole, window, etc.
    passageDict = {'Name': 'Prison cell door', 'Description': 'Just the door to the prison cell', \
        'Locked': 'y', 'KeytoOpen': 'Key'}
    
    newGame.addPassage(passageDict)