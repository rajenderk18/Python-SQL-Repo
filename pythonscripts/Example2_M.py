import time
import datetime
from threading import Thread
from pynput import keyboard
# from random import randrange
import random

import pyautogui
time.sleep(10)

d = datetime.datetime.utcnow()
# print (d, d.hour-4)
# print(time.gmtime().tm_hour)

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input('Program paused, would you like to continue? (y/n) ')

            while user_input != 'y' and user_input != 'n' and user_input != 'Y' and user_input != 'N':
                user_input = input('Incorrect input, try either "y" or "n" ')

            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'Y':
                main.status = 'run'
            elif user_input == 'N':
                main.status = 'exit'
            elif user_input == 'n':
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'run'
    # if d.hour > 10:
    #     main.status = 'exit'
    pyautogui.FAILSAFE = False

    while True:
        # print('running')
        time.sleep(1)

        # makes program execution pause for 10 sec
        # moves mouse to 1000, 1000.
        # generate random coordinate to move mouse curser to random position each time
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        pyautogui.moveTo(x, y, duration=1)

        pyautogui.click(525, 1052, interval=100)
        pyautogui.click(559, 1052, interval=500)
        pyautogui.click(618, 1052, interval=100)


        # generate random number to scroll mouse curser to random position each time
        a = random.randint(1, 10)
        b = random.randint(-10, 1)
        pyautogui.scroll(a)
        pyautogui.click()
        # pyautogui.click(button = 'right')
        pyautogui.scroll(b)

        # # drags mouse 100, 0 relative to its previous position,
        # # thus dragging it to 1100, 1000
        # pyautogui.dragRel(100, 0, duration=1)
        # pyautogui.dragRel(0, 100, duration=1)
        # pyautogui.dragRel(-100, 0, duration=1)
        # pyautogui.dragRel(0, -100, duration=1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=exit_program).start()