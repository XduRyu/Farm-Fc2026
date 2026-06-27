import time
import pyautogui as py
time.sleep(3)
x, y = py.position()
print(f"Mouse position: x={x}, y={y}")