



# FUNCTIONS



    




def acronym():
    using = True
    while using:
        print('\nCreate an Acronym')
        print('\nPlease enter your phrase of words')
        name = input('--> : ')
        
        if name == '999':
            using = False
        else:        
            words = name.split()
            acronym = ''
            for word in words:
                item = word[0]
                if item is int:
                    acronym += item
                else:
                    acronym += item.upper()

            print('\n{} - {}\n'.format(acronym,name))
            input('Press enter to continue')

def rps():
    print('\nWELCOME TO ROCK, PAPER, SCISSORS\n')
    setUp = True
    while setUp:
        print('Select game mode')    
        print('[1] - Single player')
        print('[2] - Multiplayer')
        mode = int(input('--> : '))
        if mode in range(1,3):
            pass
        else:
            print('Invalid entry\n')
            continue

        alpha = string.ascii_letters
        allowed = set("{}!- .".format(alpha))
        players = {}
        setName1 = True
        while setName1:
            name1 = input('\nEnter player 1 name : ')
            if name1 == '999':
                setName1 = False
                setUp = False
            elif name1 and all(ch in allowed for ch in name1):
                players[name1] = 0
                setName1 = False
            else:
                print('invalid charactor : {}'.format(" ".join(set(name1)- allowed)))

        if mode == 2:
            setName2 = True
            while setName2:
                name2 = input('Enter player 2 name : ')
                if name1 == '999':
                    setName1 = False
                    setUp = False
                elif name2 and all(ch in allowed for ch in name2):
                    players[name2] = 0
                    setName2 = False
                else:
                    print('invalid charactor : {}'.format(" ".join(set(name1)- allowed)))
        else:
            names = ['Gary', 'Oliver', 'Jes', 'Mary']
            nameX = random.randint(0,3)
            name2 = names[nameX]
            players[name2] = 0
        index = 1
        while players[name1] < 3 and players[name2] < 3:
            try:
                print('\nScore : {} - {} : {} - {}'.format(name1,players[name1],name2,players[name2]))
                time.sleep(2)
                print('Round {} - FIGHT\n'.format(index))
                time.sleep(0.5)
                print('[1] - \U0001F44A : ROCK')
                print('[2] - \U0001F4C4 : PAPER')
                print('[3] - \U00002702  : SCISSORS')
                options = ['rock', 'paper', 'scissors']
                op1 = int(input('\n{} turn : '.format(name1)))
                if mode == 2:
                    op2 = int(input('{} turn : '.format(name2)))
                else:
                    op2 = random.randint(1,3)
                    time.sleep(2)
                w1 = op1 - 1
                w2 = op2 - 1
                res = op1 - op2
                print('')
                if res == 0:
                    print('DRAW - {} vS {} - no score'.format(options[w1],options[w2]))
                    index += 1
                    time.sleep(2)
                elif res < 0:
                    if res == -2:
                        print('{} beats {}'.format(options[w1],options[w2]))
                        time.sleep(2)
                        print('{} wins round {}'.format(name1,index))
                        time.sleep(2)
                        players[name1] += 1
                        index += 1
                    else:
                        print('{} falls to {}'.format(options[w1],options[w2]))
                        time.sleep(2)
                        print('{} wins round {}'.format(name2,index))
                        time.sleep(2)
                        players[name2] += 1
                        index += 1
                else:
                    if res == 2:
                        print('{} falls to {}'.format(options[w1],options[w2]))
                        time.sleep(2)
                        print('{} wins round {}'.format(name2,index))
                        time.sleep(2)
                        players[name2] += 1
                        index += 1
                    else:
                        print('{} beats {}'.format(options[w1],options[w2]))
                        time.sleep(2)
                        print('{} wins round {}'.format(name1,index))
                        time.sleep(2)
                        players[name1] += 1
                        index += 1
            except Exception as e:
                print('rps game error : {}'.format(e))
                tb = traceback.format_exc()
                errorLog(tb) 
        
        if mode == 2:
            if players[name1] == 3:
                print('\nCONGRADULATIONS')
                time.sleep(2)
                print('{} IS THE WINNER'.format(name1))
                print('\nScore : {} - {} : {} - {}'.format(name1,players[name1],name2,players[name2]))
                players = {}
            elif players[name2] == 3:
                print('\nCONGRADULATIONS')
                time.sleep(2)
                print('{} IS THE WINNER'.format(name2))
                print('\nScore : {} - {} : {} - {}'.format(name1,players[name1],name2,players[name2]))
                players = {}
        else:
            if players[name1] == 3:
                print('\nCONGRADULATIONS')
                time.sleep(2)
                print('{} IS THE WINNER'.format(name1))
                print('\nScore : {} - {} : {} - {}'.format(name1,players[name1],name2,players[name2]))
                players = {}
            elif players[name2] == 3:
                print('\nGAME OVER')
                time.sleep(2)
                print('{} IS THE WINNER'.format(name2))
                print('\nScore : {} - {} : {} - {}'.format(name1,players[name1],name2,players[name2]))
                players = {}

        time.sleep(2)
        op3 = input('\nDo you wish to play again? y/n')
        if op3 == 'y':
            pass
        elif op3 == 'n':
            setUp = False
        else:
            print('Invalid input')

