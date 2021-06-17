"""
Input Reader - simple use of string charactor analysis and compare
"""

def inputReader():
    print('\nHere we will capture your information and evalute if it is acceptable as an input')
    # first create a details dict
    details = {}
    usingReader = True
    while usingReader:
        print('\nStart new Capture, [999] to end at any time')
        
        getName = True
        # Names can be alpha char but not punctuation or numbers
        while getName:
            name = input('\nName : ')
            if name == '999':
                usingReader = False
            else:
                # here we create acceptable char being letters and hyphin and apostrophy and space
                letters = string.ascii_letters+'-\' '
                # we convert to set for comparison
                chars = set(letters)
                for c in name:
                    if c in chars:
                        namePass = True
                    else:
                        print('{} Not allowed'.format(c))
                        namePass = False
                        break

            if namePass:
                details['Name'] = name
                getName = False
            else:
                print('\nName not accepted\n')
        
        getAge = True
        while getAge:
            age = input('age : ')
            if name == '999':
                usingReader = False
            
            elif age.isdigit():
                details['Age'] = age
                getAge = False
            else:
                print('\nAge can only be a numebr 0-9\n')
        
        getEmail = True
        while getEmail:
            mail = input('E-mail : ')
            if name == '999':
                usingReader = False
            
            elif '@' in mail and '.' in mail:
                details['E-Mail'] = mail
                getEmail = False
            else:
                print('\nE-mail needs to have an @ and . to be valid\n')

        print('')
        for item in details:
            print('{} : {}'.format(item,details[item]))
        
        input('\nPress enter to continue')

if __name__ == '__main__':
    inputReader()