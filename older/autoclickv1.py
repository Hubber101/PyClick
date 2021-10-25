import os



try:
    import keyboard
    import mouse
    import time
    print("Required modules are installed.")
except: ModuleNotFoundError: print("Required modules are not installed. installing modules..."); os.system("pip3 install keyboard"); os.system("pip3 install mouse"); os.system('pip3 install time'); quit()

try:
    delaybef = input('delay before starting')
    delaybeftrue = int(delaybef)
except:
    quit()




delay = input('delay? (Y is about 64.6 cps, N will probably crash something)')



time.sleep(delaybeftrue)

if delay == 'Y':
    while True:
        if keyboard.is_pressed('`'):
            quit()
        try:
            if not keyboard.is_pressed(']'):
                mouse.click('left')
                time.sleep(0.001)
        except:
            quit()
elif delay == 'N':
    while True:
        if keyboard.is_pressed('`'):
            quit()
        try:
            if not keyboard.is_pressed(']'):
                mouse.click('left')
        except:
            quit()