def palindrome():
    allowed = set(string.ascii_letters)
    print('\nIs it a Palindrome?\n')
    print('A palindrome is a word that can be writen\nforward and backwards with no change.')
    using1 = True
    while using1:
        print('\nPlease enter a word into the palindrome checker')
        word = input('--> :')
        if word == '999':
            using1 = False
        elif word and all(ch in allowed for ch in word):
            pass
        else:
            bad = set(word)-allowed
            test = list(word)
            for ch in bad:
                test = list(filter((ch).__ne__, test))
                word = "".join(test)

        count = len(word)
        if (count % 2) == 0: #even
            pass
        else:
            count -= 1
        mid = count/2
        index = 0
        while index < mid:
            index2 = -1*index-1
            if word[index] == word[index2]:
                check = True
            else:
                print('\nyour word {} is not a palindrome'.format(word))
                check = False
                break
            index += 1
        if check:
            print('\nYour word {} is a palindrone'.format(word))
                                    
def bill():
    print('\nBill/Tip Calculator')
    usingBill = True
    while usingBill:
        print('\nWhat is the bill amount?')
        try:
            amount = round(float(input('--> : R ')),2)
        except Exception as e:
            print('Error in bill : {}'.format(e))
            tb = traceback.format_exc()
            errorLog(tb) 
            continue
        print('what tip do you wish on giving as a %')
        try:
            tip1 = float(input('--> : '))
        except Exception as e:
            print('Error in bill : {}'.format(e))
            tb = traceback.format_exc()
            errorLog(tb) 
            continue
        print('how many parties will be paying the bill?')
        try:
            parties = int(input('--> : '))
        except Exception as e:
            print('Error in bill : {}'.format(e))
            tb = traceback.format_exc()
            errorLog(tb) 
            continue
        tip = float(tip1/100)
        tip = round(tip,2)
        tipAmount = amount * tip
        tipAmount = round(tipAmount,2)
        bill = amount + tipAmount
        share = round(bill / parties,2)

        print('Bill      : R {}'.format(amount))
        print('Tip       : R {} @ {}%'.format(tipAmount,tip1))
        print('Total     : R {}'.format(bill))
        print('Party pay : R {}ea'.format(share))

        print('\nEnter to continue or 999 to exit')
        try:
            op = int(input(''))
            if op == 999:
                usingBill = False
        except Exception as e:
            print('error in bill : {}'.format(e))
            tb = traceback.format_exc()
            errorLog(tb)

def mailSlicer():
    usingMail = True
    while usingMail:
        print('\nPlease enter your e-mail address')
        mail = input('--> : ')
        
        regex = r'^(\w|\.|\-)+[@](\w|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, mail)):
            names = mail.split('@')
            # better way would be to use indexing var[start:finish]
            # name = mail[:mail.index('@')]
            name = names[0]
            domains = [mail.group() for mail in re.finditer(r'(?<=\@).*?(?=\.)', mail)]
            publicDomains = ['gmail','yahoo','aol']
            
            if domains[0] in publicDomains:
                print('Hello {} nice to see you using {}'.format(name,domains[0]))
            else:
                print('Hello {}, ask me if you need coding help with your website {}'.format(name,domains[0]))
        else:
            print('invalid email entered')
  
def guess():
    print('\nGuess the number in as few attempts as possible')
    print('First to reach 10 guesses looses')
    ply = 0 
    cpu = 0
    rnd = 1
    usingGuess = True
    while usingGuess:
        
        if cpu >= 10:
            print('Congradulations you beat the computer')
            print('You played {} rounds'.format(rnd))
            print('You guessed {} guesses'.format(ply))
            print('the Computer guessed {} guesses'.format(cpu))
        elif ply >= 10:
            print('Sorry you lost')
            print('You played {} rounds'.format(rnd))
            print('You guessed {} guesses'.format(ply))
            print('the Computer guessed {} guesses'.format(cpu))
        elif (rnd % 2) == 0:
            try:
                num = int(input('enter a secrect number from 1-10 : '))
                cpuGuess = True
                atempt = 0
                while cpuGuess:
                    guess = random.randint(1,10)
                    time.sleep(2)
                    print('\nmy guess is {}'.format(guess))
                    time.sleep(2)
                    atempt += 1
                    if guess == num:
                        print('\nI was correct!')
                        print('i won this round in {} attempt/s'.format(atempt))
                        print('your turn')
                        cpu += atempt
                        cpuGuess = False
                        rnd += 1
                    else:
                        print('\nI was incorrect')
                        print('let me guess again')
            except Exception as e:
                print('error in cpuGuess : {}'.format(e))
        else:
            try:
                num = random.randint(1,10)
                plyGuess = True
                atempt = 0
                while plyGuess:
                    guess = int(input('\nGuess a number from 1-10 : '))
                    print('your guess is {}'.format(guess))
                    time.sleep(2)
                    atempt += 1
                    if guess == num:
                        print('\nYou are correct!')
                        print('You won this round in {} attempt/s'.format(atempt))
                        print('my turn')
                        ply += atempt
                        plyGuess = False
                        rnd += 1
                    else:
                        print('\nYou are incorrect')
                        print('Please guess again')
            except Exception as e:
                print('error in cpuGuess : {}'.format(e))



