from time import sleep
import sys
from os import system, name

def display():
    
    line1 = "After escaping from two previous prison, you are now being transported to Alcatraz Federal Penitentiary.\n"
    line2 = "No one in history has every excaped from Alcatraz island. Unless you can figure out how to the first, then\n"
    line3 = "this will be last place you ever see."


    for x in line1:
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
        sleep(0.1)

    sleep(2)
    system('cls') #for windows
    #system('clear') #for linux



    print("***********************************************************************************************************************************************************************")
    print("******************************************************************************************************************** **************************************************")
    print("*******************************************************************************************************************   *************************************************")
    print("***********************************************************************************************************  ******   *************************************************")
    print("*********************************************************************************************************      ****   *************************************************")
    print("*********************************************************************************************************      ****   *************************************************")
    print("***************************************************************************************                                     *******************************************")
    print("***************************************************************************************                                     *******************************************")
    print("***************************************************************************************                                     *******************************************")
    print("********************************************************************************                                                        *******************************")
    print("********************************************************************************                                                        *******************************")
    print("*********************************************************************                                                                      ****************************")
    print("***************************************************************                                                                              **************************")
    print("**************************************************************                                                                                          ***************")
    print("*************************************************************                                                                                            **************")
    print("***********************************************************************************************************************************************************************")
    print(" _______  _______  _______  _______  _______  _______     _______  _______  _______  _______     _______  _        _______  _______ _________ _______  _______  _______  ")
    print("(  ____ \(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \   (  ____ \(  ____ )(  ___  )(       )   (  ___  )( \      (  ____ \(  ___  )\__   __/(  ____ )(  ___  )/ ___   ) ")
    print("| (    \/| (    \/| (    \/| (   ) || (    )|| (    \/   | (    \/| (    )|| (   ) || () () |   | (   ) || (      | (    \/| (   ) |   ) (   | (    )|| (   ) |\/   )  | ")
    print("| (__    | (_____ | |      | (___) || (____)|| (__       | (__    | (____)|| |   | || || || |   | (___) || |      | |      | (___) |   | |   | (____)|| (___) |    /   ) ")
    print("|  __)   (_____  )| |      |  ___  ||  _____)|  __)      |  __)   |     __)| |   | || |(_)| |   |  ___  || |      | |      |  ___  |   | |   |     __)|  ___  |   /   /  ")
    print("| (            ) || |      | (   ) || (      | (         | (      | (\ (   | |   | || |   | |   | (   ) || |      | |      | (   ) |   | |   | (\ (   | (   ) |  /   /   ")
    print("| (____/\/\____) || (____/\| )   ( || )      | (____/\   | )      | ) \ \__| (___) || )   ( |   | )   ( || (____/\| (____/\| )   ( |   | |   | ) \ \__| )   ( | /   (_/\ ")
    print("(_______/\_______)(_______/|/     \||/       (_______/   |/       |/   \__/(_______)|/     \|   |/     \|(_______/(_______/|/     \|   )_(   |/   \__/|/     \|(_______/ ")


    print("\n\n")
    print("Make a selection: ")
    print("1) Start new game")
    print("2) Load saved game")
    print("3) Exit\n")

    menuSelection = input("> ")

    return (menuSelection)
