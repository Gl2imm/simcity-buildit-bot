from pyautogui import *
import pyautogui
import time
import keyboard

'''
if pixel function laggy
from PIL import ImageGrab
pixelRGB = ImageGrab.grab().getpixel((x, y))
'''

while keyboard.is_pressed('q') == False:
    flag = 0


import Locate_center
import Locate_factory
import Settings
import Storage_check

center_shop_location = Locate_center.center_shop_location
corner_locationX = Locate_center.corner_locationX
corner_locationY = Locate_center.corner_locationY
center_locationX = Locate_center.center_locationX
center_locationY = Locate_center.center_locationY

find_iron = Settings.find_iron
find_wood = Settings.find_wood
find_plastic = Settings.find_plastic
find_camera = Settings.find_camera

print(center_shop_location)
print ('Left corner:', corner_locationX, ',', corner_locationY)
print (center_locationX, center_locationY)
print("------------------------")


'''
print("Test convert string to variable:")
test_item = None
item_to_loop = "iron"
find_item = "find_" + item_to_loop
vars()[find_item] = "find_item"
print(find_item)
'''


'''
#Boxes regions
box_1 = (int(center_locationX - 280), int(center_locationY - 119), 80, 79)
box_2 = (int(center_locationX - 138), int(center_locationY - 119), 85, 79)
box_3 = (int(center_locationX + 7), int(center_locationY - 119), 84, 80)
box_4 = (int(center_locationX + 153), int(center_locationY - 119), 84, 80)
box_5 = (int(center_locationX - 280), int(center_locationY + 68), 80, 74)
box_6 = (int(center_locationX - 137), int(center_locationY + 68), 84, 74)
box_7 = (int(center_locationX + 5), int(center_locationY + 68), 86, 74)
box_8 = (int(center_locationX + 151), int(center_locationY + 68), 86, 74)
#im1 = pyautogui.screenshot(region=(box_1))
#im1.save(r"images/.check1.png")
'''

#click HQ
def click_hq():
    time.sleep(0.4)
    pyautogui.click(center_locationX - 341, center_locationY - 137)
    time.sleep(0.3)

#Going home from heighbour city
def travel_home():
    pyautogui.click(center_locationX + 318, center_locationY - 225)
    time.sleep(0.2)
    pyautogui.click(center_locationX - 592, center_locationY - 316)
    print("Travelling back Home")
    print("------------------------")
    time.sleep(4)

#check that the page fully loaded
def home_shop_load_check():
    global pixel_check
    global pixel_check2
    global shop_loaded
    shop_loaded = False
    pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 83), int(center_locationY + 209), (102, 239, 255))
    pixel_check2 = pyautogui.pixelMatchesColor(int(center_locationX - 78), int(center_locationY + 209), (102, 239, 255))
    if pixel_check or pixel_check2 == True:
        shop_loaded = True
    return shop_loaded         

def neighbor_shop_load_check():
    global neighb_shop_loaded
    neighb_shop_loaded = False    
    time.sleep(5)
    print("Waiting Neighbour Shop to be fully loaded . . .")
    pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 290), int(center_locationY - 106), (244, 213, 161))
    if pixel_check == True:
        print("Screen Loaded")
    else:
        while pixel_check == False:
            time.sleep(0.2)
            pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 290), int(center_locationY - 106), (244, 213, 161))
            if pixel_check == True:
                neighb_shop_loaded = True
                print("Neighbour Shop Loaded")
                break
    time.sleep(1)
    return neighb_shop_loaded

def next_page_check():
    global next_page
    pixel_check = pyautogui.pixelMatchesColor(int(center_locationX + 280), int(center_locationY - 139), (71, 182, 212))
    if pixel_check == True:
        next_page = True
        print("Next page found")
    else:
        print("No more pages")
        next_page = False
        return next_page

def do_next_page():
    global next_page_do_done
    next_page_do_done = False
    next_page_check()
    if next_page == True:
        print("Swiping Next page...")
        pyautogui.mouseDown(center_locationX + 264, center_locationY + 16, button='left')
        pyautogui.moveTo(center_locationX - 323, center_locationY + 16, 0.4)
        time.sleep(0.3)
        pyautogui.mouseUp(button='left')
        time.sleep(0.2)
        next_page_do_done = True
        return next_page_do_done

def refresh_shop_do():
    refresh_shop_check = False
    pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 97), int(center_locationY + 207), (42, 146, 177))
    if pixel_check == True:
        refresh_shop_check = True
        print("Refreshing Shop")
        pyautogui.click(center_locationX + 1, center_locationY + 211)
    else:
        print("Counter still running, waiting for Refresh . . .")
        while pixel_check == False:
            time.sleep(1)
            pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 97), int(center_locationY + 207), (42, 146, 177))
            if pixel_check == True:
                print("Refreshing Shop")
                pyautogui.click(center_locationX + 1, center_locationY + 211)
                time.sleep(2)
                break
    return refresh_shop_check

