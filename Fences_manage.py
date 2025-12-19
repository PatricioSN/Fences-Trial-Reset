import pyautogui
import time
from Email_manage import Email_manage
import pyperclip

class Fences_manage:
    def __init__(self):
        pyautogui.PAUSE = 0.5
        self.email = Email_manage()#Create a Randomly email

    def prepare_email(self):
        self.email.email_creation()
        pyperclip.copy(self.email.email_address) #copy the email to the clipboard

    def open_fences(self):
        pyautogui.press('winleft')
        pyautogui.write('fences')
        pyautogui.press('enter')

    def start_trial(self):
        try:
            time.sleep(0.5)
            position = pyautogui.locateCenterOnScreen(
                r"Assets\Start_30_Day_Trial.png"
            )
        #Tries two times, because the fences have a problem sometimes. If you immediately delete the cache, maybe the program doesn't open the screen of the trial test
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('alt','f4')
            self.open_fences()
            time.sleep(0.5)
            position = pyautogui.locateCenterOnScreen(
                r"Assets\Start_30_Day_Trial.png"
            )
        pyautogui.click(position)

        #Paste the email
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.5)
        position = pyautogui.locateCenterOnScreen(r"Assets\Continue_Fences.png")
        pyautogui.click(position)


    def listen_email(self):
        self.email.email_listener()

if __name__ == "__main__":
    app = Fences_manage()
    app.prepare_email()
    app.open_fences()
    app.start_trial()
    app.listen_email()