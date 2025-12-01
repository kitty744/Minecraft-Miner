import pyautogui as pt
from time import sleep

# left click = attack
def mine_block(seconds):
    pt.keyDown('x')
    sleep(seconds)
    pt.keyUp('x')

# Change based on how many pickaxes you have.
pickaxes = 9

sleep(3)

for i in range(1, pickaxes + 1):
    pt.press(str(i))
    # Change based on type of pickaxe (25 for gold)
    mine_block(25)