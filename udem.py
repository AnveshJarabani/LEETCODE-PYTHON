import pyautogui as sim
import time
for i in range(1,5):
    sim.click(x=2776, y=1483) # video position
    time.sleep(3)
    sim.click(x=3028, y=358)  # next vid
    time.sleep(3)