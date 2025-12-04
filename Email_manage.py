import time
from mailtm import Email
import re
import requests

class Email_manage:
    def __init__(self):
        self.done = False

    def listener(self, message):
        raw = message.get('html') or message.get('text') or ''

        #transforms the message (currently is a list) to a string
        content = raw if isinstance(raw, str) else str(raw)

        #list all links in the message
        urls = re.findall(r'(https?://[^\s"\']+)', content)

        for url in urls:

            #find the activation link
            if "activate.api.stardock.net" in url or "validation/validate" in url:
                print(f"Found activation link: {url}")

                #access the link
                resp = requests.get(url, allow_redirects=True)
                print("Status: ", resp.status_code)

                #enable closing the process
                self.done = True
                return

    def run(self):
        temp_email = Email()
        temp_email.register() #create a new random email
        print("\nEmail Adress: " + str(temp_email.address))

        temp_email.start(self.listener)

        #flag to wait until the activation link is found
        while not self.done:
            time.sleep(0.1)

        #close the email
        temp_email.stop()






