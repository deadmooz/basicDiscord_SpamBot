import os
import time as tm
import pyautogui
import datetime
import pyperclip as pc
count=0
word = '@ripp'
os.system(r'start C:\Users\kumar\AppData\Local\Discord\app-1.0.9003\Discord.exe')
tm.sleep(3)
pyautogui.moveTo(970,1000)
pyautogui.click()
while (count < 20):
    pyautogui.typewrite(word)
    pyautogui.press('tab')
    pyautogui.hotkey("ctrl", "v", interval=0.25 )
    pyautogui.press('enter')
    count = count + 1
