import pygetwindow as gw
from PIL import ImageGrab
import numpy as np
import cv2

# INSPIRE BY HOW OBS GRABS WINDOWS VIA TITLE

class WindowGrabber:
  def __init__(self, window_title):
    self.window_title = window_title
    self.window = None
    self.window_size = (0, 0)
    self._find_window()

  def _find_window(self):
    try:
      self.window = gw.getWindowsWithTitle(self.window_title)[0]
      self.window.activate()
      self.window_size = (self.window.width, self.window.height)
      print(f"Window '{self.window_title}' found with size {self.window_size}.")
    except IndexError:
      print(f"Error: Window titled '{self.window_title}' not found.")
      self.window = None

  def capture_window(self):
    if not self.window:
      print("Error: Window not initialized or not found.")
      return None

    bbox = (self.window.left, self.window.top, self.window.right, self.window.bottom)
    screenshot = ImageGrab.grab(bbox)
    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

  def extract_region(self, top_left, size=None):
    image = self.capture_window()
    if image is None:
      return None

    if size is None:
      size = min(self.window_size)

    bottom_right = (top_left[0] + size, top_left[1] + size)
    region = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    
    cv2.imshow("Extracted Region", region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return region

# window_title = 'Untitled - Notepad'  
# grabber = WindowGrabber(window_title)
# top_left = (0, 0)  

# will loop here and compare same as game-0engine deltaTime essentially does on certain CV objects for a basic sub system rather than timers losing modulus frequency via randomness. After such will use randomness on a 1,3 to emulate latency of thought.
# region = grabber.extract_region(top_left)

