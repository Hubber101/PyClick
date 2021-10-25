import os

from keyboard import parse_hotkey_combinations

#Auto installer

try:
    import keyboard
    import mouse
    import time
    import logging
    print("Required modules are installed.")
except: ModuleNotFoundError: print("Required modules are not installed. installing modules..."); os.system("pip3 install keyboard"); os.system("pip3 install mouse"); os.system('pip3 install time'); os.system('pip3 install logging'); quit()

print('Press the "]" button to stop it from clicking. and hit the ~ button to quit it.')

# Asking for cps and starting delay

try:
    delaybef = input('Delay BEFORE THE clicking starts: ')
    delaybeftrue = int(delaybef)
except:
    print('Must be a number.')
    quit()

delay = input('CPS? (N for no delay): ')

#Determine if "N" was entered

try:
    deltruint = int(delay)
    deltruint = 1 / deltruint
except:
    deltrustr = str(delay)

try:
    deltruint = deltruint
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
                time.sleep(deltruint)
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