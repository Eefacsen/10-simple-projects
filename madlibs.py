"""
Mad Libs - a word replacement game for kids
"""

import logs
import os

# FUNCTIONS

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def madLibs():
    usingMadLib = True
    while usingMadLib:

        print('*** MAD LIB GAME ***')

        # User data collection
        name = input('\nPlease enter your name : ')
        if name == '999':
            usingMadLib = False
            break
        place = input('Please enter your favorite place : ')
        if place == '999':
                usingMadLib = False
                break
        animal = input('Please enter your favorite animal : ')
        if animal == '999':
                usingMadLib = False
                break
        sound = input('Please enter a funny sound : ')
        if sound == '999':
                usingMadLib = False
                break

        inputGiven = True
        while inputGiven:
            clear()    
            print('\nPlease choose a story')
            print('[1] - Old McDonald Farm')
            print('[2] - Humpty Dumpty')
            print('[3] - Hickary Dickary Dock')
    
            try:
                op = int(input('--> : '))
                if op == 999:
                    inputGiven = False
                    usingMadLib = False
                elif op == 1:
                    print('\n\nOld {name} had a {place}\nEy I Ey I O\nAnd in that {place} they had a {animal}\nEy I Ey I O'.format(name=name,place=place,animal=animal))
                    print('With a {sound} {sound} here\nand a {sound} {sound} there\nHere a {sound} there a {sound}\nEverywhere a {sound} {sound}'.format(sound=sound))
                    print('Old {name} had a {place}\nEy I Ey I O\n'.format(name=name,place=place))
                    input('\nEnter to continue')
                elif op == 2:
                    print('\n\n{0} sat on the {1}\n{0} had a great {2}\nAll the kings {3}s\ncouldnt put {0} together agian\n'.format(name,place,sound,animal))
                    input('\nEnter to continue')
                elif op == 3:
                    print('\n\nHickary Dickary {0}\nThe {3} run up the {1}\nThe clock stuck one {2}\nThe {3} ran down\nHickary Dickary {0}\n'.format(name,place,sound,animal))
                    input('\nEnter to continue')
                else:
                    print('\nOption cannot be empty')
                    input('\nEnter to continue')
            except Exception as e:
                print('\nError in madLibs game : {}'.format(e))
                tb = logs.traceback.format_exc()
                logs.errorLog(tb) 

if __name__ == '__main__':
    madLibs()