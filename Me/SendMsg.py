import pyautogui
from time import sleep

msg = input('Enter your Msg >> :')
num_msg = int(input('Chose your Number of Msg >> :'))
time_msg = float(input('Chose your Time of Msg >> :'))

for num in range(num_msg + 1):
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('enter')
    sleep(time_msg)
