import pyautogui

# link to website : https://humanbenchmark.com/tests/reactiontime/


#start test
pyautogui.leftClick(498,379)

while True: #pixel is not green
    if pyautogui.pixel(498,379) == (130, 215, 120):
        pyautogui.leftClick(498,379)



