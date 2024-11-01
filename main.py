
import pyautogui
import time
import random
import argparse

_flags = argparse.ArgumentParser(description="Enable custom randrange loops.")
_flags.add_argument('--range', type=int, help="feed me an int to min max from")
_args = _flags.parse_args()

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

  pyautogui.moveTo(temp_pos) # Redundant yet I like to keep this in
  pyautogui.click(temp_pos)
  print("  CLICKED_POS:  ", temp_pos) 

  pyautogui.moveTo(move_back_pos)

  if _args.range is not None:
    sleep_clock = random.randrange(_args.range, _args.range + 2)
    print("\n  RIGGING CUSTOM sleep_clock RANGE:  ", _args.range, "\n")
  else:
    sleep_clock = random.randrange(8,12)

  time.sleep(sleep_clock)
