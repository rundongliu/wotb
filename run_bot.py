import pyautogui
import time
import random

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

def move_straight(seconds=30):
    print('press down key: w')
    pyautogui.keyDown('w')
    time.sleep(seconds)
    pyautogui.keyUp('w')


def random_move():
    print('press down key: w')
    pyautogui.keyDown('w') 
    time.sleep(random.randint(0,5))
    print('press down key: a')
    if random.randint(0,10)<=7:
        pyautogui.keyDown('a')
        #time.sleep(random.randint(0,6))

        # pyautogui.mouseDown(button='right') 
        # time.sleep(random.randint(0,6))
        # pyautogui.mouseUp(button='right')

        print('press up key: a')
        pyautogui.keyUp('a')


    #turet_move_pixel = 1000
    #print('move turret...')
    #pyautogui.move(random.randint(0-turet_move_pixel, turet_move_pixel), 0, 5)
    #shoot()

    if random.randint(0,10)<=7:
        print('press down key: d')
        pyautogui.keyDown('d')
        #time.sleep(random.randint(0,6))

        # pyautogui.mouseDown(button='right') 
        # time.sleep(random.randint(0,6))
        # pyautogui.mouseUp(button='right')

        print('press up key: d')
        pyautogui.keyUp('d')
     # Move mouse 10 pixels down from its current position.
    time.sleep(random.randint(0,5))
    
    print('press up key: w')
    pyautogui.keyUp('w')


    print('press down key: s')
    pyautogui.keyDown('s') 
    time.sleep(random.randint(0,2))
    if random.randint(0,10)<=7:
        print('press down key: a')
        pyautogui.keyDown('a')
        time.sleep(random.randint(0,3))
        print('press up key: a')
        pyautogui.keyUp('a')

    if random.randint(0,10)<=7:
        print('press down key: d')
        pyautogui.keyDown('d')
        time.sleep(random.randint(0,3))
        print('press up key: d')
        pyautogui.keyUp('d')
     # Move mouse 10 pixels down from its current position.
    time.sleep(random.randint(0,2))
    
    print('press up key: s')
    pyautogui.keyUp('s')



def check_end_game_page(BLACK_PIXEL=15):
    print('check end game page')
    pix = pyautogui.pixel(END_X, END_Y)
    if pix[0]<=BLACK_PIXEL and pix[1]<=BLACK_PIXEL and pix[2]<=BLACK_PIXEL:
        return True
    return False

def run_one_game():
    start_game()
    time.sleep(20)
    move_straight()
    for i in range(100):
        if i%2==0:
            pyautogui.mouseDown(button='right') 
        #time.sleep(20)
        random_move()

        if i%2==0:
            pyautogui.mouseUp(button='right') 

        if check_end_game_page():
            exit_end_game_page()
            time.sleep(1)
            
            break
    time.sleep(1)


for i in range(500):
    # pyautogui.move(random.randint(0-1000, 1000), 0, 5)
    # print(pyautogui.position())
    # time.sleep(3)
    #time.sleep(1)
    handle_alert()
    run_one_game()
