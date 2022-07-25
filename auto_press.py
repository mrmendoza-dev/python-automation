import pyautogui
from pyautogui import FailSafeException

pyautogui.FAILSAFE = True

initial_wait = 5
wait_time = 0.7

active = True
key = "enter"

print(f"Starting in {initial_wait} sec...")
pyautogui.countdown(initial_wait)


def presser():
	pass


def hotkey(*args):
	pyautogui.press(hotkey(*args))


def clicker():
	pass


while active:
	try:
		pyautogui.press(key)
		pyautogui.sleep(wait_time)
		print(f"Pressed key: {key}")
	except FailSafeException as fse:
		active = False
		print(fse)
		print("Program Terminating.")
	except Exception as e:
		print(f"Error: {e}")







