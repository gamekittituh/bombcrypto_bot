import pyautogui
import time
pyautogui.FAILSAFE= True
i = 0
position_green_back_button_x = 0
position_green_back_button_Y = 0

count_hero_start = 0
j = 0
print("Program bot for bormcrypto start")
print("Open browser for program one by one")
print("Keep all hero to rest")
print("After open 'Treasure Hunt' page and wait for end process")
cycle_time = input("Input cycle time (Min.): \n")
cycle_time = int(cycle_time)
while j < 999:
    print("Process find green button back. Please wait...")
    result_find_back_button = pyautogui.locateOnScreen('images/btn-back.jpg', confidence=0.8)
    if result_find_back_button is not None:
        print("Found green back button")
        x, y = pyautogui.center(result_find_back_button)
        position_green_back_button_x = x
        position_green_back_button_Y = y
        print("Save position green back button")
        print(x,y)
        pyautogui.click(x, y)
        print("Click green back button")
        print("Find button list hero. Please wait...")
        time.sleep(1)
        result_find_list_hero = pyautogui.locateOnScreen('images/btn-hero.jpg', confidence=0.8)
        if result_find_list_hero is not None:
            print("Find hero resting. Please wait...")
            x, y = pyautogui.center(result_find_list_hero)
            pyautogui.click(x, y)
            time.sleep(1)
            while i <= 5:
                result_click_btn_work = pyautogui.locateOnScreen('images/btn-work.jpg', confidence=0.9)
                if result_click_btn_work is not None:
                    x, y = pyautogui.center(result_click_btn_work)
                    time.sleep(1)
                    pyautogui.click(x, y)
                    count_hero_start += 1
                    print("Click work hero: ",count_hero_start)
                i += 1
                time.sleep(0.5)
            print("Ready to start...")
            print("Find close button")
            time.sleep(0.5)
            result_find_close_button = pyautogui.locateOnScreen('images/btn-close.jpg', confidence=0.8)
            if result_find_close_button is not None:
                x, y = pyautogui.center(result_find_close_button)
                print("Click close button")
                time.sleep(0.5)
                pyautogui.click(x, y)
                time.sleep(1)
                pyautogui.click(x, y)
                print("Find start button")
                time.sleep(1)
                result_find_start_button = pyautogui.locateOnScreen('images/btn-start.jpg', confidence=0.8)
                if result_find_start_button is not None:
                    x, y = pyautogui.center(result_find_start_button)
                    print("Click start button")
                    time.sleep(0.5)
                    pyautogui.click(x, y)
                    time.sleep(1)
                    pyautogui.click(x, y)
    print("Program ready running re process in (Min)",cycle_time)
    time.sleep(60*cycle_time)
