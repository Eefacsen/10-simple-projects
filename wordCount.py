"""
Word Count - A quick app to count the amount of words in a json file or text blob
            also count word frequency in a text file

Simply paste your own .json or .txt file in the 'myJsonFiles' or 'myTxtFiles' folder to access them

future development
    - allow all extensions of files to be handled
    - allow drag and drop files with a GUI

    - Json file selection is faulty once selecting outside the range.
    - Json word count is incorrect as the count system does not work correctly
    - the list count system also does not work correctly on multi layer lists/dictionaries
"""

import logs
import os
import json
import string

def wordCount():
    wordGame = True
    while wordGame:
        print('\n[1] - Choose a json file to word count')
        print('[2] - Print your own statment to count')
        print('[3] - Count word frequency in a txt File')
        try:
            op2 = int(input('--> : '))
            if op2 == 999:
                wordGame = False
            # user selected Json file for word count
            elif op2 == 1:
                path = os.getcwd()
                # for now a pre set location is simplest
                filePath = '{}/myJsonFiles'.format(path)
                # compile a list of files in the folder location
                files = os.scandir(filePath)
                # set empty list
                fileOptions = []
                print('\nSelect file to count words\n')

                fileSel = True
                while fileSel:
                    index = 0
                    for file in files:
                        # build the file options list
                        fileOptions.append(file)
                        # print only the file name for easy user understanding
                        name = file.name
                        print('[{}] - {}'.format(index, name))
                        index += 1
                    try:
                        op = int(input('--> : '))
                        if op == 999:
                            fileSel = False
                        elif op in range(0,index):
                            # define the user chosen file
                            chosenFile = fileOptions[op]
                            # open user chosen file for editting
                            with open(chosenFile, 'r') as myFile:
                                fileInfo = json.load(myFile)
                                entries = len(fileInfo)
                                words = 0
                                for entry in fileInfo:
                                    lng = len(entry)
                                    count = lng * 2
                                    words += count
                                
                            print('\nIn file : {}'.format(name))
                            print('there are :')
                            print('{} list items'.format(entries))
                            print('{} words'.format(words))
                            fileSel = False
                        else:
                            print('Selection not permited')
                    except Exception as e:
                        print('Error in wordCount/fileSel : {}'.format(e))
                        tb = logs.traceback.format_exc()
                        logs.errorLog(tb) 
            elif op2 == 2:
                userStat = input('\nYour statement : ')
                words = userStat.split()
                count = len(words)
                print('\nYou wrote {} word/s'.format(count))
            elif op2 == 3:
                #create a translator so later we can remove punctuation from words
                translator = str.maketrans('', '', string.punctuation)
                word_count = {}
                fileLst = []
                path = os.getcwd()
                path += '/myTxtFiles'
                myFiles = os.scandir(path)
                print('\nPlease select a file for word count frequency')
                for index, item in enumerate(myFiles):
                    print(f'[{index}] - {item.name}')
                    filePath = path+'/'+item.name
                    fileLst.append(filePath)
                while True:    
                    try:
                        op = int(input('--> : '))
                        if op != '':
                            break
                        else:
                            pass
                    except Exception as e:
                        print('Error in Txt file selection for word count : {e}')
                
                with open(fileLst[op], 'r') as myTxtFile:
                    text = myTxtFile.read()
                                
                words = text.split()
                for word in words:
                    #make our words all lower case
                    word = word.translate(translator).lower()
                    count = word_count.get(word, 0)
                    count += 1
                    word_count[word] = count
                word_count_list = sorted(word_count, key=word_count.get, reverse=True)
                print('\n\n')
                print(text)
                print('\n\n')
                print('{} words total'.format(len(words)))
                print('Word Frequency:')
                for word in word_count_list[:10]:
                    print(word, word_count[word])
                input('Enter to continue')
            else:
                print('Invalid input')

        except Exception as e:
            print('Error in wordCount : {}'.format(e))
            tb = logs.traceback.format_exc()
            logs.errorLog(tb) 

if __name__ == '__main__':
    wordCount()