def looking_iron():
    global iron_location
    iron_location = pyautogui.locateOnScreen('images/craft/iron.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.6)
    return iron_location

def looking_plastic():
    global plastic_location
    plastic_location = pyautogui.locateOnScreen('images/items/plastic.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.7)
    return plastic_location

def looking_camera():
    global camera_location
    camera_location = pyautogui.locateOnScreen('images/items/camera.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.7)
    return camera_location

def all_items_bought_check():
    global all_items_bought
    if (find_iron == 0 and find_wood == 0 and find_plastic == 0):
        all_items_bought = True
    else:
        all_items_bought = False
    return all_items_bought

def no_items_found_check():
    global no_items_found
    if find_iron != 0:
        looking_iron()
    if find_plastic != 0:
        looking_plastic()
    if iron_location and plastic_location == None:
        no_items_found = True
    else:
        no_items_found = False
    return no_items_found

#Collect iron at neighbour city
'''
need to add later
    CHECK IF THERE NEXT PAGE
    IF NO NEXT PAGE - ITEM BOUGHT
        ELSE 
            GO NEXT PAGE
            if looking_iron() != None:
                pyautogui.click(looking_iron())
            else:
                ITEM BOUGHT
'''
def pick_iron_from_neigbour():
    global find_iron
    #NEED ADD ITEM SOLD CHECK (GREY COLOR)
    looking_iron()
    time.sleep(0.5)
    if iron_location == None:
        print("!! Looks like item been bought by others !!")
    else:
        pyautogui.click(iron_location)
        print("Iron found, purchasing...")
        time.sleep(2)
        item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(iron_location), confidence=0.7)
        if item_bought != None:
            find_iron -= 1
            print("Item purchased")
            if find_iron != 0:
                print('Iron left to collect -', find_iron)
            else:
                print("Iron hunting Complete. Requested quantity found")
                print("------------------------")
        else:
            item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(iron_location), confidence=0.7)
            while item_bought == None:
                item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(iron_location), confidence=0.7)
                time.sleep(0.2)
                if item_bought != None:
                    find_iron -= 1
                    print("Item purchased")
                    if find_iron != 0:
                        print('Iron left to collect -', find_iron)
                    else:
                        print("Iron hunting Complete. Requested quantity found")
                    print("------------------------")

def pick_plastic_from_neigbour():
    global find_plastic
    #NEED ADD ITEM SOLD CHECK (GREY COLOR)
    looking_plastic()
    if plastic_location == None:
        print("!! Looks like item been bought by others !!")
    else:
        pyautogui.click(plastic_location)
        print("plastic found, purchasing...")
        time.sleep(2)
        item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(plastic_location), confidence=0.7)
        if item_bought != None:
            find_plastic -= 1
            print("Item purchased")
            if find_plastic != 0:
                print('plastic left to collect -', find_plastic)
            else:
                print("plastic hunting Complete. Requested quantity found")
                print("------------------------")
        else:
            item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(plastic_location), confidence=0.7)
            while item_bought == None:
                item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(plastic_location), confidence=0.7)
                time.sleep(0.2)
                if item_bought != None:
                    find_plastic -= 1
                    print("Item purchased")
                    if find_plastic != 0:
                        print('plastic left to collect -', find_plastic)
                    else:
                        print("plastic hunting Complete. Requested quantity found")
                    print("------------------------")

def pick_camera_from_neigbour():
    global find_camera
    #NEED ADD ITEM SOLD CHECK (GREY COLOR)
    looking_camera()
    if camera_location == None:
        print("!! Looks like item been bought by others !!")
    else:
        pyautogui.click(camera_location)
        print("camera found, purchasing...")
        time.sleep(2)
        item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(camera_location), confidence=0.7)
        if item_bought != None:
            find_camera -= 1
            print("Item purchased")
            if find_camera != 0:
                print('camera left to collect -', find_camera)
            else:
                print("camera hunting Complete. Requested quantity found")
                print("------------------------")
        else:
            item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(camera_location), confidence=0.7)
            while item_bought == None:
                item_bought = pyautogui.locateOnScreen('images/items/item_bought.png', region=(camera_location), confidence=0.7)
                time.sleep(0.2)
                if item_bought != None:
                    find_camera -= 1
                    print("Item purchased")
                    if find_camera != 0:
                        print('camera left to collect -', find_camera)
                    else:
                        print("camera hunting Complete. Requested quantity found")
                    print("------------------------")

def do_collect_iron():
    neighb_shop_loaded = False
    print("found Iron. Collecting")
    pyautogui.click(iron_location)
    print("Travelling to neighboring city")
    time.sleep(3)
    print("Waiting Neighbour Shop to be fully loaded . . .")
    time.sleep(2)
    while neighb_shop_loaded != True:
        time.sleep(0.2)
        pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 290), int(center_locationY - 106), (244, 213, 161))
        #NEED ADD ITEM SOLD CHECK (GREY COLOR)
        #if pixel_check == True:
        #print("!! Looks like item been bought by others !!")
        #travel_home()
        #break
        if pixel_check == True:
            neighb_shop_loaded = True
        if neighb_shop_loaded == True:
            print("Neighbour Shop Loaded")
            pick_iron_from_neigbour()
            travel_home()
            break

