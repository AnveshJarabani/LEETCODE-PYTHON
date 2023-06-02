import pyautogui as sim
import time
for i in range(1,4):
    sim.click(x=2776, y=1485) # video position
    time.sleep(3)
    sim.click(x=2845, y=851)  # next vid
    time.sleep(3)