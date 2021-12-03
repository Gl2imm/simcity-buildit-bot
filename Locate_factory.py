from pyautogui import *
import pyautogui
import keyboard
import Locate_center

#while keyboard.is_pressed('q') == False:
#    flag = 0


corner_locationX = Locate_center.corner_locationX
corner_locationY = Locate_center.corner_locationY
center_locationX = Locate_center.center_locationX
center_locationY = Locate_center.center_locationY

#Find 1st factory center
def locate_factory():
    pyautogui.moveTo(center_locationX, center_locationY)
    pyautogui.keyDown('Ctrl')
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.scroll(-600)
    time.sleep(0.3)
    pyautogui.keyUp('Ctrl')

    pyautogui.moveTo(corner_locationX + 2, corner_locationY + 605)
    pyautogui.dragTo(corner_locationX + 1275, corner_locationY + 4, 0.5, button='left')
    time.sleep(0.3)
    pyautogui.moveTo(corner_locationX + 2, corner_locationY + 605)
    pyautogui.dragTo(corner_locationX + 1275, corner_locationY + 4, 0.5, button='left')
    time.sleep(0.3)
    pyautogui.mouseDown(corner_locationX + 1188, corner_locationY + 65, button='left')
    pyautogui.moveTo(corner_locationX + 20, corner_locationY + 800, 0.5)
    time.sleep(0.3)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(center_locationX, corner_locationY + 65, button='left')
    pyautogui.moveTo(center_locationX, corner_locationY + 195, 0.5)
    time.sleep(0.3)
    pyautogui.mouseUp(button='left')

#locate_factory()