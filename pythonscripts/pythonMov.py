import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = True
numMin = None
if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while (True):
    x = 0
    while (x < numMin):
        time.sleep(5)
        x += 1
    # for i in range(0, 2000):
    #     # pyautogui.moveTo(0, 300)
    #     # pyautogui.click(button='right')
    #     pyautogui.scroll(i * 4)  # scroll up 10 "clicks"
    #     pyautogui.scroll(-i)  # scroll down 10 "clicks"
    #     pyautogui.scroll(10, x=100, y=100)
    # pyautogui.moveTo(1, 1)
    for i in range(0, 3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))