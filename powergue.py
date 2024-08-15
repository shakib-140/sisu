import pyautogui
import time
time.sleep(3)
for i in range(1,10,1) :
    pyautogui.write('how are you',0.05)
    pyautogui.press('enter')
    time.sleep(1)
