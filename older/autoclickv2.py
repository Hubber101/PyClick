import os

try:
    import keyboard
    import mouse
    import time
    print("Required modules are installed.")
except: ModuleNotFoundError: print("Required modules are not installed. installing modules..."); os.system("pip3 install keyboard"); os.system("pip3 install mouse"); os.system('pip3 install time'); quit()

print('very fast without delay. press the "]" button to stop it from clicking. and hit the ~ button (left of the 1 key) to quit it. 27.6 cps')

try:
    delaybef = input('cant figure out how to make the delay overridable so imma just ask what time you want the delay to be BEFORE THE clicking starts.')
    delaybeftrue = int(delaybef)
except:
    print('')
    quit()


delay = input('delay? (Y is about 27.6 cps, N will probably crash something)')

time.sleep(delaybeftrue)

if delay == 'Y' or delay == 'y':
    while True:
        if keyboard.is_pressed('`'):
            quit()
        try:
            if not keyboard.is_pressed(']'):
                mouse.click('left')
                time.sleep(0.03)
        except:
            quit()
elif delay == 'N' or delay == 'n':
    while True:
        if keyboard.is_pressed('`'):
            quit()
        try:
            if not keyboard.is_pressed(']'):
                mouse.click('left')
        except:
            quit()