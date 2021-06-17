"""
Odd Even Prime Claculator
"""

import random
import logs

# FUNCTIONS

def oddEven():
    print('\nIS YOUR NUMBER ODD OR EVEN AND/OR PRIME?')
    print('Enter any whole number or 99 for a random number')
    usingOddEven = True
    while usingOddEven:
        try:
            # get user input number
            op2 = int(input('\n--> : '))
            if op2 == 999:
                usingOddEven = False
            # if requested randomise a number
            elif op2 == 99:
                op2 = random.randint(0,1000)
            # check input is not empty
            elif op2 != '':
                pass
            else:
                print('\nNumber cannot be empty') 
        except Exception as e:
            print('Error in menu 1 op 1 : {}'.format(e))
            tb = logs.traceback.format_exc()
            logs.errorLog(tb) 

        # Check if number divided by 2 has remanders or not
        if (op2 % 2) == 0:
            print('\nYour number {} is even'.format(op2))
        else:
            print('\nYour number {} is odd'.format(op2))

        # check if number is a prime number
        index = 1
        points = 0 # a prime number will have max 2 points (divisable by only 1 and itself)
        while index <= op2: 
            if (op2 % index) == 0:
                points += 1
            index += 1
            
        if points == 2:
            print('Your number {} is a PRIME number'.format(op2))
        else:
            print('Your number {} is not a prime numer'.format(op2))

if __name__ == '__main__':
    oddEven()