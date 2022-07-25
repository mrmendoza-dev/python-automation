import pyautogui
from pyautogui import FailSafeException


pyautogui.FAILSAFE = True

initial_wait = 5
wait_time = 0.7

active = True


while active:
	pyautogui.sleep(wait_time)

	try:
		target = pyautogui.locateOnScreen('images/example.png')

		"""
		- If match is found, enter conditional
		- Save current mouse coordinates before moving to target
		- Center target and click, return to original position and repeat
		"""
		if target is not None:
			prev_x, prev_y = pyautogui.position()
			target_center = pyautogui.center(target)
			pyautogui.click(target_center)
			pyautogui.moveTo(prev_x, prev_y)

	except FailSafeException as fse:
		print(f"FailSafeException: {fse}")

	except Exception as e:
		print(f"Exception: {e}")

