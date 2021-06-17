"""
Error logging
"""
import os
import time
import traceback

# VARIABLES

projectName = 'simple10'

# LOGS

def errorLog(tb):
    global projectName
    path = os.getcwd()
    path += '/errors'
    if os.path.isdir(path):
        path += '/{}_error_log.txt'.format(projectName)
    else:
        try:
            os.mkdir(path)
            path += '/{}_error_log.txt'.format(projectName)
        except OSError:
            print ("\nDirectory cannot be created :  %s failed\n" % path)
            tb = traceback.format_exc()
            errorLog(tb) 

    try:
        os.path.isfile(path) 
        with open(path, 'r') as errorFile:
            txt = errorFile.read()
    except:
        txt = ''
    
    now = time.localtime()
    now = time.asctime(now)
    newError = '\n\n{}\n{}'.format(now,tb)
    txt += newError

    with open(path, 'w') as errorFile:
        errorFile.write(txt)
    
    print('Error Logged at : {}'.format(now))

if __name__ == '__main__':
    errorLog()