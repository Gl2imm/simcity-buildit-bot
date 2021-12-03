from pyautogui import *
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd =  r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'

import numpy as np
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2
import imutils

import Locate_center



#while keyboard.is_pressed('q') == False:
#   flag = 0
   

corner_locationX = Locate_center.corner_locationX
corner_locationY = Locate_center.corner_locationY
center_locationX = Locate_center.center_locationX
center_locationY = Locate_center.center_locationY

#Check City Storage
def storage_capacity():
    global remain_space
    print('Checking Storage capacity and remaining space...')
    im1 = pyautogui.screenshot(region=(center_locationX - 585, center_locationY - 239,77,23))
    im1.save(r"images/OCR/.used_space.png")

    storage_img = 'images/OCR/.used_space.png'
    storage_img_open = np.array(Image.open(storage_img))
    storage_text_raw = pytesseract.image_to_string(storage_img_open)
    storage_text = storage_text_raw.rstrip()
    storage_text_splitted = storage_text.split("/")
    used_space = storage_text_splitted [0]
    total_space = storage_text_splitted [1]
    remain_space = (int(total_space) - int(used_space))

    print('City Storage Space total -', total_space)
    print('City Storage Space used -', used_space)
    print('City Storage Available Space -', remain_space)
    print("------------------------")
    return remain_space


#Check quantity - Add to Storage check
'''
print("Checking how many items in store")
time.sleep(1.2)
pyautogui.mouseDown(center_locationX - 163, center_locationY - 111, button='left')

im1 = pyautogui.screenshot(region=(center_locationX - 110, center_locationY - 206,50,25))
im1.save(r"images/OCR/.iron_in_store.png")
pyautogui.mouseUp(button='left')

filename = 'images/OCR/.iron_in_store.png'
img1 = np.array(Image.open(filename))
img1_r = imutils.resize(img1, width=400)
text_raw = pytesseract.image_to_string(img1_r, lang='eng',config='--psm 13 -c tessedit_char_whitelist=0123456789')
text = text_raw.rstrip()
print("Store found", text,"iron")
'''
#storage_capacity()