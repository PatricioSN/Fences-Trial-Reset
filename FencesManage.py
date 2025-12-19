import pyautogui
import time
from EmailManage import EmailManage
import pyperclip
import logging


class FencesManage:
    def __init__(self):
        pyautogui.PAUSE = 0.5
        self.email = EmailManage() #Create a Randomly email

    def _wait_for_image(self, image_path: str, timeout: int = 5):
        start = time.time()
        while time.time() - start < timeout:
            position = pyautogui.locateCenterOnScreen(image_path)
            if position:
                return position
            time.sleep(0.2)
        raise TimeoutError("Image not found")

    def prepare_email(self) -> None:
        self.email.email_creation()
        pyperclip.copy(self.email.email_address) #copy the email to the clipboard
        logging.info("Email copied to clipboard")

    def open_fences(self):
        pyautogui.press('winleft')
        pyautogui.write('fences')
        pyautogui.press('enter')
        time.sleep(0.5)

    def start_trial(self) -> None:
        try:
            time.sleep(0.5)
            position = self._wait_for_image(
                r"Assets\Start_30_Day_Trial.png"
            )
        #Tries two times, because the fences have a problem sometimes. If you immediately delete the cache, maybe the program doesn't open the screen of the trial test
        except pyautogui.ImageNotFoundException or TimeoutError:
            logging.warning("Trial screen not found, retrying...")
            pyautogui.hotkey('alt','f4')
            self.open_fences()
            position = self._wait_for_image(
                r"Assets\Start_30_Day_Trial.png"
            )
        pyautogui.click(position)

        #Paste the email
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')


        position = self._wait_for_image(r"Assets\Continue_Fences.png")
        pyautogui.click(position)


    def listen_email(self) -> None:
        self.email.email_listener()

if __name__ == "__main__":
    app = FencesManage()
    app.prepare_email()
    app.open_fences()
    app.start_trial()
    app.listen_email()