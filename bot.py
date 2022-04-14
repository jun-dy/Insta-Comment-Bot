import pyautogui, time

time.sleep(4)
Script = open("text.txt", "r")
for text in Script:
    pyautogui.typewrite(text)
    if len(text) != 0:
        pyautogui.press("enter")
        time.sleep(8)
        pyautogui.click()
        time.sleep(8)
    else:
        continue
    time.sleep(4)