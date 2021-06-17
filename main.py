"""
10 Simple Project while learning python
"""


import os
import time

import odd_even_prime
import logs
import madlibs
import wordCount
import inputReader

import json
import csv
import string
import re
import random
import pandas as pd

# VARIABLES

projectName = 'simple10'

# FUNCTIONS

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


# MAIN LOOP

def menu1():
    usingMenu1 = True
    while usingMenu1:
        clear()
        print('------------')
        print(' Simple 10 ')
        print('------------')
        print('[1] - Odd / even / prime calculator')
        print('[2] - Mad Lib Game')
        print('[3] - Word Counter')
        print('[4] - Input Reader')
        print('[5] - Acronym Generator')
        print('[6] - Rock-Paper-Scissors Game')
        print('[7] - Is a Palindrome?')
        print('[8] - Bill/Tip Calculator')
        print('[9] - E-mail Slicer')
        print('[10] - Guess the number')
        print('At any time enter 999 to return')

        try:
            op = int(input('--> : '))
            
            if op == 999:
                usingMenu1 = False
                print('Good Bye')
            elif op == 1:
                clear()
                odd_even_prime.oddEven()
            elif op == 2:
                clear()
                madlibs.madLibs()
            elif op == 3:
                wordCount.wordCount()
            elif op == 4:
                inputReader.inputReader()
            elif op == 5:
                acronym()
            elif op == 6:
                rps()
            elif op == 7:
                palindrome()
            elif op == 8:
                bill()
            elif op == 9:
                mailSlicer()
            elif op == 10:
                guess()
            else:
                print('invalid input')
        except Exception as e:
            print('Error in menu 1 : {}'.format(e))
            tb = logs.traceback.format_exc()
            logs.errorLog(tb) 

if __name__ == '__main__':
    menu1()