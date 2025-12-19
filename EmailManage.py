import time
from mailtm import Email
import re
import requests
import logging
from threading import Event


class EmailManage:
    def __init__(self):
        self.done = Event()
        self.email_address = None
        self.email = None

    def listener(self, message: dict) -> None:
        raw = message.get('html') or message.get('text') or ''
        content = raw if isinstance(raw, str) else str(raw) #transforms the message (currently is a list) to a string

        urls = re.findall(r'(https?://[^\s"\']+)', content) #list all links in the message
        for url in urls:
            #find the activation link
            if "activate.api.stardock.net" in url or "validation/validate" in url:
                logging.info(f"Found activation link: {url}")
                resp = requests.get(url, allow_redirects=True) #access the link
                logging.info("Status: %s", resp.status_code)
                self.done.set() #enable closing the process
                return

    def email_creation(self) -> None:
        temp_email = Email()
        temp_email.register() #create a new random email

        logging.info("\nEmail Address: " + str(temp_email.address))
        self.email = temp_email
        self.email_address = temp_email.address

    def email_listener(self) -> None:
        self.email.start(self.listener) #flag to wait until the activation link is found
        self.done.wait()
        self.email.stop() #close the email

if __name__ == "__main__":
    email_manage = EmailManage()
    email_manage.email_creation()
    email_manage.email_listener()