def do_collect_plastic():
    neighb_shop_loaded = False
    print("found plastic. Collecting")
    pyautogui.click(plastic_location)
    print("Travelling to neighboring city")
    time.sleep(3)
    print("Waiting Neighbour Shop to be fully loaded . . .")
    time.sleep(2)
    while neighb_shop_loaded != True:
        time.sleep(0.2)
        pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 290), int(center_locationY - 106), (244, 213, 161))
        if pixel_check == True:
            neighb_shop_loaded = True
        if neighb_shop_loaded == True:
            print("Neighbour Shop Loaded")
            pick_plastic_from_neigbour()
            travel_home()
            break

def do_collect_camera():
    neighb_shop_loaded = False
    print("found camera. Collecting")
    pyautogui.click(camera_location)
    print("Travelling to neighboring city")
    time.sleep(3)
    print("Waiting Neighbour Shop to be fully loaded . . .")
    time.sleep(2)
    while neighb_shop_loaded != True:
        time.sleep(0.2)
        pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 290), int(center_locationY - 106), (244, 213, 161))
        if pixel_check == True:
            neighb_shop_loaded = True
        if neighb_shop_loaded == True:
            print("Neighbour Shop Loaded")
            pick_camera_from_neigbour()
            travel_home()
            break



#in HQ page
iron_location = None
plastic_location = None
camera_location = None
go_hq = True
storage_check = True
def items_buy_loop():
    global iron_location
    global plastic_location
    global camera_location
    global go_hq
    global storage_check
    shop_loaded = False
    if go_hq == True:
        print('Quantity of items to be found:','\n''Iron: ' + str(find_iron) if find_iron != 0 else "",'\n''Wood: ' + str(find_wood) if find_wood != 0 else "", '\n''Plastic: ' + str(find_plastic) if find_plastic != 0 else "", '\n''Camera: ' + str(find_camera) if find_camera != 0 else "")
        print("------------------------")
        Locate_factory.locate_factory()
        click_hq()
    print("Waiting Shop to be fully loaded . . .")
    while shop_loaded != True:
        time.sleep(0.2)
        pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 83), int(center_locationY + 209), (102, 239, 255))
        pixel_check2 = pyautogui.pixelMatchesColor(int(center_locationX - 78), int(center_locationY + 209), (102, 239, 255))
        if pixel_check or pixel_check2 == True:
            shop_loaded = True
        if shop_loaded == True:
            print("Screen fully Loaded")
            if find_iron != 0:
                iron_location = pyautogui.locateOnScreen('images/craft/iron.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.6)
                if iron_location != None:
                    print('iron detected -', iron_location)
                    do_collect_iron()
                    iron_location = None
                    go_hq = True
                    break
            if find_plastic != 0:
                plastic_location = pyautogui.locateOnScreen('images/craft/plastic.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), confidence=0.7)
                if plastic_location != None:
                    print('plastic detected -', plastic_location)
                    do_collect_plastic()
                    plastic_location = None
                    go_hq = True
                    break
            if find_camera != 0:
                camera_location = pyautogui.locateOnScreen('images/items/camera.png', region=(int(center_locationX - 335), int(center_locationY - 183), 667, 420), grayscale=False, confidence=0.7)
                if camera_location != None:
                    print('camera detected -', camera_location)
                    do_collect_camera()
                    camera_location = None
                    go_hq = True
                    break
            print("Requested items not found, checking if there is a next page")
            next_page_check()
            if next_page == True:
                do_next_page()
                go_hq = False
                storage_check = False
            else:
                pixel_check = False
                print("Checking if Shop Refresh is available")
                print("Counter still running, waiting for Refresh button . . .")
                while pixel_check == False:
                    time.sleep(1)
                    pixel_check = pyautogui.pixelMatchesColor(int(center_locationX - 97), int(center_locationY + 207), (42, 146, 177))
                    if pixel_check == True:
                        go_hq = False
                        storage_check = False
                        print("Refreshing Shop")
                        pyautogui.click(center_locationX + 1, center_locationY + 211)
                        time.sleep(2)
                        break


'''
            else:
                refresh_shop_do()
                go_hq = False
                print("Waiting Shop to be fully loaded . . .")
'''
 
def items_hunter():
    all_items_bought_check()
    print("TEST", all_items_bought)
    if all_items_bought != True:
        while all_items_bought != True:
            if storage_check == True:
                if Storage_check.storage_capacity() >= 5:
                    print("Storage space OK")
                    print("------------------------")
                    items_buy_loop()
                    all_items_bought_check()
                    if all_items_bought == True:
                        print("All items collected. Stopping the bot")
                        all_items_bought_check()
                        break
                else:
                    print("!! Storage Full. Free up the Storage !!")
                break
            else:
                items_buy_loop()
                all_items_bought_check()
    else:
        print("No items selected for hunting.")



while keyboard.is_pressed('p') == False:
    items_hunter()
    if keyboard.is_pressed('p') == True:
        print("stopped")
        break



'''
# Reading image value (currently cannot recognize digits)
def storage_capacity():
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
'''



