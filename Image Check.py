#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while keyboard.is_pressed('q') == False:
    flag = 0
    
'''
while 1:
    if  pyautogui.locateOnScreen('images/factory2.png', confidence=0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
'''

#click center
center_shop_location = pyautogui.locateOnScreen('images/shop.png', confidence=0.8)
corner_locationX = (center_shop_location.left - 1191)
corner_locationY = (center_shop_location.top - 73)
center_locationX = (1280/2 + corner_locationX)
center_locationY = (720/2 + corner_locationY)
pyautogui.click(center_locationX, center_locationY)
print(center_locationX, center_locationY)
time.sleep(0.2)

