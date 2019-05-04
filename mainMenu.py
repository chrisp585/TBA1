from time import sleep
import os
import sys
from os import system, name

#Function prints in red
def printRed(skk): print("\033[91m {}\033[00m".format(skk))

def display():
    #Sets the console window size
    os.system("mode con cols=170 lines=50")
    
    line1 = "After escaping from two previous prison, you are now being transported to Alcatraz Federal Penitentiary.\n"
    line2 = "No one in history has every excaped from Alcatraz island. Unless you can figure out how to the first, then\n"
    line3 = "this will be last place you ever see."

    #For statement create the typing effect for the game intro
    """for x in line1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)

    for x in line2:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)

    for x in line3:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)"""

    sleep(2)
    system('cls') #for windows
    #system('clear') #for linux



    print("*************************************************************************************************************************************************************************")
    print("******************************************************************************************************************** ****************************************************")
    print("*******************************************************************************************************************   ***************************************************")
    print("***********************************************************************************************************  ******   ***************************************************")
    print("*********************************************************************************************************      ****   ***************************************************")
    print("*********************************************************************************************************      ****   ***************************************************")
    print("***************************************************************************************                                     *********************************************")
    print("***************************************************************************************                                     *********************************************")
    print("***************************************************************************************                                     *********************************************")
    print("********************************************************************************                                                        *********************************")
    print("********************************************************************************                                                        *********************************")
    print("*********************************************************************                                                                      ******************************")
    print("***************************************************************                                                                              ****************************")
    print("**************************************************************                                                                                          *****************")
    print("*************************************************************                                                                                            ****************")
    print("*************************************************************************************************************************************************************************")
    printRed(" _______  _______  _______  _______  _______  _______     _______  _______  _______  _______     _______  _        _______  _______ _________ _______  _______  _______  ")
    printRed("(  ____ \(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \   (  ____ \(  ____ )(  ___  )(       )   (  ___  )( \      (  ____ \(  ___  )\__   __/(  ____ )(  ___  )/ ___   ) ")
    printRed("| (    \/| (    \/| (    \/| (   ) || (    )|| (    \/   | (    \/| (    )|| (   ) || () () |   | (   ) || (      | (    \/| (   ) |   ) (   | (    )|| (   ) |\/   )  | ")
    printRed("| (__    | (_____ | |      | (___) || (____)|| (__       | (__    | (____)|| |   | || || || |   | (___) || |      | |      | (___) |   | |   | (____)|| (___) |    /   ) ")
    printRed("|  __)   (_____  )| |      |  ___  ||  _____)|  __)      |  __)   |     __)| |   | || |(_)| |   |  ___  || |      | |      |  ___  |   | |   |     __)|  ___  |   /   /  ")
    printRed("| (            ) || |      | (   ) || (      | (         | (      | (\ (   | |   | || |   | |   | (   ) || |      | |      | (   ) |   | |   | (\ (   | (   ) |  /   /   ")
    printRed("| (____/\/\____) || (____/\| )   ( || )      | (____/\   | )      | ) \ \__| (___) || )   ( |   | )   ( || (____/\| (____/\| )   ( |   | |   | ) \ \__| )   ( | /   (_/\ ")
    printRed("(_______/\_______)(_______/|/     \||/       (_______/   |/       |/   \__/(_______)|/     \|   |/     \|(_______/(_______/|/     \|   )_(   |/   \__/|/     \|(_______/ ")


    print("\n\n")
    print("Make a selection: ")
    print("1) Start new game")
    print("2) Load saved game")
    print("3) Exit\n")

    menuSelection = input("> ")

    return (menuSelection)