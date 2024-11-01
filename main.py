
import pyautogui
import time
import random

""" @NOTES - This will possibly be enhanced in another script to use openCV and AI to 
 click on change of "input img or ENUM option" rather than randomrange timer acting as an update loop
 of course you will still use an update loop but would to check diff and creatye then illusion of a player even greater.
You then can enable randomness on click after diff is true to emulate dumbfuckery of thought. 
This is to let you play afk mmorpg wihlst still having a joba nd being able to write code and keep life fun
THIS IS NOT A BOT (the upgraded version could be for the fun coding) THIS IS AN AFK CLICKER TO LET ADULTS AFK PLAY BETWEEN BUILDS TO ALLEVIATE BURNOUT.
- simply, to me, this is a proxy input via an external medium utilizing what would harwdare itself already enables. NOT A BOT. """

print(" PLACE YOUR MOUSE WHERE YOU WANT TO AFK CLICK AND WAIT: \n")

for i in range(2, 0, -1):
  print("  ... ", i)
  time.sleep(1)

pos_using = pyautogui.position()
print("\n  USING POS:  ", pos_using, "\n") 

while(True):
  move_back_pos = pyautogui.position()
  rand = random.randrange(-2, 2)

  temp_pos = pyautogui.Point(pos_using.x + rand, pos_using.y + rand)

  pyautogui.moveTo(temp_pos)
  pyautogui.click(temp_pos)
  print("  CLICKED_POS:  ", temp_pos) 

  pyautogui.moveTo(move_back_pos) 

  sleep_clock = random.randrange(8,12)
  time.sleep(sleep_clock)
