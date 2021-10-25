import os

#Auto installer

try:
    import keyboard
    import mouse
    import time
    import logging
    print("Required modules are installed.")
except: ModuleNotFoundError: print("Required modules are not installed. installing modules..."); os.system("pip3 install keyboard"); os.system("pip3 install mouse"); os.system('pip3 install time'); os.system('pip3 install logging'); quit()

def selection():
    mouorkey = input('Auto clicker or auto typer? (1/2/quit): ')
    try:
        if mouorkey == '1':
            clicking()
        elif mouorkey == '2':
            typing()
        elif mouorkey == 'quit':
            quit()
        else:
            print('You must enter 1 or 2')
            selection()
    except Exception as exp:
        print(exp)
        selection()

print('Press the "]" button to stop it from clicking/typing. and hit the ~ button to quit it.')

# Asking for cps and starting delay

def clicking():
    try:
        delaybef = input('Delay BEFORE THE clicking starts: ')
        delaybeftrue = int(delaybef)
    except:
        print('Must be a number.')
        selection()

    delay = input('CPS?')

    #Determine if "N" was entered

    try:
        int(delay)
        isint = 1
    except:
        isint = 0

    print('Processing complete.')

    time.sleep(delaybeftrue)

    if isint == 1:
        while True:
            if keyboard.is_pressed('`'):
                quit()
            try:
                if not keyboard.is_pressed(']'):
                    mouse.click('left')
                    time.sleep(delaybeftrue)
            except Exception as exc:
                #logger
                print("Unknown Error occured. Please contact program owner with log file")
                logging.basicConfig(filename='excoor.log', level=logging.DEBUG('Usually unreachable error occured: ' + exc), force=True)
                quit()
    else:
        while True:
            if keyboard.is_pressed('`'):
                quit()
            try:
               if not keyboard.is_pressed(']'):
                mouse.click('left')
            except Exception as exc:
                #logger
                print("Unknown Error occured. Please contact program owner with code below:")
                logging.basicConfig(filename='excoor.log', level=logging.DEBUG('Usually unreachable error occured: ' + exc), force=True)
                quit()

def typing():
    keys = input('Enter sentence to repeat type (letters must be seperated by spaces.): ')
    startdelay = input('Delay before macro pressing starts: ')
    pps = input('Enter key presses per second: ')
    loopdelay = input('enter delay between key press loops')
    if pps == 'N' or pps == 'n':
        try:
            keyslist = keys.split(' ')
            length = len(keyslist)
            time.sleep(startdelay)
            while True:
                if keyboard.is_pressed('`'):
                    quit()

                i = 0
                while i < length:
                    keyboard.press(keyslist[i])
                    i = i + 1
                time.sleep(loopdelay)
        except Exception as exp:
            print('Untraceable error occured.')
            selection()
    else:
        try:
            keyslist = keys.split(' ')
            length = len(keyslist)
            time.sleep(startdelay)
            while True:
                if keyboard.is_pressed('`'):
                    quit()
                
                i = 0
                while i < length:
                    keyboard.press(keyslist[i])
                    i = i + 1
                    time.sleep(pps)
                time.sleep(loopdelay)
        except Exception as exp:
            print('You must enter N or a number')
            selection()


selection()