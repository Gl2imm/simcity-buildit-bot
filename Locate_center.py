from pyautogui import *
import pyautogui

#Find center
center_shop_location = pyautogui.locateOnScreen('images/shop.png', confidence=0.8)
corner_locationX = (center_shop_location.left - 1210)
corner_locationY = (center_shop_location.top - 73)
center_locationX = (1280/2 + corner_locationX)
center_locationY = (720/2 + corner_locationY)
time.sleep(0.2)

#print(center_shop_location)
#print ('Left corner:', corner_locationX, ',', corner_locationY)
#print (center_locationX, center_locationY)

#plastic_location = pyautogui.locateOnScreen('images/items/plastic.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.7)

#print(plastic_location)