import pyautogui
import time
from Email_manage import Email_manage
import pyperclip

#If the PC is a potato
pyautogui.PAUSE = 0.5

#Create a Randomly email
email = Email_manage()
email.email_creation()

#copy the email to the clipboard
pyperclip.copy(email.email_address)

#Open fences
def open_fences():
    pyautogui.press('winleft')
    pyautogui.write('fences')
    pyautogui.press('enter')
open_fences()

#click on 'start trial'
time.sleep(1)
def auto_fences():
    try:
        position = pyautogui.locateCenterOnScreen(r"Assets\Start_30_Day_Trial.png")
    #Tries two times, because the fences have a problem sometimes. If you immediately delete the cache, maybe the program doesn't open the screen of the trial test
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey('alt','f4')
        open_fences()
        time.sleep(0.5)
        position = pyautogui.locateCenterOnScreen(r"Assets\Start_30_Day_Trial.png")
    pyautogui.click(position)

    #Paste the email
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.5)
    position = pyautogui.locateCenterOnScreen(r"Assets\Continue_Fences.png")
    pyautogui.click(position)
auto_fences()

email.email_listener()
