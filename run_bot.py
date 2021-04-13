import pyautogui
import time
import random
from datetime import datetime
import sys

pyautogui.FAILSAFE = True

key_state = {
    'w': False,
    's': False,
    'a': False,
    'd': False  
}

screen_size = pyautogui.size()
END_X = 600
END_Y = 50

if screen_size.width == 1440:
    START_X = 737
    START_Y = 100

    CANCEL_X = 646
    CANCEL_Y= 491


else:
    START_X = 970
    START_Y = 100

    CANCEL_X = 850
    CANCEL_Y= 685

def hold_keys(hold_keys):
    for key in key_state:
        if key in hold_keys:
            if not key_state[key]: # if not pressed
                print('press key:', key)
                pyautogui.keyDown(key)
            key_state[key] = True
        else:
            if key_state[key]:
                pyautogui.keyUp(key)
            key_state[key] = False



def start_game():
    print('start game ...')
    # get handler
    pyautogui.click(START_X, START_Y)
    # start game
    pyautogui.click(START_X, START_Y)

def exit_end_game_page():
    print('exit game...')
    pyautogui.press('esc')


def handle_alert():
    print('handle_alert...')
    pyautogui.press('esc')
    pyautogui.click(CANCEL_X, CANCEL_Y)
    time.sleep(1)

def shoot():
    print('shoot...')
    pyautogui.click(START_X, START_Y)

def move_turret():
    pyautogui.moveTo(750, 450)
    pyautogui.keyDown('ctrl')
    pyautogui.drag(random.randint(-1000,1000), random.randint(-300,300), 2, button='left') 
    pyautogui.keyUp('ctrl')

def move_straight():
    turn_time = 0.5
    for i in range(5):
        hold_keys('w')
        print(key_state)
        time.sleep(4)


        hold_keys('wa')
        print(key_state)
        time.sleep(turn_time)

        hold_keys('wd')
        print(key_state)
        time.sleep(turn_time)

        turn_time += 0.5

def random_move():

    for i in range(2):
        hold_keys('w')
        move_turret()
        print(key_state)
        time.sleep(random.randint(0,10)/10.0)


        hold_keys('wa')
        print(key_state)
        time.sleep(random.randint(0,10)/10.0)

        hold_keys('wd')
        print(key_state)
        time.sleep(random.randint(0,10)/10.0)


    hold_keys('s')
    move_turret()
    time.sleep(random.randint(0,10)/10.0)

    hold_keys('sa')
    print(key_state)
    move_turret()
    time.sleep(random.randint(0,10)/10.0)

    if random.randint(0,10)<=3:
        #shoot()
        pass

    hold_keys('sd')
    print(key_state)
    move_turret()
    time.sleep(random.randint(0,10)/10.0)

    pyautogui.press('7')

def check_end_game_page(BLACK_PIXEL=15):
    print('check end game page')
    pix = pyautogui.pixel(END_X, END_Y)
    if pix[0]<=BLACK_PIXEL and pix[1]<=BLACK_PIXEL and pix[2]<=BLACK_PIXEL:
        return True
    return False

def type_something():
    words = ['Laaaaaging', 'network lag af', 'dam, too lagging', 'ipad control sucks', 'why so lagging', 'ping so high',
    'bad ping', 'this phone sucks', 'lag as sht', '500 ping']
    pyautogui.press('enter')
    pyautogui.write(random.choice(words))
    pyautogui.press('enter')


def run_one_game():
    start_game()
    time.sleep(45)
    move_straight()
    for i in range(10000):
        # if i%2==0:
        #     pyautogui.mouseDown(button='right') 
        #time.sleep(20)
        random_move()
        if i%2400==0:
            type_something()

        # if i%2==0:
        #     pyautogui.mouseUp(button='right') 

        if check_end_game_page():
            exit_end_game_page()
            time.sleep(1)
            break

    time.sleep(1)

if len(sys.argv)>=2:
    start_time = sys.argv[1]
    print('expecting time set: ', start_time)
else:
    start_time = None

while 1:
    if start_time:
        current_time = datetime.now().strftime("%m/%d/%H:%M:%S")
        if current_time < start_time:
            print('current_time: ', current_time)
            print('expecting: ', start_time)
            time.sleep(600)
            continue
    
    handle_alert()
    run_one_game()
